#!/usr/bin/env python3
"""Build PDFs from the SZZ wiki Markdown (okruhy/ + synthesis/) using pandoc + xelatex.

This runs entirely locally — there is no CI and no PDF is committed to the repo.
Output PDFs land in build/ (git-ignored).

Subcommands
-----------
  topic [SLUG]      Build one okruh PDF        -> build/okruhy/<slug>.pdf
                    (no SLUG: build every okruh individually)
  synthesis [SLUG]  Build one synthesis PDF    -> build/synthesis/<slug>.pdf
                    (no SLUG: build every synthesis individually)
  topics            Merge ALL okruhy           -> build/szz-okruhy.pdf
  syntheses         Merge ALL syntheses        -> build/szz-syntezy.pdf
  all               Merge EVERYTHING           -> build/szz-vse.pdf

Examples
--------
  python scripts/build_pdf.py topic 01-polovodicove-prvky-cmos
  python scripts/build_pdf.py synthesis relace-napric-obory
  python scripts/build_pdf.py topics
  python scripts/build_pdf.py all

Requirements: pandoc, a XeLaTeX engine (texlive-xetex), and the fonts
"Noto Serif" / "Noto Sans Mono" (override with --mainfont / --monofont).

The wiki Markdown is written for Obsidian, so before handing it to pandoc the
script rewrites the Obsidian-only constructs:
  * ![[media/...png]] embeds  -> standard ![](absolute/path) images
  * [[target|alias]] wikilinks -> plain text (alias, heading, or last path part)
  * > [!note] callouts         -> a bold-titled blockquote
  * YAML frontmatter           -> stripped (the body H1 is the real heading)
Standard `$...$` / `$$...$$` math is left untouched for pandoc to render.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER = Path(__file__).resolve().parent / "pandoc-header.tex"
OKRUHY = ROOT / "okruhy"
SYNTHESIS = ROOT / "synthesis"
BUILD = ROOT / "build"

# Obsidian callout type -> human label used in the rendered blockquote.
CALLOUT_LABELS = {
    "note": "Poznámka",
    "info": "Info",
    "tip": "Tip",
    "warning": "Pozor",
    "important": "Důležité",
    "example": "Příklad",
}

_FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
_EMBED = re.compile(r"!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
_WIKILINK = re.compile(r"\[\[([^\]]+?)\]\]")
_CALLOUT = re.compile(r"^(\s*>)\s*\[!(\w+)\]\s*(.*)$")
_ATX = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
# A line of only `=` is a Setext-H1 underline. The sources use ATX headings only,
# so any such line is a stray docx artifact that would turn the line above it into
# a phantom top-level heading; blank it out.
_SETEXT_RULE = re.compile(r"(?m)^=+[ \t]*$")


def _embed_to_image(match: re.Match) -> str:
    """![[media/szz-01/media/image2.png]] -> ![](<abs path>)."""
    target = match.group(1).strip()
    abs_path = (ROOT / target).resolve()
    return f"![]({abs_path.as_posix()})"


def _wikilink_to_text(match: re.Match) -> str:
    """Render an internal wikilink as plain text (PDF is self-contained)."""
    inner = match.group(1)
    if "|" in inner:
        return inner.split("|", 1)[1].strip()
    target = inner.strip()
    if target.startswith("#"):
        return target[1:].strip()
    return target.rsplit("/", 1)[-1].strip()


def _fix_callouts(text: str) -> str:
    out = []
    for line in text.splitlines():
        m = _CALLOUT.match(line)
        if m:
            prefix, ctype, title = m.groups()
            title = title.strip() or CALLOUT_LABELS.get(ctype.lower(), ctype.capitalize())
            out.append(f"{prefix} **{title}**")
        else:
            out.append(line)
    return "\n".join(out)


def _normalize_headings(text: str) -> str:
    """Give every document exactly one H1 (its title).

    Several source files use `#` not just for the title but also for major
    sections of the full text (okruh 31 has seven `#` headings). Left alone
    they all land at the top TOC level and clutter the merged contents. Keep
    the first heading as the H1 title and demote any later `#` heading to `##`;
    drop empty headings (one okruh has a stray `# ` with no text).
    """
    out, seen_title = [], False
    for line in text.splitlines():
        m = _ATX.match(line)
        if m:
            hashes, body = m.groups()
            if not body:
                continue  # empty heading → drop
            if not seen_title:
                seen_title = True
            elif hashes == "#":
                hashes = "##"  # stray inner H1 → H2
            out.append(f"{hashes} {body}")
        else:
            out.append(line)
    return "\n".join(out)


def preprocess(md_path: Path) -> str:
    """Turn an Obsidian Markdown file into pandoc-friendly Markdown."""
    text = md_path.read_text(encoding="utf-8")
    text = _FRONTMATTER.sub("", text)
    text = _fix_callouts(text)
    text = _EMBED.sub(_embed_to_image, text)
    text = _WIKILINK.sub(_wikilink_to_text, text)
    text = _SETEXT_RULE.sub("", text)
    text = _normalize_headings(text)
    return text.strip() + "\n"


def _pandoc_cmd(out_path: Path, args: argparse.Namespace, *, toc: bool, title: str | None) -> list[str]:
    cmd = [
        "pandoc",
        # We strip frontmatter ourselves and pass the title via -M, so disable
        # YAML metadata parsing — otherwise the `---` thematic breaks in the doc
        # footers get misread as metadata blocks when files are concatenated.
        # We strip frontmatter ourselves and pass the title via -M, so disable
        # YAML metadata parsing — otherwise the `---` thematic breaks in the doc
        # footers get misread as metadata blocks.
        "-f", "markdown-yaml_metadata_block",
        # Parse each input file on its own. Without this, concatenated files are
        # reparsed as one stream and the `---`/footer at a file boundary can
        # swallow the next file's `#` title, dropping most okruhy from the TOC.
        "--file-scope",
        f"--pdf-engine={args.engine}",
        "--include-in-header", str(HEADER),
        "--resource-path", str(ROOT),
        "-V", "geometry:margin=2.5cm",
        "-V", "lang=cs",
        "-V", f"mainfont={args.mainfont}",
        "-V", f"monofont={args.monofont}",
        "-V", "colorlinks=true",
        "-V", "linkcolor=blue",
        "-V", "urlcolor=blue",
        "-o", str(out_path),
    ]
    if title:
        cmd += ["-M", f"title={title}"]
    if toc:
        cmd += ["--toc", "--toc-depth=1"]
    return cmd


def _build(paths: list[Path], out_path: Path, args: argparse.Namespace, *, toc: bool, title: str | None) -> None:
    """Preprocess each source file to a temp file and run pandoc over them all.

    Files are passed as separate inputs (with --file-scope) so each parses
    cleanly; a trailing raw `\\newpage` between them keeps documents on their
    own pages in the merged output.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_paths: list[Path] = []
    try:
        for i, src in enumerate(paths):
            content = preprocess(src)
            if i < len(paths) - 1:
                content += "\n\\newpage\n"
            with tempfile.NamedTemporaryFile("w", suffix=".md", dir=ROOT, delete=False, encoding="utf-8") as tmp:
                tmp.write(content)
                tmp_paths.append(Path(tmp.name))
        cmd = _pandoc_cmd(out_path, args, toc=toc, title=title) + [str(p) for p in tmp_paths]
        subprocess.run(cmd, check=True)
    finally:
        for p in tmp_paths:
            p.unlink(missing_ok=True)
    print(f"  ✓ {out_path.relative_to(ROOT)}")


