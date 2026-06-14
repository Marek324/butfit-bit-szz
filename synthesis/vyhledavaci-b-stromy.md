---
title: Vyhledávací stromy × paměťová hierarchie (od ADT k disku)
category: synthesis
tags: [data-structures, algorithms, operating-systems, databases]
sources: ["topics/29-datove-ridici-struktury.md", "topics/30-vyhledavani-razeni.md", "topics/38-sprava-souboru-pameti.md", "topics/04-hierarchie-pameti.md"]
summary: Vyvážený vyhledávací strom se objevuje na třech úrovních abstrakce; přechod z RAM na disk mění nákladový model a binární strom se mění na B+ strom.
provenance:
  extracted: 0.2
  inferred: 0.7
  ambiguous: 0.1
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
created: 2026-06-03T19:30:00Z
updated: 2026-06-03T19:30:00Z
---

# Vyhledávací stromy × paměťová hierarchie

## Spojení

Vyvážený vyhledávací strom vypadá v každém okruhu jinak, ale je to **jedna myšlenka (logaritmická hloubka) přeladěná podle toho, kde data leží**:

- **[[topics/29-datove-ridici-struktury|okruh 29]]** — binární strom jako **ADT**; vyvažování (AVL, red-black) drží O(log n) a brání degradaci na seznam.
- **[[topics/30-vyhledavani-razeni|okruh 30]]** — **BVS** pro vyhledávání a **stromy s více klíči ve vrcholech (B/B+)**, které snižují výšku.
- **[[topics/38-sprava-souboru-pameti|okruh 38]]** — **B+ stromy** jako reálná organizace souborů/DB **na disku**.

## Kde se potkávají

Pojem „mnoho klíčů v jednom uzlu" se objeví v 30 (zrychlení vyhledávání) i v 38 (uložení na disk) — ale **teprve dohromady dává smysl**: snižování výšky stromu má cenu právě tehdy, když je každý sestup do nižší úrovně drahý.

## Průřezový poznatek

**Jak se posouváme od RAM k disku, mění se nákladový model a datová struktura se podle toho proměňuje.** ^[inferred]

- V RAM ([[topics/04-hierarchie-pameti|okruh 4]]) je náhodný přístup levný → stačí **binární** strom (vyvážený AVL/red-black).
- Na disku je drahý **blokový I/O** (čtení celého alokačního bloku) → každý sestup o úroveň = jedno čtení bloku. Proto **B+ strom**: vysoký fan-out (mnoho klíčů/uzel = málo úrovní = málo čtení) a **propojené listy** pro sekvenční průchod.

Otázka „proč mít mnoho klíčů v uzlu" (okruh 30) má odpověď až ve vrstvě úložiště (okruh 38): **velikost uzlu ≈ velikost diskového bloku**. Stejné O(log n), jiná báze logaritmu — a ta báze je tažená paměťovou hierarchií. ^[inferred]

## Napětí a kompromisy

- **Výška × šířka uzlu**: binární strom má nejjednodušší uzel, ale nejvíc úrovní; B+ strom platí složitějším uzlem (štěpení/slučování při vkládání/mazání) za méně I/O. Volba závisí na tom, jestli je úzké hrdlo CPU/RAM nebo disk.
- **Hašování vs. stromy** (okruh 30): hash tabulka dává O(1) bez uspořádání; strom dává O(log n), ale **zachovává pořadí** (rozsahové dotazy, sekvenční scan) — proto DB indexy volí B+ strom, ne hash, když potřebují rozsahy.

## Otevřené otázky

- Kde přesně leží hranice, za kterou se vyplatí B+ strom místo binárního — jak ji určuje poměr velikosti bloku a velikosti klíče?

## Související

- [[topics/29-datove-ridici-struktury]]
- [[topics/30-vyhledavani-razeni]]
- [[topics/38-sprava-souboru-pameti]]
- [[topics/04-hierarchie-pameti]]
