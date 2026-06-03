> Obsah

Vytvoreno s pouzitim excelu ze 4_skript_statistika_otazok, ChatGPT a
Claude Sonnet

Je dobre to kombinovat s kartickama <http://isz.ipoul.cz/>

Dá se předpokládat, že na nic víc se asi většinou ptát nebudou.\
Neručím za správnost a že si nic AI nevymyslela, ale po rychlém projití
to vypadá legit.

# Princip činnosti polovodičových prvků (dioda, bipolární a unipolární tranzistor ve spínacím režimu, realizace logických členů NAND a NOR v technologii CMOS)

Dioda

- Nakreslit diodu a určit anodu/katodu
- Zapojení diody v propustném a závěrném směru
- VA charakteristika diody
- Co se stane při opačném zapojení nebo bez rezistoru
- Jednocestný a dvoucestný usměrňovač
- Účel rezistoru před diodou
- Průběh napětí při střídavém proudu
- Jak se chová Zenerova dioda
- Využití diod

2\. PN přechod a polovodiče

- Vysvětlit PN přechod (stručně, ne do fyzikálních detailů)
- Vysvětlit P a N typ, jejich vlastnosti
- Princip polovodiče (valenční elektrony, ale spíš stručně)

3\. Bipolární tranzistor

- NPN tranzistor: značka, schéma, popis funkce
- Princip činnosti (bez hlubok é fyziky)
- VA charakteristika tranzistoru
- Zapojení tranzistoru ve **spínacím režimu** (včetně schématu, odporu,
  proudů)
- Co kam připojit, aby fungoval ve spínacím režimu
- Závislost proudu na napětí (výstupní charakteristika)
- Vysvětlit tranzistor jako **invertor**
- Zapojení se společným kolektorem

4\. Unipolární tranzistor / MOSFET

- Princip unipolárního tranzistoru (MOSFET)
- Rozdíl mezi NMOS a PMOS
- Nákres struktury (source, gate, drain)
- Jaký oxid je použit k oddělení gate
- VA charakteristika

5\. CMOS technologie

- Co je CMOS a jak funguje
- Proč se používá kombinace NMOS a PMOS
- Nakreslit logický člen (NAND, NOR, případně inverter) pomocí CMOS
- Vysvětlit, co se stane při sepnutí, proudové toky
- Opačné napájení – co způsobí chybu v logice

6\. Obecné / ostatní

- Ohmův zákon
- Napěťový dělič
- Graf závislosti napětí a proudu
- Usměrnění AC na DC a jeho průběh
- Jak zmenšit amplitudu – použití kondenzátoru
- Typy usměrňovačů – jednofázové, Graetzovo zapojení
- Kde měříme logickou 0/1 v obvodu

# Kombinační logické obvody (multiplexor, demultiplexor, kodér, dekodér, binární sčítačka). 

Obecná teorie kombinačních obvodů

- Co jsou **kombinační logické obvody**, jaký je jejich **rozdíl oproti
  sekvenčním obvodům**

- Jakými **formami** lze kombinační obvody **popisovat**:

  - pravdivostní tabulka
  - logický výraz
  - schéma

- Jaké **základní logické hradla** používáme

- Co je **Booleova algebra**, její význam

- Rozdíl mezi **NAND, NOR** a jejich **ekvivalence**

Multiplexor (MUX)

- Co je **multiplexor**, k čemu se používá
- Jak **funguje** – vstupy, výstupy, řídicí signály
- Vztah mezi počtem vstupů a řídicích vstupů
- Nakreslit **vnitřní schéma** multiplexoru pomocí AND/OR/NOT
- Vyjádření výstupu pomocí **logického výrazu**
- **Použití v praxi**

Demultiplexor (DMX)

- Definice demultiplexoru, rozdíl oproti multiplexoru
- Nakreslit **schéma**, popsat funkci
- Počet vstupů/výstupů, řídicí signály
- **Pravdivostní tabulka**

Dekodér a kodér (DEC, COD)

- Co je **dekodér**, jak funguje, vstupy/výstupy, využití
- Co je **kodér**, jak funguje – **binarni vs. prioritní kodér**
- Nakreslit **schéma** kodéru nebo dekodéru
- Získání logického výrazu ze schématu nebo tabulky

Sčítačky (HA/FA)

- **Poloviční sčítačka** (half adder – HA):

  - schéma, pravdivostní tabulka
  - jaké hradla používá

- **Úplná sčítačka** (full adder – FA):

  - Vstupy X výstupy
  - schéma a **pravdivostní tabulka**

- Jak realizovat **vícebitovou sčítačku** – zřetězení FA

- **Zpoždění** při sčítání – např. při 3bitové sčítačce se zpožděním
  delta → celkem 3×delta

- Rozdíl mezi **běžnou sčítačkou** a **CLA** (carry look-ahead adder)

Praktické a navazující otázky

- Kde se **kombinační obvody používají**
- Jak realizovat např. **8bitový přenos po jedné lince** pomocí MUX/DMX
- Použití obvodů v **FPGA** (např. dekodér → LUT)\
  \

# Sekvenční logické obvody (klopné obvody, čítače, registry, stavové automaty – reprezentace a implementace). 

Základy sekvenčních obvodů

- Co je sekvenční logický obvod?
- Jaký je rozdíl mezi sekvenčním a kombinačním obvodem?
- Proč sekvenční obvody potřebují paměť?
- Jaké jsou části sekvenčního obvodu
- Jaký je rozdíl mezi asynchronními a synchronními obvody?

Klopné obvody (KO)

- Vyjmenuj typy klopných obvodů (RS, JK, D, T).
- Popiš jednotlivé KO – vstupy, výstupy, pravdivostní tabulka, schéma.
- Čím se liší RS od D / JK / T?
- Co se děje při zakázaném stavu RS (1/1)?
- Co je to **metastabilní stav**?
- Jaký je rozdíl mezi hladinově a hranově řízenými KO?
- Co znamená "toggle" v kontextu JK?
- K čemu se jednotlivé KO používají (registry, čítače)?
- Jak bys navrhl čítač pomocí D KO?

Stavové automaty (FSM – finite state machines)

- Jak se realizuje stavový automat pomocí KO?

- Rozdíl mezi **Mooreovým** a **Mealyho** automatem:

  - Výstup závisí jen na stavu (Moore) vs. i na vstupu (Mealy).

- Transformace Moore ⇄ Mealy.

- Jak bys navrhl FSM (např. automat na kávu)?

  - definice stavů, přechody, výstupy, způsob reprezentace (tabulka,
    graf).

- Jak bys realizoval modulární sčítačku (počítání do N)?

Ostatní doplňující otázky

- Jaké znáš typy KO podle řízení (hladinový, derivační, dvojfázový)?
- Jaká je přenosová/výstupní funkce v FSM?
- Jak řešit hazardy u KO?
- Co je derivační KO?
- Kódování stavů (např. binární, jedním horkým stavem – one-hot)?

# Hierarchie paměti v počítači (typy a principy pamětí, princip lokality, organizace rychlé vyrovnávací paměti).  

Hierarchie pamětí

- Vyjmenujte paměti podle rychlosti / ceny / kapacity.
- Proč existuje hierarchie pamětí?
- Jaké jsou typy pamětí v počítači (registry, cache, RAM, SSD, HDD)?
- Jaký je rozdíl mezi SRAM a DRAM? (včetně: co to je, jak fungují, proč
  se používají)
- Kde v hierarchii se nachází RVP/cache?
- Co chceme od pamětí – rychlost, velikost, cena – a proč to nelze
  splnit jednou pamětí?
- Co znamená, že je paměť primární, sekundární, terciární?
- Kde se v systému ukládají nejčastěji přistupovaná data?

Princip lokality

- Co je princip časové a prostorové lokality?
- Uveďte příklad využití principu lokality.
- Proč princip lokality zvyšuje účinnost cache?
- Existují případy, kdy princip lokality nefunguje? (např. náhodný
  přístup)
- Jak lokalita ovlivňuje návrh RVP?

Rychlá vyrovnávací paměť (cache/RVP)

Základní otázky

- Co je to cache/RVP a proč se používá?
- Jak funguje cache (vztah CPU ↔ cache ↔ RAM)?
- Co znamenají pojmy *hit* a *miss*?
- Co se stane při cache miss?

Organizace cache

- Jak procesor pozná, jestli je proměnná/data v cache?

  - validity bit, tag, index, offset

- Jak se provádí výběr oběti (LRU, FIFO, random)?

- Jaká je struktura záznamu v cache?

- Popište přímé mapování (direct-mapped cache).

- Popište plně asociativní cache a vícecestné (n-way set associative).

- Co je tag a jak se používá?

- Jak probíhá adresace v cache (např. rozdělení 32bit adresy)?

- Jak probíhá čtení a zápis do cache?

- Jak cache vyhledává správný blok?

Pokročilejší dotazy

- Jaké jsou rozdíly mezi přímým a asociativním mapováním?
- Proč se používá vícecestné mapování?
- Jak velké jsou části adresy: index, offset, tag?
- Jaké výhody a nevýhody má přímé mapování vs. asociativní?
- Jak cache ovlivňuje výkon programu?
- Jaký vliv má velikost cache na její účinnost?

# Vestavěné systémy (mikrokontrolér, periferie, rozhraní, převodníky). 

**Mikrokontrolér - co to je, jak funguje, z čeho se skládá**

- Popis bloků uvnitř MCU (CPU jádro, paměť, periferie)
- Vestavěné periferie (watchdog, časovače, čítače, přerušení)
- K čemu slouží jednotlivé periferie

**Periferie**

- Jaké periferie jsou na MCU vestavěné vs. externí
- Popis funkce periferie (watchdog, časovače, vstupní/výstupní porty)
- Připojení periferních zařízení (klávesnice, displej apod.)

**Rozhraní / komunikace mezi zařízeními**

- Typy sériových rozhraní: UART (SCI), SPI, I2C
- Princip synchronní a asynchronní komunikace
- Základní vlastnosti těchto rozhraní (master/slave, half/full duplex,
  data frame)
- Signály jako MOSI, MISO, SCLK, SS (SPI)
- Co znamená baud rate, jak se nastavuje

**Analogově-digitální (A/D) a digitálně-analogové (D/A) převodníky**

- Princip činnosti A/D převodníku (postupné vzorkování, převod napětí na
  digitální hodnotu)
- Typy A/D převodníků (flash ADC, aproximace)
- Převodní graf (schodovitý průběh – digitální výstup je diskrétní,
  nikoli spojitá čára)
- Vliv počtu bitů (např. 8 bitů) a rozsahu vstupního napětí na přesnost
  převodu
- Jak dlouho trvá převod (u různých typů převodníků)
- Jak funguje S/H (sample and hold) obvod a multiplexor v AD převodníku

**Vestavěné systémy (embedded systems)**

- Co to je vestavěný systém
- Jaké má vlastnosti a použití
- Jaké periferní moduly jsou běžné

# Principy řízení a připojování periferních zařízení (přerušení, programová obsluha, přímý přístup do paměti, sběrnice). 

1\. Periferní zařízení a připojování

- Co je periferní zařízení (PZ)?
- Jak se periferní zařízení připojují k mikrokontroléru/CPU? (mapování
  do paměti, adresový prostor)
- Jak probíhá komunikace CPU s periferií? (registr, start bit, instrukce
  IN/OUT)
- Typy připojení PZ – izolované vstupy/výstupy, sběrnice, point-to-point
  apod.
- Jak funguje připojení PZ pomocí sběrnice? Jaká jsou specifika (např.
  DMA, interní sběrnice)?

