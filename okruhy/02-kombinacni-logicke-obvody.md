---
title: "2. Kombinační logické obvody (multiplexor, demultiplexor, kodér, dekodér, binární sčítačka)"
category: okruh
okruh: 2
tags: [digital-logic, hardware, computer-architecture]
aliases: [multiplexor, demultiplexor, kodér, dekodér, sčítačka, half adder, full adder, CLA]
relationships:
  - target: "[[okruhy/01-polovodicove-prvky-cmos]]"
    type: uses
  - target: "[[okruhy/03-sekvencni-logicke-obvody]]"
    type: related_to
sources: ["_sources/docx/szz-02.docx"]
summary: Obvody bez paměti, jejichž výstup závisí pouze na aktuální kombinaci vstupů — multiplexor, dekodér, kodér a binární sčítačky (RCA, CLA).
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

# 2. Kombinační logické obvody

> SZZ okruh 2 (FIT BUT). **Kombinační obvod** nemá paměť — výstup závisí **pouze** na aktuální kombinaci vstupů. Staví se z hradel popsaných v [[okruhy/01-polovodicove-prvky-cmos]].

## Shrnutí

## Výběrové obvody

- **Multiplexor** — z N řídicích vstupů vybírá na výstup hodnotu jednoho z až **$2^N$** vstupů.
- **Demultiplexor** — opačně: vstup posílá na jeden z $2^N$ výstupů.

![[media/szz-02/media/image20.png]]
*Multiplexor — výběr jednoho z $2^N$ vstupů podle řídicích vstupů.*

![[media/szz-02/media/image23.png]]
*Demultiplexor — směrování vstupu na jeden z výstupů.*

## Kódovací obvody

- **Kodér / dekodér** — převádějí informaci podle kombinační tabulky.
- **Binární kodér** — zakóduje $2^N$ vstupů (vždy aktivní právě jeden) na N výstupů.
- **Binární dekodér** — N vstupů → $2^N$ výstupů (aktivní jeden výstup); lze realizovat demultiplexorem.
- **Prioritní kodér** — připouští více aktivních vstupů, kóduje ten s nejvyšší prioritou (využití v obsluze [[okruhy/06-periferie-preruseni-dma-sbernice|přerušení]] a ve [[okruhy/05-vestavene-systemy|Flash ADC]]).

## Binární sčítačky

- **Poloviční sčítačka (half adder)** — sčítá dva bity → součet **S** a přenos **C**; neumí zpracovat přenos z nižšího řádu.
- **Úplná sčítačka (full adder)** — přidává vstupní přenos C.

![[media/szz-02/media/image9.png]]
*Poloviční sčítačka (half adder).*

- **Ripple Carry Adder (RCA)** — řetězení úplných sčítaček, přenos se postupně šíří → pomalé; zpoždění S_i ≈ 3·i − 1 logických členů.

![[media/szz-02/media/image4.png]]
*Ripple Carry Adder — postupné šíření přenosu (carry).*

- **Carry Lookahead Adder (CLA)** — paralelní výpočet přenosů přes **generate (G)** a **propagate (P)**: C_{i+1} = G_i + P_i·C_i. Rychlejší, ale nákladnější; pro velká čísla se kombinuje přes **LCU**.

## Souvislosti

Doplnění o paměťový prvek (klopný obvod D) vede na [[okruhy/03-sekvencni-logicke-obvody]] (např. sekvenční sčítačka). Aritmetické principy rozvíjí [[okruhy/09-reprezentace-cisel-ieee754]].


## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Obecná teorie**
- *Kombinační vs. sekvenční obvod?* → Kombinační nemá paměť (výstup jen z aktuálních vstupů); sekvenční má vnitřní stav.
- *Formy popisu?* → pravdivostní tabulka, logický výraz, schéma.
- *NAND vs. NOR — ekvivalence?* → Obě jsou funkčně úplné — z každé lze sestavit libovolnou logickou funkci.

