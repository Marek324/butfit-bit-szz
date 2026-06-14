---
title: "24. Numerické metody (přímé a iterační metody pro soustavy lineárních rovnic, numerické řešení ODR)"
category: okruh
okruh: 24
tags: [math, numerical-methods]
aliases: [Gaussova eliminace, LU rozklad, Cramerovo pravidlo, Jacobiho metoda, Gauss-Seidel, Eulerova metoda, Runge-Kutta]
relationships:
  - target: "[[topics/17-diferencialni-integralni-pocet]]"
    type: uses
  - target: "[[topics/28-modelovani-simulace]]"
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

Matematický základ viz [[topics/17-diferencialni-integralni-pocet]]; využití ve [[topics/28-modelovani-simulace|spojité simulaci]].

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

$$A = \begin{pmatrix} 0 & 1 & 5 \\ 8 & 5 & 23 \\ 47 & 154 & 2 \end{pmatrix}$$

- **Nulová matice** - Všechny prvky jsou 0.

$$A = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

- **Jednotková matice** - Čtvercová matice, která má na hlavní diagonále (úhlopříčka z levého horního rohu do pravého dolního rohu) jedničky a všude jinde 0.

$$I = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

- **Schodová matice** - Každý následující řádek má na začátku více nul než předchozí řádek.

$$A_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & \pi \\ 0 & 0 & 1 \end{pmatrix}, \quad A_2 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}, \quad A_3 = \begin{pmatrix} 1 & 1 & 1 & 1 & 8 \\ 0 & 0 & 0 & 5 & 1 \\ 0 & 0 & 0 & 0 & 5 \end{pmatrix}$$

- **Transponovaná matice** - Zamění se řádky a sloupce (prvek co byl na 1;2 bude na 2;1).

$$\begin{pmatrix} 0 & 1 & 5 \\ 8 & 5 & 23 \\ 47 & 154 & 2 \end{pmatrix}^T = \begin{pmatrix} 0 & 8 & 47 \\ 1 & 5 & 154 \\ 5 & 23 & 2 \end{pmatrix}, \quad \begin{pmatrix} 3 & 4 & 5 \\ 6 & 7 & 8 \end{pmatrix}^T = \begin{pmatrix} 3 & 6 \\ 4 & 7 \\ 5 & 8 \end{pmatrix}$$

- **Symetrická matice** - Každá taková **čtvercová** matice, která je osově souměrná podle své hlavní diagonály. Zůstává tedy stejná i po transponování.

$$A = \begin{pmatrix} 9 & 3 & 4 \\ 3 & 7 & 0 \\ 4 & 0 & 2 \end{pmatrix}$$

- **Antisymetrická matice** - Podobné jako symetrická, ale prvky na druhé straně jsou obrácené ($A = -A^T$). Hlavní diagonála tedy musí být 0.

$$A = \begin{pmatrix} 0 & -3 & -4 \\ 3 & 0 & 5 \\ 4 & -5 & 0 \end{pmatrix}$$

- **Diagonální matice** - Všude jinde než na hlavní diagonále jsou 0 (na hlavní diagonále být můžou ale nemusí).

$$A_1 = \begin{pmatrix} 9 & 0 & 0 \\ 0 & 7 & 0 \\ 0 & 0 & 2 \end{pmatrix}, \quad A_2 = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

- **REGULÁRNÍ matice** - Její **determinant je** **nenulový**.
- **Diagonálně dominantní matice** - Pokud je absolutní hodnota každého prvku na diagonále větší nebo rovna součtu absolutních hodnot zbylých prvků ve sloupci nebo řádku (řádkově/sloupcově).

$$A = \begin{pmatrix} 3 & -2 & 1 \\ 1 & -3 & 2 \\ -1 & 2 & 4 \end{pmatrix}$$

Je diagonálně dominantní, protože $|a_{11}| \ge |a_{12}| + |a_{13}|$ ($|3| \ge |{-2}| + |1|$), 
$|a_{22}| \ge |a_{21}| + |a_{23}|$ ($|{-3}| \ge |1| + |2|$) a $|a_{33}| \ge |a_{31}| + |a_{32}|$ ($|4| \ge |{-1}| + |2|$).