2\. Přerušení a obsluha přerušení

- Co je přerušení?
- Jak procesor zjistí, že periferní zařízení dokončilo svou operaci?
  (pooling vs přerušení)
- Kdy se používá pooling a kdy přerušení? (jednovláknový systém vs
  vícev)
- Co je potřeba pro použití přerušení? (podpora v interní sběrnici,
  podprogram obsluhy)
- Jak funguje maskování přerušení? (priorita, ignorování)
- Existují přerušení, která nelze maskovat? (reset)
- Popis vektorů přerušení a jejich role
- Programová obsluha přerušení

3\. DMA (Direct Memory Access)

- Co je DMA?
- Jak DMA spolupracuje s periferiemi a CPU?
- Postup zpracování přerušení v kombinaci s DMA

4\. Rozhraní a komunikace s periferiemi

- Popis sériových rozhraní (SPI, SCI/UART, USB, I2C)
- Jak fungují jednotlivá rozhraní? (master/slave, synchronní/asynchronní
  komunikace)
- Signály a registry používané při komunikaci s periferiemi
- Přerušení spojená s komunikací

5\. Instrukce a registry

- Jaké instrukce se používají pro práci s periferiemi? (IN, OUT)
- Jaké registry a flagy jsou důležité pro přerušení a komunikaci s
  periferií?
- Detailní popis kroků při obsluze přerušení a práci s periferními
  zařízeními

6\. Principy vestavěných systémů a mikrokontrolérů

- Co je vestavěný systém?
- Co je mikrokontrolér a jaké má periferní moduly? (watchdog, časovače)
- Funkce časovače, typy časovačů (podle náběžné hrany apod.)

# Princip činnosti počítače (řetězené zpracování instrukcí, RISC, CISC). 

**1. Princip činnosti počítače / základní fungování CPU**

- Popis obecného principu činnosti počítače (fetch-decode-execute
  cyklus)
- Co se děje v CPU během zpracování instrukcí

**2. Zřetězené (pipeline) zpracování instrukcí**

- Popis jednotlivých fází pipeline: F (fetch), D (decode), E (execute),
  M (memory), W (write back)
- Jak funguje zřetězení instrukcí a proč se používá
- Nakreslit pipeline a popsat, jak instrukce procházejí jednotlivými
  fázemi
- Popis, jak se instrukce navzájem ovlivňují (konflikty/hazardy)

**3. Konflikty (hazardy) při zřetězeném zpracování**

- Typy hazardů:

  - Strukturální (resource conflicts)
  - Datové (RAW, WAR, WAW)
  - Řídicí (control hazards)

- Jak se řeší hazardy (bypassing/forwarding, NOP, přeskládání instrukcí,
  predikce skoku)

**4. RISC vs CISC architektura**

- Rozdíly mezi RISC a CISC (např. počet a složitost instrukcí)
- Proč je RISC vhodný pro pipeline zpracování
- Příklad instrukce v RISC (např. ADD CX AX BX) a její průchod pipeline
- Co znamená reduced instrukční sada (RISC) a proč je efektivní
- Příklady procesorů, které používají RISC nebo CISC

**5. Výkon a efektivita zřetězení**

- CPI (cycles per instruction), proč není vždy 1 při pipeline
- Výhody a nevýhody pipeline zpracování instrukcí
- Jak pipeline zrychluje vykonávání instrukcí

**6. Další detaily a doplňující otázky**

- Vysvětlit, jak probíhá vykonávání konkrétní instrukce (např. ADD) přes
  F/D/E/M/W fáze
- Rozdíl mezi Von Neumann a Harvard architekturou (někdy zmiňováno)
- Statická analýza programů (zmíněno jen okrajově)
- Predikce skoku (branch prediction)
- Požadavky na registr PC a další registry pro podporu pipeline

# Minimalizace logických výrazů (algebraické metody, Karnaughova mapa, Quine McCluskey). 

**Proč se minimalizuje?**

- Co je cílem minimalizace logických výrazů?
- Jaký je význam minimalizace v návrhu logických obvodů?

**Co je Karnaughova mapa a jak funguje?**

- Nakreslete Karnaughovu mapu (obvykle pro 3 nebo 4 proměnné).
- Popište princip fungování Karnaughovy mapy.
- Jak v mapě probíhá minimalizace? (smyčky, skupiny)

**Minimalizace pomocí Karnaughovy mapy:**

- Ukažte postup minimalizace zadané logické funkce pomocí Karnaughovy
  mapy.
- Jaké jsou pravidla pro zakružkování sousedních políček?
- Co znamená “Booleanova sousednost” (Booleovská sousednost)?
- Jaký je vztah Karnaughovy mapy k Booleově algebře?

**Algebraické metody minimalizace:**

- Popište algebraické metody minimalizace logických výrazů.
- Uveďte a vysvětlete De Morganovy zákony.
- Proveďte algebraickou minimalizaci daného výrazu.
- Uveďte příklad algebraické minimalizace a porovnejte s minimalizací
  pomocí mapy.

**Metoda Quine–McCluskey:**

- Co je metoda Quine–McCluskey?
- Jak se liší od Karnaughovy mapy?
- Kdy je vhodné ji použít?
- Popište její postup (stručně).

**Typy minimalizace:**

- Jaké máme metody minimalizace (algebraické, grafické – Karnaughova
  mapa, algoritmické – Quine–McCluskey).
- Kdy je vhodné použít kterou metodu?

**Teoretické otázky:**

- Co znamenají hodnoty v Karnaughově mapě (1, 0, “true”, “false”)?
- Co je tautologie?
- Jaké jsou výhody minimalizace v návrhu obvodů?
- Jak minimalizace souvisí s optimalizací (náklady, rychlost,
  složitost)?

# Reprezentace čísel a základní dvojkové aritmetické operace v počítači (doplňkové kódy, sčítání, odčítání, násobení, pevná a plovoucí řádová čárka, standard IEEE 754). 

1\. Reprezentace čísel:

- Vysvětlení **pevné řádové čárky (fixed point)** a **plovoucí řádové
  čárky (floating point)**.
- Rozdíl mezi nimi, výhody a nevýhody.
- Jak jsou čísla reprezentována v binárním systému.
- Obecný vzorec pro zápis čísla ve floating point (např. ∑ai×Bi\sum a_i
  \times B^i∑ai​×Bi).
- Jak funguje **IEEE 754 standard** (bitové rozdělení na sign bit,
  exponent, mantisu).
- Co je to **BIAS** a jeho role ve floating point.
- Příklady: single precision (32 bitů), double precision (64 bitů).

2\. Kódy pro záporná čísla:

- Vyjmenovat a vysvětlit:

  - **Přímý kód**
  - **Doplňkový kód (two’s complement)**
  - **Inverzní kód (one’s complement)**
  - **Transponovaná nula**

- K čemu se jednotlivé kódy používají a jejich vlastnosti.

- Grafické znázornění reprezentace čísel v doplňkovém kódu (zejména u 4
  bitů).

- Co se stane s nejmenším záporným číslem (např. proč nejde invertovat v
  doplňkovém kódu).

3\. Aritmetické operace:

- Jak se provádí sčítání, odčítání, násobení v různých kódech (zejména v
  doplňkovém kódu).
- Podmínky, kdy je výsledek operace korektně zobrazitelný (např. stavové
  příznaky přenosu **z** a **přenosu do řádu**).
- Jak počítač zjistí, zda je výsledek zobrazitelný (např. oba příznaky
  buď nastaveny, nebo oba nenastaveny).
- Pro floating point: jak se provádí sčítání a násobení, co je
  normalizace.
- Příklady výpočtů (např. přepočet binárních čísel, sčítání, násobení,
  posuny).

4\. Speciální situace a detaily IEEE 754:

- Normalizovaný stav mantisy.
- Význam implicitní jedničky u mantisy.
- Speciální hodnoty: nekonečno, NaN (Not a Number).
- Omezení přesnosti (např. proč není možné přesně reprezentovat číslo
  0.1).
- Kolik hodnot lze reprezentovat v 32 bitovém floatu.
- Porovnání složitosti sčítání a násobení v floating point.
- Proč se používá více formátů IEEE 754 (single, double, extended
  precision).
- Proč se používá exponent s BIASem.
- 

# Technologie FPGA (vnitřní struktura, LUT), kroky návrhu aplikací využívajících FPGA a základy syntetizovatelného popisu hardware (strukturní a behaviorální popis obvodů).

\
**1. Co je to VHDL?**

- Popis jazyka VHDL (co to je, k čemu slouží)
- Výhody používání VHDL
- Proč se VHDL začal používat (např. dokumentace, popis složitých
  integrovaných obvodů)

### 2. Co je entita ve VHDL?

- Popis entity (co reprezentuje, že definuje rozhraní modulu)
- Jaká je role entity ve VHDL návrhu

### 3. Co je architektura ve VHDL?

- Popis architektury (vnitřní realizace entity)

- Typy architektur:

  - Behavioral (popis chování)
  - Structural (strukturní popis, jak je modul složen z jiných
    komponent)
  - Dataflow (popis toků dat)

### 4. Co je proces ve VHDL?

- Definice procesu, jeho role ve VHDL
- Jak proces souvisí se signály a změnami signálů
- Sensitivity list (seznam signálů, na které proces reaguje)

### 5. Jaký je rozdíl mezi signálem a proměnnou?

- Jaký mají význam v procesu
- Kdy se mění a jak se liší jejich chování

### 6. Jak probíhá simulace a jaký je rozdíl mezi simulací a reálným hardwarem (IRL)?

- Zpoždění v simulaci vs. skutečné zpoždění
- Co je možné simulovat a co syntetizovat (např. není možné syntetizovat
  rekurzi)

### 7. Co je sensitivity list a k čemu slouží?

- Vysvětlení seznamu signálů, na které je proces citlivý
- Kdy se proces spouští (po změně signálu ze sensitivity listu)

### 8. Kolik procesů může běžet současně ve VHDL?

- Základní znalost paralelismu v HDL

### 9. Co je syntéza a co se z VHDL kódu dá převést do hardwaru?

- Vysvětlení syntézy a jaký kód je syntetizovatelný

### 10. Jaký je rozdíl mezi architekturou a entitou?

- Entity jako rozhraní, architektura jako implementace

### 11. Co je testbench a jak se používá?

- Vysvětlení testovacího prostředí ve VHDL (někdy dotaz v rámci
  podotázek)

### 12. Případné doplňkové otázky k FPGA:

- Co je to FPGA, LUT, klopný obvod (např. D klopný obvod)
- Jak souvisí FPGA a sekvenční obvody

# 2D vektorová grafika: metody rasterizace úseček a polygonů, reprezentace objektů pomocí Bézierovy křivky. 

1\. Co je rasterizace? Proč se rasterizují vektorové objekty?

- Definice rasterizace
- Důvod rasterizace vektorových dat (displeje jsou rastrové)
- Výhody vektorové grafiky před rasterovou (transformace, popis)

2\. Popis úsečky

- Rovnice úsečky (obecná, parametrická, směrnicová)
- Co je směrnice úsečky (tangens úhlu)
- Jak se úsečka rasterizuje (naivní přístup)

3\. Algoritmy rasterizace úsečky

- DDA algoritmus: princip, nevýhody, co je krok (pixel)
- DDA s fixed-point aritmetikou
- Bresenhamův algoritmus: princip, sledování chyby, výhody oproti DDA,
  rekurentní výpočet
- Midpoint algoritmus (podobný Bresenhamovi)
- Jak se řeší rasterizace úseček v různých oktantech

4\. Rasterizace kružnice a elipsy

