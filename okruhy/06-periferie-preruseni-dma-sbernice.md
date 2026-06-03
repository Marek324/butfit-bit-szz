---
title: "6. Principy řízení a připojování periferních zařízení (přerušení, programová obsluha, přímý přístup do paměti, sběrnice)"
category: okruh
okruh: 6
tags: [computer-architecture, io, hardware, embedded]
aliases: [přerušení, polling, DMA, sběrnice, mapovaný IO, izolovaný IO, řadič periferního zařízení]
relationships:
  - target: "[[okruhy/05-vestavene-systemy]]"
    type: related_to
  - target: "[[okruhy/07-princip-cinnosti-pocitace-pipelining]]"
    type: related_to
sources: ["_sources/docx/szz-06.docx"]
summary: Principy připojení a obsluhy periferií — přerušení, programová obsluha (polling), přímý přístup do paměti (DMA) a sběrnice.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 6. Řízení a připojování periferních zařízení

> SZZ okruh 6 (FIT BUT). Přístup k periferiím řídí **řadič periferního zařízení** (datový, řídicí a stavový registr). Navazuje na [[okruhy/05-vestavene-systemy|rozhraní MCU]].

## Shrnutí

## Logické a fyzické připojení

- **Mapovaný IO** — registry zařízení na adresách hlavní paměti (sdílený adresový prostor, adresový dekodér).
- **Izolovaný IO** — oddělený adresový prostor, speciální instrukce (IN/OUT).
- Fyzicky: **point-to-point** (vyhrazené vodiče, vysoká propustnost, např. PCIe) × **sběrnice** (sdílené vodiče, levné, škálovatelné, nižší propustnost).

## Přerušení

Mechanismus pro **asynchronní** obsluhu událostí (z periferií i z CPU — např. dělení 0):
1. Periferie vyvolá přerušení na řadiči.
2. Řadič identifikuje a upozorní CPU.
3. CPU dokončí instrukci, vyžádá nejprioritnější nemaskované přerušení.
4. Uloží stav (EFLAGS, CS, IP) na **zásobník**.
5. Podle **vektoru přerušení** spustí **obslužnou rutinu**.
6. Obnoví stav a pokračuje.

![[media/szz-06/media/image2.png]]
*Obsluha přerušení — řadič přerušení mezi periferiemi a CPU.*

## Polling a DMA

- **Programová obsluha (polling)** — program se periodicky dotazuje na stav zařízení; jednoduché, ale **neefektivní**.
- **DMA (Direct Memory Access)** — řadič DMA přenáší data mezi periferií a pamětí **bez zatížení CPU**; po dokončení vyvolá přerušení. Vhodné pro velké objemy dat.

## Sběrnice

- Definuje komunikační **rozhraní**, **protokol** a **transakce**; kanály: **adresa, data, řízení**.
- Synchronní (řízena hodinami) × asynchronní (MSYN/SSYN).
- Přidělování: centrální × decentralizované; prioritní × spravedlivé × cyklické × náhodné.

![[media/szz-06/media/image3.png]]
*Připojení periferie přes řadič — systémová a V/V sběrnice (adresa, data, řízení, stav).*

## Souvislosti

Přerušení jsou zdrojem **řídicích hazardů** v [[okruhy/07-princip-cinnosti-pocitace-pipelining|zřetězené lince]] a základ [[okruhy/13-graficka-uzivatelska-rozhrani|systémů řízených událostmi]].


## Související syntéza