- **Pozitivně definitní matice** - Čtvercová matice, u které pro každý nenulový vektor $\mathbf{x}$ platí $\mathbf{x}^T \mathbf{M} \mathbf{x} > 0$:

$$\mathbf{x} \neq 0 \implies \mathbf{x}^T \mathbf{M} \mathbf{x} > 0$$

### Determinant

Udává orientovaný obsah, respektive objem u 3×3 matice.

- **Křížové pravidlo** - Slouží pro výpočet determinantu **2×2 matice**.

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, \quad \det A = ad - bc$$

- **Sarrusovo pravidlo** - Slouží pro výpočet determinantu **3×3 matice**.

$$\det A = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}$$

- **Determinant N×N matice** - Rozloží se na menší matice pomocí **Laplaceova rozvoje** podle vybraného řádku nebo sloupce. Obsahuje-li matice **nulový řádek**, je její **determinant nulový**. Obsahuje-li matice **dva stejné řádky**, je její **determinant nulový**. Vznikla-li matice B z matice A **výměnou řádků**, pak $|B| = -|A|$. Vznikla-li matice B z matice A **vynásobením** jednoho jejího **řádku** konstantou $c \in \mathbb{R}$, platí $|B| = c|A|$.

Při Laplaceově rozvoji se střídají znaménka kofaktorů (rozmístěná jako na šachovnici):

$$A_{ij} = (-1)^{i+j} M_{ij}$$

Příklad – výpočet determinantu pomocí Laplaceova rozvoje (výhodný je rozvoj podle třetího sloupce, který obsahuje nejvíce nul):

$$A = \begin{pmatrix} 8 & 3 & 0 & 4 \\ 6 & 7 & 0 & 5 \\ -1 & 0 & 3 & 0 \\ 0 & 2 & 0 & 1 \end{pmatrix}, \qquad |A| = 3 \cdot (-1)^{3+3} \begin{vmatrix} 8 & 3 & 4 \\ 6 & 7 & 5 \\ 0 & 2 & 1 \end{vmatrix} = 3 \cdot 6 = 18$$

## Přímé metody pro řešení algebraických rovnic

Vedou k řešení soustavy po **konečném počtu kroků**. Toto řešení by bylo **přesné**, kdybychom se nedopouštěli zaokrouhlovacích chyb.

### Cramerovo pravidlo

Vhodné pro **velmi malé** soustavy rovnic. Metoda je **použitelná**, je-li **matice soustavy regulární** ($D \neq 0$). Při výpočtu i-tého determinantu vždy nahrazujeme i-tý sloupec sloupcem s výsledky (pravá strana soustavy, za znakem =).

$$x_1 = \frac{D_1}{D}, \quad x_2 = \frac{D_2}{D}, \quad \dots, \quad x_n = \frac{D_n}{D}$$

Příklad (2×2) – řešení soustavy $x + y = 3$, $x - 2y = 1$:

$$\det A = \begin{vmatrix} 1 & 1 \\ 1 & -2 \end{vmatrix} = -3$$

Poněvadž $\det A \neq 0$, lze použít Cramerovo pravidlo:

$$\det A_1 = \begin{vmatrix} 3 & 1 \\ 1 & -2 \end{vmatrix} = -7, \qquad \det A_2 = \begin{vmatrix} 1 & 3 \\ 1 & 1 \end{vmatrix} = -2$$

$$x = \frac{\det A_1}{\det A} = \frac{-7}{-3} = \frac{7}{3}, \qquad y = \frac{\det A_2}{\det A} = \frac{-2}{-3} = \frac{2}{3}$$

Příklad (3×3) – soustava:

$$\begin{aligned} x_1 + 2x_2 - x_3 &= 1 \\ -2x_1 + x_2 - 3x_3 &= 2 \\ 2x_2 - x_3 &= -2 \end{aligned}$$

