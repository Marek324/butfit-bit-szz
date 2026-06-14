---
title: Asymptotická složitost napříč algoritmy
category: synthesis
tags: [algorithms, complexity, theory]
sources: ["topics/32-slozitost-algoritmu.md", "topics/25-teorie-grafu.md", "topics/26-reseni-uloh-prohledavani.md", "topics/30-vyhledavani-razeni.md"]
summary: Asymptotická složitost je společné měřítko, kterým se na stejné úrovni porovnávají řazení, grafové algoritmy i prohledávání; tytéž vzorce (cykly→polynom, rekurze→exponenciála) se opakují všude.
provenance:
  extracted: 0.2
  inferred: 0.7
  ambiguous: 0.1
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
created: 2026-06-03T19:45:00Z
updated: 2026-06-03T19:45:00Z
---

# Asymptotická složitost napříč algoritmy

## Spojení

[[topics/32-slozitost-algoritmu|Okruh 32]] definuje aparát (O/Ω/Θ, P/NP, určování z cyklů a rekurze) — a ten **se používá jako jednotné měřítko v každém algoritmickém okruhu**:

- **[[topics/30-vyhledavani-razeni|okruh 30]]** — řazení O(n²) vs. O(n log n), dolní mez porovnávacího řazení **O(n log n)**, vyhledávání O(log n)/O(1).
- **[[topics/25-teorie-grafu|okruh 25]]** — Dijkstra O((V+E)·log V), Kruskal O(E·log V), BFS/DFS O(V+E).
- **[[topics/26-reseni-uloh-prohledavani|okruh 26]]** — prohledávání s faktorem větvení **b^d**, kritéria úplnost/optimalita vedle složitosti.

## Kde se potkávají

Pojmy „nejhorší případ", „faktor větvení", „logaritmická hloubka" zaznívají ve 25, 26 i 30 — ale teprve okruh 32 dává formální rámec, proč jsou srovnatelné.

## Průřezový poznatek

**Tentýž asymptotický rámec dovoluje postavit vedle sebe řadicí, grafový i AI-search algoritmus na stejné misky vah; opakují se v něm tytéž vzorce.** ^[inferred]

- **Vnořené cykly → polynom** (bubble sort O(n²) v 30, násobení matic O(n³) v 32).
- **Rekurze / faktor větvení → exponenciála** (b^d u prohledávání v 26, 2ⁿ u rekurze v 32).
- **Půlení → logaritmus** (binární vyhledávání v 30, hloubka vyvážených stromů, Dijkstra s haldou v 25).

Dolní meze fungují všude stejně: **O(n log n) pro porovnávací řazení** (30) i **b^d blowup** u neinformovaného prohledávání (26) říkají „rychleji to bez další informace nepůjde" — heuristika (A*, 26) nebo struktura klíče (radix, 30) jsou způsoby, jak mez obejít. ^[inferred]

Prostorová složitost přitom propojuje tento okruh se [[synthesis/zasobnik-napric-obory|zásobníkem]]: hloubka rekurze = paměť (Quicksort O(log n) stack, DFS O(b·d)). ^[inferred]

## Napětí a kompromisy

- **Čas × paměť**: Merge sort O(n log n) za cenu O(n) paměti vs. in-situ Heap sort (30); BFS úplné, ale paměťově drahé vs. DFS úsporné (26). Stejný kompromis, jiná doména.
- **Průměrný × nejhorší případ**: Quicksort O(n log n) prům. / O(n²) nejhorší (30) — asymptotika sama neřekne, který případ nastane; proto se u řazení sleduje i *přirozenost*.

## Otevřené otázky

- Kde v těchto okruzích narážíme na **NP** úlohy (32) a co to znamená pro praktickou řešitelnost (heuristiky v 26)?

## Související

- [[topics/32-slozitost-algoritmu]]
- [[topics/25-teorie-grafu]]
- [[topics/26-reseni-uloh-prohledavani]]
- [[topics/30-vyhledavani-razeni]]
- [[synthesis/zasobnik-napric-obory]]
