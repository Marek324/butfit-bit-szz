---
title: "24. Numerické metody (přímé a iterační metody pro soustavy lineárních rovnic, numerické řešení ODR)"
category: okruh
okruh: 24
tags: [math, numerical-methods]
aliases: [Gaussova eliminace, LU rozklad, Cramerovo pravidlo, Jacobiho metoda, Gauss-Seidel, Eulerova metoda, Runge-Kutta]
relationships:
  - target: "[[okruhy/17-diferencialni-integralni-pocet]]"
    type: uses
  - target: "[[okruhy/28-modelovani-simulace]]"
    type: related_to
sources: ["_sources/docx/szz-24.docx"]
summary: Přímé (Gauss, LU, Cramer) a iterační (Jacobi, Gauss-Seidel) metody řešení soustav lineárních rovnic a numerické řešení ODR (Eulerova metoda, Runge-Kutta) včetně chyb.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T17:30:00Z
updated: 2026-06-03T17:30:00Z
---

# 24. Numerické metody

> SZZ okruh 24 (FIT BUT). Řešení soustav lineárních rovnic a obyčejných diferenciálních rovnic numericky.

## Shrnutí

### Soustavy lineárních rovnic
- Zápis **Ax = b**; počet řešení 0/1/∞ (Frobeniova věta). Matice **regulární** ⇔ determinant ≠ 0.
- **Přímé metody** (přesné po konečném počtu kroků, až na zaokrouhlení):
  - **Gaussova eliminace (GEM)** — úprava na schodovitý tvar; složitost ~n³/3 (kubická).
  - **Cramerovo pravidlo** — přes determinanty, jen malé soustavy, D ≠ 0.
  - **LU rozklad** — A = L·U; výhodný pro opakované řešení s jinou pravou stranou.

### Iterační metody
- Postupné zlepšování aproximace (výsledek přibližný).
- **Jacobiho** a **Gauss-Seidelova** (používá hned nové hodnoty) — konvergují pro **ostře diagonálně dominantní** matici (G-S i pro pozitivně definitní).

### Diferenciální rovnice
- **Eulerova metoda** — jednokroková, směrnice tečny (1. derivace) v bodě.
- **Runge-Kutta** (RK4) — jednokroková, přesnější (odpovídá Taylorovu polynomu); vícekrokové (Adams-Bashforth), prediktor-korektor.
- Chyby: **lokální** (zaokrouhlovací/aproximační v kroku) a **akumulovaná** (globální); volba kroku h ovlivňuje přesnost i stabilitu.

