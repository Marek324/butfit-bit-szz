# SZZ wiki — FIT BUT (bakalářské státnice)

Studijní wiki pokrývající **všech 44 okruhů** státní závěrečné zkoušky. Je to **Obsidian vault** — pro plný zážitek (klikací odkazy `[[…]]`, vložené obrázky, graf) ji **otevři v [Obsidianu](https://obsidian.md)**: *Open folder as vault* → vyber tuto složku. V GitHubu / běžném prohlížeči markdownu se wikilinky a obrázky nezobrazí pěkně.

Vault je zároveň připravený jako **[LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** ve smyslu [Andreje Karpathyho](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — destilované markdown stránky, na které stačí namířit schopného coding agenta (např. Claude Code) a ptát se; odpovědi čerpá přímo z těchto okruhů, ne z prázdna.

## Kde začít

➡️ Otevři **[[index]]** (`index.md`) — je to **rozcestník se všemi 44 okruhy** rozdělenými do tematických bloků. Klikni na okruh, nebo čti popořadě.

## Struktura každého okruhu

Každá stránka v `okruhy/` má stejné tři vrstvy (čti shora dolů):

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
| **`okruhy/`** | 44 stránek `NN-nazev.md`, jedna na okruh (číslované → řadí se 01→44) |
| **`synthesis/`** | 9 **průřezových** stránek — pojmy, co se vrací napříč okruhy (automaty, zásobník, Fourier, B+ stromy, transakce/ACID, složitost, kryptografie, přerušení, relace) |
| **`media/`** | ~855 obrázků a schémat (`szz-NN/…`), vkládané do stránek |
| **`index.md`** | rozcestník — **začni tady** |
| `_sources/docx/` | původní docx, ze kterých wiki vznikla |
| `_raw/` | zdrojové podklady (mj. soubor častých otázek) |
| `_meta/taxonomy.md` | seznam tagů |

## ⚠️ Než tomu uvěříš na 100 %

Plné znění je **doslovně převzaté** ze studentských materiálů (které samy disklejmují správnost) — neupravoval jsem ho. Při kontrole jsem našel **10 míst s možnou nepřesností**, každé označené blokem **`> [!note] Ke kontrole`** přímo na stránce. **Osm** z nich jsou **ověřené chyby zdroje** (ověřeno proti standardům/učebnicím):

- **okruh 9** — hranice IEEE 754 jsou o jedničku posunuté (správně single 2⁻¹²⁶/2⁻¹⁴⁹, double 2⁻¹⁰²²/2⁻¹⁰⁷⁴).
- **okruh 31** — t-test ↔ z-test prohozené (t-test = *neznámý* rozptyl).
- **okruh 1** — „záměnou tranzistorů z NAND vznikne OR" je chybně; statické CMOS hradlo je vždy invertující (OR/AND až s invertorem).
- **okruh 14** — FFT není „jen pro N = mocnina 2" (to platí jen pro radix-2); JPEG navíc používá DCT.
- **okruh 15** — pro číslicové (diskrétní) filtry je to Z-transformace, ne Laplaceova (vnitřní nekonzistence okruhu).
- **okruh 17** — typ extrému se určuje definitností Hessovy matice, ne znaménkem jediné hodnoty.
- **okruh 20** — infimum/supremum = největší dolní / nejmenší horní závora, ne „menší/větší z operandů".
- **okruh 30** — Merge sort není „in situ"; vyžaduje O(n) pomocné paměti.

Zbylé dva flagy (okruhy **26, 27**) nejsou chyby, ale **poznámky k rozsahu** zkoušení — ověř si u své komise. Ber wiki jako **studijní pomůcku, ne ověřenou pravdu** — u označených míst si fakt ověř.

## PDF (k tisku / offline)

> [!warning] Neudržováno
> Tahle část mě nezajímá a **aktivně ji neudržuju** — skript ani návod nemusí odpovídat aktuálnímu stavu. Ber jako „funguje mi to lokálně", ne jako podporovanou cestu.

PDF se **negenerují automaticky ani neverzují** v repu — vyrobíš si je lokálně skriptem `scripts/build_pdf.py` (pandoc + LuaLaTeX). Výstup jde do `build/` (ignorováno gitem).

**Potřebuješ:** `pandoc`, LuaLaTeX engine (balík `texlive-luatex`) a fonty **Noto Serif** + **Noto Sans Mono** (`fonts-noto`). Python prostředí spravuje [uv](https://docs.astral.sh/uv/) — skript samotný je jen standardní knihovna (žádné pip závislosti). Poradí si s Obsidian syntaxí (vložené obrázky `![[…]]`, wikilinky, callouty) i s matematikou (`$…$`).

```bash
uv sync                                              # připraví .venv (jednou)

# jeden okruh                         → build/okruhy/<slug>.pdf
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