**Multiplexor / demultiplexor** ↪ [[#Výběrové obvody]]
- *Co je MUX/DMX?* → MUX vybírá z N řídicích vstupů jeden z $2^N$ datových na výstup; DMX opačně (1 → jeden z $2^N$).
- *Vztah počtu vstupů a řídicích?* → $2^N$ datových ↔ N řídicích.

**Kodér / dekodér** ↪ [[#Kódovací obvody]]
- *Dekodér?* → N vstupů → $2^N$ výstupů, aktivní právě jeden.
- *Binární vs. prioritní kodér?* → Binární vyžaduje právě jeden aktivní vstup; prioritní připouští více a kóduje ten s nejvyšší prioritou.

**Sčítačky (HA/FA)** ↪ [[#Binární sčítačky]]
- *Half vs. full adder?* → HA: S=A⊕B, C=A∧B (neumí vstupní přenos); FA přidává vstupní přenos C.
- *Vícebitová sčítačka a zpoždění?* → Zřetězení FA = RCA, přenos se šíří → zpoždění lineární (~3·i členů).
- *RCA vs. CLA?* → CLA počítá přenosy paralelně přes generate/propagate (G,P) → rychlejší, ale dražší.

## Plné znění (ke studiu)

Kombinační obvod je takový, kde jsou **hodnoty
výstupních hodnot závislé pouze na kombinaci hodnot na vstupu**. Tedy
nemají paměť.

## **Multiplexor** 

Kombinací **N** **řídících vstupů** vybírá na
**výstup hodnotu jednoho** z až **$2^N$** vstupů.\

![[media/szz-02/media/image20.png]]

![[media/szz-02/media/image18.png]]



![[media/szz-02/media/image3.png]]


2-1 multiplexor pomocí **NOT**, **AND**,
**OR**
![[media/szz-02/media/image7.png]]


> 2-1 multiplexor pomocí **NAND** hradel
>
> 
![[media/szz-02/media/image22.png]]
 style="width:3.99479in;height:1.5242in" />

## Demultiplexor

Kombinací **N** **řídících vstupů** vysílá vstup na
jeden z obvykle **$2^N$** **výstupů**.\

![[media/szz-02/media/image23.png]]




1-2 demultiplexor pomocí **NOT** a **AND**
hradel


![[media/szz-02/media/image17.png]]

![[media/szz-02/media/image10.png]]


1-2 demultiplexor pomocí **NAND**
hradel
![[media/szz-02/media/image11.png]]


## Kodér a dekodér

**Kodér** kóduje (**kombinuje**, převádí) informaci z
**N** vstupů na **K** výstupů na základě **kombinační tabulky**. Obecně
platí, že $N > K$ (jinak jde spíš o dekodér) a $2^K \geq N$ (jinak
nelze zaručit jednoznačné kódování).

**Dekodér** je kombinační logický obvod
**komplementární** ke kodéru. Dekóduje (**kombinuje**, převádí)
informaci z **N** vstupů na **K** výstupů. Obecně platí, že $N < K$.

- To znamená, že zapojení kodéru a za ním dekodéru se
  **stejnou kombinační** tabulkou, která je **jednoznačná** (pro každý
  vstup generuje unikátní výstup), se bude chovat, jako by tam nebyl ani
  jeden. Může jít například o kodér ze **7-segmentového displeje** na
  **BCD** (nepoužívá se…) a dekodér z **BCD** na **7-segmentový
  displej.**

| **vstupní kód** | **výstupní kód** |
|----|----|
| 0 | 11 |
| 1 | 00 |
| 2 | 10 |
| 3 | 01 |


![[media/szz-02/media/image19.png]]


## Binární kodér (Encoder)

Umožňuje na **N** **výstupů** zakódovat až **$2^N$**
**vstupů**. Musí ale platit, že vždy je **aktivní** **pouze jeden** ze
vstupů. Pomocí kodéru lze například převádět stisknutou klávesu (vstup)
na její binární hodnotu. Klávesa 0 je zapojena na první vstup, klávesa 1
na druhý atd. Na výstupu je poté 0b0000 pro klávesu 0, 0b0001 pro
klávesu 1, 0b0010 pro klávesu 2, …


![[media/szz-02/media/image1.png]]


## Binární dekodér (Decoder)

Dekóduje **N vstupů** na **$2^N$ výstupů**, narozdíl od
kodéru mohou být vstupy libovolně aktivní. Pro daný vstup je ale aktivní
vždy **pouze jeden výstup**. Dekodér lze například použít pro adresaci
zařízení na sběrnici (binární adresa umožňuje aktivovat jedno z
připojených zařízení). Dekodér lze implementovat pomocí
**demultiplexoru**, vstup se zapojí na log. 1 a na **sel** se zapojí
vstupy.

## Prioritní kodér
![[media/szz-02/media/image5.png]]


Narozdíl od běžného binárního kodéru umožňuje mít na
**vstupu více aktivních vodičů**. V tom případě na výstup kóduje hodnotu
odpovídající tomu s **největší prioritou**. Využívá se například k
řízení **obsluhy přerušení**. Na obrázku má **I(3)**

![[media/szz-02/media/image13.png]]
**největší**
prioritu a I(0) nejmenší.

## Binární sčítačka
![[media/szz-02/media/image6.png]]


- **Poloviční sčítačka** (**half adder**) - realizuje
  sčítání dvou jednobitových čísel. Výstupem je **jednobitový součet**
  (**S**) a jednobitový **příznak přenosu** do vyššího řádu (**C**).
  Poloviční sčítačka ale sama **nedokáže zpracovat přenos z nižšího
  řádu**.
![[media/szz-02/media/image9.png]]


- **Úplná sčítačka** (**full adder**) - narozdíl od
  poloviční sčítačky umožňuje zpracovat i přenos z nižšího řádu. Vstupem
  jsou tedy sčítance **A**, **B** a přenos z nižšího řádu **C**.
  Výstupem je součet **S** a přenos do vyššího řádu **C**.

> 
![[media/szz-02/media/image2.png]]
 style="width:3.56983in;height:1.18994in" />
![[media/szz-02/media/image15.png]]
 style="width:3.51563in;height:1.57937in" />

- **Sčítačka s přenosem (Ripple carry adder)** -
  Vzniká propojením více úplných sčítaček, tak aby se mohl šířit carry
  bit. **Pseudoparalelní**, přenos carry se **postupně šíří sčítačkou**.
  Poměrně pomalá kvůli čekání na carry bit. Zpoždění každého carry bitu
  je rovno zpoždění **3 log. členů**, zpoždění sečtení je rovno zpoždění
  **2 log. členů**. Z toho plyne, že zpoždění **S_i = 3\*(i-1) + 2 =
  3\*i - 1** (i-1, protože na 1. carry bit se nečeká, **i** je od 1 -
  značí počet bitů sčítačky)\
  
![[media/szz-02/media/image4.png]]
 

  - RCA lze urychlit **sčítačkou s výběrem přenosu
    (carry-select adder)** - předpočítáním si výsledků pro carry = 0 i
    carry = 1; 4 bitovými sčítačkami a zvolení těch správných pomocí
    multiplexoru na základě výsledků z předchozích sčítaček. Zpoždění
    této sčítačky je rovno zpoždění 4 bitové RCA sčítačky včetně carry =
    **4\*3 = 12 log. členů** a zpoždění 3 multiplexorů = **3\*3** = **9
    log. členů**. Celkově tedy **21 log.
    členů**.
![[media/szz-02/media/image24.png]]


  - libovolně dlouhá binární čísla lze také sečíst
    jednou **úplnou binární sčítačkou** za využití **posuvných
    registrů** (pro sčítance a součet; délka registrů určuje maximální
    délku binárního čísla) a **klopného obvodu typu D**, který je použit
    pro zapamatování si carry bitu (přenosu) **nejedná se kombinační
    obvod**.\
    
![[media/szz-02/media/image8.png]]


- **Sčítačka s predikcí přenosu (CLA - Carry
  Lookahead Adder)** - Rychlejší jak **RCA**, výpočet opravdu probíhá
  paralelně, teoreticky lze sečíst dvě jakkoliv dlouhá bitová čísla s
  **konstantním zpožděním** S_i = **4 log. členů** (a se zpožděním carry
  bitu C_i = **3 log. členů**). Reálně je délka sčítaných čísel omezena
  schopností implementovat **více vstupá hradla s ekvivalentním
  zpožděním jako dvouvstupá**, počtem hradel sčítačky a s tím
  souvisejícím počtem spojů. Pro velká čísla přestává být tudíž
  praktická (náročná na výrobu, vysoká cena atd.) a je potřeba výpočet
  rozdělit. [<u>16-bit adder using 4-bit
  CLA</u>](https://youtu.be/1CgzmPFrsaI)

  - z tabulky vstupů do CLA lze odvodit carry bit
    **C_i+1 = A_i and B_i or (A_i xor B_i) and C_i = G_i or P_i and
    C_i** (G - generate, P - propagate).\
    Z těchto rovnic lze učit, že výpočet **C_i** bude mít zpoždění **3
    log. členů**, v případě, že máme více vstupá hradla (1. - A xor
    B, 2. P and C, 3. or všech
    vstupů).
![[media/szz-02/media/image21.png]]


  - výpočet **S_i** bude probíhat jako **((A_i xor
    B_i) xor C_i)**, což znamená zpoždění dalšího log. členu a celkově
    tedy **4. log
    členů**.
![[media/szz-02/media/image16.png]]


- **Vícebitové sčítačky s použitím 4 bitových
  (případně více) CLA sčítaček:**

  - zřetězení CLA sčítaček ve stylu RCA sčítačky,
    např. 16 bitová sčítačka pomocí 4 CLA sčítaček bude mít zpoždění
    **C_16 = 4\*3 = 12 log.** členů a zpoždění **S_15 = 3\*3 + 4 = 13
    log. členů** (3x carry + poslední výpočet).

  - spojením více CLA sčítaček pomocí **LCU
    (lookahead carry unit)**, které dokáží opět s **konstantní
    rychlostí** spočítat přenosy mezi jednotlivými CLA sčítačkami.
    **C_4**, **C_8**, **C_12** a **C_16** jsou dle rovnice níže
    vypočteny se zpožděním **5 log. členů** a protože **G** a **P** již
    jsou vypočteny, zabere výpočet **S_i4** až **S_i15** už jen další
    **3 log. členy** a zpoždění tak bude celkem **8 log.
    členů**.
![[media/szz-02/media/image12.png]]


  - obdobně jde vytvořit pomocí čtyř 16 bitových
    **LCU** sčítaček 64 bitovou sčítačku s dalším zanořením
    **LCU**. 
![[media/szz-02/media/image14.png]]


## Zdroje

- SZZ okruh 2 — studijní materiály FIT BUT (`szz-02.docx`). Další obrázky: `media/szz-02/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/01-polovodicove-prvky-cmos|1. Polovodičové prvky]] · další: [[okruhy/03-sekvencni-logicke-obvody|3. Sekvenční logické obvody]] ▶