Matematický základ viz [[okruhy/17-diferencialni-integralni-pocet]]; využití ve [[okruhy/28-modelovani-simulace|spojité simulaci]].

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Soustavy lineárních rovnic** ↪ [[#Soustavy lineárních rovnic]]
- *Ax=b, počet řešení?* → 0, 1 nebo ∞ (dle Frobeniovy věty / hodnosti matice).
- *Přímé metody?* → Gaussova eliminace (schodovitý tvar), Cramerovo pravidlo (determinanty), LU rozklad.
- *Kdy LU?* → Opakované řešení téže soustavy s různou pravou stranou.

**Iterační metody** ↪ [[#Iterační metody]]
- *Jacobi vs. Gauss-Seidel?* → G-S používá už nové hodnoty proměnných v rámci téže iterace → rychlejší.
- *Podmínka konvergence?* → Ostře diagonálně dominantní matice (řádkově/sloupcově).

**Diferenciální rovnice** ↪ [[#Diferenciální rovnice]]
- *Eulerova metoda?* → Aproximace pomocí směrnice tečny (1. derivace), vyžaduje počáteční podmínku.
- *RK4 vs. Euler?* → RK4 počítá více částečných odhadů → přesnější (odpovídá vyššímu Taylorovu polynomu).
- *Chyby?* → lokální (v každém kroku) a akumulovaná (globální); závisí na velikosti kroku h.

## Plné znění (ke studiu)

## Matice

Slouží pro zjednodušený zápis soustavy rovnic. Využívají se pro řešení lineárních rovnic.

- **Čtvercová matice** - Stejný počet řádků a sloupců.

- **Nulová matice** - Všechny prvky jsou 0
![[media/szz-24/media/image11.png]]


- **Jednotková matice** - Čtvercová matice, která má na hlavní diagonále (úhlopříčka z levého horního rohu do pravého dolního rohu) jedničky a všude jinde 0.
![[media/szz-24/media/image42.png]]


- **Schodová matice** - Každý následující řádek má na začátku více nul než předchozí řádek.
![[media/szz-24/media/image21.png]]


- **Transponovaná matice** - Zamění se řádky a sloupce (prvek co byl na 1;2 bude na 2;1)
![[media/szz-24/media/image8.png]]


- **Symetrická matice** - Každá taková **čtvercová** matice, která je osově souměrná podle své hlavní diagonály. Zůstává tedy stejná i po transponování.
![[media/szz-24/media/image6.png]]


- **Antisymetrická matice** - Podobné jako symetrická, ale prvky na druhé straně jsou obrácené (A = -A<sup>T</sup>). Hlavní diagonála tedy musí být 0.
![[media/szz-24/media/image31.png]]


- **Diagonální matice** - Všude jinde než na hlavní diagonále jsou 0 (na hlavní diagonále být můžou ale nemusí).
![[media/szz-24/media/image16.png]]


- **REGULÁRNÍ matice** - Její **determinant je** **nenulový**.
![[media/szz-24/media/image23.png]]


- **Diagonálně dominantní matice** - Pokud je absolutní hodnota každého prvku na diagonále větší nebo rovna součtu absolutních hodnot zbylých prvků ve sloupci nebo řádku (řádkově/sloupcově).

- **Pozitivně definitní matice** - Čtvercová matice, u které platí
![[media/szz-24/media/image41.png]]


### Determinant
![[media/szz-24/media/image20.png]]


Udává orientovaný obsah, respektive objem u 3. řádkové matice.

- **Křížové pravidlo** - Slouží pro výpočet determinantu **2x2 matice**.

> 
![[media/szz-24/media/image4.png]]


- **Sarrusovo pravidlo** - Slouží pro výpočet determinantu **3x3 matice**.

> 
![[media/szz-24/media/image34.png]]


- **Determinant NxN matice** - Rozloží se na menší matice. Obsahuje-li matice **nulový řádek**, je její **determinant nulový**. Obsahuje-li matice **dva stejné řádky**, je její **determinant nulový**. Vznikla-li matice B z matice A **výměnou řádků**, pak **\|B\| = −\|A\|**. Vznikla-li matice B z matice A **vynásobením** jednoho jejího **řádku** konstantou c ∈ R, platí **\|B\| = c\|A\|**.

## Přímé metody pro řešení algebraických rovnic
![[media/szz-24/media/image12.png]]

![[media/szz-24/media/image17.png]]


Vedou k řešení soustavy po **konečném počtu kroků**. Toto řešení by bylo **přesné**, kdybychom se nedopouštěli zaokrouhlovacích chyb.

### Cramerovo pravidlo

Vhodné pro **velmi malé** soustavy rovnic. Metoda je **použitelná**, je-li **matice** **soustavy** **regulární** (**D != 0**). Při výpočtu i-tého determinantu vždy nahrazujeme i-tý sloupec sloupcem s výsledky (pravá strana soustavy, za znakem =).
![[media/szz-24/media/image14.png]]

![[media/szz-24/media/image43.png]]

![[media/szz-24/media/image36.png]]

![[media/szz-24/media/image22.png]]

![[media/szz-24/media/image9.png]]

![[media/szz-24/media/image19.png]]


### Gaussova eliminační metoda
![[media/szz-24/media/image3.png]]


Základem je úprava matice soustavy na **schodovitý tvar** - prohazování řádků, násobením a dělením nenulovým číslem a **přičítáním/odečítáním násobků jednotlivých řádků** k jiným. Pomineme-li zaokrouhlovací chyby, metoda poskytuje přesný výsledek, ale je poměrně náročná pro výpočet, konkrétně je třeba provést (**n^3)/3** (složitost v počtu provedených aritmetických operací je tedy **kubická**) aritmetických operací.
![[media/szz-24/media/image29.png]]


### LU rozklad

[<u>LU decomposition - An Example</u>](https://youtu.be/BFYFkn-eOQk)

Při Lower-Upper rozkladu se začne s jednotkovou maticí, která násobí původní matici, provádí se úpravy jako při GEM a zapisují se do jednotkové matice viz příklad (pozor na **znaménka**: do Lower matice zapisujeme opačná znaménka).
![[media/szz-24/media/image24.png]]


Následně je nutné pomocí matice **L** upravit vektor pravé strany rovnice a na základě tohoto vektoru vypočítat řešení rovnice pomocí matice **U**.
![[media/szz-24/media/image10.png]]

![[media/szz-24/media/image30.png]]


Metoda je vhodná, pokud potřebujeme počítat opakovaně tu stejnou rovnici pro jiné hodnoty pravé strany.
![[media/szz-24/media/image37.png]]

![[media/szz-24/media/image32.png]]


## Iterační metody

Narozdíl od přímých **nevedou** k **přesnému** **výsledku** po konečném, předem daném počtu kroků. Zvolíme počáteční aproximaci řešení a tu v každém kroku **zlepšujeme**. K řešení se **přibližujeme postupně** a až je dostatečně přesný výpočet ukončíme (**výsledek** je tedy **přibližný**, k přesnému bychom se dostali s nekonečným počtem operací).

### Jacobiho metoda

[<u>The Jacobi Method</u>](https://youtu.be/bR2SEe8W3Ig)

Konverguje, pokud je matice soustavy rovnic **ostře** **řádkově diagonálně dominantní** (součet absolutních hodnot řádku je **menší** než absolutní hodnota hodnoty na diagonále) nebo **ostře** **sloupcově diagonálně dominantní** (součet absolutních hodnot sloupce je **menší** než absolutní hodnota hodnoty na diagonále). Pokud podmínky nejsou splněny, může konvergovat, ale nemusí.\
(V tomhle případě je matice řádkově i sloupcově dominantní.)


![[media/szz-24/media/image35.png]]


### Gauss-Seidelova metoda ([<u>The Gauss-Seidel Method</u>](https://www.youtube.com/watch?v=F6J3ZmXkMj0))

Metoda je podobná Jacobiho metodě. Liší se v tom, že v každém kroku používá již **novou hodnotu proměnné** (pokud je známa) a ne tu z minulé iterace. Konverguje pro **ostře řádkově nebo sloupcově dominantní matice** a navíc, pokud je matice **pozitivně definitní** (lze zjistit např., že všechny její subdeterminanty z levého horního rohu musí být **větší** než 0 [<u>Checking if a Matrix is Positive Definite</u>](https://youtu.be/ttMZB5Gm_fM) nebo lze zjistit **pivot testem** - převodem matice na horní trojúhelníkovou matici a porovnáním hodnot na diagonále s 0, pokud jsou **větší než** 0, je matice pozitivně definitní [<u>Positive Definite Matrices and Minima</u>](https://youtu.be/cfn2ZUuWPd0)(pro větší nebo rovno 0 jsou matice semidefinitní)).\

![[media/szz-24/media/image18.png]]


> 
![[media/szz-24/media/image39.png]]


## Numerické řešení obyčejných diferenciálních rovnic

Diferenciální rovnice jsou rovnice, kde jako proměnné vystupují **derivace funkcí**. U některých lze nalézt přesné analytické řešení, ale většinou **nelze nebo je to velmi** obtížné. Naštěstí lze řešení diferenciální rovnice velmi **dobře aproximovat** použitím **numerických metod**, které jsou založené na **iteračním řešení** těchto rovnic. Numerické metody dělíme na:

- **jednokrokové**: vychází pouze z **aktuálního stavu** (aktuální ohodnocení proměnných), např. **Eulerova metoda**, metody **Runge-Kutta** (**RK2, RK4, RK8**).

- **vícekrokové**: využívají historii stavů (ohodnocení proměnných), používají **hodnoty zapamatované z předchozích kroků**. Mohou být rychlejší než jednokrokové, ale obvykle mají **problém se startem** (pro prvních **n** iterací se použije **jednokroková** metoda → nevhodné pro nespojité funkce). Jedná se např. o **metodu Adams-Bashforth**. (Existují i samostartující metody.)

- **prediktor-korektor**: Nejprve se vypočítá odhad nového **y_n+1**. V tomto bodě je vypočtena derivace **f_n+1**, která je následně použita pro výpočet přesnější aproximace **y_n+1**.

- **explicitní**: výsledek v každé iteraci získáme **dosazením do vzorce**.

- **implicitní**: vyžaduje řešení **algebraických rovnic** v každé iteraci.

### Eulerova metoda

Nejjednodušší jednokroková metoda. Založená na principu **směrnice tečny** v bodě, která je daná **1. derivací** funkce v tomto bodě. Směrnice udává, o kolik se **zvětší**/**zmenší** hodnota **y** při změně **x** (definuje tak přímku).
![[media/szz-24/media/image2.png]]

![[media/szz-24/media/image45.jpg]]

![[media/szz-24/media/image1.png]]


Př. 2: y’ = x - y; y(0) = 1; h=0,2 na \<0; 0,6\>

### Runge-Kutta
![[media/szz-24/media/image40.png]]


Jednokroková metoda. Vylepšuje Eulerovu metodu. Existují RK metody různých řádů (RK1 - Eulerova metoda, RK2, RK4, RK8). Koeficienty u těchto metod jsou vypočteny tak, aby metoda řádu **b** odpovídala **Taylorovu polynomu** funkce y(t) stejného řádu. Pro výpočty se nejčastěji používá metoda **Runge-Kutta 4. řádu**. Pro RK metodu **k-tého** řádu se počítá **k** částečných odhadů (druhý odhad je závislý na prvním, třetí na druhým, … - nejdříve se vypočte 1. derivace, pak se udělá půlkrok na základě této derivace, v tom bodě se vypočte další derivace, …) a výsledný odhad se poté vypočte jako krok vynásobený jejich váženým průměrem.
![[media/szz-24/media/image38.png]]

![[media/szz-24/media/image33.png]]

![[media/szz-24/media/image27.png]]


### Adams-Bashforth
![[media/szz-24/media/image5.png]]

![[media/szz-24/media/image28.png]]


**Vícekroková metoda**, pamatuje si výsledky předchozích kroků. Např. dvojkrokový a čtyřkrokový:
![[media/szz-24/media/image7.png]]

![[media/szz-24/media/image13.png]]


### Adams-Bashforth-Moulton
![[media/szz-24/media/image25.png]]


Metoda typu **prediktor-korektor**, zpřesňují výsledek použitím prvotního odhadu pro výpočet výsledného odhadu.

### Tuhé systémy
![[media/szz-24/media/image26.png]]


Problematické pro řešení pomocí běžných numerických metod (RK). Vyskytují se zde velmi rozdílné časové konstanty - rychlost změny jedné proměnné je řádově větší než druhé. Zkrácení kroku často nelze (zaokrouhlovací chyby, malá efektivita). Je nutné použít speciální metody.

## Chyby numerických metod
![[media/szz-24/media/image15.png]]


Při každé aproximaci se musí počítat s chybou výsledku.

- **Lokální chyba** - Vzniká v každém kroku - **zaokrouhlovací** nebo **aproximační**.

- **Akumulované chyby** - Sesbírané chyby po **celou dobu výpočtu**.
![[media/szz-24/media/image44.png]]


## Zdroje

- SZZ okruh 24 — studijní materiály FIT BUT (`szz-24.docx`). Obrázky: `media/szz-24/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/23-struktura-prekladace|23. Struktura překladače]] · další: [[okruhy/25-teorie-grafu|25. Teorie grafů]] ▶
