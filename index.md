---
title: Wiki Index
---

# Wiki Index — szz (FIT BUT státnice)

*This index is automatically maintained. Last updated: 2026-06-03 19:00:00 +0200*

Wiki je organizovaná podle **okruhů státní závěrečné zkoušky**. Každá stránka má strukturu **Shrnutí → Časté otázky u zkoušky → Plné znění (ke studiu)** a na konci **navigaci ◀ ▶**. Lze tak číst **lineárně okruh po okruhu** i procházet po **provázaných odkazech** mezi souvisejícími tématy. **Všech 44 okruhů zpracováno.**

## Okruhy (otázky SZZ)

### Technické vybavení a logika (1–10)

1. [[topics/01-polovodicove-prvky-cmos|Princip činnosti polovodičových prvků (dioda, BJT, MOSFET, CMOS)]]
2. [[topics/02-kombinacni-logicke-obvody|Kombinační logické obvody (mux, dekodér, sčítačka)]]
3. [[topics/03-sekvencni-logicke-obvody|Sekvenční logické obvody (klopné obvody, automaty)]]
4. [[topics/04-hierarchie-pameti|Hierarchie paměti (lokalita, cache)]]
5. [[topics/05-vestavene-systemy|Vestavěné systémy (MCU, rozhraní, převodníky)]]
6. [[topics/06-periferie-preruseni-dma-sbernice|Řízení a připojování periferií (přerušení, DMA, sběrnice)]]
7. [[topics/07-princip-cinnosti-pocitace-pipelining|Princip činnosti počítače (pipelining, RISC, CISC)]]
8. [[topics/08-minimalizace-logickych-vyrazu|Minimalizace logických výrazů (Karnaugh, Quine-McCluskey)]]
9. [[topics/09-reprezentace-cisel-ieee754|Reprezentace čísel a binární aritmetika (IEEE 754)]]
10. [[topics/10-fpga-vhdl|Technologie FPGA a popis HW (VHDL)]]

### Grafika a signály (11–15)

11. [[topics/11-2d-vektorova-grafika|2D vektorová grafika (rasterizace, Bézier)]]
12. [[topics/12-3d-transformace-pipeline|Transformace 3D modelů a vykreslovací řetězec]]
13. [[topics/13-graficka-uzivatelska-rozhrani|Principy grafických uživatelských rozhraní]]
14. [[topics/14-spektralni-analyza|Spektrální analýza signálů (Fourier, DFT, FFT)]]
15. [[topics/15-cislicove-filtry|Číslicové filtry (FIR/IIR, přenosová funkce)]]

### Matematika a teorie (16–25)

16. [[topics/16-mnoziny-relace-zobrazeni|Množiny, relace a zobrazení]]
17. [[topics/17-diferencialni-integralni-pocet|Diferenciální a integrální počet]]
18. [[topics/18-ciselne-soustavy|Číselné soustavy a převody mezi nimi]]
19. [[topics/19-vyrokova-predikatova-logika|Výroková a predikátová logika]]
20. [[topics/20-boolovy-algebry|Boolovy algebry]]
21. [[topics/21-regularni-jazyky|Regulární jazyky (konečné automaty, regulární výrazy)]]
22. [[topics/22-bezkontextove-jazyky|Bezkontextové jazyky (zásobníkové automaty, gramatiky)]]
23. [[topics/23-struktura-prekladace|Struktura překladače a fáze překladu]]
24. [[topics/24-numericke-metody|Numerické metody]]
25. [[topics/25-teorie-grafu|Teorie grafů (nejkratší cesta, minimální kostra)]]

### Algoritmy, AI a programování (26–32)

26. [[topics/26-reseni-uloh-prohledavani|Řešení úloh (prohledávání, hraní her)]]
27. [[topics/27-strojove-uceni|Strojové učení]]
28. [[topics/28-modelovani-simulace|Modelování a simulace systémů]]
29. [[topics/29-datove-ridici-struktury|Datové a řídicí struktury imperativních jazyků]]
30. [[topics/30-vyhledavani-razeni|Vyhledávání a řazení]]
31. [[topics/31-pravdepodobnost-statistika|Pravděpodobnost a statistika]]
32. [[topics/32-slozitost-algoritmu|Hodnocení složitosti algoritmů]]