- Midpoint algoritmus pro kružnici a elipsu
- Využití symetrie a překrývání kvadrantů
- Jak začíná výpočet (z bodu na kružnici)

5\. Rasterizace křivek

- Rozdělení křivek: aproximační vs. interpolační
- Bezierovy křivky (parametrické křivky)
- De Casteljau algoritmus
- Základní vlastnosti a použití (např. pohyb kamery, modelování)
- Pseudokód pro rasterizaci křivky (jak vykreslit)

6\. Rasterizace polygonů

- Řádkové vyplňování polygonů
- Inverzní řádkové vyplňování
- Pinedův algoritmus
- Detekce průsečíků hran s řádkou
- Semínkové vyplňování (flood fill)

7\. Obecné otázky k rasterizaci

- Jak často probíhá rasterizace v počítači? (připravenost
  před-renderování vs. realtime)
- Výhody rychlých algoritmů rasterizace
- Vliv fixed-point aritmetiky
- Proč je třeba zaokrouhlovat výsledky (k určení pixelu)

8\. Další doplňující otázky

- Příklady výstupních zařízení používajících vektorovou a rastrovou
  grafiku (např. osciloskop)
- Jak by se rasterizovala úsečka libovolně v prostoru (př. pod úhlem 11
  hodin)
- Kdy použít který algoritmus (DDA, Bresenham, Midpoint)
- Význam prediktoru a sledování chyby v Bresenhamově algoritmu

# Transformace a zobrazení 3D polygonálních modelů, principy programovatelného vykreslovacího řetězce. 

1\. Zobrazovací řetězec (rendering pipeline)

- Jaké jsou části řetězce (vertex processing, rasterizace, fragment
  shader, výstup do framebufferu)
- Vstupy a výstupy jednotlivých kroků
- Jak se pracuje s transformacemi během pipeline

2\. Beziérova křivka a její vykreslení, transformace ve 3D

- Matematické základy Beziérovy křivky (parametrická forma, kontrolní
  body)
- Jak se Beziérova křivka vykresluje (vznik bodů křivky)
- Jak se křivka transformuje v 3D prostoru (matice transformace
  aplikované na kontrolní body)
- Co se při vykreslování a transformaci děje krok po kroku

3\. Homogenní souřadnice

- Co jsou homogenní souřadnice (rozšíření kartézských souřadnic o další
  složku w)
- Proč se používají (umožňují reprezentovat posuny pomocí maticové
  transformace, skládání transformací v jedné matici)
- Popis základních transformací (posun, rotace, škálování) pomocí
  homogenních souřadnic a příslušných transformačních matic
- Jak se skládají transformace (násobení matic, pořadí má vliv)
- Konkrétní příklad s maticemi (např. posun -\> škálování -\> posun
  zpět, ukázat matice a jejich násobení)
- Vysvětlení, proč W=1 u bodů (rozlišení bodů a vektorů, pravidla pro
  transformace)

4\. Matematická definice lineární transformace

- Lineární transformace jako zobrazení, které zachovává sčítání a
  násobení skalárem
- Vztah k maticím (každá lineární transformace může být vyjádřena
  maticí)
- Rozdíl mezi lineární a afinní transformací (posun není lineární, proto
  se používají homogenní souřadnice)

5\. Reprezentace 3D objektů v počítači

- Jak reprezentovat objekty v 3D (polygony, trojúhelníky s vybarvenými
  plochami – polygonální modely)
- Další způsoby (CSG, voxely, volumetrické objekty)
- Proč jsou polygony standard (efektivita, jednoduchost vykreslování)
- Jaké jsou nevýhody a výhody jednotlivých reprezentací

6\. Příklad násobení transformační matice s homogenním vektorem (W=1)

- Ukázat konkrétní matici posunu
- Vynásobit ji vektorem \[x, y, z, 1\]
- Vysvětlit výsledek a proč W zůstává 1

7\. Skládání transformací v praxi

- Jak provést složenou transformaci, např. posun -\> rotace -\> posun
  zpět
- Matematické vyjádření a význam pořadí násobení matic
- Praktický dopad (rotace kolem libovolného bodu, nikoliv pouze kolem
  počátku)

8\. Další témata (dle konkrétní zkoušejícího)

- Nelineární transformace (základní představení)
- Projekce (perspektivní a paralelní, jejich využití)
- Z-buffer a stínování
- Ray tracing a radiozita (krátce)
- Vykreslovací pipeline a principy texturování
- Gimbal lock (v souvislosti s rotacemi)
- Pojmy jako asociativita a komutativita transformací

# Principy grafických uživatelských rozhraní (komunikační kanály, módy komunikace, systémy řízené událostmi, standardní prvky rozhraní). 

**Principy grafických uživatelských rozhraní (GUI)**

- Obecný úvod do GUI.
- Komunikační kanály (módy komunikace mezi uživatelem a systémem).
- Modalita (modálnost) - vysvětlení pojmu.
- Rozdíl mezi aktivní a pasivní komunikací (tento dotaz byl
  problematický).

**Módy komunikace**

- Různé režimy nebo způsoby, jakými uživatel komunikuje s počítačem
  (například event-driven systém apod.).
- Komunikační módy, které nechtěl slyšet jako aktivní/pasivní, chtěl
  spíše formální a přesné definice.

**Co je to WIMP**

- Dotaz na vysvětlení pojmu WIMP (Windows, Icons, Menus, Pointer).
- Zkoušející chtěl pochopit, jak to souvisí s GUI a komunikací uživatele
  se systémem.

**Metafora ve spojení s GUI**

- Co znamená metafora v rámci uživatelského rozhraní (např. desktop,
  složky, ikony jako odraz reality).
- Jak metafory pomáhají uživatelům lépe chápat a používat GUI.

**Další možné dotazy**

- MVC (Model-View-Controller) - popis architektury GUI.
- Identifikace uživatelských potřeb a přizpůsobení rozhraní.

# Spektrální analýza spojitých a diskrétních signálů. 

Typy signálů

- Spojitý signál
- Diskrétní signál
- Deterministický / náhodný
- Periodický / neperiodický
- Konečný / nekonečný

Spektrální analýza

- Co je spektrální analýza
- K čemu se používá
- Jaký je vstup a výstup
- Vztah mezi časovou a frekvenční doménou
- Jak vypadá spektrum různých typů signálů
- Spektrum harmonického signálu (modul, fáze)
- Co znamená „posunutý signál“ a jak se to projeví ve spektru
- Jak vypadá spektrum po vzorkování (periodizace)

Vzorkování

- Jak převést spojitý signál na diskrétní

- Nakreslit spojitý a diskrétní signál

- Vzorkovací teorém (Shannonův / Nyquistův)

  - Co se stane, když není splněn
  - Jaký je dopad na spektrum
  - Aliasing

- Jaké osy má graf při vzorkování

- Proč dolní propust před vzorkováním

- Jak se projeví špatné vzorkování (alias, přeložení spektra)

Fourierova analýza a transformace

- Fourierova řada (FŘ)

  - Vzorec, co značí jednotlivé symboly
  - Koeficienty, výpočet
  - Periodičnost výsledku
  - Harmonické složky

- Fourierova transformace (FT)

  - Spojitý signál, vzorec, význam proměnných

- Diskrétní Fourierova transformace (DFT)

  - Vstup, výstup, vzorec
  - Normalizovaná kruhová frekvence
  - Vztah mezi časem a frekvencí
  - Periodicita spektra
  - Vztah s DTFT
  - Proč je výstupem jen N/2 koeficientů

- Diskrétní časová Fourierova transformace (DTFT)

- Rychlá Fourierova transformace (FFT) – zmíněno okrajově

- Promítání do báze (kontext výpočtu spektra)

Komplexní čísla a exponenciály

- Význam komplexní exponenciály ve Fourierově transformaci
- Modul a argument komplexního čísla
- Komplexně sdružené hodnoty ve spektru
- Interpretace bodu na jednotkové kružnici

Další témata a otázky

- Konvoluční teorém
- Komprese (např. JPEG) pomocí Fourierovy transformace
- Korelace
- Kvantování
- Rozlišení ve frekvenční oblasti
- Interpretace spektra konkrétních signálů
- Příklady z reálného světa (např. hudba, hluk v místnosti)
- Jak by se spektrální analýza použila prakticky
- Co říká spektrum o signálu

Formální požadavky

- Nakreslit grafy (signály, spektrum)
- Zvolit a popsat jednu transformaci (libovolně: FT, DFT, FŘ…)
- Popsat význam jednotlivých členů ve vzorci
- Napsat vzorec a vysvětlit písmena

# Číslicové filtry (diferenční rovnice, impulsní odezva, přenosová funkce, frekvenční charakteristika). 

 1. Diferenční rovnice

- Obecný tvar diferenční rovnice číslicového filtru.
- Vysvětlení jednotlivých členů rovnice (koeficienty, zpětná vazba).
- Rozlišení mezi **FIR** (bez zpětné vazby) a **IIR** (se zpětnou
  vazbou).
- Rekurze / nerekurze, stabilita, kauzalita.

2. Přenosová (přechodová) funkce

- Zápis přenosové funkce (např. H(z)=Y(z)X(z)H(z) =
  \frac{Y(z)}{X(z)}H(z)=X(z)Y(z)​).
- Získání přenosové funkce ze Z-transformace diferenční rovnice.
- Význam pólů a nul, stabilita pomocí jednotkové kružnice.
- Lineární, časově invariantní systém.

3. Impulzní odezva

- Definice (reakce filtru na jednotkový impulz).
- Zobrazení v čase (časová osa).
- Rozdíl mezi konečnou (FIR) a nekonečnou (IIR) odezvou.
- Vztah ke konvoluci: výstup je konvoluce vstupu s impulzní odezvou.

4. Frekvenční charakteristika

- Co to je, jak ji získat (Fourierova transformace impulzní odezvy).
- Nakreslit a vysvětlit (např. pro dolní/horní propust).
- Vztah mezi přenosovou funkcí a frekvenční charakteristikou.

5. Typy filtrů

- FIR / IIR (vlastnosti, rozdíly).

- Klasifikace podle průchodu frekvencí:

  - **Dolní propust**
  - **Horní propust**
  - **Pásmová propust**
  - **Pásmová zádrž**
  - Vyhlazovací filtr

6. Blokové schéma

- Nakreslit filtr (FIR/IIR), správné umístění zpoždění (z⁻¹),
  koeficientů.
- Rozpoznat typ filtru podle schématu (např. zpětná vazba = IIR).
- Význam jednotlivých bloků (součty, násobení, zpoždění).

7. Doplňkové koncepty