def _slug_path(directory: Path, slug: str) -> Path:
    slug = slug.removesuffix(".md")
    path = directory / f"{slug}.md"
    if not path.exists():
        available = ", ".join(sorted(p.stem for p in directory.glob("*.md")))
        sys.exit(f"error: '{slug}.md' not found in {directory.relative_to(ROOT)}/.\nAvailable: {available}")
    return path


# ── subcommands ───────────────────────────────────────────────────────────────

def cmd_single(directory: Path, out_subdir: str, slug: str | None, args: argparse.Namespace) -> None:
    if slug:
        paths = [_slug_path(directory, slug)]
    else:
        paths = sorted(directory.glob("*.md"))
    print(f"Building {len(paths)} PDF(s) from {directory.relative_to(ROOT)}/ …")
    for path in paths:
        out = BUILD / out_subdir / f"{path.stem}.pdf"
        _build([path], out, args, toc=False, title=None)


def cmd_topic(args):
    cmd_single(OKRUHY, "okruhy", args.slug, args)


def cmd_synthesis(args):
    cmd_single(SYNTHESIS, "synthesis", args.slug, args)


def cmd_topics(args):
    paths = sorted(OKRUHY.glob("*.md"))
    print(f"Merging {len(paths)} okruhy …")
    _build(paths, BUILD / "szz-okruhy.pdf", args,
           toc=True, title="SZZ — Okruhy (FIT BUT)")


def cmd_syntheses(args):
    paths = sorted(SYNTHESIS.glob("*.md"))
    print(f"Merging {len(paths)} syntéz …")
    _build(paths, BUILD / "szz-syntezy.pdf", args,
           toc=True, title="SZZ — Syntézy (FIT BUT)")


def cmd_all(args):
    paths = sorted(OKRUHY.glob("*.md")) + sorted(SYNTHESIS.glob("*.md"))
    print(f"Merging everything ({len(paths)} dokumentů) …")
    _build(paths, BUILD / "szz-vse.pdf", args,
           toc=True, title="SZZ — Kompletní materiály (FIT BUT)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build PDFs from the SZZ wiki Markdown (local, pandoc + LuaLaTeX).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--engine", default="lualatex",
                        help="LaTeX PDF engine (default: lualatex; xelatex also works if installed)")
    parser.add_argument("--mainfont", default="Noto Serif", help="main text font (default: Noto Serif)")
    parser.add_argument("--monofont", default="Noto Sans Mono", help="monospace font (default: Noto Sans Mono)")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("topic", help="one okruh PDF (or all individually if SLUG omitted)")
    p.add_argument("slug", nargs="?", help="okruh slug, e.g. 01-polovodicove-prvky-cmos")
    p.set_defaults(func=cmd_topic)

    p = sub.add_parser("synthesis", help="one synthesis PDF (or all individually if SLUG omitted)")
    p.add_argument("slug", nargs="?", help="synthesis slug, e.g. relace-napric-obory")
    p.set_defaults(func=cmd_synthesis)

    sub.add_parser("topics", help="merge all okruhy into one PDF").set_defaults(func=cmd_topics)
    sub.add_parser("syntheses", help="merge all syntheses into one PDF").set_defaults(func=cmd_syntheses)
    sub.add_parser("all", help="merge okruhy + syntheses into one PDF").set_defaults(func=cmd_all)

    args = parser.parse_args()
    if not HEADER.exists():
        sys.exit(f"error: pandoc header not found at {HEADER}")
    args.func(args)


if __name__ == "__main__":
    main()