### Softwarové inženýrství, databáze, sítě (33–44)

33. [[topics/33-zivotni-cyklus-sw|Životní cyklus softwaru]]
34. [[topics/34-uml|Jazyk UML]]
35. [[topics/35-konceptualni-modelovani-db|Konceptuální modelování a návrh relační databáze]]
36. [[topics/36-relacni-data-sql-transakce|Strukturovaná data, relační model, SQL, transakce]]
37. [[topics/37-webova-rozhrani-autentizace|Webová rozhraní, správa sezení a autentizace]]
38. [[topics/38-sprava-souboru-pameti|Principy správy souborů a paměti]]
39. [[topics/39-planovani-synchronizace-procesu|Plánování a synchronizace procesů]]
40. [[topics/40-objektova-orientace|Objektová orientace]]
41. [[topics/41-assembler|Programování v jazyku symbolických instrukcí (assembler)]]
42. [[topics/42-sluzby-aplikacni-vrstvy|Služby aplikační vrstvy (web, e-mail, DNS, SNMP, NetFlow)]]
43. [[topics/43-tcp-ip-komunikace|TCP/IP komunikace]]
44. [[topics/44-smerovani-zabezpeceni-siti|Směrování a zabezpečení přenosů v sítích]]

## Stav

- **44 / 44** okruhů zpracováno (`topics/`), všechny v hybridní podobě (Shrnutí + Časté otázky + Plné znění).
- Diagramy (≈894 vložených) jsou ve `media/szz-NN/`.
- Zkušební otázky integrovány ze souboru `_raw/caste-otazky-szz.md`.
- **10 míst** označeno `> [!note] Ke kontrole` — okruhy **1, 9, 14, 15, 17, 20, 26, 27, 30, 31**. Z toho **8 ověřených chyb zdroje**: okruh 9 (IEEE 754 hranice o jedničku posunuté), 31 (t-test/z-test prohozeny), 1 (CMOS hradla vždy invertující), 14 (FFT ne jen pro N=2ᵏ; JPEG=DCT), 15 (Z- místo Laplaceovy transformace), 17 (definitnost Hessiánu), 20 (inf/sup = největší dolní/nejmenší horní závora), 30 (Merge sort není in-place). Okruhy 26, 27 jsou jen poznámky k rozsahu zkoušení.

## Concepts

*Sdílené průřezové pojmy nejsou vyčleněny — okruhy se prolinkují přímo mezi sebou. Pro hlubší provázání lze spustit `cross-linker`, pro souhrny `wiki-synthesize`.*

## Entities

## Skills

## References

## Synthesis

Průřezové stránky propojující pojmy, které se vrací napříč okruhy:

- [[synthesis/konecne-automaty-napric-obory]] — KA jako HW, akceptor jazyka, scanner i řídicí automat (okruhy 3, 10, 21, 22, 23)
- [[synthesis/zasobnik-napric-obory]] — zásobník/rekurze: PDA, DFS, parser, call stack, stack procesu (22, 23, 26, 29, 39, 41)
- [[synthesis/fourier-konvoluce-filtry]] — spektrální analýza ↔ filtry přes konvoluční teorém + FFT (14, 15)
- [[synthesis/vyhledavaci-b-stromy]] — vyhledávací stromy od ADT k disku (B+); vliv paměťové hierarchie (29, 30, 38, 4)
- [[synthesis/transakce-acid-db-os]] — transakce a ACID: co se přenáší mezi DB a OS (36, 38, 39)
- [[synthesis/slozitost-napric-algoritmy]] — asymptotická složitost jako společné měřítko (25, 26, 30, 32)
- [[synthesis/kryptografie-autentizace]] — krypto primitiva a jejich použití na webu/e-mailu (37, 42, 44)
- [[synthesis/preruseni-udalosti-signaly]] — asynchronní obsluha: IRQ, GUI události, signály (6, 13, 39)
- [[synthesis/relace-napric-obory]] — relace = graf = tabulka (16, 25, 36)

## Journal