$$D = \begin{vmatrix} 1 & 2 & -1 \\ -2 & 1 & -3 \\ 0 & 2 & -1 \end{vmatrix} = 5, \qquad D_1 = \begin{vmatrix} 1 & 2 & -1 \\ 2 & 1 & -3 \\ -2 & 2 & -1 \end{vmatrix} = 15$$

$$D_2 = \begin{vmatrix} 1 & 1 & -1 \\ -2 & 2 & -3 \\ 0 & -2 & -1 \end{vmatrix} = -14, \qquad D_3 = \begin{vmatrix} 1 & 2 & 1 \\ -2 & 1 & 2 \\ 0 & 2 & -2 \end{vmatrix} = -18$$

$$x_1 = \frac{D_1}{D} = 3, \qquad x_2 = \frac{D_2}{D} = -2{,}8, \qquad x_3 = \frac{D_3}{D} = -3{,}6$$

### Gaussova eliminační metoda

Základem je úprava matice soustavy na **schodovitý tvar** - prohazování řádků, násobením a dělením nenulovým číslem a **přičítáním/odečítáním násobků jednotlivých řádků** k jiným. Pomineme-li zaokrouhlovací chyby, metoda poskytuje přesný výsledek, ale je poměrně náročná pro výpočet, konkrétně je třeba provést $(n^3)/3$ (složitost v počtu provedených aritmetických operací je tedy **kubická**) aritmetických operací.

Příklad – úprava rozšířené matice soustavy na schodovitý tvar a zpětná substituce:

$$\left(\begin{array}{ccc|c} 2 & 3 & 7 & 47 \\ 3 & 8 & 1 & 50 \\ 0 & 3 & 3 & 27 \end{array}\right) \sim \left(\begin{array}{ccc|c} 6 & 9 & 21 & 141 \\ 0 & 7 & -19 & -41 \\ 0 & 3 & 3 & 27 \end{array}\right) \sim \left(\begin{array}{ccc|c} 6 & 9 & 21 & 141 \\ 0 & 21 & -57 & -123 \\ 0 & 0 & 78 & 312 \end{array}\right)$$

$$\begin{aligned} 6x_1 + 9x_2 + 21x_3 &= 141 \\ 21x_2 - 57x_3 &= -123 \\ 78x_3 &= 312 \end{aligned} \quad\Rightarrow\quad x_3 = 4,\ x_2 = 5,\ x_1 = 2$$

### LU rozklad

