---
title: Konečné automaty × hardware × jazyky × překladače
category: synthesis
tags: [theory, automata, computer-architecture, compilers]
sources: ["topics/03-sekvencni-logicke-obvody.md", "topics/10-fpga-vhdl.md", "topics/21-regularni-jazyky.md", "topics/22-bezkontextove-jazyky.md", "topics/23-struktura-prekladace.md"]
summary: Konečný automat je jeden matematický objekt, který se vrací ve čtyřech okruzích jako sekvenční obvod, akceptor regulárních jazyků, scanner a řídicí automat — a jeho hranice určuje fáze překladače.
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

# Konečné automaty × hardware × jazyky × překladače

## Spojení

Konečný automat **M = (Q, Σ, …)** není „téma jednoho okruhu" — je to **jeden a tentýž objekt**, který se v různých okruzích objevuje v jiném kabátě:

- **[[topics/03-sekvencni-logicke-obvody|okruh 3]]** — FSM jako **hardware**: Mealy/Moore automat = registr stavu (klopné obvody) + kombinační next-state logika.
- **[[topics/21-regularni-jazyky|okruh 21]]** — FSM jako **akceptor jazyka**: DFA/NFA rozpoznávající regulární jazyk; přesně tatáž pětice.
- **[[topics/23-struktura-prekladace|okruh 23]]** — FSM jako **scanner**: lexikální analýza je implementace DKA (switch ve while cyklu).
- **[[topics/10-fpga-vhdl|okruh 10]]** — FSM jako **řídicí automat** datové cesty v RT metodologii návrhu FPGA.
- **[[topics/22-bezkontextove-jazyky|okruh 22]]** — FSM **rozšířený o zásobník** = zásobníkový automat (viz [[synthesis/zasobnik-napric-obory]]).

## Kde se potkávají

Definice automatu z okruhu 3 (Mealy/Moore) a z okruhu 21 (DFA/NFA) jsou **tatáž matematika** zapsaná dvakrát. Okruh 23 to spojuje prakticky: scanner *je* DKA z okruhu 21 a zároveň sekvenční obvod ve smyslu okruhu 3.

## Průřezový poznatek

**Hierarchie automatů přímo mapuje na fáze překladu i na hardware.** ^[inferred]

- Co umí rozpoznat **bezpaměťový** automat = **regulární jazyk** = co zvládne **lexikální analýza** (DKA) = co zvládne **fixní sekvenční obvod** s konečným počtem stavů.
- Přidáním **zásobníku** (PDA) skočíme na **bezkontextové jazyky** = doménu **syntaktické analýzy** (parser).

Jinými slovy: **LA = konečný automat, SA = zásobníkový automat** není náhoda — je to přímý důsledek Chomského hierarchie. Stejná hranice „kolik paměti automat má" odděluje (a) co jde rozpoznat fixním HW stavovým strojem, (b) regulární vs. bezkontextové jazyky, (c) scanner vs. parser. ^[inferred]

## Napětí a kompromisy

- **Moore vs. Mealy** (okruh 3) je návrhový kompromis (zpoždění výstupu × méně stavů), který v teorii jazyků (okruh 21) nehraje roli — oba přijímají tytéž regulární jazyky. Stejný objekt, jiná optimalizační kritéria podle vrstvy.
- **NFA ↔ DFA** (okruh 21) je „zdarma" v teorii (determinizace), ale v HW (okruh 3) by nedeterminismus znamenal nerealizovatelnost — proto se scanner staví vždy nad **deterministickým** automatem.

## Otevřené otázky

- Kde přesně leží UML stavový diagram ([[topics/34-uml|okruh 34]]) na této ose — je to jen vizualizace Mealy/Moore, nebo přidává sémantiku navíc?

## Související

- [[topics/03-sekvencni-logicke-obvody]]
- [[topics/21-regularni-jazyky]]
- [[topics/22-bezkontextove-jazyky]]
- [[topics/23-struktura-prekladace]]
- [[topics/10-fpga-vhdl]]
- [[synthesis/zasobnik-napric-obory]]
