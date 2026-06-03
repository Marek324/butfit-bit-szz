---
title: Přerušení × události × signály (asynchronní obsluha)
category: synthesis
tags: [computer-architecture, operating-systems, gui]
sources: ["okruhy/06-periferie-preruseni-dma-sbernice.md", "okruhy/13-graficka-uzivatelska-rozhrani.md", "okruhy/39-planovani-synchronizace-procesu.md"]
summary: Tentýž vzor asynchronní obsluhy — neptej se (polling), zaregistruj handler, nech se přerušit, ulož kontext, obsluž, obnov — se opakuje od HW přerušení přes GUI smyčku událostí po signály procesů.
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

# Přerušení × události × signály

## Spojení

Asynchronní obsluha události je **jeden vzor na třech vrstvách**:

- **[[okruhy/06-periferie-preruseni-dma-sbernice|okruh 6]]** — **HW přerušení** (IRQ): periferie vyvolá přerušení, CPU uloží stav na zásobník, podle vektoru spustí obslužnou rutinu, pak obnoví stav.
- **[[okruhy/13-graficka-uzivatelska-rozhrani|okruh 13]]** — **systémy řízené událostmi** (GUI): smyčka čeká na událost, detekuje ji a spustí obsluhu; okruh sám říká „HW realizace je přes **přerušení**".
- **[[okruhy/39-planovani-synchronizace-procesu|okruh 39]]** — **signály** = softwarová přerušení procesu; okruh sám uvádí „analogie s HW přerušením", dějí se asynchronně a mají obslužné funkce.

## Kde se potkávají

Oba okruhy 13 i 39 **explicitně odkazují na přerušení** (6) jako na základ: GUI události jsou dole HW přerušení (13), signály jsou SW obdoba HW přerušení (39).

## Průřezový poznatek

**Tentýž tvar řízení toku — „neptej se opakovaně, zaregistruj handler a nech se přerušit" — se opakuje od drátu po proces.** ^[inferred]

- **Polling × přerušení** (6) je tatáž efektivnostní volba jako **polling × event listener** (13): aktivní dotazování plýtvá výkonem, asynchronní upozornění ho šetří.
- Mechanika je všude stejná: **ulož kontext → skoč na handler → obnov kontext** (uložení registrů na zásobník u přerušení v 6 = uložení stavu procesu u signálu v 39 = zachování stavu UI smyčky v 13).
- **DMA** (6) je tentýž princip „nech to udělat asynchronně a dej mi vědět přerušením" aplikovaný na přenos dat.

## Napětí a kompromisy

- **Handler musí být krátký a reentrantní**: ISR má být krátká (6); v obsluze signálu **nelze volat některé funkce** (např. `printf`), protože vznikají asynchronně (39). Asynchronní handlery všude sdílí omezení „buď rychlý a bezpečný vůči souběhu" → vede na [[okruhy/39-planovani-synchronizace-procesu|synchronizaci]] (race condition, kritická sekce).
- **Priorita a maskování** (6) řeší, co když přijde víc přerušení naráz — obdoba priorit a inverze priorit u plánování procesů (39).

## Otevřené otázky

- Jak se vzor „event loop" (13) implementuje nad blokujícími vs. neblokujícími sokety/rourami (38/39) — kde končí přerušení a začíná aktivní `select`?

## Související

- [[okruhy/06-periferie-preruseni-dma-sbernice]]
- [[okruhy/13-graficka-uzivatelska-rozhrani]]
- [[okruhy/39-planovani-synchronizace-procesu]]
