# SZZ wiki — FIT BUT (bakalářské státnice)

Studijní wiki pokrývající **všech 44 okruhů** státní závěrečné zkoušky. Je to **Obsidian vault** — pro plný zážitek (klikací odkazy `[[…]]`, vložené obrázky, graf) ji **otevři v [Obsidianu](https://obsidian.md)**: *Open folder as vault* → vyber tuto složku. V GitHubu / běžném prohlížeči markdownu se wikilinky a obrázky nezobrazí pěkně.

Vault je zároveň připravený jako **[LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** ve smyslu [Andreje Karpathyho](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — destilované markdown stránky, na které stačí namířit schopného coding agenta (např. Claude Code) a ptát se; odpovědi čerpá přímo z těchto okruhů, ne z prázdna.

## Kde začít

➡️ Otevři **[[index]]** (`index.md`) — je to **rozcestník se všemi 44 okruhy** rozdělenými do tematických bloků. Klikni na okruh, nebo čti popořadě.

## Struktura každého okruhu

Každá stránka v `topics/` má stejné tři vrstvy (čti shora dolů):

1. **## Shrnutí** — destilovaný přehled + odkazy na související okruhy + klíčové diagramy s popisky. Na rychlé zopakování.
2. **## Časté otázky u zkoušky** — na co se zkoušející typicky ptají, se stručnými odpověďmi a odkazy do plného znění. *(Zdroj: sdílený soubor častých otázek.)*
3. **## Plné znění (ke studiu)** — **kompletní text** ke každému okruhu se **všemi obrázky**. Hlavní materiál na učení.

Dole je vždy **navigace ◀ ▶** na předchozí/další okruh, takže jdou číst „jeden po druhém".

## Dvě osy čtení

- **Lineárně** — okruh 1 → 2 → … → 44 (navigace dole na každé stránce + obsah v `index.md`).
- **Po souvislostech** — okruhy se vzájemně prolinkují (sekce „Souvislosti" a `[[odkazy]]` v textu).

## Složky

| Složka / soubor | Co obsahuje |
|---|---|
| **`topics/`** | 44 stránek `NN-nazev.md`, jedna na okruh (číslované → řadí se 01→44) |
| **`synthesis/`** | 9 **průřezových** stránek — pojmy, co se vrací napříč okruhy (automaty, zásobník, Fourier, B+ stromy, transakce/ACID, složitost, kryptografie, přerušení, relace) |
| **`media/`** | ~855 obrázků a schémat (`szz-NN/…`), vkládané do stránek |
| **`index.md`** | rozcestník — **začni tady** |
| `_sources/docx/` | původní docx, ze kterých wiki vznikla |
| `_raw/` | zdrojové podklady (mj. soubor častých otázek) |
| `_meta/taxonomy.md` | seznam tagů |

## ⚠️ Než tomu uvěříš na 100 %

Plné znění je **doslovně převzaté** ze studentských materiálů (které samy disklejmují správnost) — neupravoval jsem ho. Při kontrole jsem narazil na **několik nepřesností** (většinou ověřených chyb zdroje, plus pár poznámek k rozsahu zkoušení). Každá je označená blokem **`> [!note] Ke kontrole`** přímo na dané stránce. Ber wiki jako **studijní pomůcku, ne ověřenou pravdu** — u označených míst si fakt ověř.

## PDF (k tisku / offline)

> [!warning] Bez záruky
> Tohle mi **fungovalo lokálně**, ale pořádně to neověřuju — nechce se mi to procházet. Takže klidně **může být něco rozbité**; ber to jako „takhle si to vyrábím já", ne jako prověřený postup.

PDF se **negenerují automaticky ani neverzují** v repu — vyrobíš si je lokálně skriptem `scripts/build_pdf.py` (pandoc + LuaLaTeX). Výstup jde do `build/` (ignorováno gitem).

**Potřebuješ:** `pandoc`, LuaLaTeX engine (balík `texlive-luatex`) a fonty **Noto Serif** + **Noto Sans Mono** (`fonts-noto`). Python prostředí spravuje [uv](https://docs.astral.sh/uv/) — skript samotný je jen standardní knihovna (žádné pip závislosti). Poradí si s Obsidian syntaxí (vložené obrázky `![[…]]`, wikilinky, callouty) i s matematikou (`$…$`).

```bash
uv sync                                              # připraví .venv (jednou)

# jeden okruh                         → build/topics/<slug>.pdf
uv run scripts/build_pdf.py topic 09-reprezentace-cisel-ieee754

# jedna syntéza                       → build/synthesis/<slug>.pdf
uv run scripts/build_pdf.py synthesis relace-napric-obory

# bez slugu = vyrobí všechny jednotlivě
uv run scripts/build_pdf.py topic
uv run scripts/build_pdf.py synthesis

# sloučené dokumenty
uv run scripts/build_pdf.py topics      # všechny okruhy   → build/szz-okruhy.pdf
uv run scripts/build_pdf.py syntheses   # všechny syntézy  → build/szz-syntezy.pdf
uv run scripts/build_pdf.py all         # úplně vše        → build/szz-vse.pdf
```

Engine i fonty jdou přepsat: `--engine xelatex`, `--mainfont "…"`, `--monofont "…"`. Nápověda: `uv run scripts/build_pdf.py -h`. (Bez uv funguje i `python scripts/build_pdf.py …`.)

---
*Wiki byla sestavena z docx podkladů; obsah je v češtině (jazyk zkoušky). Hodně štěstí u státnic! 🎓*
