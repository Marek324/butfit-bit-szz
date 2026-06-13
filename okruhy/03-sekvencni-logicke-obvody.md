---
title: "3. Sekvenční logické obvody (klopné obvody, čítače, registry, stavové automaty – reprezentace a implementace)"
category: okruh
okruh: 3
tags: [digital-logic, hardware, computer-architecture]
aliases: [klopný obvod, flip-flop, čítač, registr, stavový automat, Mealy, Moore, SRAM]
relationships:
  - target: "[[okruhy/02-kombinacni-logicke-obvody]]"
    type: extends
  - target: "[[okruhy/01-polovodicove-prvky-cmos]]"
    type: uses
sources: ["_sources/docx/szz-03.docx"]
summary: Obvody s pamětí, jejichž výstup závisí i na minulých vstupech — klopné obvody, čítače, registry a konečné automaty (Mealy/Moore).
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

# 3. Sekvenční logické obvody

> SZZ okruh 3 (FIT BUT). **Sekvenční obvod** = [[okruhy/02-kombinacni-logicke-obvody|kombinační]] část + **paměť**; výstup závisí na vstupech i na **vnitřním stavu**. Synchronní (řízené CLK) × asynchronní.

## Shrnutí

## Klopné obvody (flip-flops)

- Dělení: **astabilní** (oscilátor), **monostabilní** (časovač/generátor pulzu), **bistabilní** (flip-flop, dva stabilní stavy), **Schmittův** (hystereze).
- **R-S** — set/reset; současné S=R=1 je zakázaná kombinace.
- **J-K** — eliminuje zakázanou kombinaci (J=K=1 → toggle).
- **T** — toggle z J-K se společným vstupem.
- **D** — z R-S (R = ¬S), nikdy nevznikne zakázaný stav; přenáší vstup na výstup se zpožděním.
- **Master-Slave** a **hranové (derivační)** dvoufázové obvody se řídí hodinami **CLK**.

![[media/szz-03/media/image30.png]]
*Klopný obvod se zpětnou vazbou (typ SET) — Moorův výstup se zpožděním Δt.*

![[media/szz-03/media/image20.png]]
*Přechodová tabulka klopného obvodu T: T=0 drží stav (Hold), T=1 překlápí (Toggle).*

## Čítače a registry

- **Čítače** — synchronní/asynchronní; up/down, s výstupem přetečení **RCO/TC**; kaskáda prodlužuje dělicí poměr. Varianty: Grayův, Johnsonův, one-hot.
- **Registry** — z klopných obvodů D; paměťový (latch) a **posuvný (shift)** registr (UART, SPI, ukládání operandů, sekvenční sčítačka).

![[media/szz-03/media/image25.png]]
*4bitový čítač realizovaný klopnými obvody typu T.*

## Stavové automaty

Konečný automat M = (S, Σ, Λ, T, G, s₀): **next-state logika** (kombinační) + **paměť** (stav) + **výstupní funkce**.

- **Mealy** — výstup je funkcí stavu *i* vstupu (Y = f(X, Z)).
- **Moore** — výstup je funkcí pouze stavu (Y = f(Z)), má **zpoždění**.

![[media/szz-03/media/image10.png]]
*Struktura automatu (next-state logika, paměť, výstup) — Moore/Mealy.*

## SRAM

Klopný obvod z **2 PMOS + 4 NMOS** uchovává 1 bit — rychlá paměť pro registry a [[okruhy/04-hierarchie-pameti|cache]] (L1–L3).

![[media/szz-03/media/image21.png]]
*Paměťová buňka SRAM (6 tranzistorů).*

## Souvislosti

Automaty se realizují i ve [[okruhy/10-fpga-vhdl|FPGA]] a jsou základem [[okruhy/21-regularni-jazyky|konečných automatů]] v teorii jazyků.

## Související syntéza

