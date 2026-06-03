---
title: "10. Technologie FPGA (vnitřní struktura, LUT), kroky návrhu a základy syntetizovatelného popisu hardware"
category: okruh
okruh: 10
tags: [hardware, fpga, hdl, digital-logic]
aliases: [FPGA, LUT, CLB, VHDL, Verilog, strukturální popis, behaviorální popis, dataflow, logická syntéza]
relationships:
  - target: "[[okruhy/03-sekvencni-logicke-obvody]]"
    type: uses
  - target: "[[okruhy/02-kombinacni-logicke-obvody]]"
    type: uses
sources: ["_sources/docx/szz-10.docx"]
summary: Vnitřní struktura FPGA (CLB, LUT, propojení), postup návrhu shora dolů a strukturální/behaviorální/dataflow popis obvodů v HDL.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 10. Technologie FPGA a syntetizovatelný popis HW

> SZZ okruh 10 (FIT BUT). **FPGA** = programovatelné hradlové pole, kompromis mezi rychlým neměnným **ASIC** a flexibilním SW řešením.

## Shrnutí

## Vnitřní struktura FPGA

- **Configurable Logic Blocks (CLB)** — z více *slice*; obsahují:
  - **LUT (Look-Up Table)** — 2^N bitový registr s výsledky kombinační logiky N proměnných (volatilní → konfigurace z FLASH při startu).
  - **2^N−1 multiplexor** — vybírá hodnotu z LUT podle vstupů.
  - **klopný obvod typu D** — paměť pro [[okruhy/03-sekvencni-logicke-obvody|sekvenční obvody]].
  - **2-1 multiplexor** — volí mezi kombinačním (LUT) a sekvenčním výstupem.
- **Programmable Interconnects** — programovatelné propojení (switch v křížení).
- **Programmable I/O Blocks (IOB)** — propojení s vnějšími piny.
- **Vestavěné bloky** — paměti, sčítačky, násobičky, ethernet.

![[media/szz-10/media/image7.png]]
*Struktura CLB — LUT, multiplexory a klopný obvod typu D.*

## Návrh aplikací (Top-Down)

- Postup **shora dolů**: dekompozice problému na jednoduché komponenty ([[okruhy/02-kombinacni-logicke-obvody|sčítačka]], registr, čítač), verifikace na každé úrovni.
- Metodologie **RT (register transfer)**: stavový automat → datová cesta (datapath) → řídicí signály → řídicí [[okruhy/03-sekvencni-logicke-obvody|Mealy/Moore automat]].

## Popis ve VHDL/Verilog

- **Strukturální** — entita propojením komponent (hradel); návrhář má kontrolu nad výslednou strukturou.
- **Behaviorální** — algoritmický popis chování (procesy běží paralelně, uvnitř sekvenčně); nejabstraktnější.
- **Dataflow** — modelování přes tok dat (paralelní přiřazení signálů).
- **Logická syntéza** — automatická transformace HDL na netlist cílové technologie (FPGA/ASIC) dle constraints (rychlost, spotřeba, plocha).

![[media/szz-10/media/image6.png]]
*Strukturální popis ve VHDL — entita složená propojením komponent.*


## Související syntéza

- [[synthesis/konecne-automaty-napric-obory|Konečné automaty napříč obory]] — syntéza

## Časté otázky u zkoušky

*U tohoto okruhu se ptají hlavně na VHDL. Plné odpovědi níže.*

