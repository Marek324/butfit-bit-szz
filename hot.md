---
title: Hot Cache
updated: 2026-06-03 19:00:00 +0200
---

# Hot Cache

*A ~500-word semantic snapshot of recent activity. Updated after every major write operation.*

## Recent Activity

- [2026-06-03 19:45:00 +0200] SYNTÉZA — vytvořeno **9 průřezových stránek** v `synthesis/` (automaty; zásobník; Fourier×konvoluce×filtry; vyhledávací/B+ stromy; transakce/ACID; složitost napříč algoritmy; kryptografie×autentizace; přerušení×události×signály; relace×graf×tabulka); zpětné odkazy ve **22 okruzích**. Také accuracy pass (viz Flagged Contradictions) — 10 flagů, 2 web-ověřené chyby (okruh 9, 31).
- [2026-06-03 19:00:00 +0200] HOTOVO — **všech 44 okruhů zpracováno** v hybridní podobě (Shrnutí + Časté otázky u zkoušky + Plné znění s diagramy + navigace). Dokončeny okruhy 16–44 (matematika/logika, formální jazyky, překladače, numerika, grafy, AI/ML, simulace, programování, algoritmy, statistika, SWE/UML, DB, web, OS, sítě). Validace: 894 obrázků, anchors i cross-linky OK. `index.md` = úplný obsah 1–44. `_raw/szz-*.md` smazány (zbývá jen `caste-otazky-szz.md`).
- [2026-06-03 16:56:21 +0200] OTÁZKY — integrován soubor častých zkouškových otázek do sekcí „Časté otázky u zkoušky".
- [2026-06-03 16:05:00 +0200] HYBRID — zavedena struktura Shrnutí + Plné znění s vloženými diagramy.

## Active Threads

- Obsah je kompletní. Možné navazující kroky: `cross-linker` (hlubší provázání), `wiki-synthesize` (průřezové souhrny), `wiki-lint` (kontrola zdraví), případně extrakce sdílených `concepts/` stránek pro opakující se pojmy (RISC/CISC, automaty, Fourier, stromy).

## Key Takeaways

- **Dvě osy přístupu**: lineárně okruh po okruhu (navigace ◀ ▶ + obsah v `index.md`) i průchodem po cross-lincích mezi okruhy.
- **Plné znění je verbatim** ze zdroje (jen strip hlavičky + `<img>`→`![[...]]`), text nebyl měněn — dle zadání.
- **6 míst „Ke kontrole"**: okruh 17 (extrémy více proměnných / Hessián), 20 (infimum/supremum — zdroj se sám opravuje), 26 a 27 (rozsah zkoušení), 30 (Merge sort „in situ"), 31 (t-test vs. známý/neznámý rozptyl).

## Flagged Contradictions

Po dedikovaném accuracy passu (web-ověřeno u 9 a 31) — **10 flagů**, all as `> [!note]` in pages:

- **okruh 9** — IEEE 754 hranice o jedničku posunuté (single 2^-127/2^-150 → správně 2^-126/2^-149; double 2^-1023/2^-1075 → 2^-1022/2^-1074). **Ověřeno proti standardu.** (nejvýznamnější)
- **okruh 31** — t-test „se známým rozptylem"; správně t-test = neznámý, z-test = známý. **Ověřeno (Penn State, Wikipedia).**
- **okruh 1** — „záměnou tranzistorů v CMOS NAND vznikne OR"; statické CMOS je vždy invertující, OR/AND vyžadují invertor.
- **okruh 14** — „FFT jen pro mocninu 2"; platí jen pro radix-2, obecně libovolné N. (+ JPEG používá DCT)
- **okruh 15** — přenosová funkce „pomocí Laplaceovy transformace"; u diskrétních filtrů Z-transformace (vnitřní nekonzistence).
- **okruh 20** — infimum/supremum zprvně „menší/větší z operandů" (zdroj se sám opravuje).
- **okruh 17** — extrémy funkcí více proměnných: Hessián vs. „gradient druhé derivace".
- **okruh 30** — Merge sort „in situ, O(log n)"; potřebuje O(n) pomocné paměti.
- **okruhy 26, 27** — poznámky o rozsahu zkoušení (ne chyba obsahu).

Cross-okruh konzistence ověřena (RISC/CISC, automaty, Fourier, B+ stromy, ACID, Dijkstra) — bez rozporů.