- [[synthesis/konecne-automaty-napric-obory|Konečné automaty napříč obory]] — syntéza (HW × jazyky × překladače)

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Základy** ↪ [[#Klopné obvody (flip-flops)]]
- *Sekvenční vs. kombinační, proč paměť?* → Výstup závisí i na minulých vstupech → nutný vnitřní stav (paměť).
- *Asynchronní vs. synchronní?* → Synchronní řízen hodinami CLK; asynchronní reaguje okamžitě na vstup.

**Klopné obvody** ↪ [[#Klopné obvody (flip-flops)]]
- *Typy a rozdíly?* → RS (zakázaný stav S=R=1), JK (řeší ho, J=K=1 → toggle), D (nikdy zakázaný, vstup → výstup), T (toggle).
- *Hladinové vs. hranové?* → Hladinové reagují po celou úroveň CLK; hranové (derivační) jen na hranu.
- *Metastabilní stav?* → Nestabilní mezistav při porušení setup/hold času; výstup dočasně nedefinovaný.

**Stavové automaty (FSM)** ↪ [[#Stavové automaty]]
- *Moore vs. Mealy?* → Moore: výstup = f(stav) (má zpoždění); Mealy: výstup = f(stav, vstup).
- *Realizace FSM?* → next-state logika (kombinační) + registr stavu (paměť) + výstupní funkce; návrh = definice stavů, přechodů, výstupů.
- *Kódování stavů?* → binární, one-hot, Grayův kód.

**Čítače a registry** ↪ [[#Čítače a registry]]
- *Čítač pomocí D KO?* → Z výstupů a next-state logiky se zapojí D vstupy tak, aby stav přecházel v požadované posloupnosti.

## Plné znění (ke studiu)

**Sekvenční logický obvod (SO)** - Výstup obvodu závisí **nejen na vstupu**, ale také na **minulých vstupech**. Skládají se z **kombinační** části a **paměťové** části. Paměť v sekvenčním obvodu uchovává **vnitřní (současný) stav**.

- **Asynchronní SO** - Změna vstupní hodnoty hned ovlivní výstup. Reagují okamžitě.
- **Synchronní SO** - Řízený **hodinovým signálem**. Až při přechodu hodinového signálu se vstup projeví na výstupu. Reagují v periodických intervalech.
  - **Úrovňové SO** - SO sleduje vstupy po celou dobu hodinového signálu a průběžně na ně reaguje.
  - **Hranové (derivační) SO** - Reaguje na vstupy jen při přechodu hrany (náběžné nebo sestupné).

## Klopný obvod

Klopné obvody jsou nejjednodušší sekvenční obvody. Jedná se o obvody, které **skokově** (neuvažujeme zpoždění změny úrovně hradla) přechází mezi **několika diskrétními stavy**.

Klopné obvodu dělíme na:

- **Astabilní** - nemají žádný stabilní stav - neustále kmitají (**oscilují**).
  - např. pro generování obdélníkového signálu, hodinového signálu
- **Monostabilní** - mají **jeden stabilní stav**, jedná se o sekvenční obvod, který při spuštění **generuje puls**. Lze si jej představit jako misku a do ní hozený míček.
  - časovače
- **Bistabilní (flip-flop)** - nejpoužívanější typ klopných obvodů, má dva stabilní stavy, mezi kterými lze přepínat (**0** a **1**)
  - je základním stavebním prvkem rychlých **volatilních** pamětí (registry, paměti operandů, čítače, …)
- **Schmittovy** - slouží k **úpravě tvaru impulzů**. Jeho základní vlastností je **hystereze**. Jeho výstup je závislý nejen na hodnotě vstupu, ale i na jeho **původním stavu**. Hystereze zabraňuje vzniku **zákmitů** výstupního signálu v okolí **střední** úrovně spínání.

### Bistabilní klopné obvody

- **SET klopný obvod** - velmi jednoduchý, ale prakticky nepoužitelný. Nelze překlopit zpět ze stavu v **log. 1**. Produkuje **Moorův výstup**.
![[media/szz-03/media/image30.png]]

![[media/szz-03/media/image36.png]]

- **R-S klopný obvod** (reset-set)
![[media/szz-03/media/image8.png]]

![[media/szz-03/media/image32.png]]

![[media/szz-03/media/image18.png]]

![[media/szz-03/media/image37.png]]

  - Přivedení **log. 1** na vstup **R** (reset) nastaví na výstupu **log. 0**.
  - Přivedení **log. 1** na vstup **S** (set) nastaví na výstup **log. 1**.
  - Současné přivedení **log. 1** na **S** i **R** je **zakázaná** kombinace, dříve **nešlo určit** v této situaci hodnotu na výstupu, dnes u hradel **NOR** bude na obou **log. 0** (negovaný výstup bude stejný jako přímý). Lze tomu zabránit prioritou jednoho ze vstupů.
- **R-S s povolovacím vstupem** - Povolovací vstup **C** (Control, Enable), který povoluje činnost KO – obvod lze **nastavit** či **nulovat**, jen pokud je vstup **C** aktivní (aktivní může být v log. 1 i log. 0, záleží na návrhu).
![[media/szz-03/media/image16.png]]

![[media/szz-03/media/image31.png]]

![[media/szz-03/media/image35.png]]

- **J-K klopný obvod (J** odpovídá **S, K** odpovídá **R)** - Zavádí zpětnou vazbu, která eliminuje zakázanou kombinaci. V případě, že jsou oba vstupy v **log. 1**, dochází ke **změně aktuální hodnoty na výstupu** (překlop - toggle).
![[media/szz-03/media/image23.png]]

![[media/szz-03/media/image17.png]]

- **T** (toggle) **klopný obvod** - Jedná se o **J-K** klopný obvod, který na oba vstupy posílá jednu hodnotu **T**. Pokud je **T** v **log. 0**, na výstupu zůstává aktuální hodnota, pokud je na vstupu **log. 1**, dochází k překlopení aktuální hodnoty na výstupu. Držení **log 1.** na vstupu **T** (a případně vstupu **C**) způsobí oscilování, změny log. 1 a log. 0.
![[media/szz-03/media/image11.png]]

![[media/szz-03/media/image20.png]]

- **D** (data) **klopný obvod** - Jedná se **R-S** klopný obvod, který posílá na vstup **S** hodnotu **D** a na vstup **R** její negaci **not D**. Nemůže takto vzniknout nepovolený stav (**R** a **S** nikdy nebude současně v **log. 1**). Na výstup posílá hodnotu na vstupu (vytváří tedy zpoždění).
![[media/szz-03/media/image27.png]]

- **D klopný obvod s povolovacím vstupem** - Narozdíl od jednoduchého **D** klopného obvodu, zde dochází ke **změně hodnoty** na výstupu, **jen** pokud je aktivní vstup **C** (pokud je C v **log. 0**, na výstupu setrvává nastavená hodnota).
![[media/szz-03/media/image26.png]]

![[media/szz-03/media/image5.png]]

## Dvoufázové bistabilní klopné obvody

Využívají se v **synchronních obvodech**, které jsou řízeny hodinami **CLK**. Mohou být typu **Master-Slave** nebo **Derivační**.

- U **Master-Slave** dochází ke změně hodnoty na výstupu **buď** když je **CLK** v **log. 0 (‾\|, první obrázek)**, **nebo** v **log. 1 (**\_\|, druhý obrázek).
- Informace ze vstupů se při **CLK=0** zapisuje do **Master** **R-S** KO a následně se při **CLK=1** přepisuje do **Slave** **R-S** KO, případně opačně. Zapojení Master-Slave se používá z toho důvodu, aby se hodnota na výstupu KO **změnila až pro příští takt hodin** (tj. aby zde bylo zpoždění, jinak by došlo ke změně ihned). Na obrázku se při CLK v **log. 1** **změní** hodnota **Master**, v **log. 0** se pak **změní** hodnota **Slave** a při **příští CLK** **log. 1** je na výstupu hodnota z **minulé log. 1**.
- různé typy: **RS**, **JK**, **T**, **D**.
![[media/szz-03/media/image19.png]]

![[media/szz-03/media/image2.png]]

![[media/szz-03/media/image28.png]]

- **Derivační** mění hodnotu na výstupu při změně úrovně CLK, tj. buď s **nástupnou** hranou nebo se **sestupnou** hranou. (**\>** nástupná, náběžná; **\<** sestupná, doběžná)

## Čítače
![[media/szz-03/media/image1.png]]

Jedná se o speciální automaty, které reagují na vstupní impulsy (např. nástupná hrana) přechodem ze stavu do stavu (**přičítají** nebo **odečítají**).

- **Asynchronní čítač** - Neobsahuje synchronizační hodiny, čítání (přechod ze stavu do stavu) je řízeno pouze vstupem.
- **Synchronní čítač** - Je řízen hodinami, k přechodu ze stavu do stavu dochází např při náběžné hraně hodin.

Mohou mít řídící vstupy, které umožňují:

- **UP/DOWN** - specifikovat **směr čítání** (vzestupná/sestupná posloupnost stavů)
- **CE** (clock enable) - pro **CE=0 si pamatuje** aktuální stav, pro **CE=1 čítá**
- **P Enable** - čítač čítá, pouze když je v **log. 1**, nemá vliv na **RCO**.
- **T Enable** - čítač čítá, pouze když je v **log. 1**

Mají výstup indikující přetečení (podtečení) čítače:

- **RCO** nebo **TC**

Prodloužení doby **čítání**/**dělícího poměru**/**vzniku přetečení** se implementuje kaskádovým zapojením čítačů. Čítače jsou zapojeny **vstupem** **CE** na **výstup** **RCO** (**TC**) předchozího čítače. (tři čítače MOD 10 za sebou přetékají jednou za 10\*10\*10=1000 impulsů)

### Čítače řešené T klopným obvodem

- 4 bitový čítač
- při přechodu z **15 do 0** dochází k přetečení (RCO v log. 1)
- aktuální stav čítače (binární hodnotu) lze získat z výstupů **Q0** až **Q3**
![[media/szz-03/media/image25.png]]

### Čítač v Grayově kódu

- Grayův kód kóduje po sobě jdoucí čísla tak, že je mezi nimi vždy změna pouze v jediném bitu.
- redukce počtu operací při změně čísla o jedničku
- binární reprezentace (b) na Grayův kód (g):
  - MSB zůstává stejný
  - pro každý bit: **g_i = b_i+1 xor b_i**
  - **1110 bin == 1001 Gray**

### Up/Down čítač

Postup: [<u>3-Bit & 4-bit Up/Down Synchronous Counter</u>](https://youtu.be/svFUEJkoeVY)

- určení tabulky … Q2 Q1 Q0 (podle počtu bitů) aktuálního stavu - **present state logic**
- určení tabulek následujícího stavu (Up - obrázek/Down) - **next state logic**
![[media/szz-03/media/image15.png]]

- určení log. úrovní vstupů klopných obvodů (budou se lišit u R-S, J-K, T - na obrázku, D) pro jednotlivé stavy
![[media/szz-03/media/image24.png]]

![[media/szz-03/media/image29.png]]

- zjednodušení logiky vstupů klopných obvodů pomocí **Karnaughových** map, pro každý KO jedna mapa
- implementace obvodu na základě určené logiky přechodů s použitím zvoleného klopného obvodu (na obrázku **T**)
![[media/szz-03/media/image13.png]]

![[media/szz-03/media/image7.png]]

### Čítač one-hot (straight counter)

V **log. 1** je vždy pouze jeden **D** klopný obvod, výstup kaskády je přiveden na vstup. Pro N klopných obvodů je délka posloupnosti N.

![[media/szz-03/media/image4.png]]

![[media/szz-03/media/image12.png]]

Čítač v Johnsonově kódu

Opět čítá pomocí **D** klopných obvodů, **negovaný** výstup kaskády je přiveden na vstup. Pro N klopných obvodů je délka posloupnosti 2N
![[media/szz-03/media/image34.png]]

## Registry

Umožňují ukládat informaci o určitém počtu bitů. Pro realizaci se obvykle používá klopný obvod typu **D**. KO jsou připojeny ke stejnému zdroji hodinového signálu. Mohou mít asynchronní **CLR** pro nulování, povolení činnosti **CE**. Mají vektor vstupů např. **D31-D0** a vektor výstupů např. **Q31-Q0**, lze je zapisovat jednotlivě, ale obvykle se tak neděje. Reprezentují např. 32-bit číslo, které vstupuje do **ALU** jako **operand**. Dále se používají při konstrukci automatů pro uchování **vnitřního stavu**.

### Paměťový registr (latch)

Paměť pro několik bitů.

### Posuvný registr (shift)

Synchronní obvod (mají stejný CLK) sestaven z klopných obvodů zapojených do série. Posouvání uložených bitů o jeden bit vlevo nebo vpravo při každém hodinovém impulsu. Existuje mnoho druhů, lze je použít např:

1. **Master-Slave SPI** - MISO, MOSI,
2. zápis dat pro odeslání přes **UART,**
3. čtení obdržených dat z **UART,**
4. ukládání hodnot operandů,
5. **sekvenční sčítačka**

![[media/szz-03/media/image6.png]]

## Stavové automaty

**Stavový automat** - Konečný automat (KA) je **šestice** (případně jako **sedmice**, pokud chceme definovat i množinu koncových stavů): $M = (S, \Sigma, \Lambda, T, G, s_0)$, kde:

- S je konečná neprázdná množina stavů (vnitřní abeceda),
![[media/szz-03/media/image3.png]]

- Σ je konečná **vstupní abeceda**,
- Λ je konečná **výstupní abeceda**,
- T je **přechodová funkce** (T : S × Σ → S),
- G je **výstupní funkce** (G : S × Σ → Λ pro Mealyho automat; G : S → Λ pro Mooreův automat)
- s ∈ S je počáteční stav.

Stavový automat v elektronice tvoří 3 části:

- **Next-state logika** (přechodová funkce) - **Kombinační logická síť** KLS. Na základě **současného stavu** (paměť) a **vstupů** generuje hodnotu následujícího stavu automatu.
- **Paměť** - Pro **zapamatování si současného stavu**.
- **Výstupy** - Mealy, Moore, kombinace.
- [<u>From a Finite State Machine to a Circuit</u>](https://youtu.be/Z4Zz7n-Lj0g)

Dle výstupní funkce je dělíme na:

- **Mealyho automat** - Výstup je funkcí jak aktuálního stavu v kombinaci se vstupem **Y = f(X, Z)**.
  - značení přechodu: **vstup**/**výstup**

![[media/szz-03/media/image14.png]]

- **Mooreův automat** - Výstup je funkcí aktuálního stavu automatu - **Y = f(Z)**. Tedy změna na výstupu se projeví až po přechodu do následujícího stavu (Mooreův automat má **zpoždění**).
  - značení stavů: **jméno stavu**/**výstup**

![[media/szz-03/media/image22.png]]

- **Moore/Mealy automat** - Kombinace mealyho a mooreova automatu.

![[media/szz-03/media/image10.png]]

- Převod **Moore na Mealy**: [<u>Conversion of Moore Machine to Mealy Machine</u>](https://youtu.be/HEVWx4irOx4)
- Převod **Mealy na Moore**: [<u>Conversion of Mealy Machine to Moore Machine</u>](https://youtu.be/-etILQcfgTg)

## SRAM

Klopný obvod tvořený **dvěma PMOS** tranzistory a **čtyřmi NMOS** tranzistory. Umožňuje uložit **1 bit** dat a používá se pro rychlé VP (L1, L2, L3) a také pro **registry**.
![[media/szz-03/media/image21.png]]

![[media/szz-03/media/image9.png]]

![[media/szz-03/media/image33.png]]

**Odkazy:**

- SO: [<u>SEKVENČNÍ LOGICKÉ OBVODY</u>](http://isst.hys.cz/images/prezentace/sekven%C4%8Dni_log_obvody.pdf)
- Mealyho automat: [<u>Mealyho automat</u>](https://cs.wikipedia.org/wiki/Mealyho_automat)
- Mooreův automat: [<u>Mooreův stroj</u>](https://cs.wikipedia.org/wiki/Moore%C5%AFv_stroj)

## Zdroje

- SZZ okruh 3 — studijní materiály FIT BUT (`szz-03.docx`). Další obrázky: `media/szz-03/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/02-kombinacni-logicke-obvody|2. Kombinační logické obvody]] · další: [[okruhy/04-hierarchie-pameti|4. Hierarchie paměti]] ▶
