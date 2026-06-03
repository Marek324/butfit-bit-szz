---
title: Relace × graf × tabulka (jeden objekt, tři obory)
category: synthesis
tags: [math, discrete-math, graph-theory, databases]
sources: ["okruhy/16-mnoziny-relace-zobrazeni.md", "okruhy/25-teorie-grafu.md", "okruhy/36-relacni-data-sql-transakce.md"]
summary: „Relace = podmnožina kartézského součinu" je jediná definice, která se vrací jako relace v diskrétní matematice, jako graf v teorii grafů a jako tabulka v relačním modelu.
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

# Relace × graf × tabulka

## Spojení

Tatáž věta — **„relace je podmnožina kartézského součinu"** — je základem tří různých okruhů:

- **[[okruhy/16-mnoziny-relace-zobrazeni|okruh 16]]** — binární relace **R ⊆ A×B**; vlastnosti (reflexivní, symetrická, tranzitivní); **ekvivalence** a **uspořádání**.
- **[[okruhy/25-teorie-grafu|okruh 25]]** — graf **JE relace** na vrcholech (hrany ⊆ V×V); relace „spojeno sledem" je **ekvivalence** → komponenty souvislosti.
- **[[okruhy/36-relacni-data-sql-transakce|okruh 36]]** — relace v DB **JE podmnožina kartézského součinu domén** = **tabulka**.

## Kde se potkávají

Okruh 25 sám říká, že graf je speciální případ binární relace; okruh 36 odvozuje „tabulku" přímo z matematické definice relace (16). Tatáž definice, tři jména.

## Průřezový poznatek

**Jeden a tentýž matematický objekt (podmnožina kartézského součinu) je „relace" v diskrétní matematice, „graf" v teorii grafů a „tabulka" v databázích.** ^[inferred]

- **Ekvivalence** z okruhu 16 se doslova objevuje jako **komponenty souvislosti** grafu (25) a stojí za **seskupováním** dat.
- Když rozkládáš množinu podle ekvivalence (16), hledáš komponenty souvislosti (25) nebo děláš `GROUP BY` (36), provádíš **tutéž algebru**. ^[inferred]
- Název **„relační model"** (36) pochází přímo z této definice — není to náhodné pojmenování.

## Napětí a kompromisy

- **Abstraktní × konečná struktura**: matematická relace (16) může být nekonečná a bez omezení; DB relace (36) je **konečná tabulka s integritními omezeními** (klíče). Abstrakce získává praktickou strukturu (integrita, klíče) za cenu obecnosti.
- **Orientace**: graf (25) bývá symetrický (neorientovaný) i nesymetrický (orientovaný) — což je přesně vlastnost *symetrie relace* z 16; v DB se „směr" projevuje cizím klíčem (kdo na koho odkazuje).

## Otevřené otázky

- Jak se *zobrazení/funkce* (16, speciální relace s nejvýše jedním obrazem) promítá do DB (funkční závislost, [[okruhy/35-konceptualni-modelovani-db|normalizace]])?

## Související

- [[okruhy/16-mnoziny-relace-zobrazeni]]
- [[okruhy/25-teorie-grafu]]
- [[okruhy/36-relacni-data-sql-transakce]]
- [[okruhy/35-konceptualni-modelovani-db]]
