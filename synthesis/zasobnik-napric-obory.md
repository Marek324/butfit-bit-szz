---
title: Zásobník × rekurze napříč obory
category: synthesis
tags: [theory, algorithms, data-structures, operating-systems]
sources: ["topics/22-bezkontextove-jazyky.md", "topics/23-struktura-prekladace.md", "topics/26-reseni-uloh-prohledavani.md", "topics/29-datove-ridici-struktury.md", "topics/39-planovani-synchronizace-procesu.md", "topics/41-assembler.md"]
summary: LIFO zásobník je společný mechanismus za „zanořením" a rekurzí — od zásobníkového automatu přes DFS a parser až po volání funkcí a paměť procesu.
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

# Zásobník × rekurze napříč obory

## Spojení

Zásobník (LIFO) vypadá jako „jen jedna datová struktura z okruhu 29", ale je to **společný mechanismus za vším, co je zanořené nebo rekurzivní**:

- **[[topics/22-bezkontextove-jazyky|okruh 22]]** — zásobník je přesně to, co povýší **regulární → bezkontextové** jazyky (paměť pro zanoření: aⁿbⁿ, párové závorky).
- **[[topics/23-struktura-prekladace|okruh 23]]** — parser používá zásobník (prediktivní analýza, reversal pravidel na zásobník); rekurzivní sestup používá **implicitní** zásobník přes rekurzi.
- **[[topics/26-reseni-uloh-prohledavani|okruh 26]]** — **DFS** a backtracking používají explicitní zásobník (OPEN).
- **[[topics/29-datove-ridici-struktury|okruh 29]]** — zásobník jako ADT; každou **rekurzi lze přepsat na iteraci** s explicitním zásobníkem.
- **[[topics/41-assembler|okruh 41]]** — **zásobníkový rámec** volání funkce (CALL/RET, EBP/ESP), zásobník roste dolů.
- **[[topics/39-planovani-synchronizace-procesu|okruh 39]]** — každý proces/vlákno má **vlastní zásobník**; přepnutí kontextu jej ukládá.

## Kde se potkávají

Tatáž operace „ulož a vrať se později" se objevuje jako zásobník PDA (22), zásobník parseru (23), OPEN v DFS (26), call frame v assembleru (41) a stack vlákna (39). Okruh 29 je pojítko: definuje ADT a explicitně říká, že rekurze ↔ zásobník.

## Průřezový poznatek

**„Zanoření/rekurze" a „zásobník" jsou tatáž věc viděná na různých vrstvách.** ^[inferred]

Bezkontextová gramatika má zanořenou strukturu → potřebuje zásobník (PDA, okruh 22) → ten realizuje parser (23) → a za běhu **to JE procesorový call stack** (rekurzivní sestup, 41) → který OS alokuje per vlákno (39). Hloubka zanoření vaší úlohy = hloubka zásobníku, kterou zaplatíte (pamětí). ^[inferred]

Proto má praktický smysl trik z [[topics/30-vyhledavani-razeni|Quicksortu]] (na zásobník dávat **menší** část → hloubka jen O(log n)): je to tentýž zdrojový limit „kolik zanoření si můžu dovolit", jen vyjádřený v paměťové složitosti ([[topics/32-slozitost-algoritmu|okruh 32]]).

## Napětí a kompromisy

- **Implicitní (rekurze) vs. explicitní zásobník**: rekurze je čitelná, ale hloubka je omezená velikostí stacku vlákna (39) → u hlubokého zanoření hrozí stack overflow; explicitní zásobník (na haldě) to obchází za cenu složitějšího kódu (29).
- PDA z teorie (22) má **neomezený** zásobník; reálný call stack (41/39) je **konečný** — teoretická síla vs. praktický limit.

## Otevřené otázky

- Které reálné jazyky/parsery se záměrně vyhýbají rekurzi kvůli limitu stacku a volí explicitní zásobník?

## Související

- [[topics/22-bezkontextove-jazyky]]
- [[topics/23-struktura-prekladace]]
- [[topics/26-reseni-uloh-prohledavani]]
- [[topics/29-datove-ridici-struktury]]
- [[topics/41-assembler]]
- [[topics/39-planovani-synchronizace-procesu]]
- [[synthesis/konecne-automaty-napric-obory]]