**VHDL základy** ↪ [[#Popis ve VHDL/Verilog]]
- *Co je VHDL a proč?* → Jazyk pro popis hardwaru (HDL); popis a dokumentace složitých obvodů, simulace i syntéza.
- *Entita vs. architektura?* → Entita = rozhraní modulu (vstupy/výstupy); architektura = jeho vnitřní realizace.
- *Typy architektur?* → behavioral (chování), structural (složení z komponent), dataflow (toky dat).
- *Proces a sensitivity list?* → Proces běží uvnitř sekvenčně a spustí se při změně signálu ze sensitivity listu; více procesů běží navzájem paralelně.
- *Signál vs. proměnná?* → Signál se aktualizuje až po vyhodnocení (se zpožděním), proměnná okamžitě uvnitř procesu.
- *Co lze syntetizovat?* → Ne vše — např. rekurzi ne; syntéza převede syntetizovatelný popis na netlist hardwaru. Simulace umí i nesyntetizovatelné konstrukce.
- *Testbench?* → Testovací prostředí pro simulaci (generuje vstupy, ověřuje výstupy); samo se nesyntetizuje.

**FPGA** ↪ [[#Vnitřní struktura FPGA]]
- *Co je FPGA, LUT, vztah k sekvenčním obvodům?* → Programovatelné hradlové pole; LUT = tabulka realizující kombinační funkci N proměnných; CLB obsahuje LUT + D klopný obvod → umožní i sekvenční obvody.

## Plné znění (ke studiu)

## FPGA (Field Programmable Gate Array)
![[media/szz-10/media/image8.png]]

![[media/szz-10/media/image10.png]]


FPGA je programovatelné hradlové pole, které je
kompromisem mezi pouze HW řešením - ASIC (Application specific
integrated circuit - nejrychlejší, nejúspornější) a pouze SW řešení
(největší flexibilita). Je tvořeno z:

- **Configurable Logic Blocks** (**CLBs**) — umožňují
  naprogramovat logické funkce realizované hardwarově. Jsou tvořeny
  součástkami, které dohromady v nejjednodušším případě mohou tvořit
  jeden **CLB** nebo **slice**. **CLB** může být tvořeno více
  **slice**:

  - Look Up Table (**LUT**): **2^N** bitový register
    obsahující výsledky kombinační logiky **N** proměnných. Jedná se
    volatilní paměť, tzn. konfigurace jednotlivých LUT musí být uložena
    v nevolatilní paměti (FLASH), ze které jsou LUT při spuštění
    nakonfigurovány.

  - **2^N-1** multiplexor: **N** určuje počet
    vstupních proměnných. Pomocí kterého se **vybírá** hodnota z **LUT**
    na výstup na základě hodnot **vstupních proměnných**.

  - klopný obvod (typ **D**): vytváří paměť a
    umožňuje tvorbu sekvenčních obvodů.

  - **2-1** multiplexor: vybírá mezi výstupem z LUT
    (získaného pomocí **2^N-1** multiplexoru) nebo výstupem z klopného
    obvodu. Tento multiplexor tak určuje, jestli půjde o sekvenční. nebo
    kombinační logiku.
![[media/szz-10/media/image7.png]]


  - případně další komponenty…

- **Programmable Interconnects** — programovatelné
  **propojení** mezi **CLBs**, jedná se o spoje vedené horizontálně a
  vertikálně. V místech křížení lze naprogramovat logiku propojování
  (**switch**).

- **Programmable I/O Blocks** (**IOBs**) — slouží k
  propojování **konfigurovatelných logických bloků** s externími
  součástkami pomocí propojovacích **pinů** FPGA čipu.

- **Vestavěné bloky** — paměti, sčítačky, násobičky,
  ethernet, …

# VHDL (VHSIC Hardware Description Language)

## Kroky návrhu aplikací využívajících FPGA

Pro návrh aplikací využívající FPGA se používá systém
návrhu **shora dolů** (**Top-Down**). Začíná z celkového popisu problému
a končí návrhem s úplnou mírou detailů jeho částí - **dekompozice** a
začlenění do celku. Na každé úrovni abstrakce je potřeba **verifikovat
správnou** funkci navrhovaného systému. Dekompozicí vzniknou **jednoduše
realizovatelné komponenty** (sčítačka, posuvný registr, násobička,
čítač, …), které lze popsat ve VHDL nebo Verilog. Např. zpracování
obrazu:

### Metodologie návrhu na úrovni meziregistrových přesunů (RT)
![[media/szz-10/media/image9.png]]


Návrh je vhodné rozdělit do několika kroků:

- **Popis obvodu na úrovni základního stavového
  automatu** - automat popisuje základní stavy obvodu, ale neřeší
  konkrétní nastavení řídících, vstupních nebo výstupních
  signálů.

- **Vytvoření datové cesty (datapath)** - datová
  cesta provádí manipulaci s daty, a to na základě řízení z obecného
  automatu.

- **Identifikace signálů pro řízení datové cesty** -
  definice signálů, které jsou potřeba pro napojení datové cesty na
  řídící blok.

- **Návrh řídícího automatu** - převedení obecného
  automatu na Mealyho nebo Moorův automat, který řídí datovou
  cestu
![[media/szz-10/media/image3.png]]


## Strukturální, behaviorální a dataflow popis ve VHDL

V praxi se typy popisů často kombinují, jedna logika
lze současně popsat strukturálně, behaviorálně i pomocí dataflow. Pomocí
syntézy (něco jako kompilace) jsou tyto popisy převáděny na konkrétní
obvodová řešení pro danou technologii (FPGA, ASIC). VHDL umožňuje také
pouze simulovat dané obvody.

### Strukturální popis

Při strukturálním popisu **definujeme** **entitu**
(např. poloviční sčítačku), **propojením** vstupů a výstupů a
**komponent** (AND a XOR hradla), které realizují logiku entity. Samotné
komponenty mohou být předtím popsány jako entity na nižší úrovni
abstrakce. Strukturální popis **umožňuje rozdělit** **komplexní** systém
**na méně komplexní** části, ty mohou být vyvíjeny a ověřovány samotně.
Návrhář má u tohoto typu popisu kontrolu (pokud komponenty postupně
popisuje od úrovně hradel nebo i níže) nad tím, jak bude výsledný obvod
vypadat (z jakých bude prvků - hradel).

![[media/szz-10/media/image6.png]]


### Behaviorální popis

Popisuje chování systému/funkce/bloku algoritmicky.
Jedná se o nejvíce abstraktní popis. Z behaviorálního popisu není přímo
jasné, jaká bude implementace na úrovni hradel (HW realizace).
Behaviorální popis prvku obsahuje jeden nebo více procesů, které se dějí
paralelně. Popis uvnitř procesu se odehrává sekvenčně. V procesu se
nastavují výstupy na základě hodnot
vstupů.
![[media/szz-10/media/image2.png]]


### Dataflow popis

Pomocí DataFlow popisu se modelují systémy na základě
toho, jak jimi putují data. Tento způsob popisu využívá odpovídající
implementace logických hradel. DataFlow popis popisuje systém/prvek
jedním nebo více přiřazeními paralelních
signálů.
![[media/szz-10/media/image5.png]]


**Logická syntéza**

Automatická transformace mezi různými úrovněmi
popisu. Transformace na jemnější popis s cílem vylepšit parametry zadané
uživatelem: rychlost, spotřeba,
rozměry.
![[media/szz-10/media/image1.png]]


# 
![[media/szz-10/media/image4.png]]


Rozpoznání prvků cílové technologie a jejich mapování
do FPGA. Výsledkem procesu je konfigurační soubor pro FPGA.

**Automatická syntéza:**

- vstup: popis obvodu v HDL, knihovna prvků cílové
  technologie, constraints (např. spotřeba, velikost na čipu,
  čas...)

- výstup: optimalizovaný NetList na úrovni prvků
  cílové technologie

## Zdroje

- SZZ okruh 10 — studijní materiály FIT BUT (`szz-10.docx`). Další obrázky: `media/szz-10/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/09-reprezentace-cisel-ieee754|9. Reprezentace čísel]] · další: [[okruhy/11-2d-vektorova-grafika|11. 2D vektorová grafika]] ▶