- [[synthesis/preruseni-udalosti-signaly|Přerušení × události × signály]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Připojování periferií** ↪ [[#Logické a fyzické připojení]]
- *Jak se PZ připojují logicky?* → mapovaný IO (registry na adresách hlavní paměti, adresový dekodér) nebo izolovaný IO (vlastní adresový prostor, instrukce IN/OUT).
- *Fyzické typy?* → point-to-point (vyhrazené vodiče, vysoká propustnost, PCIe) vs. sběrnice (sdílené vodiče, levné, škálovatelné).

**Přerušení** ↪ [[#Přerušení]]
- *Polling vs. přerušení?* → Polling = CPU se periodicky ptá (plýtvá výkonem); přerušení = PZ samo asynchronně upozorní (efektivní).
- *Průběh obsluhy?* → CPU dokončí instrukci, uloží stav (EFLAGS, CS, IP) na zásobník, podle vektoru přerušení spustí obslužnou rutinu, pak obnoví stav.
- *Maskování / nemaskovatelná?* → Maskovaná lze dle priority ignorovat; nemaskovatelná (např. reset) ne.

**DMA** ↪ [[#Polling a DMA]]
- *Co je DMA?* → Řadič DMA přenáší data mezi PZ a pamětí bez zatížení CPU; po dokončení vyvolá přerušení. Vhodné pro velké objemy dat.

**Sběrnice** ↪ [[#Sběrnice]]
- *Co sběrnice definuje?* → rozhraní (vodiče + el. charakteristiky), protokol, transakce; kanály adresa / data / řízení.

## Plné znění (ke studiu)

Přístup k periferním zařízením řídí **řadič
periferního zařízení** (každé periferní zařízení má svůj řadič), jeho
funkce jsou:

- **komunikace s CPU**,

- **vyvolání přerušení**,

- **řízení** a časování **operací** periferních
  zařízení,

- realizace vyrovnávací paměti,

- detekce a reportování poruch.

Řadič periferních zařízení obsahuje registry, kterými
procesor se zařízením komunikuje - **datový register**, **řídící
register**, **stavový registr**.

Logicky lze periferní zařízení připojit dvěma způsoby
(logicky, tj. pro přístup v kódu):

- **mapovaný IO**: registry pro ovládání zařízení
  jsou **namapovány** na adresy **hlavní paměti**, periferní zařízení
  (registry) a paměť **sdílí stejný adresový prostor** a CPU tak může
  operace s periferním zařízením provádět stejně jako operace s pamětí
  (čtení a zápis). Řešení využívá **adresový dekodér**.

- **izolovaný IO**: hlavní paměť a periferní zařízení
  mají **různé adresové prostory**. Operace s periferními zařízeními
  provádí procesor pomocí speciálních instrukcí, např. **IN**, **OUT**
  nebo **READ**, **WRITE**.

Fyzicky (kabelem) lze periferních zařízení obecně
připojit dvěma způsoby:

- **Point-to-point linky**: Mezi **každými dvěmi**
  zařízeními (většinou je jeden ze dvojice **CPU**), které chtějí
  komunikovat je nutné vést k tomu vyhrazené vodiče.

  - **výhody**: kratší vodiče - vyšší kmitočty a
    **rychlost** přenosu, komunikace 1 ku 1, současně může komunikovat
    **více párů** zařízeních - **velká propustnost**.

  - **nevýhody**: velký **počet** vodičů, **cena**,
    složitost, zařízení musí mít adekvátní počet vstupů/výstupů.

  - Například
    [<u>PCIe</u>](https://en.wikipedia.org/wiki/PCI_Express) (PCI
    Express, [<u>rozšířený
    popis</u>](https://www.design-reuse.com/articles/38437/challenges-in-verifying-pci-express-in-complex-socs.html)):
    jednotlivá zařízení jsou zapojena do crossbar switche v root
    complexu, pomocí pomocných komunikačních protokolů se identifikují
    zařízení a root complex si vybírá s jakým zařízením bude
    komunikovat.

- **Sběrnice**: **velký** počet zařízení sdílí
  poměrně **malý** počet vodičů (připojují se na jeden centrální). Jedná
  se např. o Universal Serial Bus (**USB**), Peripheral Component
  Interconnect (**PCI**), I2C

  - **výhody**: **nižší** počet vodičů, **levné**,
    lze dobře **škálovat**, zařízení stačí **jeden vstup/výstup** pro
    komunikaci s více jinými zařízeními.

  - **nevýhody**: delší vodiče - nižší kmitočty -
    **pomalejší** přenos, současně může komunikovat pouze **jeden pár**
    zařízení (respektive pouze jedno zařízení může v daný okamžik
    **vysílat**, přijímat mohou všechny) - **nižší propustnost**,
    složitější komunikace - **výběr příjemce**.

## Přerušení

Přerušení, respektive **obsluha přerušení**, je
mechanismus, kterým lze obsloužit **asynchronně** vznikající události
mimo procesor - z **periferních zařízeních**, např. úder do klávesnice
(přerušení mohou vznikat i **uvnitř** procesoru, např. **dělení 0**,
umožňuje tak OS řešit tyto události, případně mohou být vyvolána i
programově). Průběh obsluhy přerušení:

1.  Periferní zařízení vyvolá přerušení (elektrický
    impuls) na řadiči přerušení.

2.  Řadič přerušení identifikuje a upozorní
    procesor.

3.  Jakmile CPU je ve stavu, kdy může přerušení
    obsloužit (dokončí instrukci), požádá řadič o aktuálně
    **nejprioritnější nemaskované** přerušení a započne jeho
    obsluhu.

4.  CPU uloží **stav** aktuálně běžícího procesu na
    **zásobník** (register EFLAGS, CS a IP).

5.  Na základě vektoru přerušení vybere **obslužnou
    rutinu** (její adresu v paměti), vyhledá ji a spustí (skočí na danou
    adresu v paměti).

6.  Po dokončení obslužné rutiny **obnoví stav**
    přerušeného programu a pokračuje v jeho vykonávání.

**Priorita přerušení** udává, v jakém **pořadí**
budou přerušení zpracována, pokud jich současně vznikne více. Existují
maskovatelná přerušení, která procesor
ignoruje.
![[media/szz-06/media/image2.png]]


## Programová obsluha (polling)

Jedná se o nenáročný a **neefektivní** způsob obsluhy
periferních zařízení. Běžící program se **periodicky dotazuje** ve
smyčce na periferní zařízení, jestli nedošlo ke změně jeho stavu (stisk
klávesy). Běžící program tak zbytečně plýtvá výpočetním výkonem a
elektrickou energií, protože změny stavu zařízení vznikají v poměru k
testování na tyto změny málo často.

## Přímý přístup do paměti (DMA - Direct Memory Access)

Koncept přerušení je nevýhodný, pokud je třeba
přenášet **větší objemy dat**. Při obsluze přerušení se procesor
**podílí na datových přenosech**, což ho zatěžuje. Přímý přístup do
paměti umožňuje přenášet data z periferního zařízení do paměti nebo z
paměti do paměti bez zatížení procesoru. Ten tak může provádět výpočet
běžícího programu. Proces přímého přístupu do paměti probíhá
následovně.

1.  CPU předá **řadiči DMA** (specializovaný obvod,
    který obstarává přímý přístup do paměti) **adresu** v paměti,
    **adresu** periferního zařízení, **druh přenosu** (čtení/zápis) a
    **počet** přenášených **slov**.

2.  Řadič DMA provádí **přesun** dat **bez** zásahu
    CPU, který může vykonávat další kód. Procesor je **omezen** na
    využití sběrnice.

3.  Po **dokončení** přenosu dat (případně při chybě)
    **řadič DMA** zasílá procesoru **přerušení**, čímž ho o této
    skutečnosti informuje.

Rozšířením řadiče DMA je koncept IO procesoru, což je
co-procesor, řídící IO periferních zařízení.

## Sběrnice

Jedná se o propojovací soustavu umožňující komunikaci
mezi **více** než jedním **zdrojem** dat a **přijímači** dat. Zajišťuje
přenos dat a řídících povelů mezi nimi a definuje:

- **komunikační rozhraní**: soustava vodičů, jejich
  význam a elektrické charakteristiky.

- **komunikační protokol**: přesně **určuje**, jak
  bude **komunikace** mezi dvěma zařízeními **probíhat**, např. definuje
  **pořadí změn hodnot signálů** (viz start a stop condition u
  I2C)

- **transakce** (cyklus): **posloupnost** kroků,
  která **realizuje** danou funkci, např. přečtení dat z adresy.

### Způsoby komunikace

popis viz minulá otázka.

- **synchronní - asynchronní,**

- **sériová - paralelní,**

- **simplex - half duplex - full duplex.**

- **jednostranně** (bez handshake) **- oboustranně**
  (potvrzení přenosu - handshake)

### Druhy sběrnic

- **Sériová**/**Paralelní sběrnice** - viz okruh
  5.

- **Interní/Externí sběrnice** - Pro propojení
  interních nebo externích periferií.

- **Nesdílená (Dedikovaná) sběrnice** - Pro každý
  **signál (data, adresa, řízení)** je samostatný vodič. Připojení pouze
  jednoho zařízení.

- **Sdílená sběrnice** - Všechny signály se posílají
  po **společné** sadě vodičů. Pro rozlišení o jaký signál se jedná se
  používají **identifikační signály** (adresy).

### Komunikační kanály
![[media/szz-06/media/image3.png]]


- **Adresa**

- **Data**

- **Řízení**

### Parametry

- **Rychlost sběrnice** - určuje ji **šířka
  sběrnice**, **technologie** (paralelni/sériová), **kmitočet**
  synchronizačních hodin.

- **Šířka pásma** - **šířka sběrnice \* rychlost
  sběrnice**

### Synchronní sběrnice

Komunikace řízena hodinovým signálem, který je
rozveden do všech
zařízení.
![[media/szz-06/media/image1.png]]


### Asynchronní sběrnice

Generování signálů je **vázáno** na **výskyt**
událostí, obvykle zařízení mají signály definující začátek a konec
čtení/zápisu (**MSYN** a **SSYN**).\

![[media/szz-06/media/image4.png]]


### Rozhodování o přidělení sběrnice

Pokud současně žádá o přidělení sběrnice více
zařízení, musí být nějak zajištěno, aby na ni vysílalo vždy pouze jedno.
Pro zajištění se používají přístupy:

- **centrální řízení** x **decentralizované
  řízení**,

- **prioritní přístup** x **spravedlivé přidělování
  sběrnice** x **cyklické přidělování** x **náhodné**.

## Zdroje

- SZZ okruh 6 — studijní materiály FIT BUT (`szz-06.docx`). Další obrázky: `media/szz-06/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/05-vestavene-systemy|5. Vestavěné systémy]] · další: [[okruhy/07-princip-cinnosti-pocitace-pipelining|7. Princip činnosti počítače]] ▶