[<u>LU decomposition - An Example</u>](https://youtu.be/BFYFkn-eOQk)

Při Lower-Upper rozkladu se začne s jednotkovou maticí, která násobí původní matici, provádí se úpravy jako při GEM a zapisují se do jednotkové matice viz příklad (pozor na **znaménka**: do Lower matice zapisujeme opačná znaménka).

Příklad – pomocí nalezeného LU rozkladu matice A najděte řešení soustavy:

$$\begin{aligned} 2x_1 - 3x_2 + x_3 &= 5 \\ -3x_1 + 5x_2 + 2x_3 &= -4 \\ x_1 + 2x_2 - x_3 &= 1 \end{aligned}$$

Eliminací (jako u GEM) získáme horní trojúhelníkovou matici **U**; do **L** zapisujeme opačná znaménka použitých násobků řádků:

$$\begin{pmatrix} 2 & -3 & 1 \\ -3 & 5 & 2 \\ 1 & 2 & -1 \end{pmatrix} \sim \begin{pmatrix} 2 & -3 & 1 \\ 0 & 0{,}5 & 3{,}5 \\ 0 & 3{,}5 & -1{,}5 \end{pmatrix} \sim \begin{pmatrix} 2 & -3 & 1 \\ 0 & 0{,}5 & 3{,}5 \\ 0 & 0 & -26 \end{pmatrix}$$

$$L = \begin{pmatrix} 1 & 0 & 0 \\ -1{,}5 & 1 & 0 \\ 0{,}5 & 7 & 1 \end{pmatrix}, \qquad U = \begin{pmatrix} 2 & -3 & 1 \\ 0 & 0{,}5 & 3{,}5 \\ 0 & 0 & -26 \end{pmatrix}$$

Následně pomocí matice **L** upravíme vektor pravé strany (dopředná substituce $Ly = b$) a na základě tohoto vektoru vypočítáme řešení pomocí matice **U** (zpětná substituce $Ux = y$):

$$\begin{aligned} y_1 &= 5 &&\Rightarrow\ y_1 = 5 \\ -1{,}5\,y_1 + y_2 &= -4 &&\Rightarrow\ y_2 = 3{,}5 \\ 0{,}5\,y_1 + 7y_2 + y_3 &= 1 &&\Rightarrow\ y_3 = -26 \end{aligned}$$

$$\begin{aligned} 2x_1 - 3x_2 + x_3 &= 5 &&\Rightarrow\ x_1 = 2 \\ 0{,}5\,x_2 + 3{,}5\,x_3 &= 3{,}5 &&\Rightarrow\ x_2 = 0 \\ -26\,x_3 &= -26 &&\Rightarrow\ x_3 = 1 \end{aligned}$$

Metoda je vhodná, pokud potřebujeme počítat opakovaně tu stejnou rovnici pro jiné hodnoty pravé strany.

## Iterační metody

Narozdíl od přímých **nevedou** k **přesnému** **výsledku** po konečném, předem daném počtu kroků. Zvolíme počáteční aproximaci řešení a tu v každém kroku **zlepšujeme**. K řešení se **přibližujeme postupně** a až je dostatečně přesný výpočet ukončíme (**výsledek** je tedy **přibližný**, k přesnému bychom se dostali s nekonečným počtem operací).

### Jacobiho metoda

[<u>The Jacobi Method</u>](https://youtu.be/bR2SEe8W3Ig)

Konverguje, pokud je matice soustavy rovnic **ostře** **řádkově diagonálně dominantní** (součet absolutních hodnot řádku je **menší** než absolutní hodnota hodnoty na diagonále) nebo **ostře** **sloupcově diagonálně dominantní** (součet absolutních hodnot sloupce je **menší** než absolutní hodnota hodnoty na diagonále). Pokud podmínky nejsou splněny, může konvergovat, ale nemusí. (V tomhle případě je matice řádkově i sloupcově dominantní.)

Příklad – soustava:

$$\begin{aligned} 15x_1 - x_2 + 2x_3 &= 30 \\ 2x_1 - 10x_2 + x_3 &= 23 \\ x_1 + 3x_2 + 18x_3 &= -22 \end{aligned}$$

Matice soustavy je diagonálně dominantní ($|15| > |{-1}| + |2|$, $|{-10}| > |2| + |1|$, $|18| > |1| + |3|$), proto je konvergence zaručena. Iterační vztahy:

$$\begin{aligned} x_1^{(r+1)} &= \tfrac{1}{15}\left(30 + x_2^{(r)} - 2x_3^{(r)}\right) \\ x_2^{(r+1)} &= -\tfrac{1}{10}\left(23 - 2x_1^{(r)} - x_3^{(r)}\right) \\ x_3^{(r+1)} &= \tfrac{1}{18}\left(-22 - x_1^{(r)} - 3x_2^{(r)}\right) \end{aligned}$$

Jako počáteční aproximaci zvolíme $x = (0, 0, 0)^T$:

| r | $x_1^{(r)}$ | $x_2^{(r)}$ | $x_3^{(r)}$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 2 | −2,3 | −1,2222 |
| 2 | 2,0096 | −2,0222 | −0,9500 |
| 3 | 1,9918 | −1,9930 | −0,9968 |
| 4 | 2,0000 | −2,0013 | −1,0007 |

### Gauss-Seidelova metoda ([<u>The Gauss-Seidel Method</u>](https://www.youtube.com/watch?v=F6J3ZmXkMj0))

Metoda je podobná Jacobiho metodě. Liší se v tom, že v každém kroku používá již **novou hodnotu proměnné** (pokud je známa) a ne tu z minulé iterace. Konverguje pro **ostře řádkově nebo sloupcově dominantní matice** a navíc, pokud je matice **pozitivně definitní** (lze zjistit např., že všechny její subdeterminanty z levého horního rohu musí být **větší** než 0 [<u>Checking if a Matrix is Positive Definite</u>](https://youtu.be/ttMZB5Gm_fM) nebo lze zjistit **pivot testem** - převodem matice na horní trojúhelníkovou matici a porovnáním hodnot na diagonále s 0, pokud jsou **větší než** 0, je matice pozitivně definitní [<u>Positive Definite Matrices and Minima</u>](https://youtu.be/cfn2ZUuWPd0)(pro větší nebo rovno 0 jsou matice semidefinitní)).

Obecné iterační vztahy (v rámci jedné iterace se ihned využívají již přepočítané hodnoty, $a_{i4}$ je pravá strana):

$$\begin{aligned} x_1^{(r+1)} &= \frac{a_{14} - a_{12}x_2^{(r)} - a_{13}x_3^{(r)}}{a_{11}} \\ x_2^{(r+1)} &= \frac{a_{24} - a_{21}x_1^{(r+1)} - a_{23}x_3^{(r)}}{a_{22}} \\ x_3^{(r+1)} &= \frac{a_{34} - a_{31}x_1^{(r+1)} - a_{32}x_2^{(r+1)}}{a_{33}} \end{aligned}$$

Příklad – iterační vztahy a průběh výpočtu:

$$\begin{aligned} x_1^{k+1} &= \tfrac{1}{2}\left(x_2^{k} + \tfrac{1}{3}\right) \\ x_2^{k+1} &= \tfrac{1}{2}\left(x_1^{k+1} + x_3^{k} + 1\right) \\ x_3^{k+1} &= \tfrac{1}{2}\left(x_2^{k+1} - \tfrac{1}{3}\right) \end{aligned}$$

| k | $x_1^{k}$ | $x_2^{k}$ | $x_3^{k}$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 0,1667 | 0,5833 | 0,1250 |
| 2 | 0,4583 | 0,7917 | 0,2290 |
| ⋮ | ⋮ | ⋮ | ⋮ |
| 14 | 0,6666 | 1,0000 | 0,3333 |
| 15 | 0,6666 | 1,0000 | 0,3333 |

## Numerické řešení obyčejných diferenciálních rovnic

Diferenciální rovnice jsou rovnice, kde jako proměnné vystupují **derivace funkcí**. U některých lze nalézt přesné analytické řešení, ale většinou **nelze nebo je to velmi** obtížné. Naštěstí lze řešení diferenciální rovnice velmi **dobře aproximovat** použitím **numerických metod**, které jsou založené na **iteračním řešení** těchto rovnic. Numerické metody dělíme na:

- **jednokrokové**: vychází pouze z **aktuálního stavu** (aktuální ohodnocení proměnných), např. **Eulerova metoda**, metody **Runge-Kutta** (**RK2, RK4, RK8**).
- **vícekrokové**: využívají historii stavů (ohodnocení proměnných), používají **hodnoty zapamatované z předchozích kroků**. Mohou být rychlejší než jednokrokové, ale obvykle mají **problém se startem** (pro prvních **n** iterací se použije **jednokroková** metoda → nevhodné pro nespojité funkce). Jedná se např. o **metodu Adams-Bashforth**. (Existují i samostartující metody.)
- **prediktor-korektor**: Nejprve se vypočítá odhad nového **y_n+1**. V tomto bodě je vypočtena derivace **f_n+1**, která je následně použita pro výpočet přesnější aproximace **y_n+1**.
- **explicitní**: výsledek v každé iteraci získáme **dosazením do vzorce**.
- **implicitní**: vyžaduje řešení **algebraických rovnic** v každé iteraci.

### Eulerova metoda

Nejjednodušší jednokroková metoda. Založená na principu **směrnice tečny** v bodě, která je daná **1. derivací** funkce v tomto bodě. Směrnice udává, o kolik se **zvětší**/**zmenší** hodnota **y** při změně **x** (definuje tak přímku). Řešíme počáteční úlohu:

$$y' = f(x, y), \quad y(x_0) = y_0$$

Další hodnotu počítáme z aktuální pomocí směrnice tečny:

$$y_{i+1} = y_i + h \cdot f(x_i, y_i), \quad i = 0, 1, 2, \dots$$

![[media/szz-24/media/image45.jpg]]

Př. 2: $y' = x - y$; $y(0) = 1$; $h = 0{,}2$ na $\langle 0; 0{,}6 \rangle$:

$$\begin{aligned} y_1 &= y_0 + h \cdot f(x_0, y_0) = 1 + 0{,}2 \cdot (0 - 1) = 0{,}8 \\ y_2 &= y_1 + h \cdot f(x_1, y_1) = 0{,}8 + 0{,}2 \cdot (0{,}2 - 0{,}8) = 0{,}68 \\ y_3 &= y_2 + h \cdot f(x_2, y_2) = 0{,}68 + 0{,}2 \cdot (0{,}4 - 0{,}68) = 0{,}624 \end{aligned}$$

### Runge-Kutta

Jednokroková metoda. Vylepšuje Eulerovu metodu. Existují RK metody různých řádů (RK1 - Eulerova metoda, RK2, RK4, RK8). Koeficienty u těchto metod jsou vypočteny tak, aby metoda řádu **b** odpovídala **Taylorovu polynomu** funkce y(t) stejného řádu. Pro výpočty se nejčastěji používá metoda **Runge-Kutta 4. řádu**. Pro RK metodu **k-tého** řádu se počítá **k** částečných odhadů (druhý odhad je závislý na prvním, třetí na druhým, … - nejdříve se vypočte 1. derivace, pak se udělá půlkrok na základě této derivace, v tom bodě se vypočte další derivace, …) a výsledný odhad se poté vypočte jako krok vynásobený jejich váženým průměrem.

Např. metoda **RK2** počítá dva odhady směrnice a výsledek získá z jejich váženého průměru:

$$k_1 = f(t_n, y_n), \qquad k_2 = f(t_n + h, y_n + h k_1)$$

$$y_{n+1} = y_n + h\left(\tfrac{1}{2}k_1 + \tfrac{1}{2}k_2\right)$$

![[media/szz-24/media/image38.png]]

![[media/szz-24/media/image33.png]]

![[media/szz-24/media/image27.png]]

### Adams-Bashforth

**Vícekroková metoda**, pamatuje si výsledky předchozích kroků. Např. dvojkrokový a čtyřkrokový vzorec:

$$y_{n+2} = y_{n+1} + \tfrac{3}{2}h\,f(t_{n+1}, y_{n+1}) - \tfrac{1}{2}h\,f(t_n, y_n)$$

$$y_{n+1} = y_n + \frac{h}{24}\left(55 f_n - 59 f_{n-1} + 37 f_{n-2} - 9 f_{n-3}\right)$$

### Adams-Bashforth-Moulton

Metoda typu **prediktor-korektor**, zpřesňují výsledek použitím prvotního odhadu pro výpočet výsledného odhadu (zde čtyřkrokový korektor Adams-Moulton):

$$y_{n+1} = y_n + \frac{h}{24}\left(9 f_{n+1} + 19 f_n - 5 f_{n-1} + f_{n-2}\right)$$

### Tuhé systémy

Problematické pro řešení pomocí běžných numerických metod (RK). Vyskytují se zde velmi rozdílné časové konstanty - rychlost změny jedné proměnné je řádově větší než druhé. Příkladem je rovnice s velmi rozdílnými vlastními čísly:

$$y'' + 101y' + 100y = 0$$

Zkrácení kroku často nelze (zaokrouhlovací chyby, malá efektivita). Je nutné použít speciální metody.

## Chyby numerických metod

Při každé aproximaci se musí počítat s chybou výsledku.

- **Lokální chyba** - Vzniká v každém kroku - **zaokrouhlovací** nebo **aproximační**.
- **Akumulované chyby** - Sesbírané chyby po **celou dobu výpočtu**.

![[media/szz-24/media/image44.png]]

## Zdroje

- SZZ okruh 24 — studijní materiály FIT BUT (`szz-24.docx`). Obrázky: `media/szz-24/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[topics/23-struktura-prekladace|23. Struktura překladače]] · další: [[topics/25-teorie-grafu|25. Teorie grafů]] ▶
