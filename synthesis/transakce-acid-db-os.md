---
title: Transakce a ACID — databáze × operační systém
category: synthesis
tags: [databases, operating-systems, concurrency]
sources: ["topics/36-relacni-data-sql-transakce.md", "topics/38-sprava-souboru-pameti.md", "topics/39-planovani-synchronizace-procesu.md"]
summary: Pojem transakce přechází mezi databází a OS, ale ACID plně platí jen v DB; atomicita je přenositelné jádro, kdežto trvalost a konzistence se nepřenášejí čistě. Žurnálování je znovupoužitý DB write-ahead log.
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

# Transakce a ACID — databáze × operační systém

## Spojení

„Transakce" se objevuje ve třech okruzích, ale **ACID v plné síle platí jen v jednom**:

- **[[topics/36-relacni-data-sql-transakce|okruh 36]]** — databázová transakce = plné **ACID** (Atomicity, Consistency, Isolation, Durability); BEGIN/COMMIT/ROLLBACK.
- **[[topics/39-planovani-synchronizace-procesu|okruh 39]]** — transakce na úrovni **OS** (skupina operací jako celek); sám okruh upozorňuje, že definice ACID „**nemusí být přesná**" — např. trvalost (durability) u přepnutí kontextu nezajistíme.
- **[[topics/38-sprava-souboru-pameti|okruh 38]]** — zápis na disk přes **žurnálování** (REDO/UNDO) — týž princip jako zotavení DB.

## Kde se potkávají

Okruh 39 explicitně srovnává OS transakci s databázovou ACID a říká, kde se rozcházejí. Okruh 38 ukazuje konkrétní mechanismus (žurnál), který je 1:1 s databázovým **write-ahead logem** z okruhu 36.

## Průřezový poznatek

**Atomicita je přenositelné jádro „transakce" napříč DB i OS; trvalost a sémantická konzistence jsou části, které se čistě nepřenášejí.** ^[inferred]

- **Atomicity** (vše/nic) má smysl všude: DB transakce, skupina OS operací, zápis bloku na disk.
- **Durability** se na úrovni OS láme — přepnutí kontextu nelze „učinit trvalým" při pádu systému (okruh 39).
- **Consistency** ve smyslu *významu dat* nedokáže OS posoudit (okruh 38 zajistí jen, že **bity** jsou zapsané přesně) — sémantickou konzistenci hlídá až aplikace/DB.
- **Žurnálování** souborového systému (38) je doslova znovupoužitý nápad DB recovery (36): zapiš záměr do logu, pak teprve data; po pádu REDO/UNDO. ^[inferred]

Souvislost se [[topics/39-planovani-synchronizace-procesu|synchronizací]]: izolace (I) v DB je tatáž starost jako **kritická sekce / race condition** u procesů — souběžný přístup ke sdílenému stavu se řeší vzájemným vyloučením v obou světech. ^[inferred]

## Napětí a kompromisy

- **Plné ACID stojí výkon** (zámky, log, fsync). OS i DB proto nabízejí slabší úrovně izolace / „jednopříkazové" operace bez explicitní transakce, když konzistence není kritická.
- **Isolation × propustnost**: striktní serializace transakcí (36) brání souběhu — stejný kompromis jako preemce vs. konzistence u plánování procesů (39).

## Otevřené otázky

- Jak přesně mapovat úrovně izolace DB (read committed, serializable…) na synchronizační primitiva OS (semafor, monitor)?

## Související

- [[topics/36-relacni-data-sql-transakce]]
- [[topics/39-planovani-synchronizace-procesu]]
- [[topics/38-sprava-souboru-pameti]]
