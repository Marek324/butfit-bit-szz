---
title: Wiki Log
---

# Wiki Log

- [2026-06-03 14:56:34 +0200] INIT vault_path="/home/marek/wikis/szz" categories=concepts,entities,skills,references,synthesis,journal
- [2026-06-03 14:56:34 +0200] SOURCES Downloaded 44 SZZ topic docs from Google Drive, converted docx→md into _raw/ (855 images extracted). Originals + manifest.json in _sources/docx/.
- [2026-06-03 15:12:58 +0200] INGEST source="_raw/szz-01..15.md" pages_updated=0 pages_created=15 mode=raw
- [2026-06-03 15:45:00 +0200] RESTRUCTURE Moved 15 pages concepts/ → okruhy/NN-slug (numbered, linear navigation), added okruhy category to .env, moved _raw/media → media/ (855 images), embedded + caption-verified 38 diagrams against source images (10 captions corrected), rebuilt index.md as ordered TOC of all 44 okruhů.
- [2026-06-03 16:05:00 +0200] HYBRID Each okruh page now = "## Shrnutí" (distilled + cross-links + key captioned diagrams) + "## Plné znění (ke studiu)" (complete source text + ALL diagrams). Full text regenerated from docx via pandoc -t gfm, mark-spans stripped, img tags → wikilink embeds. 299 image embeds total, all resolve.
- [2026-06-03 16:56:21 +0200] INGEST source="_raw/caste-otazky-szz.md" pages_updated=15 pages_created=0 mode=manual — Exam question bank (ODT from Downloads, 44 okruhů of frequent exam questions, no answers). Added "## Časté otázky u zkoušky" section (grouped questions + short answers + same-page jump-links) between Shrnutí and Plné znění on okruhy 1–15. All anchors verified.
- [2026-06-03 19:00:00 +0200] INGEST source="_raw/szz-16..44.md" pages_created=29 mode=raw — Built remaining okruhy 16–44 in the same hybrid format (Shrnutí + Časté otázky + verbatim Plné znění + nav). Each source read and validated; Plné znění kept verbatim (only header strip + img→wikilink). Added "## Časté otázky u zkoušky" to all 29 from the question bank. Flagged 6 source inaccuracies/scope notes with "> [!note] Ke kontrole" (okruhy 17, 20, 26, 27, 30, 31). Deleted promoted _raw/szz-16..44.md.
- [2026-06-03 19:00:00 +0200] VALIDATE All 44 okruhy: 894 image embeds resolve, all same-page anchors resolve, all [[okruhy/...]] cross-links resolve, no leftover conversion artifacts. index.md rebuilt as full 1–44 TOC.
- [2026-06-03 19:30:00 +0200] WIKI_SYNTHESIZE pages_scanned=44 synthesis_created=5 candidates_skipped=4 — Vytvořeny průřezové stránky: Konečné automaty napříč obory; Zásobník napříč obory; Spektrální analýza × konvoluce × filtry; Vyhledávací stromy × paměťová hierarchie; Transakce a ACID DB × OS. Zpětné odkazy přidány do 15 okruhů (sekce „## Související syntéza").
- [2026-06-03 19:45:00 +0200] WIKI_SYNTHESIZE pages_scanned=44 synthesis_created=4 candidates_skipped=0 — Doplněny 4 zbývající průřezové stránky: Asymptotická složitost napříč algoritmy; Kryptografie × autentizace; Přerušení × události × signály; Relace × graf × tabulka. Celkem 9 syntéz, zpětné odkazy ve 22 okruzích.