- **Stabilita**: Póly uvnitř jednotkové kružnice.
- **Lineárnost**: Superpozice platí (např. žádné ((x\[n\])^2).
- **Kauzalita**: Výstup závisí jen na současných/předchozích vstupech.
- **Časová invariantnost**: Posun vstupu ⇒ posun výstupu.

# Množiny, relace a zobrazení. 

400. **Množiny**

     - Definice množiny
     - Operace s množinami (sjednocení, průnik, rozdíl)
     - Typy množin (konečné, nekonečné, spočetné, nespočetné)
     - Potenční množina
     - Mohutnost množin, srovnání pomocí bijekce

401. **Relace**

     - **Definice binární relace** (podmnožina kartézského součinu)

     - Vlastnosti relací:

       - Reflexivita
       - Symetrie
       - Tranzitivita
       - Antisymetrie
       - Irreflexivita apod.

     - **Relace ekvivalence**

       - Definice (reflexivní, symetrická, tranzitivní)
       - Rozklad množiny podle relace ekvivalence
       - Vztah mezi relací ekvivalence a rozkladem množiny

402. **Zobrazení (funkce)**

     - Definice zobrazení (formálně, predikátem)

     - Typy zobrazení:

       - Injekce (prosté zobrazení)
       - Surjekce (na zobrazení)
       - Bijekce (injekce + surjekce)

     - Speciální vlastnost bijekce: **existence inverzní funkce**

     - Příklady zobrazení (např. sinus)

403. **Tranzitivní uzávěr relace**

     - Co to je
     - Jak se vytváří
     - Operace "po" na relaci
     - Jak zjistit, že je uzávěr hotov (žádné nové prvky nepřibudou)

404. **Kartézský součin**

     - Definice (A × B = {(a, b) \| a ∈ A, b ∈ B})
     - Použití v definici relací

Doplňková témata (méně častá, ale zmíněná):

- Uspořádání (relace uspořádání, supremum)
- Spojení zobrazení
- Rozlišení pojmů relace vs. zobrazení vs. funkce
- Výroková logika (vyjádření definic formálně)

Často požadované schopnosti:

- Umět **formálně definovat** základní pojmy (množina, relace,
  zobrazení, typy relací a zobrazení)
- Umět **vysvětlit vlastnosti relací a zobrazení** slovně i symbolicky
- Schopnost **uvést příklad**
- Propojit pojmy (např. relace ekvivalence ↔ rozklad množiny)
- Zvládnout zápis ve **výrokové logice nebo predikátové logice**

# Diferenciální a integrální počet funkcí jedné a více proměnných. 

1\. Derivace (funkce jedné i více proměnných)

- Definice pomocí limity
- Geometrický význam – směrnice tečny
- Využití v praxi – rychlost změny
- Derivace v počítačích – numerické metody (např. Euler)
- Parciální derivace
- Gradient

2\. Extrémy funkcí (lokální/globální)

- Funkce jedné proměnné: první/druhá derivace
- Funkce více proměnných: hledání extrémů, podmínky, sedlové body
- Postup: najít kritické body (derivace = 0 nebo neexistuje), krajní
  body, rozhodnout o typu extrému

3\. Funkce více proměnných

- Definice a znázornění (graf, plocha)
- Parciální derivace, gradient, směr derivace
- Vyšetřování extrémů

4\. Integrál

- Určitý vs neurčitý
- Geometrický význam – obsah pod křivkou
- Dvojný/trojný integrál – výpočet objemu, plošný integrál
- Aplikace – délka křivky, plocha, objem
- Numerické metody (např. Monte Carlo, lichoběžníkové pravidlo)
- Per partes (integrační pravidla)

5\. Základy a definice

- Limita: formální i intuitivní definice
- Spojitost funkce
- Vztah mezi spojitostí a derivovatelností
- Co je funkce, definiční obor

6\. Numerické metody

- Eulerova metoda pro derivace/integrály
- Odhad derivace z diskrétních dat
- Monte Carlo integrace

7\. Doplňková témata

- Jakobián – matice parciálních derivací
- Diferenciál – jako lineární aproximace přírůstku
- Derivace absolutní hodnoty – funkce bez derivace v bodě (např. \|x\|)

# Číselné soustavy a převody mezi nimi. 

1\. Typy číselných soustav

- **Poziční vs. nepoziční soustavy**

  - Co to je, příklady

- **Polyadické vs. nepolyadické soustavy**

  - Definice, příklady, rozdíl mezi nimi

2\. Zápis čísel v soustavách

- **Polynomiální zápis čísel**

  - Vzorec, vysvětlení jednotlivých členů sumy

- **Zápis pomocí váženého součtu**

3\. Převody mezi soustavami

- Z **desítkové do binární**

- Z **binární do desítkové**

- Z **desítkové do šestnáctkové**

- Z **binární do šestnáctkové** (často pomocí mezikroku přes binární)

- Z **osmičkové do šestnáctkové** (např. 8 → 2 → 16)

- Převody čísel **s desetinnou čárkou**

  - Metody: **dělení základem**, **násobení základem**

4\. Algoritmy a metody převodů

- **Substituční metoda**
- **Metoda dělení základem** (pro celá čísla)
- **Metoda násobení základem** (pro desetinná čísla)

5\. Zobrazování záporných čísel

- **Přímý kód**
- **Inverzní kód**
- **Doplnkový kód (Two's complement)**

6\. Obecné otázky a principy

- Co je to **číselná soustava**
- **Použití různých soustav v informatice**
- Proč se používá např. **šestnáctková soustava**
- **Výhody soustavy se základem 12** (Herout)

# Výroková logika a predikátová logika. Syntaxe a sémantika výrokové logiky. Splnitelnost a platnost. Logická ekvivalence a logický důsledek. Normální formy. Jazyk predikátové logiky prvního řádu. Syntaxe, termy a formule, volné a vázané proměnné. Dokazování ve výrokové a predikátové logice. Prvořádové teorie a jejich vlastnosti.

1\. Rozdíl mezi výrokovou a predikátovou logikou

- Co navíc přináší predikátová logika (proměnné, kvantifikátory, termy
  apod.)
- Porovnání výroků a formulí

2\. Základní pojmy predikátové logiky

- **Predikát**
- **Funkční symbol**
- **Term**
- **Formule**
- **Volné a vázané proměnné**
- **Syntax vs. sémantika**
- **Interpretace / realizace** formule (např. co znamená splnění
  formule, kdy je pravdivá)

3\. Kvantifikátory

- Existenciální (∃) a univerzální (∀) kvantifikátor
- Převod negace přes kvantifikátor (např. ¬∃x φ ≡ ∀x ¬φ)

4\. Normální formy (DNF, CNF)

- Jak převést výrokovou formuli do DNF/CNF
- Využití pravdivostních tabulek

5\. Výroková logika - základy

- Postup dokazování, pravidla (např. modus ponens)
- Tautologie vs. dokazatelnost
- Z čeho se skládá (pravidla, formule, operace)

6\. Teorie a ohodnocení v PL

- **Teorie** jako množina axiomů
- **Ohodnocení** a splnitelnost formulí
- Otázky typu: „Co je potřeba k určení pravdivosti formule?“ (univerzum,
  interpretace, ohodnocení)

ČASTÉ KONKRÉTNÍ OTÁZKY / ÚKOLY

- Definujte **term**
- Co je **funkční symbol**? Uveďte příklad
- Jak se liší **syntax a sémantika**?
- **Napište** nebo **převeďte** formuli do logiky / DNF / PL
- Zapište výrok jako **formuli v predikátové logice**
- Je výroková formule dokazatelná ⇒ tautologie?
- Z čeho se skládá **predikátová logika** (jazyk)?
- Co znamená, že dvě množiny mají **prázdný průnik** – zapište v PL
- Co je **interpretace formule**?
- Jak zjistíme, jestli je formule **splnitelná**?
- Co je **ohodnocení**?
- Kolik má **pravdivostní tabulka řádků** pro N proměnných?

# Boolovy algebry.

Booleova algebra – hlavní téma

Typické otázky:

- Co je **Booleova algebra** – definice jako **šestice** (M, ∨, ∧, ', 0,
  1)
- Jaké jsou **axiomy** a **theorémy**
- **De Morganovy zákony**
- **Použití Booleovy algebry** (logické funkce, množinové operace)
- Rozdíl oproti svazům, vztah ke svazům
- Kolik je možných výstupů (např. 2⁴ kombinací)
- Co je to **implikace** v rámci BA
- **Částečně uspořádané množiny**, **zvazy**, **Booleovský svaz**
- **Hasseův diagram** (v kontextu uspořádání)
- **Základní vlastnosti uspořádání** (reflexivita, tranzitivita,
  antisymetrie)

Algebra, svazy, uspořádání – podpůrná témata

Typické otázky:

- Co je to **algebra** obecně
- Definice **svazu**
- Rozdíl mezi **svazem a Booleovou algebrou**
- **Reflexivita, tranzitivita, antisymetrie**
- Co je **infimum/supremum**, jejich znázornění
- **Částečné uspořádání**, vlastnosti relací

Regulární jazyky a jejich modely – vedlejší téma

Typické otázky:

- **Regulární výrazy** – vysvětlit, popsat, použití
- **Konečné automaty** – fungování a vztah k regulárním jazykům

# Regulární jazyky a jejich modely (konečné automaty, regulární výrazy). 

1\. Konečné automaty (KA)

- Formální definice KA (množiny, přechodová funkce, počáteční stav,
  koncové stavy).
- Rozdíl mezi deterministickým (DFA) a nedeterministickým KA (NFA).
- Převod z NFA na DFA (včetně powerset konstrukce, max. počet stavů).
- Zápis přechodové funkce.
- Konfigurace a akceptace slova automatem.
- Návrh KA pro konkrétní jazyk (např. slovo „ahoj“, podmínka jako lichý
  počet „a“ atd.).
- Komplementace automatu – úprava na úplný automat, změna koncových
  stavů.
- Minimalizace KA.

2\. Regulární výrazy (RV)

- Definice RV.
- Operace nad RV: sjednocení (+), konkatenace, iterace (\*).
- Příklady jednoduchých i složitějších RV.
- Vyjádření jazyků pomocí RV (např. a(a+b)\*b).
- Převod RV na KA a zpět.

3\. Regulární jazyky

- Definice regulárního jazyka.
- Co je jazyk, slovo, abeceda (Σ, Σ\*).
- Rozpoznatelnost jazyků konečnými automaty.
- Příklady regulárních jazyků.
- Příklady jazyků, které nejsou regulární.

4\. Gramatiky

- Regulární gramatika (definice, pravidla).
- Převod mezi regulární gramatikou a KA.
- Základní přehled Chomského hierarchie (RJ, BKJ…).
- Rozlišení mezi RG a RV.

5\. Převody a algoritmy

- Převod RV na KA (praktický i teoretický).
- Převod KA na gramatiku a naopak.
- Determinizace a minimalizace KA.
- Algoritmy – jmenovitě se ptají na postupy, ale i jejich jména (např.
  powerset konstrukce).

# Bezkontextové jazyky a jejich modely (zásobníkové automaty, bezkontextové gramatiky). 

**Bezkontextová gramatika (BKG)**

- Definice (čtveřice: G=(N,T,P,S))
- Jak vypadá pravidlo bezkontextové gramatiky (např. A→xA \rightarrow
  xA→x, kde AAA je neterminál a xxx je řetězec terminálů a neterminálů)
- Derivační krok, derivační strom
- Co generuje BKG (množina řetězců generovaných z počátečního symbolu
  pomocí pravidel)
- Příklady jazyků generovaných BKG (např. anbna^n b^nanbn)

**Zásobníkový automat (ZA/ZKA)**

- Formální definice (sedmice: (Q,Σ,Γ,R,s,S,F)
- Vysvětlení jednotlivých prvků sedmice
- Přechodová pravidla – jak fungují
- Jak ZA přijímá jazyk – princip fungování
- Příklady přijímání jazyků pomocí ZA
- Kreslení automatu a průchodu konkrétním řetězcem

**Srovnání jazyků**

- Rozdíl mezi regulárním jazykem (RJ) a bezkontextovým jazykem (BKJ)

- Příklad jazyka, který je:

  - regulární i bezkontextový (např. a∗a^\*a∗)
  - bezkontextový, ale ne regulární
  - ani regulární, ani bezkontextový

**Obecné pojmy a principy:**

- Co je abeceda, jazyk, terminály, neterminály
- Proč se jazyku říká „bezkontextový“
- Co je jazyk generovaný gramatikou (množina všech derivovatelných
  řetězců z počátečního symbolu)

**Příklady a aplikace:**

553. Napsat pravidla gramatiky pro daný jazyk
554. Napsat zásobníkový automat pro daný jazyk
555. Ukázat přechody automatu krok za krokem
556. Popis nebo kreslení derivačního stromu

# Struktura překladače a charakteristika fází překladu (lexikální analýza, deterministická syntaktická analýza a generování kódu)

**Fáze překladače – obecně i detailně**

- Jaké jsou **jednotlivé fáze překladače** (vyjmenovat, stručně popsat)
- Co je **vstupem a výstupem** jednotlivých fází
- Kde se překladač **dělí na frontend a backend**, co do kterého patří
- Jaké **metody a nástroje** se ve fázích používají (např.
  deterministický konečný automat, BKG, zásobníkový automat)
- Co je **účelem každé fáze** (např. LA rozpoznává lexémy, SA ověřuje
  gramatiku, semantika řeší smysluplnost)
- Co se používá v konkrétních jazycích (např. C) pro syntaktickou
  analýzu

**Lexikální analýza (LA)**

- Co je **lexém, token**, jaký je mezi nimi rozdíl
- Jak se tokeny ukládají, co všechno o nich překladač ví
- Jak se LA implementuje (DKA, regulární výrazy)
- Co je výstupem lexikální analýzy (tokeny, tok tokenů)

**Syntaktická analýza (SA)**

- Co je vstupem a výstupem SA (typicky tok tokenů → **derivační strom**)

- Rozdíl mezi **derivačním a abstraktním syntaktickým stromem**

- Popis gramatik (např. BKG, LL, LR)

- **Způsoby analýzy**:

  - **Shora dolů (top-down)**: rekurzivní sestup, prediktivní analýza
  - **Zdola nahoru (bottom-up)**: precedenční analýza

- **LL tabulka** – co je v řádcích, sloupcích a buňkách

- Co znamená **prázdná buňka** v LL tabulce (syntaktická chyba)

- **Precedenční tabulka** – co obsahuje

- Jak se střídá **scanner a parser**

**Sémantická analýza**

- Co je jejím výstupem (**abstraktní syntaktický strom** – AST)
- Na co se zaměřuje, jaké chyby odhaluje
- Využívání symbolické tabulky

**Vnitřní kód a optimalizace**

- Jaký vnitřní kód se používá – např. **trojadresný kód (3-address
  code)**: např. C := A + B
- K čemu slouží a jak se používá při optimalizaci
- Optimalizace **cílového kódu** – jestli a jak probíhá

**Závislost na jazyce**

- Které části překladače závisí na **vstupním jazyku** a které na
  **výstupním**
- Které části jsou na vstupním/výstupním jazyku **nezávislé**

**Konkrétní dotazy / úkoly**

- Nakresli derivační strom pro pravidlo (např. E → E + E)
- Napiš **syntakticky nesprávný kód v C**
- Rozlišení **simulace derivačního stromu vs. AST**
- Uveď příklad **syntaktické chyby** a co se při ní stane

# Numerické metody (přímé a iterační metody pro řešení soustav lineárních rovnic, numerické řešení obyčejných diferenciálních rovnic). 

1\. Soustavy lineárních rovnic

- **Zápis soustavy jako Ax = b** – matice soustavy, vektor pravé strany

- **Možnosti počtu řešení** – 0, 1, ∞ (Frobeniova věta)

- **Přímé metody:**

  - **Gaussova eliminační metoda (GEM)** – základní řádkové operace,
    redukce na trojúhelníkový tvar
  - **Cramerovo pravidlo** – vzorce, podmínka nenulového determinantu
  - **LU rozklad** – princip (A = LU, L dolní, U horní trojúhelníková)

- **Iterační metody:**

  - **Iterační výpočty** – obecný princip iterace (x\_{n+1} = g(x_n))
  - **Jacobiho metoda**
  - **Gauss-Seidelova metoda**
  - **Podmínky konvergence** – diagonální dominance (řádková/sloupcová)
  - **Ukončovací podmínka** – podle normy rozdílu mezi iteracemi /
    rezidua
  - Metoda půlení intervalu (bisekce)

2\. Řešení diferenciálních rovnic

- **Eulerova metoda**

  - Potřeba počáteční podmínky (Cauchyho úloha)

  - Grafická interpretace – přímky směrů, aproximace řešení

  - Chyby metody:

    - **Lokální, globální (kumulativní)**
    - **Zaokrouhlovací chyba – vzniká při sčítání**

- **Runge-Kutta metoda (RK4 zmíněna jen okrajově)**

- **Volba kroku (h)** – vliv na přesnost, stabilitu

# Teorie grafů. Pojem grafu, základní pojmy, isomorfismus grafů, souvislost. Grafové algoritmy pro hledání nejkratší cesty a minimální kostry.

Základní definice a pojmy

- Formální definice grafu
- Orientované vs. neorientované grafy
- Hrany, vrcholy
- Podgrafy
- Sled, cesta, tah
- Souvislost grafů
- Izomorfismus grafů

Minimální kostra grafu

- Co je to kostra grafu (strom bez kružnic)

- Vlastnosti minimální kostry

- **Algoritmy pro nalezení minimální kostry:**

  - Kruskalův algoritmus
  - Jarníkův algoritmus

Nejkratší cesta v grafu

- **Algoritmy pro nalezení nejkratší cesty:**

  - Dijkstrův algoritmus (nejčastěji zmiňovaný)
  - BFS, DFS (méně často)

- Složitost algoritmů

- Reprezentace grafů v paměti (matice sousednosti)

# Řešení úloh (prohledávání stavového prostoru, rozklad na podúlohy, metody hraní her).

Prohledávání stavového prostoru - základy

- **Formální definice stavového prostoru** (stavy, operátory, přechody)
- Expanze uzlů pomocí operátorů
- Reprezentace stavového prostoru
- Kdy se stavový prostor používá
- Řešení problému zacyklení
- Co je cílový stav a cena řešení

Dělení metod prohledávání

- **Neinformované (slepé) metody vs. informované metody**
- Rozdíl mezi nimi
- Příklady jednotlivých metod

Konkrétní algoritmy - neinformované metody

- **BFS (Breadth-First Search)**
- **DFS (Depth-First Search)**
- **UCS (Uniform Cost Search)**
- Vlastnosti algoritmů: úplnost, optimalita, časová/prostorová složitost
- Rozdíly mezi BFS a DFS
- Seznam CLOSED v rozšířených verzích

Konkrétní algoritmy - informované metody

- **A**\* algoritmus
- **Greedy Search**
- Rozdíl mezi Greedy Search a A\*
- Heuristická funkce a její vlastnosti
- Co představují hodnoty n v A\*

Metody hraní her

- **Jednoduché vs. složité hry**
- **Hry s neurčitostí**
- **Reprezentace her** (uzly a hrany)
- **MinMax algoritmus** - detailní popis a ukázka na příkladu
- **Alfa-Beta ořezávání** - kdy nastane α≥β a proč se neprohledává část
  prostoru
- Proč jeden hráč vybírá maximum a druhý minimum
- Aplikace na reálné hry (např. šachy)

# Strojové učení (učení s učitelem, učení bez učitele, posilované učení). 

Konkrétní oblasti, na které se ptají:

Základní dělení strojového učení

- Učení s učitelem (supervised learning)
- Učení bez učitele (unsupervised learning)
- Posilované učení (reinforcement learning)
- Rozdíly mezi jednotlivými typy
- Kdy se který typ používá

Učení s učitelem - detaily

- Princip a cíl učení s učitelem
- Vstupní data - tabulka s anotacemi/labely
- Co poskytuje učitel
- Stratová funkcia
- Rozdělení dat na trénovací a testovací sadu - proč se nepoužívá celá
  sada na učení

Algoritmy učení s učitelem

- Rozhodovací stromy (Decision Trees)

  - Jak se sestavují
  - ID3 algoritmus - podle čeho se vybírá atribut
  - Entropie - vzorec pro výpočet
  - Kreslení rozhodovacích stromů
  - Praktické příklady na datech

Učení bez učitele - detaily

- Princip učení bez učitele
- Typy problémů pro tento typ učení

Algoritmy učení bez učitele

- K-Means algoritmus

  - Jak funguje krok za krokem
  - Kreslení na tabuli s body v prostoru
  - Výpočet středů jako aritmetický průměr
  - Iterativní proces

Posilované učení - detaily

- Princip posilovaného učení
- Policy on-policy vs off-policy - rozdíly
- Konkrétní algoritmy posilovaného učení

Neuronové sítě

- Základní principy (často jen okrajově)

> 

# Principy modelování a simulace systémů (systémy, modely, simulace, algoritmy řízení simulace). 

Základní pojmy a principy

- Co je simulace a proč se používá
- Základní etapy simulace
- Systém vs. model vs. simulace - rozdíly a vztahy
- Identifikace systémů (pokročilejší téma)

Typy simulace

- Diskrétní simulace
- Spojitá simulace
- Kombinovaná simulace
- Rozdíly mezi jednotlivými typy

Algoritmy řízení simulace

- Algoritmus diskrétní simulace
- Algoritmus spojité simulace
- Algoritmus kombinované simulace
- Kalendář událostí - co to je, jak jsou uspořádané prvky
- Dokročování u kombinované simulace

Spojitá simulace - detaily

- Reprezentace modelů se spojitým časem

  - Bloková schémata
  - Diferenciální rovnice
  - Vztah mezi nimi

- Řešení diferenciálních rovnic

  - Snižování řádu derivace
  - Eulerova metoda
  - Runge-Kutta metody

- Velikost kroku a její vliv na simulaci

- Vstupy a výstupy systémů

Stochastické metody

- Monte Carlo metoda

  - Co to je (stochastická/náhodná metoda)
  - K čemu se používá (výpočet určitého integrálu, obsahu pod křivkou)
  - Jak funguje
  - Praktické aplikace

# Datové a řídicí struktury imperativních programovacích jazyků.

 1. Datové struktury

- Co to je, jak vypadají v paměti

- Statická vs. dynamická alokace paměti

- Implementace konkrétních DS:

  - **Seznam**, **fronta**, **zásobník**
  - **Binární strom**, průchody: **in-order**, **pre-order**
  - Implementace pomocí **pole** nebo **ukazatelů**

- Diagram signatury (např. pro frontu)

- Vlastnosti a použití různých DS

2. Abstraktní datové typy (ADT)

- Definice a specifikace ADT
- Výhody ADT – proč jsou důležité
- Příklady: fronta, zásobník, seznam
- Rozdíl mezi ADT a implementací
- Proč používat ADT místo konkrétních struktur

3. Řídicí struktury (Control Structures)

- **Sekvence**, **selekce (if)**, **iterace (cykly)**
- Různé typy cyklů: for, while, do-while
- Převod for na while a naopak
- Možnost převést cyklus na rekurzi a opačně (ne vždy možné)
- Význam řídicích struktur v imperativním jazyce

4. Imperativní programovací jazyky

- Co je to imperativní jazyk
- Jaké má vlastnosti
- Jak se liší od jiných paradigmat (např. deklarativní)
- Datové a řídicí struktury používané v imperativních jazycích

5. Paměť a alokace

- Statická vs. dynamická paměťová alokace
- Jak se alokuje paměť pro různé typy struktur
- Jak jsou datové struktury reprezentovány v paměti (např. pole vs.
  spojový seznam)

6. Funkce a rekurze

- Význam funkcí v programu
- Rozdíl mezi cyklem a rekurzí
- Kdy je rekurze nezbytná (např. u stromů)
- Možnost převést cyklus na rekurzi a naopak

# Vyhledávání a řazení. 

1\. Vyhledávání (Search)

Obecně:

- **Typy vyhledávání**:

  - Sekvenční (lineární)
  - Binární (v seřazeném poli)
  - Vyhledávání v BVS (binárním vyhledávacím stromu)
  - Vyhledávání v hash tabulce
  - Vyhledávání se zarážkou (sentinel)
  - Adaptivní vyhledávání
  - B-stromy, B+ stromy (zejména zmatení mezi nimi)

Požadované informace:

- **Časová složitost** jednotlivých přístupů
- **Podmínky**, kdy lze který algoritmus použít (např. binární jen v
  seřazeném poli)
- **Výhody/nevýhody** (např. operace v hash tabulce vs. BVS)
- **Způsob vyhledávání v jednotlivých strukturách**
- **Chování při kolizích v hashovací tabulce** (implicitní/explicitní
  zřetězení)
- **Co nejde provádět u hash tabulek s explicitním zřetězením**
- **Změna složitosti při použití zarážky, uspořádanosti dat**
- **Struktury s logaritmickou složitostí pro vyhledávání i vkládání**
  (např. AVL)

2. Řazení (Sort)

Algoritmy, které se často objevovaly:

- QuickSort
- HeapSort
- MergeSort
- BubbleSort (a jeho zlepšení)
- RadixSort
- SelectSort
- InsertionSort

Požadované informace:

- **Časové a prostorové složitosti** (nejlepší/průměrný/nejhorší případ)
- **Stabilita řazení**
- **Přirozenost (naturalness)** algoritmu
- **In-place vs. out-of-place**
- **Využití jednotlivých algoritmů (např. pro externí řazení, malé
  vstupy)**
- **Popis principu algoritmu** (často bez potřeby pseudokódu)
- **Rozdíl rekurzivní vs. nerekurzivní QuickSort** (zásobník, hloubka)
- **Heap sort – implementace pomocí pole, výpočet indexů potomků**
- **Reálné využití (např. proč BubbleSort existuje)**
- **Vhodnost algoritmů pro různé typy vstupních dat**
- **Zda lze řadit rychleji než O(n log n)** (např. pomocí bitových polí
  – radix, counting sort)

3. Vlastnosti algoritmů

Často chtěli definice + příklady algoritmů, které danou vlastnost
splňují/nesplňují:

- **Stabilita**
- **Přirozenost**
- **In-place (in situ) řazení**
- **Časová a prostorová složitost**
- **Kdy se hodí použít konkrétní algoritmus podle těchto vlastností**

4. Teoretické koncepty

- **Asymptotická složitost**
- **Označení O(n), Θ(n), Ω(n)**
- **Význam logaritmické a lineární složitosti**
- **Kreslení grafů složitostí**
- **Důvod, proč nelze porovnávací algoritmy řazení rychleji než O(n log
  n)**

# Pravděpodobnost a statistika (základní pojmy, náhodná veličina a vektor, rozdělení pravděpodobnosti, generování pseudonáhodných čísel, bodové a intervalové odhady parametrů, testování hypotéz, regresní a korelační analýza).

1\. Základní pojmy pravděpodobnosti

- Definice pravděpodobnosti (klasická, geometrická)
- Náhodný jev, základní prostor (Ω)
- Podmíněná pravděpodobnost
- Formální definice vs. vysvětlení vlastními slovy

2\. Náhodná veličina

- Rozdíl mezi diskrétní a spojitou náhodnou veličinou
- Definice a vlastnosti

3\. Distribuční funkce

- Definice: pravděpodobnost, že náhodná veličina ≤ určité hodnoty
- Vlastnosti distribuční funkce
- Kreslení grafů pro různá rozložení
- Vztah k funkci hustoty pravděpodobnosti

4\. Funkce hustoty pravděpodobnosti

- Definice a vlastnosti
- Vztah k distribuční funkci (integrál)
- Kontrola, zda je daná funkce funkcí hustoty (plocha pod křivkou = 1)

5\. Rozložení pravděpodobnosti

**Diskrétní:**

- Rovnoměrné rozložení
- Poissonovo rozložení
- Binomické rozložení

**Spojitá:**

- Rovnoměrné rozložení
- Normální (Gaussovo) rozložení
- Exponenciální rozložení

6\. Normální (Gaussovo) rozložení

- Vzorec a parametry (μ, σ²)
- Standardizace na N(0,1)
- Pravidlo 3 sigma (99,7% hodnot v intervalu μ ± 3σ)
- Kreslení grafu hustoty i distribuční funkce
- Interpretace parametrů z grafu

7\. Generování pseudonáhodných čísel

- Rozdíl mezi náhodností a pseudonáhodností
- Lineární kongruentní generátor (vzorec, vlastnosti)
- Maximální perioda (2^m)
- Rozsah generátora
- Inverzní a vylučovací metoda

# Hodnocení složitosti algoritmů (paměťová a časová složitost, asymptotická časová složitost, určování časové složitosti). 

1\. Základní pojmy a definice

- **Časová složitost** - definice a co přesně měří
- **Prostorová složitost** - definice a vztah k paměťovým nárokům
- Závislost složitosti na **velikosti vstupu**
- Počet **elementárních operací/instrukcí** (ne čas!)

2\. Asymptotická složitost

- **Formální definice** asymptotických notací
- **Omikron (O)** - horní ohraničení
- **Omega (Ω)** - dolní ohraničení
- **Theta (Θ)** - přesné ohraničení
- **Matematická funkce** jako základ

3\. Grafické znázornění

- Kreslení grafů složitosti
- **Osy grafu**: X = velikost vstupu (n), Y = počet instrukcí/operací
- Konstanty **n₀** a **c** v definicích
- Průběh různých funkcí složitosti

4\. Typy složitostí s příklady

- **Konstantní O(1)** - přístup k prvku pole přes index
- **Logaritmická O(log n)** - binární vyhledávání
- **Lineární O(n)** - procházení pole
- **Kvadratická O(n²)** - bubble sort, vnořené cykly
- **Kubická O(n³)** - násobení matic
- **Exponenciální O(2ⁿ)** - některé rekurzivní algoritmy

5\. Řadicí algoritmy a jejich složitosti

- **Bubble Sort** - O(n²)
- **Quick Sort** - průměrně O(n log n), nejhorší O(n²)
- **Merge Sort** - O(n log n)
- **Heap Sort** - O(n log n)
- Nejlepší možná složitost pro porovnávací řazení: **O(n log n)**

6\. Určování složitosti algoritmů

- **Analýza cyklů** - vnořené cykly → vyšší složitost
- **Měření/testování** - zvyšování velikosti vstupu
- **Profilování** algoritmů
- Příklad: for(0..n) { for(0..n) { for(0..5) } } → O(n²)

7\. Praktické příklady na výpočet

- **Dva vnořené cykly** → O(n²)
- **Tři vnořené cykly** s různým počtem iterací
- **Násobení matic** → O(n³)
- Proč se **konstantní operace vynechávají**

# Životní cyklus softwaru (charakteristika etap a základních modelů). 

1\. Etapy životního cyklu software

- **Základní etapy** - výčet a popis jednotlivých fází
- **Analýza požadavků** - specifikace, sběr požadavků
- **Návrh** (Design) - architektura, detailní návrh
- **Implementace** (Coding) - programování
- **Testování** - různé typy a úrovně testů
- **Integrace** - spojování komponent
- **Nasazení** (Deployment) - uvedení do provozu
- **Údržba** (Maintenance) - opravy, aktualizace

2\. Modely životního cyklu

**Lineární modely:**

- **Vodopádový model (Waterfall)** - sekvenční přístup
- **V-model** - rozšíření vodopádového s důrazem na testování

**Iterativní modely:**

- **Spirálový model** - cyklické opakování fází
- **Incrementální model** - postupné přidávání funkcionalit
- **Prototypování** - rychlé vytváření prototypů

3\. Agilní metodologie

- **Principy agilního vývoje**
- **Scrum** - konkrétní agilní framework
- **Iterativní a inkrementální přístup**
- **Flexibilita a adaptabilita**
- **Continuous Integration/Delivery**

4\. Porovnání přístupů

- **Heavyweight vs. Agilní** metodologie
- **Lineární vs. Iterativní** modely
- **Kdy použít který model** - praktické aplikace
- **Výhody a nevýhody** jednotlivých přístupů

5\. Testování v životním cyklu

- **Kdy se testuje** - průběžně vs. na konci

- **Typy testování**:

  - Unit testování
  - Integrační testování
  - Systémové testování
  - **Akceptační testování** - kdy a kde v cyklu

- **Testování v různých modelech**

6\. Kvalita software

- **Faktory kvality** - funkčnost, spolehlivost, použitelnost
- **Měření kvality** - metriky, standardy
- **Zajištění kvality** - Quality Assurance (QA)
- **Kontrola kvality** - Quality Control (QC)

7\. Praktické aplikace

- **Výběr modelu pro konkrétní projekt**

- **Faktory ovlivňující výběr**:

  - Velikost projektu
  - Stabilita požadavků
  - Časové omezení
  - Zkušenosti týmu

- **Příklad**: IFJ projekt → lineární model (stabilní požadavky)

# Jazyk UML. 

UML – KONKRÉTNÍ OTÁZKY A INFORMACE:

Obecné otázky:

- Co je UML a k čemu slouží?
- Jaké existují typy UML diagramů? (strukturální vs. behaviorální)
- Jaké jsou „pohledy“ v UML?

Diagramy (často kreslit na tabuli):

- **Diagram tříd:**

  - Co obsahuje (třídy, atributy, metody).

  - Vztahy mezi třídami:

    - Asociace, agregace, kompozice, generalizace (dědičnost),
      implementace rozhraní.

  - Syntaxe (např. stereotyp \<\<interface\>\>, viditelnosti).

- **Use Case diagram:**

  - Aktéři, případy užití, vztahy (\<\<include\>\>, \<\<extend\>\>).

- **Sekvenční diagram:**

  - Kdo s kým komunikuje, co znamená šipka (zpráva).
  - Rozdíl mezi synchronní a asynchronní komunikací.

- **Komunikační diagram vs. sekvenční – rozdíly.**

- **Stavový diagram:**

  - Popis stavového automatu (např. automat na kávu).
  - Akce při přechodu (syntax: událost / akce).

- **Diagram aktivit (activity diagram):**

  - Kdy se používá, co popisuje.

# Konceptuální modelování a návrh relační databáze.

1\. Konceptuální modelování databází

- Co to je, proč se dělá, kdy ve vývoji se provádí
- ER model / ER diagram – co je entita, atribut, vztah, kardinalita
- Jak se převádí ER diagram do relační databáze (tabulky, primární a
  cizí klíče)
- Alternativy k ER – třídní diagramy (UML)

2\. Relační model a převod modelu do schématu databáze

- Relace – definice relace na doménách, n-tice
- Relační schéma – jak vypadá, jak vzniká z ER diagramu
- Vztahy 1:N, N:M – jak se převádí (např. spojovací tabulka u M:N)
- Silné vs. slabé entity

3\. Normalizace databází

- Co je normalizace – vstup, výstup, smysl, cíle (odstranit redundanci,
  zlepšit konzistenci)
- Normální formy – 1NF, 2NF, 3NF, BCNF, případně 4NF
- Podmínky pro jednotlivé normální formy
- Jak opravit tabulku, která není ve 2NF (např. dekompozice tabulky, FK
  vztahy)

4\. Funkční závislosti

- Definice funkční závislosti, plná vs. částečná funkční závislost
- Význam funkčních závislostí při normalizaci
- Kandidátní a primární klíč, složený klíč

5\. Systémy souborů (výjimečně)

- Správa souborů, i-uzly, alokační bloky, FAT tabulka (spíše Orság)

# Reprezentace a uložení strukturovaných dat, serializace a deserializace, relační datový model, jazyk SQL, transakce (DB a business). 

Klíčová témata, která se často opakují:

Strukturovaná data, serializace a deserializace

- **Struktura vs. kolekce** – Nutné rozlišovat (např. struktura =
  záznam, kolekce = seznam struktur).
- **Serializace = převod struktury do řetězce** (např. JSON, XML).
- **Deserializace = opak – načtení řetězce zpět do paměti**.
- Ukázky v **JSON** nebo **XML** – nutné být schopen napsat a popsat
- **Proč JSON?** – jednodušší, rozšířenější, zdarma.

Relační model

- **Relace = podmnožina kartézského součinu domén** – chtějí slyšet
  přesnou definici.
- **Doména = množina hodnot daného typu**.
- **Schéma relace = název + názvy a typy atributů**.
- **Tělo relace = konkrétní řádky (n-tice)**.

**🔧 SQL – klíčové konstrukce**

- **Rozdělení příkazů**:

  - DDL (CREATE, ALTER, DROP),
  - DML (INSERT, UPDATE, DELETE),
  - DQL (SELECT),
  - DCL (GRANT, REVOKE),
  - TCL (COMMIT, ROLLBACK).

- **SELECT** – projekce, **WHERE** – selekce, **GROUP BY**, **HAVING**.

- Umět vysvětlit a napsat

SELECT AVG(plata)

FROM Zamestnanci

GROUP BY oddeleni

HAVING AVG(plata) \> 30000;

JOINy

- **INNER JOIN** – spojení jen pokud existuje shoda.
- **LEFT / RIGHT OUTER JOIN** – i když na jedné straně není shoda,
  zůstanou řádky.
- **NATURAL JOIN** – automaticky spojuje podle stejně pojmenovaných
  sloupců.
- **CROSS JOIN** – kartézský součin.
- Užitečné je kreslit si **tabulky a výsledky spojení**.

Transakce a ACID

- **A**tomicity – vše nebo nic,
- **C**onsistency – data jsou konzistentní,
- **I**solation – nezávislé transakce,
- **D**urability – po potvrzení zůstanou změny trvalé.
- **Příkazy**: BEGIN, COMMIT, ROLLBACK.

Vztah relační algebry a SQL

- SQL příkazy odpovídají relačním operacím:

  - Projekce = SELECT sloupců,
  - Selekce = WHERE,
  - Sjednocení = UNION,
  - Průnik = INTERSECT,
  - Rozdíl = EXCEPT.

Další pojmy a oblasti

- **Integritní omezení** – NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY.
- **Klíče** – primární, kandidátní, cizí.
- **Reprezentace strukturovaných dat** – nejen tabulky, ale i hierarchie
  (např. XML).

# Webová uživatelská a aplikační rozhraní, správa sezení a autentizace

1\. Správa sezení a autentizace (Sessions & Authentication)

**Časté prvky:** HTTP protokol, cookies, session ID, stavovost vs.
bezstavovost, rozdíl mezi Session a JWT

- HTTP je **bezstavový protokol** → nutnost udržovat stav na serveru
  nebo klientovi.

- **Session**:

  - Server si uloží data (např. přihlášený uživatel) pod unikátním
    **Session ID**.
  - Session ID se předává pomocí **cookie**.

- **Autentizace pomocí Session**:

  - Uživatelské jméno + heslo → ověření → vytvoření session → session ID
    do cookie.
  - Každý další požadavek: cookie s session ID → ověření identity na
    serveru.

- **JWT**

2\. REST API a HTTP komunikace

**Časté prvky:** HTTP metody, endpointy, status kódy, komunikace
klient-server

- Základy REST (Representational State Transfer):

  - Použití **HTTP metod**: GET, POST, PUT, DELETE
  - Jednoduchý a **bezstavový protokol**
  - **Resource-oriented** přístup

- **fetch() v JavaScriptu** – klientská knihovna pro posílání HTTP
  požadavků

3\. Relační databáze a SQL

**Časté prvky:** Relace, primární a cizí klíče, základní SQL dotazy
(SELECT, INSERT…)

- **Relace** = vztah mezi tabulkami pomocí klíčů (1:N, M:N…)

- **SQL příkazy**:

  - SELECT – výběr
  - INSERT – vkládání
  - UPDATE – aktualizace
  - DELETE – mazání

- Ne šlo o hloubku, ale **porozumění základnímu modelu a syntaxe**

4\. Objektově orientované programování (OOP)

**Časté prvky:** Třídy, dědičnost, zapouzdření, rozdíl oproti
procedurálnímu programování

- Co OOP přináší:

  - **Modularita, opakovatelnost, rozšiřitelnost**
  - **Dědičnost**, **polymorfismus**, **zapouzdření**

- Srovnání s procedurálním přístupem

# Principy a struktury správy souborů a správy paměti. 

1\. SPRÁVA PAMĚTI

Základní koncepty:

- **LAP (Logický/Lineární Adresový Prostor)** vs **FAP (Fyzický Adresový
  Prostor)**
- **MMU (Memory Management Unit)** - mapování LAP na FAP
- **Virtualizace paměti** - proč je virtuální paměť větší než fyzická

Přidělování paměti:

- Proces přidělení paměti procesu (např. 5B RAM)
- **Strategie přidělování paměti**
- **Fragmentace** - co to je a jak se řeší

2\. STRÁNKOVÁNÍ

Základy:

- **Co je stránkování** a k čemu slouží
- **Stránky** (v LAP) vs **Rámce** (ve FAP)
- **Velikost stránek** - typicky 4KiB
- **Kdo řeší překlad** - HW implementace

Typy stránkování:

- **Víceúrovňové tabulky stránek**
- **Invertované tabulky stránek**
- **Hashovací tabulky stránek**

Konkrétní výpočty:

- Kolik bitů má hodnota v tabulce stránek
- Indexování stránek při dané velikosti (např. stránka 4KiB, prostor
  32b)

3\. SOUBOROVÉ SYSTÉMY

Základní pojmy:

- **Alokační blok** - základní jednotka na disku (obvykle 4096 bajtů)
- **Organizace** - od fyzického disku po OS

Konkrétní systémy:

- **FAT** - File Allocation Table
- **Unix FS** - i-uzly, boot block, super block
- **B+ stromy** pro organizaci dat
- **Extenty** pro velké soubory

Detaily:

- Obsah adresáře (číslo prvního bloku souboru)
- Velikost i-uzlu a jeho obsah
- Kde je uložené jméno souboru

4\. PROCESOR A INSTRUKCE

Architektura:

- Složení PC (Personal Computer)
- **Registry** - typy a účel
- **Instrukční sada** - proč Intel
- **Příznakový registr**

Programové konstrukce:

- **Volání funkcí** - co se děje
- Implementace **while** a **do-while** smyček v assembleru

Tipy pro zkoušky:

- Důležité je umět **konkrétní výpočty** a **praktické příklady**
- Při stránkování znát **HW vs SW implementaci**

# Plánování a synchronizace procesů, transakce. 

1\. SYNCHRONIZACE PROCESŮ

Základní koncepty:

- **Proč se synchronizace dělá** - zabránění současnému přístupu k datům
- **Race condition** a **data race** - co to je a kdy vzniká
- **Kritická sekce** - ochrana před současným přístupem více procesů
- **Atomicita** - operace, které se nesmí přerušit

Synchronizační mechanismy:

- **Semafory:**

  - Datová struktura (integer + fronta čekajících procesů)
  - Operace **lock/unlock** (musí být atomické)
  - **Pasivní čekání** vs **aktivní čekání**
  - Implementace (obvykle OS)

- **Mutexy** - základní princip

- **Atomické instrukce**

- **Bakery algoritmus** - práce s lístky

Problémy:

- **Deadlock:**

  - Definice a vznik
  - **Coffmanovy podmínky** (4 podmínky pro deadlock)
  - Řešení - prevence, detekce, recovery

- **Spinlock** - aktivní čekání

2\. PLÁNOVÁNÍ PROCESŮ

Základy:

- **Co je proces** - definice a vlastnosti
- **Vlákno vs proces** - rozdíly a porovnání
- **Stavy procesu** - init, runnable, running, waiting, terminated
- **Přepínání kontextu**
- **Plánovač vs dispečer** - rozdíl funkcí

Plánovací algoritmy:

- **FCFS (First Come First Served)** - FIFO princip

- **Round Robin:**

  - Princip časových kvant
  - **Kvantum** - velikost časového úseku

- **SJF (Shortest Job First)**

- **CFS (Completely Fair Scheduler)** - složitější, férový algoritmus

- **Víceúrovňové plánování**

Typy plánování:

- **Preemptivní plánování** - proces může být přerušen
- **Nepreemptivní plánování** - proces běží do konce
- **Stárnutí procesů** - jak se řeší

Problémy plánování:

- Čemu se snažíme vyhnout při plánování
- Podle čeho se určuje, jak dlouho proces poběží

3\. MEZIPROCESOVÁ KOMUNIKACE

- Základní principy komunikace mezi procesy
- Metody komunikace

4\. DATABÁZOVÉ TRANSAKCE (vedlejší téma)

- Základní vlastnosti a principy

Tipy pro zkoušky:

- Umět **praktické příklady** (např. 2 procesy měnící společnou
  proměnnou)
- Znát **konkrétní implementace** (struktura semaforu, operace
  lock/unlock)

# Objektová orientace (základní koncepty, třídně a prototypově orientované jazyky, OO přístup k tvorbě SW). 

1\. ZÁKLADNÍ KONCEPTY OOP

Definice základních pojmů:

- **Objekt** - entita s atributy a metodami, výpočetně plná entita
- **Třída** - **NIKDY neříkat "šablona"!** Burget chce slyšet **"datový
  typ"**
- **Rozdíl mezi třídou a objektem** - třída je předpis, objekt je
  instance
- **Konstruktor** - jak se vytváří objekty

Čtyři základní principy OOP:

954. **Zapouzdření (Encapsulation)**

     - Identifikátory viditelnosti: **Public, Private, Protected**
     - Udržování konzistence vnutřního stavu
     - Výhody zapouzdření
     - K čemu jsou dobré privátní objekty

955. **Dědičnost (Inheritance)**

     - Potomek **je kompatibilní s rodičem, ale ne naopak**
     - Jak se ukládají **instanční proměnné při dědění**
     - Které proměnné se alokují při instanciaci potomka
     - **UML diagram tříd** - vztah generalizace
     - Symbol pro dědičnost v UML

956. **Polymorfismus**

     - **Přetěžování metod** (Method Overloading)
     - **Virtuální metody**
     - Výhody polymorfismu (často se ptají)

957. **Abstrakce**

     - **Abstraktní třídy** vs **rozhraní (interface)**
     - Rozdíl mezi interface a dědičností

2\. TŘÍDNÍ vs PROTOTYPOVÉ JAZYKY

Třídní jazyky:

- Jak se vytváří objekty (konstruktor)
- Příklady v konkrétních jazycích (Python, Java)
- Ukládání metod a stavových proměnných v paměti

Prototypové jazyky:

- **Klonování objektů**
- **Delegování**
- **Rys (Trait)**
- Jak funguje **"new"** v JavaScriptu
- **Tabulka metod**
- **Sloty**
- Co se dá měnit po klonování

3\. VÝHODY OOP

Proti strukturálnímu programování:

- **Z pohledu programátora** (ne jen uživatele tříd)
- **Z pohledu softwarového inženýrství**
- **Znovupoužitelnost kódu**
- **Modularita**
- Křena často vyvrací, že i strukturální programování to umí -
  **připravit se na argumentaci**

4\. NÁVRHOVÉ VZORY (Design Patterns)

- **Factory (Továrna)**
- **Observer**
- Základní znalost pattern

5\. POKROČILÉ KONCEPTY

Ukládání v paměti:

- Jak se ukládají **instance tříd** v paměti
- Ukládání při **dědičnosti** - co se děje s pamětí
- Jak se ukládají **metody vs stavové proměnné**

Komunikace objektů:

- Jak mezi sebou objekty komunikují
- Jak mohou sdílet vlastnosti

# Programování v jazyku symbolických instrukcí (činnost počítače, strojový jazyk, symbolický jazyk, assembler). 

**Volání funkcí v assembleru:**

- Instrukce CALL, RET, PUSH, POP.
- Co se ukládá na zásobník a proč (návratová adresa, EBP, parametry).
- Vytvoření zásobníkového rámce pomocí PUSH EBP, MOV EBP, ESP, práce s
  ESP.

**Zásobník:**

- Jak roste (směrem dolů).
- Kam ukazují registry ESP, EBP v různých momentech.
- Lokální proměnné – alokace na zásobníku (SUB ESP, X).

**Předávání parametrů funkcím:**

- Předávání přes zásobník.
- Kdo uklízí zásobník – konvence (cdecl, stdcall apod.).
- Alternativy: přes registry, globální paměť, datovou sekci.

**Zásobníkový rámec (stack frame):**

- Popis, nakreslení schématu.
- Co kam patří – návratová adresa, EBP, parametry, lokální proměnné.

**Konvence volání funkcí:**

- Pořadí argumentů.
- Kdo je odpovědný za úklid zásobníku (caller/callee).
- Zmínka o ABI.

**Příznakový registr (Flags):**

- CF, ZF, OF a jejich využití (zejména u podmínek a skoků).
- Význam při znaménkových/bez znaménkových operacích.
- Využití pro podmíněné skoky (JE, JNE, JG, JL, atd.).

**Cykly a podmínky v assembleru:**

- Tvorba while, do-while, for smyček v JSI.
- Použití skokových instrukcí (JMP, LOOP, JZ, JNZ...).

**Formát instrukcí a práce s pamětí:**

- Paměťové operandy.
- Přístup přes \[\] – např. \[ebp-4\] jako lokální proměnná.

**Rozdíl mezi symbolickým a strojovým jazykem:**

- Proč programujeme v assembleru.
- Výhody symboliky (čitelnost, optimalizace, ladění).

# Služby aplikační vrstvy (web, e-mail, DNS, IP telefonie, správa SNMP, Netflow). 

** 1. VoIP / SIP / RTP**\
**Důležité okruhy:**

- Co je VoIP, SIP, RTP – obecná architektura
- Ústředny, telefony, registrace uživatele (REGISTER, INVITE, OK, ACK)
- **SIP URI** – formát např. sip:uzivatel@domena.cz
- **DNS SRV záznam** – ukázat konkrétní zápis
- Signaling vs. media (RTP běží mimo SIP proxy)
- RTP přes UDP – co se stane při ztrátě paketu

**2. DNS**\
**Důležité okruhy:**

- Co je DNS, jaký je jeho účel
- **Hierarchie domén**, root servery, TLD, autoritativní / rekurzivní /
  cache DNS servery
- **Typy záznamů**: A, AAAA, MX, CNAME, SRV
- **Záznam SRV** – formát: \_service.\_proto.name. TTL class SRV
  priority weight port target.
- **DNS zpráva** – struktura hlavičky a dotazu
- Proces překladu jména na IP (rezoluce), forward/reverse lookup
- **DNSSEC** (zmíněno okrajově)

**3. HTTP**\
**Důležité okruhy:**

- Jak vypadá požadavek a odpověď (formát, hlavičky)
- **GET vs POST**
- **Stavové kódy**: 200 OK, 301, 404, 500 atd.
- Co je URL a jak ji rozdělíme
- Jak vypadá základní komunikace mezi klientem a serverem

**4. Email (SMTP, POP3, IMAP)**\
**Důležité okruhy:**

- Architektura emailových služeb: MUA, MTA, MDA
- SMTP – jak funguje, kde hledá kam doručit email (MX záznam)
- Rozdíl mezi **SMTP** (odesílání) a **POP3/IMAP** (stahování)
- E-mailová adresa, jak se zpracuje – přes DNS → MX → A záznam
- **Obálka vs. hlavička emailu**
- Proces doručení zprávy: co se děje od odeslání po doručení

**5. NetFlow**\
**Důležité okruhy:**

- Co je to **tok** (flow), jak se definuje
- Exportér vs. kolektor – role, co posílá a co sbírá
- Časovače u UDP – jak poznáme konec toku (inactive, active timer)
- U TCP – poznání konce z **flagů** (např. FIN)
- **Agregace** – proč se dělá, jak pomáhá (úspora dat)
- **Sampling** (u velkého množství dat)
- Možnosti detekce útoků (např. DDoS)

**6. SNMP**\
**Důležité okruhy:**

- Co to je, k čemu slouží
- Architektura: agent, manager
- Typy zpráv: GET, SET, TRAP
- Na jakém portu běží (UDP 161 / 162)
- Verze protokolu a bezpečnostní rozdíly (v3 s autentizací)

# TCP/IP komunikace (model klient-server, protokoly TCP, UDP a IP, řízení a správa toku TCP). 

1\. Model TCP/IP vs. ISO/OSI

- Popis vrstev obou modelů, hlavně:

  - **Aplikační**
  - **Transportní**
  - **Síťová**

- **Porovnání** s OSI – kolik vrstev, které odpovídají sobě.

- Často chtějí **nakreslit TCP/IP model** a pak jdou vrstvu po vrstvě.

- Příklad: co se přidává do hlavičky na každé vrstvě (porty, IP adresy,
  checksum, atd.).

2\. TCP vs UDP

- **Základní rozdíly**:

  - TCP: spojovaný, spolehlivý, stream bajtů, řízení toku a přetížení,
    pořadí paketů.
  - UDP: nespojovaný, nespolehlivý, žádné pořadí, rychlejší.

- **Aplikační protokoly**, které používají TCP (např. HTTP, FTP) vs UDP
  (např. DNS, VoIP).

- **Často se ptají, proč zvolit jeden nebo druhý.**

- Otázky typu: *"K čemu bys použil UDP a proč ne TCP?"*

3\. TCP: detaily

- **3-way handshake**: SYN, SYN-ACK, ACK – často chtějí **nakreslit**.

- **Sekvenční a potvrzovací čísla** – na co jsou, proč jsou potřeba.

- **Spořádaný přenos**, **znovuodeslání** ztracených segmentů.

- **Řízení toku a zahlcení**:

  - Sliding Window
  - Go-back-N
  - Selective Repeat
  - **Tahoe a Reno** (chytáky – když to zmíníš, někdy se na to rovnou
    ptají)

- **Checksum** – detekce poškození dat.

- **Zajištění správného pořadí paketů**.

4\. UDP: detaily

- Žádné navazování spojení.
- Nespolehlivý – **ale** někdy aplikace řeší spolehlivost samy (pozor,
  není to součástí UDP).
- Používá se tam, kde nevadí ztráta nebo je důležitá rychlost.

5\. Adresace

- Na **transportní vrstvě**: porty (číslo portu zdroje a cíle).

  - Kdo je přiděluje (IANA), známé vs dynamické porty.

- Na **síťové vrstvě**: IP adresy (IPv4 vs IPv6, jejich tvar).

- **DNS**, URL, A záznam – jak z doménového jména dostaneš IP.

- Vědět rozdíl mezi **adresací na různých vrstvách.**

6\. Chytáky / Detaily, kde se studenti zadrhli

- K čemu přesně je sequence number, acknowledgement number.
- Co je **spoľahlivý** přenos, co přesně to znamená a jak se zajišťuje.
- **TCP může ztratit data?** (→ **ne**, pokud spojení funguje správně,
  zajistí doručení).
- Fragmentace na síťové vrstvě (IP) – pole jako „offset“.
- K čemu je **multicast, broadcast, unicast**.
- Když zmíníš sliding window, často se ptají na detaily (velikost okna,
  jak funguje přetečení).
- **ICMP** – správně na síťové vrstvě, ne transportní.
- **Zmatek mezi směrováním zařízení vs síťovky** – u IP adres se směruje
  síťové rozhraní, ne celé zařízení.

# Směrování a zabezpečení přenosů v počítačových sítích (algoritmy Link-State, Distance-Vector, šifrování, autentizace a integrita dat)

Téma: Autentizace, integrita dat, šifrování, digitální podpisy

1069. **Autentizace**

      - Co je to autentizace (ověření identity účastníka komunikace)
      - Metody: hesla, tokeny, digitální podpisy
      - Asymetrická kryptografie: použití public/private klíčů

1070. **Digitální podpis**

      - Co to je, jak funguje:

        - Zpráva → hash → zašifrování privátním klíčem → přiložení k
          zprávě
        - Příjemce: dešifruje podpis pomocí veřejného klíče → porovná s
          vlastním hashem

      - Účel: zajištění **autenticity** a **integrity**

      - Algoritmy: RSA (šifrování), MD5, SHA (hashování)

      - Neplést hash s šifrováním — Matoušek je na to velmi přísný

1071. **Certifikáty**

      - K čemu slouží: důvěryhodnost veřejných klíčů
      - Obsah: jméno subjektu, veřejný klíč, platnost, podpis CA
      - Certifikační autorita (CA): kdo certifikát vydává a podepisuje

1072. **Integrita dat**

      - Zajišťuje, že data nebyla po cestě změněna
      - Prostředek: kryptografické hashování
      - Kryptografický hash ≠ běžný hash: odolnost vůči kolizím,
        nevratnost
      - Problém: MitM může podvrhnout zprávu i hash → řešení: HMAC,
        asym. kryptografie

1073. **Šifrování**

      - Rozdíl: **symetrické** (rychlé, 1 klíč), **asymetrické**
        (pomalejší, 2 klíče)
      - Proč se v TLS přechází z asym. na sym. – kvůli výkonu

Téma: Směrování, Distance Vector vs Link State

1074. **Obecně o směrování**

      - Co je to směrování, co dělá router
      - Co je ve směrovací tabulce
      - ISO/OSI vrstva směrování (síťová)

1075. **Směrovací algoritmy**

      - **Distance Vector (DV)**: RIP, každému sousedovi posílá celou
        tabulku
      - **Link State (LS)**: OSPF, posílá informace o stavu linek,
        Dijkstra
      - Rozdíly mezi DV a LS: kdo co ví, jaké informace posílá

1076. **Praktické otázky**

      - Jak se naplní směrovací tabulka (staticky / dynamicky)
      - Nakreslit jednoduchou síť a vytvořit směrovací tabulky
      - Pochopení iterací (např. u DV)

Doporučení k přípravě:

- Umět vysvětlit:

  - rozdíl hash vs šifra vs podpis
  - co dělá router a směrovací protokoly
  - digitální podpis krok za krokem
  - TLS a výměna klíčů

- Umět **nakreslit jednoduché schéma sítě**

- Naučit se pojmy: CA, DV, LS, HMAC, RSA, OSPF, RIP
