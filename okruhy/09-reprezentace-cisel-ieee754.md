---
title: "9. Reprezentace čísel a základní dvojkové aritmetické operace (doplňkové kódy, pevná a plovoucí řádová čárka, IEEE 754)"
category: okruh
okruh: 9
tags: [computer-architecture, number-representation, math, hardware]
aliases: [dvojkový doplněk, doplňkový kód, pevná řádová čárka, plovoucí řádová čárka, IEEE 754, float, double, BCD]
relationships:
  - target: "[[okruhy/02-kombinacni-logicke-obvody]]"
    type: uses
  - target: "[[okruhy/18-ciselne-soustavy]]"
    type: related_to
sources: ["_sources/docx/szz-09.docx"]
summary: Reprezentace celých a desetinných čísel v počítači (kódy se znaménkem, pevná/plovoucí řádová čárka, IEEE 754) a základní aritmetické operace.
provenance:
  extracted: 0.9
  inferred: 0.07
  ambiguous: 0.03
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 9. Reprezentace čísel a binární aritmetika

> SZZ okruh 9 (FIT BUT). Rozsah čísel je omezen **počtem bitů** (short int 16 b, int 32 b, long 64 b).

## Shrnutí

## Celá čísla se znaménkem

- **Přímý kód** — první bit znaménko; problém **dvojí nuly**, komplikuje sčítání/odčítání.
- **Aditivní kód (posunutá nula)** — číslo posunuté o konstantu (využití v exponentu IEEE 754).
- **Jedničkový doplněk** — záporné = negace bitů; opět dvojí nula.
- **Dvojkový doplněk** — záporné = negace + 1; **jediná nula**, sčítání/odčítání **stejně jako bez znaménka** → nejpoužívanější.

## Desetinná čísla

- **Pevná řádová čárka** — pevný počet bitů na celou a desetinnou část; dnes vzácné.
- **Plovoucí řádová čárka (IEEE 754)** — znaménko **S**, **mantisa** M (přímý kód, implicitní 1), exponent **E** (kód s posunutou nulou), základ 2.
  - **single (float, 32 b)** — exponent 8 b (posun −127), mantisa 23 b, přesnost ~7 dekadických číslic.
  - **double (64 b)** — exponent 11 b (posun −1023), mantisa 52 b, přesnost ~16 číslic.

![[media/szz-09/media/image11.png]]
*IEEE 754 (single): interpretace hodnot podle exponentu — normalizovaná/denormalizovaná čísla, ±0, ±∞, NaN.*

> [!note] Ke kontrole (ověřeno proti standardu IEEE 754)
> Plné znění uvádí u **single** rozlišitelnost normalizovaných **2^-127** a nenormalizovaných **2^-150** a u **double** **2^-1023** / **2^-1075** — všechny jsou **o jedničku posunuté**. Správně: single nejmenší normalizované = **2^-126**, nejmenší denormalizované = **2^-149**; double **2^-1022** / **2^-1074**. Rozsah „〈-2^127, 2^127〉" je také přibližný — největší konečné single ≈ 2^128.

- **Chyba zobrazení** — např. 0,1 nelze přesně vyjádřit; pro finance se používá **BCD** nebo **fixní řád** (uložení celého čísla setin).

## Aritmetické operace

- **Sčítání** — celočíselné jako v desítkové soustavě; přetečení → **OF** (signed) / **CF** (unsigned). Floating point **není asociativní** (zaokrouhlovací chyby); nutno převést na společný exponent.
- **Odčítání** — bitová negace + sčítání s C0 = 1.
- **Násobení** — výsledek až 2× širší; u doplňkového kódu nutno **rozšířit MSB** (znaménko). IEEE 754: znaménko = XOR, exponenty se sčítají, mantisy se násobí.
- **Dělení** — náročné (např. bez restaurace zbytku, SRT).

![[media/szz-09/media/image6.png]]
*Sčítání čísel v plovoucí řádové čárce — zarovnání na společný exponent.*

## Souvislosti

Sčítačky realizující tyto operace popisuje [[okruhy/02-kombinacni-logicke-obvody]]; převody mezi soustavami viz [[okruhy/18-ciselne-soustavy]].


## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Reprezentace čísel** ↪ [[#Desetinná čísla]]
- *Fixed vs. floating point?* → Pevná: pevný počet bitů na celou/desetinnou část (omezený rozsah); plovoucí: mantisa × 2^exponent (velký rozsah, omezená přesnost).
- *Struktura IEEE 754?* → sign bit + exponent (s BIASem) + mantisa (implicitní 1); single 32 b (E 8 b, M 23 b, bias 127), double 64 b (E 11 b, bias 1023).
- *Co je BIAS?* → Posun exponentu (kód posunuté nuly) → umožní záporné exponenty bez znaménkového bitu.

**Kódy záporných čísel** ↪ [[#Celá čísla se znaménkem]]
- *Přímý / jedničkový / dvojkový doplněk?* → Přímý (znaménkový bit, dvojí nula); jedničkový doplněk (negace bitů, dvojí nula); dvojkový doplněk (negace + 1, jediná nula → nejpoužívanější, sčítání/odčítání jako bez znaménka).
- *Proč nejmenší záporné nelze invertovat?* → Jeho kladný protějšek se nevejde do rozsahu (asymetrie doplňkového kódu).

**Aritmetické operace** ↪ [[#Aritmetické operace]]
- *Kdy je výsledek zobrazitelný / přetečení?* → signed → overflow flag (OF); unsigned → carry flag (CF).
- *FP sčítání a normalizace?* → Zarovnat na společný (větší) exponent, sečíst mantisy, normalizovat; FP sčítání není asociativní (zaokrouhlení).
- *Proč nelze přesně 0,1?* → Není konečným součtem mocnin 2 → pro finance BCD / fixní řád.

## Plné znění (ke studiu)

Čísla jsou v počítačích reprezentována hodnotami
jednotlivých bitů - **binárně**, tedy ve **dvojkové soustavě**. Narozdíl
od reálného světa je rozsah čísel omezen **počtem bitů**, které jsou pro
číslo vyhrazeny. Dnes jsou obvykle používány tři číselné rozsahy, které
mohou být **znaménkové** i **bez znaménka**, jsou to:

- **short** **int** - 16 bitů,

- **integer** - 32 bitů,

- **long int** - 64 bitů.

## Reprezentace celých čísel se znaménkem

Reprezentace znaménka vždy sníží rozsah **absolutní**
hodnoty čísla na **polovinu**, nicméně umožňuje reprezentovat **záporná
čísla** a **celkový počet** čísel se tak **nezmění** (až na dvojí nulu).
Reprezentace znaménka je realizována následovně:

- **Přímý kód**: **První bit** je rezervován pro
  znaménko (**1** pro **záporná**, **0** pro **kladná**). Existují zde
  však **2 nuly** (**+0** a **-0**). Použití například v IEEE754.
  (10000001 = -1). Kód **komplikuje** algoritmy pro **sčítání**,
  **odčítání** i **násobení**, nutnost testovat na znaménko. Dalším
  problémem je existence **dvojí** nuly.

- **Aditivní kód (kód s posunutou nulou)**: Číslo je
  posunuté o nějakou danou konstantu (Např. -127 = 00000000; 128 =
  11111111; 1 = 10000000; 0 = 01111111 - viz IEEE 754; -1 = 01111110…).
  **Nevýhodou** je, že reprezentace kladných znaménkových čísel se
  **liší** od neznaménkových, a při **násobení** se musí odečítat určená
  konstanta. Sčítání lze provádět normálně.

- **Jedničkový doplněk** (inverzní kód): Záporná
  hodnota se získá **znegováním** všech bitů kladného čísla (MSB musí
  být u **kladných** vždy **0** a u **záporných** vždu **1**). Např.
  0101 = 5, 1010 = -5, 0000 = 0, 1111 = -0. Kód **komplikuje** algoritmy
  pro **sčítání** a **odčítání** (jiné než u čísel bez znaménka) i
  **násobení**. Dalším problémem je existence **dvojí** nuly.

- **Dvojkový doplněk** (doplňkový kód): Kladné číslo
  je reprezentováno normálně, záporné však je **inverzí** kladného čísla
  a **přičtením** **1**. **Nejpoužívanější** formát. Pouze jedna
  reprezentace 0. (11111111 = -1). Sčítání a odčítání lze realizovat
  **stejně** jako s neznaménkovými čísly, u násobení je nutné
  **replikovat** (nakopírovat) pŭvodní **MSB** na **dvojnásobný** rozsah
  čísla na všechny následující pozice až po nový MSB, aby nedošlo ke
  změně znaménka po operaci.

## Reprezentace desetinných čísel

Umožňují reprezentovat reálná čísla s omezenou
přesností.

### Pevná řádová čárka

Pro zobrazení kladných reálných čísel. **Přesný
počet** bitů je rezervováno pro **celou** část a **zbytek** pro
**desetinnou** část čísla. Dnes se skoro nevyužívá. Např. 5 číslic pro
celou část a 3 číslice pro desetinnou, **00101001** = **5.125**.

### Plovoucí řádová čárka (Floating point) - IEEE 754

Číslo je reprezentováno:

- **znaménkovým bitem** (*S*) - MSB - **1** znamená
  záporný, **0** kladný,

- **mantisou** (*M*) - v přímém kódu, obsahuje
  **implicitní 1**,

- **základem** (*B*) - je implicitní, rovna číslu
  **2**,

- **exponentem** (*E*) - v kódu posunuté nuly, což
  umožňuje vyjádřit záporný exponent.

**IEEE 754** definuje uložení čísla v plovoucí řadové
čárce jako MSB je znaménkový bit, následují bity exponentu a poté až
bity mantisy. Definovány jsou dvě reprezentace lišící se přesností a
rozsahem čísla.

- **Single precision** (float - 32 bitů): Exponent má
  rozsah **8** bitů a je posunut o **-127** (polovinu rozsahu, 0 a 255 v
  exponentu představují speciální hodnoty; exponent je roven 0, pokud je
  jeho hodnota 127 binárně), mantisa je vyjádřena na **23** bitech, MSB
  je znaménkový. **Přesnost** je **7** dekadických čísel, rozsah
  zobrazení je **〈-2^127, 2^127〉**, rozlišitelnost **normalizovaných**
  čísel je **2^-127** a **nenormalizovaných** **2^-150**. Největší a
  **druhé** největší číslo se liší o **2^104** (23 jedniček \<\< 127 -
  (22 jedniček a 0) \<\< 127 = 2^104).
  
![[media/szz-09/media/image11.png]]

![[media/szz-09/media/image3.png]]


- **Double precision** (double - 64 bitů): Exponent
  má rozsah **11** bitů a je posunut o **-1023** (polovinu rozsahu),
  mantisa je vyjádřena na **52** bitech, MSB je znaménkový. **Přesnost**
  je **16** dekadických čísel, rozsah zobrazení je **〈-2^1023,
  2^1023〉**, rozlišitelnost **normalizovaných** čísel je **2^-1023** a
  **nenormalizovaných** **2^-1075**.

**Explicitní jednička** - V mantise čísla je nutné
explicitně mít jedničku.
![[media/szz-09/media/image7.png]]


**Implicitní jednička** - Umožňuje zvýšit rozsah
reprezentovaného čísla o jeden bit, v mantise se jednička neuvádí. Až na
**denormalizované** čísla se s ní pracuje implicitně - **1.011 -\>
011**.

### Chyba zobrazení

Jelikož se číslo skládá ze **součtu zlomků** mocnin 2
(např. 2<sup>-2</sup> = ¼) **není** možné na konečném počtu bitů
(registru) **reprezentovat** všechna čísla, a tak dochází k
**nepřesnostem**. Např. číslo **0.1** nelze přesně vyjádřit, což je
obvyklá hodnota ve finančnictví a je nutné pro tyto aplikace používat
jiné kódování čísel. Používá se **BCD (Binary Coded Decimal)
kód**

- Každá dekadická číslice je zobrazena v jednom niblu
  (4 bitech bytu). Znaménko může být v prvním bitu. 01000010 =
  42.

Další nepřesnosti vznikají při sčítání/odčítání
čísel, která jsou od sebe **řádově** vzdálená, mají **výrazně** rozdílný
exponent (menší číslo může být úplně ignorováno).

**Fixní řád**

- Čísla se ukládají jako celá s předem definovaným
  počtem desetinných míst. Např. 0,1 Kč = 10 setin -\> uložíme jako
  integer 10\
  123,45 Kč -\> 12345

- Pak při získávání hodnoty pouze podělíme
  /100

- **Nevýhoda:** Náchylné na chyby -\> využívat
  gettery a settery pro získávání a nastavování hodnoty

- **Výhoda:** Mnohem rychlejší než práce s
  floaty

## Matematické operace

### Sčítání

- **Celočíselné** sčítání se provádí stejně jako v 10
  soustavě. V případě sčítání v procesoru může dojít k **přetečení**
  (součet se nevleze do podporovaného rozsahu)\
  -\> nastavení **overflow flag** (OF) pro signed, **carry flag** (CF)
  pro unsigned.\
  
![[media/szz-09/media/image4.png]]


- **Floating point** sčítání není **asociativní**
  vlivem **zaokrouhlovacích** chyb. V **IEEE 754** se u sčítání musí
  nejdříve převést obě čísla na **stejný exponent**. Vždy se převádí
  číslo **s** **menším** exponentem **na větší**. (Nezapomenout na
  **implicitní 1**)[<u>HOW TO: Adding IEEE-754 Floating Point
  Numbers</u>](https://youtu.be/mKJiD2ZAlwM)
![[media/szz-09/media/image6.png]]


### Odečítání

V CPU lze odčítání realizovat **bitovou negací**
jednoho ze sčítanců a použít sčítání s nastavením **C0** na **1**.
Stejně tak je výhodné provádět ručně, pro člověka je to přirozenější.\



![[media/szz-09/media/image5.png]]


### Násobení

- **Celočíselné**: Výsledek může zabírat až
  **dvojnásobek** bitů. Při násobení čísel v doplňkovém kódu musí být
  nejdřív u obou čísel **rozšířen** **MSB** značící znaménko na
  **dvojnásobnou** přesnost původního čísla ve dvojkovém doplňkovém
  kódu.
![[media/szz-09/media/image8.png]]

![[media/szz-09/media/image10.png]]


- **IEEE 754**:

  - **znaménko** výsledku se určí jako **XOR**
    znamének **činitelů**,

  - **exponent** se určí součtem exponentů
    činitelů,

  - **mantisa** se určí celočíselným násobením
    činitelů doplněných o **implicitní 1**.

- Bootovo překódování (Může se také hodit
  nastudovat.)
![[media/szz-09/media/image9.png]]


### Celočíselné dělení

V počítači velmi náročná operace prováděná mnoha
různými metodami. Znaménkové dělení se může provádět s absolutní
hodnotou a až poté dojde k doplnění znaménka.

Postupy dělení:

- triviálně na principu **dělení pod
  sebou**,
![[media/szz-09/media/image1.png]]


- **bez restaurace nezáporného zbytku**

  1.  začne se odečtením dělitele od dělence,

  2.  na základě MSB se určí výsledek **i-tého**
      bitu: pro **MSB=1** je výsledek **0** - záporné číslo, pro
      **MSB=0** je výsledek **1** - kladné číslo),

  3.  dělitel se posune o 1 bit doleva (násobení 2) a
      **MSB** se **zahodí**,

  4.  pokud je výsledek i-tého bitu **0**, **přičte**
      se dělitel, v **opačném** případě se dělitel **odečte**.

  5.  pokud nebylo dosaženo maximálního posuvu,
      pokračuje se bodem **b)**,

  6.  na konci může být nutné provést korekci
      zbytku

- **algoritmem
  SRT**
![[media/szz-09/media/image2.png]]


**Odkazy:**

- [<u>How to Convert a Number from Decimal to IEEE
  754 Floating Point
  Representation</u>](https://www.wikihow.com/Convert-a-Number-from-Decimal-to-IEEE-754-Floating-Point-Representation)

  - [<u>Video</u>](https://www.youtube.com/watch?v=tx-M_rqhuUA) -
    HOW TO: Convert Decimal to IEEE-754 Single-Precision Binary

- [<u>HOW TO: Adding IEEE-754 Floating Point
  Numbers</u>](https://www.youtube.com/watch?v=mKJiD2ZAlwM)

## Zdroje

- SZZ okruh 9 — studijní materiály FIT BUT (`szz-09.docx`). Další obrázky: `media/szz-09/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/08-minimalizace-logickych-vyrazu|8. Minimalizace logických výrazů]] · další: [[okruhy/10-fpga-vhdl|10. Technologie FPGA]] ▶
