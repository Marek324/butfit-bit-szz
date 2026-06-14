---
title: "31. Pravděpodobnost a statistika (náhodná veličina, rozdělení, odhady, testování hypotéz, regrese a korelace)"
category: okruh
okruh: 31
tags: [math, probability, statistics]
aliases: [pravděpodobnost, náhodná veličina, distribuční funkce, normální rozdělení, odhady, testování hypotéz, regrese, korelace]
relationships:
  - target: "[[okruhy/28-modelovani-simulace]]"
    type: related_to
  - target: "[[okruhy/27-strojove-uceni]]"
    type: related_to
sources: ["_sources/docx/szz-31.docx"]
summary: Základní pojmy pravděpodobnosti, náhodná veličina/vektor a distribuční/hustotní funkce, rozdělení (normální, Poisson, binomické), generování pseudonáhodných čísel, bodové/intervalové odhady, testování hypotéz a regresní/korelační analýza.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T18:15:00Z
updated: 2026-06-03T18:15:00Z
---

# 31. Pravděpodobnost a statistika

> SZZ okruh 31 (FIT BUT). Od náhodných jevů po regresi.

## Shrnutí

### Základní pojmy
- **Základní prostor Ω**, náhodný jev (podmnožina Ω); operace průnik/sjednocení/doplněk.
- **Klasická pravděpodobnost** P(A) = |A|/|Ω|; **podmíněná** pravděpodobnost a **Bayesův vzorec**.

### Náhodná veličina
- **Diskrétní** × **spojitá**; **distribuční funkce** F(x) = P(X ≤ x) (neklesající, zprava spojitá), **hustota** f(x) = F′(x).
- Charakteristiky: **střední hodnota** E(X), **rozptyl** D(X), **směrodatná odchylka** σ. Náhodný vektor (sdružená/marginální distribuce).

### Rozdělení a generování
- Diskrétní: rovnoměrné, **binomické**, **Poissonovo** (počet výskytů za jednotku času). Spojitá: rovnoměrné, **normální (Gaussovo)** (CLV), exponenciální (doba mezi výskyty).
- **Pseudonáhodná čísla**: kongruentní generátor (rovnoměrné rozložení, perioda); transformace (inverzní, vylučovací, kompoziční metoda).

### Odhady a testování hypotéz
- **Bodový odhad** (výběrový průměr/rozptyl; nestrannost, konzistence) × **intervalový** (interval spolehlivosti; nepřímá úměra spolehlivost ↔ přesnost).
- **Testování hypotéz**: H0/H1, kritický obor, **chyba 1. druhu α** (false positive) a **2. druhu β**; t-test, F-test.
- **Regrese** (funkční závislost, predikce; metoda nejmenších čtverců) × **korelace** (síla závislosti; korelace ≠ kauzalita).

> [!note] Ke kontrole (ověřeno)
> Zdroj uvádí Studentův **t-test** jako „test střední hodnoty se **známým** rozptylem" — to je **prohozené**. Správně: **t-test** se používá při **neznámém** rozptylu (odhadovaném z výběru), **z-test** při známém.

Náhodnost a Monte Carlo viz [[okruhy/28-modelovani-simulace]]; statistika v ML viz [[okruhy/27-strojove-uceni]]; hustota jako integrál viz [[okruhy/17-diferencialni-integralni-pocet]].

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Pravděpodobnost** ↪ [[#Základní pojmy]]
- *Klasická pravděpodobnost?* → P(A) = |A|/|Ω| (příznivé / všechny možné).
- *Podmíněná pravděpodobnost?* → P(A|B) = P(A∩B)/P(B); Bayes ji obrací.

**Náhodná veličina** ↪ [[#Náhodná veličina]]
- *Distribuční vs. hustotní funkce?* → F(x)=P(X≤x) (neklesající); hustota f(x)=F′(x), plocha pod f = 1.
- *Diskrétní vs. spojitá?* → Skoková (schodovitá F) × spojitá (integrál hustoty).

**Rozdělení a generování** ↪ [[#Rozdělení a generování]]
- *Normální rozdělení?* → N(μ,σ²); pravidlo 3σ (99,7 %); CLV. Poisson = počet výskytů; exponenciální = doba mezi nimi.
- *Pseudonáhodná čísla?* → Deterministické (kongruentní generátor); rozdíl náhodnost × pseudonáhodnost; perioda.

**Odhady a hypotézy** ↪ [[#Odhady a testování hypotéz]]
- *Bodový vs. intervalový odhad?* → Jediná hodnota × interval spolehlivosti (95–99 %).
- *Chyba 1. a 2. druhu?* → α = zamítneme platnou H0 (false positive); β = nezamítneme neplatnou (false negative).
- *Regrese vs. korelace?* → Regrese = funkční závislost + predikce; korelace = síla závislosti (≠ kauzalita).

## Plné znění (ke studiu)

## Základní pojmy

**Ω** - množina všech hodnot, kterých může **náhodná veličina** X nabývat - **základní prostor**, všechny možné jevy. Základní prostor pro dva po sobě následující hody mincí vypadá následovně: **Ω = { (rub, rub), (líc, líc), (rub, líc), (líc, rub) }**.

### Náhodný jev

Libovolná podmnožina **Ω**.

- jev nemožný: **∅,** za daných podmínek jev **nemůže nastat** (na dvou tradičních (šestibokých) hracích kostkách nám padne součet 30),
- jev jistý: **Ω,** za daných podmínek jev **nastane vždy** (při hodu mincí padne rub nebo líc).

#### **Průnik jevů**

Průnik jevů **A** a **B** je jev, který nastane právě tehdy, když **nastanou** jevy **A** a **B** **současně**. Značíme jej **A ∩ B**. Pokud je **A ∩ B = ∅**, mluvíme o jevech **disjunktních** (**neslučitelných**).

#### **Sjednocení jevů**

Sjednocení jevů **A** a **B** je jev, který nastane právě tehdy, když **nastane alespoň jeden** z jevů A a B. Značíme jej **A ∪ B**.

#### **Opačný jev**

Opačný jev (doplněk) k jevu **A** je jev, který nastane právě tehdy, když **nenastane jev A**. Značíme **A’** a platí **A’ = Ω \\ A**.

### Úplný systém jevů

Jevy **A1**, **A2**, ... tvoří úplný systém jevů, jestliže **A1 ∪ A2** **∪ ··· = Ω**. Pokud navíc platí **Ai ∩ Aj = ∅, ∀ i != j**, jedná se o **úplný systém neslučitelných jevů**.

### Axiomatická definice pravděpodobnosti

Nechť $(\Omega, \mathcal{A})$ je jevové pole a $P$ je množinová funkce definovaná na $\mathcal{A}$ s vlastnostmi:

1. $P(\Omega) = 1$,
2. $P(A) \ge 0 \quad \forall A \in \mathcal{A}$,
3. jsou-li $A_k \in \mathcal{A}$, $k = 1, 2, \dots$ navzájem disjunktní jevy ($A_i \cap A_j = \emptyset$ pro $i \neq j$), pak

$$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$$

Funkci $P$ nazveme **pravděpodobností** a trojici $(\Omega, \mathcal{A}, P)$ **pravděpodobnostním prostorem**.

### Klasická pravděpodobnost

Klasická pravděpodobnost je definována jako **podíl počtu příznivých jevů ku počtu všech možných jevů**. $P(A) = |A|/|\Omega|$, kde:

- $|A|$ značí počet prvků množiny příznivých jevů,
- $|\Omega|$ značí počet prvků všech možných jevů - velikost základního prostoru.

### Vlastnosti pravděpodobnosti

Nechť $(\Omega, \mathcal{A}, P)$ je pravděpodobnostní prostor. Pak pravděpodobnost $P$ má následující vlastnosti:

1. $P(\emptyset) = 0$,
2. $A, B \in \mathcal{A}, A \cap B = \emptyset \Rightarrow P(A \cup B) = P(A) + P(B)$,
3. $A, B \in \mathcal{A}, A \subseteq B \Rightarrow P(B - A) = P(B) - P(A)$,
4. $A, B \in \mathcal{A}, A \subseteq B \Rightarrow P(A) \le P(B)$,
5. $A \in \mathcal{A} \Rightarrow 0 \le P(A) \le 1$,
6. $A \in \mathcal{A} \Rightarrow P(A') = 1 - P(A)$,
7. $A, B \in \mathcal{A} \Rightarrow P(A \cup B) = P(A) + P(B) - P(A \cap B)$,
8. $A_1, \dots, A_n \in \mathcal{A} \Rightarrow P\left(\bigcup_{i=1}^{n} A_i\right) \le \sum_{i=1}^{n} P(A_i)$,
9. princip inkluze a exkluze:

$$P\left(\bigcup_{i=1}^{n} A_i\right) = \sum_i P(A_i) - \sum_{i<j} P(A_i \cap A_j) + \sum_{i<j<k} P(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n-1} P(A_1 \cap \cdots \cap A_n)$$

### Podmíněná pravděpodobnost

O proběhlém pokusu máme doplňující informace a můžeme tak lépe určit jeho pravděpodobnost. Nechť $(\Omega, \mathcal{A}, P)$ je pravděpodobnostní prostor, $B \in \mathcal{A}$, $P(B) > 0$. Pak číslo

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

nazveme **podmíněnou pravděpodobností** jevu $A$ za podmínky, že nastal jev $B$.

### Bayesův vzorec

Lze jednoduše vyjádřit z podmíněné pravděpodobnosti dosazením za průnik. Mějme dva náhodné jevy $A$ a $B$, přičemž $P(B) \neq 0$. Potom platí

$$P(A \mid B) = \frac{P(B \mid A)\, P(A)}{P(B)}$$

kde $P(A \mid B)$ je podmíněná pravděpodobnost jevu $A$ za předpokladu, že nastal jev $B$; $P(B \mid A)$ je podmíněná pravděpodobnost jevu $B$ podmíněná výskytem $A$; a $P(A)$, $P(B)$ jsou pravděpodobnosti jevů $A$ a $B$.

### Sčítání pravděpodobností

$$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(A \cap C) - P(B \cap C) + P(A \cap B \cap C)$$

Pro **nezávislé** jevy jsou průniky **nulové**.

# Náhodná veličina a vektor

Náhodná veličina je číselné ohodnocení náhodného pokusu (který dokážeme číselně ohodnotit). **Náhodnou veličinu** značíme **velkými písmeny X, Y, Z**. **Pravděpodobnost** se značí **malými x, y, z, p**. Pravděpodobnost, že náhodná veličina $X$ nabývá hodnoty $x$, zapíšeme jako $P(X = x)$; podobně lze interpretovat $P(X < x)$, $P(X \ge x)$ atd.

Rozlišujeme dva základní typy náhodných veličin:

- **diskrétní** a
- **spojitá**.

### Distribuční funkce

Popisuje **rozdělení** (**pravděpodobnostní chování**) náhodných veličin. Je **neklesající a zprava spojitá**. Distribuční funkce **F(x)** náhodné veličiny **X** přiřazuje každému reálnému číslu **x** pravděpodobnost, že náhodná veličina **X** nabude hodnoty **menší nebo rovné číslu** **x**:

$$F(x) = P(X \le x)$$

U **diskrétní** náhodné veličiny je distribuční funkce **schodovitá** (vlevo), u spojité náhodné veličiny je distribuční funkce spojitá (vpravo).
![[media/szz-31/media/image20.png]]

Příklad distribuční funkce diskrétní náhodné veličiny:
![[media/szz-31/media/image24.png]]

Vlastnosti:

- $0 \le F(x) \le 1$ pro $\forall x \in \mathbb{R}$,
- $F(x)$ je neklesající a zprava spojitá funkce,
- $\lim_{x \to -\infty} F(x) = 0$, $\lim_{x \to \infty} F(x) = 1$,
- $P(a < X \le b) = F(b) - F(a)$ pro každé $a, b \in \mathbb{R}$, $a < b$,
- $P(X = x) = F(x) - \lim_{t \to x^-} F(t)$,
- $F$ má nejvýše spočetně mnoho bodů nespojitosti.

### Funkce hustoty pravděpodobnosti (pravděpodobnostní funkce u diskrétní)

Určuje **rozdělení pravděpodobnosti náhodné veličiny** (u **diskrétní** náhodné veličiny lze vyjádřit tak, že se určí pravděpodobnost **P(x)** pro všechna x definičního oboru veličiny **X**). Značíme ji **f(x)** (u diskrétní náhodné veličiny též **p(x)**) a získá se první derivací distribuční funkce: **f(x) = F’(x)**.

Pravděpodobnostní funkce diskrétní náhodné veličiny:
![[media/szz-31/media/image39.png]]

Vlastnosti:

- $f(x) \ge 0$,
- $f(x) = \dfrac{dF(x)}{dx}$,
- $\int_{-\infty}^{\infty} f(x)\,dx = 1$,
- $P(a \le X \le b) = \int_a^b f(x)\,dx$.

Obsah plochy pod hustotou nalevo od bodu $x_p$ odpovídá pravděpodobnosti $p$ (kvantil), napravo $1 - p$:
![[media/szz-31/media/image37.png]]

## Charakteristiky náhodné veličiny

### Střední hodnota **E(X)**

Střední hodnota **diskrétní** náhodné veličiny je **pravděpodobnostně vážený průměr všech jejích možných hodnot**. Pro **spojitou** náhodnou veličinu je součet nahrazen **integrálem**:

$$E(X) = \sum_x x \cdot p(x) \qquad E(X) = \int_M x f(x)\,dx$$

Vlastnosti střední hodnoty:

$$E(a) = a, \qquad E(aX + b) = a\,E(X) + b, \qquad E(X \pm Y) = E(X) \pm E(Y)$$

Příklad (diskrétní náhodná veličina):

| $x$ | 0 | 100 | 200 | 400 |
|---|---|---|---|---|
| $p(x)$ | $\tfrac{1}{2}$ | $\tfrac{1}{4}$ | $\tfrac{1}{8}$ | $\tfrac{1}{8}$ |

$$E(X) = \sum_x x \cdot p(x) = 100$$

Střední hodnotu lze chápat jako „těžiště“ rozdělení — na obrázku vodorovná čára $y = 2{,}6$ je průměr známek žáků:
![[media/szz-31/media/image60.png]]

### Rozptyl **D(X)**

Také **střední kvadratická odchylka**. Jedná se o **charakteristiku** variability rozdělení pravděpodobnosti **náhodné veličiny**, která vyjadřuje variabilitu rozdělení **souboru náhodných hodnot kolem její střední hodnoty**. Jedná se o **součet obsahů čtverců** jednotlivých hodnot dle vzdálenosti od střední hodnoty.

**Definiční tvar** (střední hodnota kvadrátu odchylky od $E(X)$):

$$D(X) = \sigma^2 = E\big([X - E(X)]^2\big)$$

Pro **diskrétní** náhodnou veličinu se střední hodnota nahradí váženým součtem, pro **spojitou** integrálem:

$$\sigma^2 = \sum_{i=1}^{n} [x_i - E(X)]^2\, p_i \qquad \sigma^2 = \int_{-\infty}^{\infty} [x - E(X)]^2 f(x)\,dx$$

**Výpočetní (zkrácený) tvar** — rozdíl střední hodnoty kvadrátu a kvadrátu střední hodnoty:

$$D(X) = E(X^2) - [E(X)]^2$$

$$\sigma^2 = \sum_{x \in M} x^2\, p(x) - [E(X)]^2 \qquad \sigma^2 = \int_{-\infty}^{\infty} x^2 f(x)\,dx - [E(X)]^2$$

Vlastnosti rozptylu:

$$D(X) \ge 0, \qquad D(aX + b) = a^2 D(X), \qquad D(X \pm Y) = D(X) + D(Y) \text{ pro nezávislé } X, Y$$

### Směrodatná odchylka **σ(X)**

Směrodatná odchylka vypovídá o tom, **nakolik se od sebe navzájem typicky liší** **jednotlivé případy** v souboru zkoumaných hodnot. Vypočítá se jako odmocnina z rozptylu:

$$\sigma(X) = \sqrt{D(X)}$$

## Náhodný vektor

Často je výsledkem pokusu **n-tice** reálných čísel - **vektor**. Poté můžeme zjednodušeně říct, že se jedná o **vektor více náhodných veličin**, které jsou definované na pravděpodobnostním prostoru. Nechť $X, Y$ jsou náhodné veličiny definované na stejném pravděpodobnostním prostoru $(\Omega, \mathcal{A}, P)$. Pak $(X, Y)'$ nazveme **náhodným vektorem**.

### Sdružená distribuční funkce

Obdobná distribuční funkci pro jednu náhodnou veličinu s tím rozdílem, že je **n-rozměrná** (**n** je počet veličin náhodného vektoru). Platí také obdobná pravidla.

$$F(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f(u, v)\,dv\,du \qquad \text{(spojitý vektor)}$$

$$\sum_x \sum_y p(x, y) = 1, \qquad F(x, y) = \sum_{u \le x} \sum_{v \le y} p(u, v) \qquad \text{(diskrétní vektor)}$$

$$\lim_{x \to -\infty} F(x, y) = \lim_{y \to -\infty} F(x, y) = 0, \qquad \lim_{(x,y) \to (\infty, \infty)} F(x, y) = 1$$

Příklad **diskrétní vlevo** a **spojité vpravo**:
![[media/szz-31/media/image38.png]]

![[media/szz-31/media/image5.png]]

### Marginální distribuční funkce

Jedná se o distribuční funkci **jedné z náhodných proměnných náhodného vektoru**, pokud jsou náhodné jevy popsané **zbylými proměnnými** jisté (100%). Je-li $F(x, y)$ sdružená distribuční funkce veličin $X$ a $Y$, pak

$$F_X(x) = P(X \le x) = \lim_{y \to \infty} F(x, y), \quad x \in \mathbb{R}, \qquad F_Y(y) = P(Y \le y) = \lim_{x \to \infty} F(x, y), \quad y \in \mathbb{R}$$

### Sdružená pravděpodobnostní funkce (sdružená hustota pst.)

$$p(x, y) = P(X = x, Y = y) \qquad \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y)\,dx\,dy = 1$$

### Marginální pravděpodobnostní funkce

Všechny ostatní náhodné veličiny až na jednu (tu, u které zjišťujeme marginální pravděpodobnostní funkci), jsou jisté (100%).

$$p_X(x) = P(X = x) = \sum_y p(x, y), \quad x \in \mathbb{R}, \qquad p_Y(y) = P(Y = y) = \sum_x p(x, y), \quad y \in \mathbb{R}$$

U spojitého vektoru se sumy nahradí integrály, např. $f_X(x) = \int_{-\infty}^{\infty} f(x, y)\,dy = \int_0^{\infty} e^{-x-y}\,dy = e^{-x}$ pro $x > 0$.

Příklad (diskrétní vektor a jeho marginály):

| $x \backslash y$ | 0 | 1 | 2 | $p_X(x)$ |
|---|---|---|---|---|
| 0 | 0,42 | 0,12 | 0,06 | 0,6 |
| 1 | 0,28 | 0,08 | 0,04 | 0,4 |
| $p_Y(y)$ | 0,7 | 0,2 | 0,1 | 1 |

### Podmíněné rozdělení

Mějme diskrétní náhodný vektor $(X, Y)'$ se sdruženou pravděpodobnostní funkcí $p(x, y)$. **Podmíněná pravděpodobnostní funkce** je

$$p(x \mid y) = P(X = x \mid Y = y) = \frac{p(x, y)}{p_Y(y)}, \quad p_Y(y) > 0, \qquad p(y \mid x) = \frac{p(x, y)}{p_X(x)}, \quad p_X(x) > 0$$

Pro spojitý vektor se sdruženou hustotou $f(x, y)$ je **podmíněná hustota pravděpodobnosti**

$$f(x \mid y) = \frac{f(x, y)}{f_Y(y)}, \quad f_Y(y) > 0, \qquad f(y \mid x) = \frac{f(x, y)}{f_X(x)}, \quad f_X(x) > 0$$

### Nezávislost

Mějme (diskrétní nebo spojitý) náhodný vektor $(X, Y)'$. Pak veličiny $X, Y$ jsou **nezávislé**, právě když

$$F(x, y) = F_X(x) \cdot F_Y(y) \quad \forall (x, y) \in \mathbb{R}^2$$

ekvivalentně pomocí hustot (spojitý), resp. pravděpodobnostních funkcí (diskrétní):

$$f(x, y) = f_X(x) \cdot f_Y(y), \qquad p(x, y) = p_X(x) \cdot p_Y(y) \quad \forall (x, y) \in \mathbb{R}^2$$

Příklad: v následující tabulce platí $p(x, y) = p_X(x) \cdot p_Y(y)$ pro všechna $(x, y)$, veličiny $X$ a $Y$ jsou tedy nezávislé:

| $x \backslash y$ | 3 | 4 | 5 | $p_X(x)$ |
|---|---|---|---|---|
| 1 | 0,3 | 0,24 | 0,06 | 0,6 |
| 2 | 0,2 | 0,16 | 0,04 | 0,4 |
| $p_Y(y)$ | 0,5 | 0,4 | 0,1 | 1 |

### Střední hodnota a rozptyl

Pro **diskrétní** náhodný vektor:

$$E(X) = \sum_x x \cdot p_X(x), \qquad E(Y) = \sum_y y \cdot p_Y(y), \qquad E(XY) = \sum_x \sum_y xy \cdot p(x, y)$$

$$D(X) = E(X^2) - [E(X)]^2, \qquad E(X^2) = \sum_x x^2 \cdot p_X(x)$$

Pro **spojitý** náhodný vektor:

$$E(X) = \int_{-\infty}^{\infty} x \cdot f_X(x)\,dx, \qquad E(XY) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy \cdot f(x, y)\,dx\,dy$$

$$D(X) = E(X^2) - [E(X)]^2, \qquad E(X^2) = \int_{-\infty}^{\infty} x^2 \cdot f_X(x)\,dx$$

# Rozdělení pravděpodobnosti

### Rovnoměrné rozložení

Spojité rozdělení s konstantní hustotou na intervalu $(a, b)$. Hustota a distribuční funkce:

$$f(x) = \begin{cases} \dfrac{1}{b-a} & \text{pro } x \in (a, b) \\ 0 & \text{pro } x \notin (a, b) \end{cases} \qquad F(x) = \begin{cases} 0 & \text{pro } x \le a \\ \dfrac{x-a}{b-a} & \text{pro } a < x < b \\ 1 & \text{pro } x \ge b \end{cases}$$

Hustota (vlevo) a distribuční funkce (vpravo):
![[media/szz-31/media/image46.png]]

![[media/szz-31/media/image53.png]]

### Normální rozdělení

Jeho důležitost ukazuje **centrální limitní věta** (CLV), jež zhruba řečeno tvrdí, že součet či aritmetický průměr **velkého počtu libovolných** vzájemně nezávislých a nepříliš „divokých“ náhodných veličin se vždy **podobá normálně rozdělené** náhodné veličině. Hustota a distribuční funkce rozdělení $N(\mu, \sigma^2)$:

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}} \qquad F(x) = \int_{-\infty}^{x} \frac{1}{\sigma \sqrt{2\pi}}\, e^{-\frac{(t-\mu)^2}{2\sigma^2}}\,dt$$

Hustota s pravidlem $3\sigma$ (68,3 % – 95,5 % – 99,7 %) a distribuční funkce $\Phi(x)$:
![[media/szz-31/media/image45.png]]

![[media/szz-31/media/image50.png]]

### Exponenciální rozdělení

Určuje **dobu do výskytu 1. události v Poissonově procesu** (dobu mezi dvěma následnými výskyty dané náhodné události). Hustota a distribuční funkce:

$$f_X(x) = \begin{cases} \lambda e^{-\lambda x} & x > 0 \\ 0 & x \le 0 \end{cases} \qquad F(x) = \begin{cases} 1 - e^{-\lambda x} & x > 0 \\ 0 & x \le 0 \end{cases}$$

$$E(X) = \frac{1}{\lambda}, \qquad D(X) = \frac{1}{\lambda^2}$$

![[media/szz-31/media/image49.png]]

### Poissonovo rozdělení

Jedná se o **diskrétní rozdělení**. Udává **počet výskytů dané náhodné události za jednotku času**. Jedná se o opak exponenciálního rozdělení. Pravděpodobnostní funkce a distribuční funkce:

$$P(X = x) = \frac{\lambda^x}{x!}\, e^{-\lambda} \qquad F(x) = \sum_{x_i \le x} \frac{\lambda^{x_i}}{x_i!}\, e^{-\lambda}$$

Pravděpodobnostní funkce a distribuční funkce pro $\lambda = 1, 4, 10$:
![[media/szz-31/media/image48.png]]

![[media/szz-31/media/image43.png]]

### Binomické rozdělení

Opět se jedná o **diskrétní rozdělení** — popisuje počet úspěchů v $n$ nezávislých pokusech s pravděpodobností úspěchu $p$:

$$P[X = x] = \binom{n}{x} p^x (1-p)^{n-x}$$

Pravděpodobnostní funkce a distribuční funkce pro různá $n$, $p$:
![[media/szz-31/media/image13.png]]

![[media/szz-31/media/image33.png]]

# Generování pseudonáhodných čísel

- **fyzikální zdroje náhodnosti**: využívají **senzory** zařízení (teplota, akcelerace, poloha, …), vygenerovaná čísla jsou opravdu **náhodná** (**nedeterministické** generování). Problémem je rychlost, generují jen málo bitů za sekundu.
- **algoritmické generátory**: **pseudonáhodné** (**deterministické**), generují řádově miliardy bitů za sekundu.

### Kongruentní generátor

$$x_{n+1} = (a x_n + b) \bmod m$$

konstanty a, b, m musí být vhodně zvolené, jinak budou generovaná čísla nekvalitní (závislost mezi čísly).

- generují **rovnoměrné rozložení**,
- generují **konečnou posloupnost** čísel - perioda generátoru.

```c
static uint32_t ix = SEED; // počáteční hodnota, 32b
double Random(void) {
    ix = ix * 69069u + 1u; // mod 2^32 je implicitní
    return ix / ((double)UINT32_MAX + 1.0);
}
```

Požadavky na generátor:

- **Rovnoměrnost rozložení**,
- Statistická **nezávislost generované posloupnosti**,
- Co **nejdelší perioda**,
- Rychlost.

Další algoritmy generování:

- **Mersenne twister** (perioda $2^{19937} - 1$),
- **Xorshift**.

## Transformace na jiná rozložení

Náhodné a pseudonáhodné generátory generují ideálně čísla dle **rovnoměrného rozložení**. Při výpočtech ale často potřebujeme generovat čísla dle jiného rozložení.

### Metoda inverzní transformace

Ideální metoda pro generování rozložení, kde je rozložení určeno **analyticky** pomocí **inverzní distribuční funkce cílového rozložení**. Často ale distribuční funkci nemusíme znát nebo **nelze vyjádřit její inverzní funkce elementárními funkcemi**.

Příklad — exponenciální rozložení $F(x) = 1 - e^{-\frac{x - x_0}{A}}$ má inverzní funkci $y = x_0 - A \ln(1 - x)$ (obrázek pro $x_0 = 0$, $A = 1$):
![[media/szz-31/media/image47.png]]

[<u>Inverse Transform Sampling : Data Science Concepts</u>](https://www.youtube.com/watch?v=9ixzzPQWuAY)

### Vylučovací metoda

Sérií pokusů hledáme číslo, které vyhovuje funkci hustoty pravděpodobnosti cílového rozložení. Metoda je **nevhodná** pro **neomezená rozložení** a rozložení, kde je **velká část** hustoty pravděpodobnosti koncentrovaná **do malého intervalu** (**špičaté** normální rozložení: obtížně se trefuje do oblasti pod křivkou). Abychom byli schopni touto metodou generovat rozložení, musíme znát jeho ohraničení (osa **x - definiční obor** a osa **y - obor hodnot**). Funguje na principu, že se vygenerují 2 pseudonáhodná čísla **x** a **y**, **x** se dosadí **do funkce hustoty pravděpodobnosti f(x)** a její hodnota se **porovná** s **y**. Pokud **je menší**, je **x** vráceno jako **hodnota náhodné veličiny**, jinak se proces **opakuje**. Problém může být mnoho iterací při nesprávném rozložení.

### Kompoziční metoda

**Složitou funkci hustotu** (případně distribuční) **rozdělíme** na několik jednodušších po **intervalech**. Na každém intervalu můžeme použít **jinou metodu** pro generování rozložení.

# Bodové a intervalové odhady parametrů

- **Základní soubor** (populace) - obsahuje **všechny** vymezené jednotky.
- **Výběrový soubor** (výběr) - obsahuje pouze **některé** jednotky.

**Vlastnosti výběrového** souboru se snažíme **zobecnit pro celý základní** soubor. Např. při volebním průzkumu se snažíme zobecnit **1000 dotázaných** voličů **na 8 milionů** voličů. Musíme použít **reprezentativní** výběr - **náhodný**.

### Bodový odhad

**Neznámý parametr** (např. průměr) **základního souboru** odhadujeme pomocí **jediného čísla, bodu** na základě **výběrového souboru**. Bodovým odhadem parametru základního souboru jsou **popisné charakteristiky** **výběrového souboru**. pro odhady používáme **výběrový průměr** a **výběrový rozptyl**. Příklad:

- Pokud je **neznámým parametrem základního souboru** 10 000 nových baterek **průměrné napětí**, může jich náhodně vybrat **200 - výběrový soubor**. U těchto 200 baterek určíme **průměrné napětí,** např. 1.49 V a tuto hodnotu prohlásíme za odhad neznámého parametru (v tomto případě průměrného napětí) základního souboru. Takto bychom bodový odhad mohli opakovat např. i pro hmotnost.

Bodový odhad nebude téměř nikdy **přesnou** hodnotou neznámého parametru. Za **lepší** považujeme ten, jehož **rozdělení je více koncentrované okolo neznámé hodnoty** parametru → má **menší rozptyl**, respektive **směrodatnou odchylku**.

- **NEstranný odhad**: Odhad je nestranný, pokud skutečnou hodnotu parametru **nepodhodnocuje ani nenadhodnocuje**. Nezaručí dobrý odhad, pouze **vyloučí systematickou chybu**. **Výběrový průměr** a **výběrový rozptyl** jsou nestranné odhady, pouhý **rozptyl není nestranný**.

**Konzistentní** (dobrý) odhad se tím více **blíží** ke skutečné hodnotě odhadovaného neznámého parametru, **čím větší počet** pozorování provádíme (čím větší je výběrový soubor).

#### **Střední kvadratická chyba**

Umožňuje měřit přesnost bodového odhadu, kombinuje **vychýlení** a **rozptyl**. Jsme poté schopni například říct, že odhadem je **1.49 V** se střední kvadratickou chybou **0.008V**.

#### **Výběrový průměr**

Jedná se o **aritmetický průměr**:

$$\overline{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$$

#### **Výběrový rozptyl**

Výběrový rozptyl $s^2$ je **nestranný** a **konzistentní** odhad rozptylu:

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \overline{X})^2$$

Statistiku $\tfrac{1}{n}\sum_i (X_i - \overline{X})^2 = \tfrac{n-1}{n} s^2$ lze také použít — má menší rozptyl než $s^2$, ale je **vychýlená**.

### Intervalové odhady

Protože bodové odhady jsou poměrně nepřesné, používají se v praxi spíše intervalové odhady, u kterých můžeme říct, že s **určitou pravděpodobností** (vysokou **95–99 %** – **interval spolehlivosti**) se zde **neznámý parametr základního souboru bude vyskytovat**.

- Spolehlivost odhadu je dána zvolenou **pravděpodobností** intervalu spolehlivosti, **čím** je pravděpodobnost **větší**, **tím** je daný odhad **spolehlivější**. **Čím** je ale **odhad spolehlivější**, **tím** se **zvětšuje** i příslušný **interval spolehlivosti**. Tj. **čím širší** interval spolehlivosti, tím je odhad **spolehlivější**, ale **méně přesný**, což je **nepraktické**. Mezi spolehlivostí a přesností je **nepřímá úměrnost**.

Interpretace: pokud budu mnohokrát po sobě generovat náhodný výběr $X_1, \dots, X_n$ a pro každý výběr sestrojím 95% interval spolehlivosti pro parametr $\theta$ (resp. parametrickou funkci $\tau(\theta)$), pak přibližně **95 % z nich bude obsahovat skutečnou hodnotu** parametru. Např. určím-li 95% interval 100×, asi v 5 případech dostanu interval, který skutečnou hodnotu $\theta$ neobsahuje.

V některých případech nás může zajímat pouze **horní hranice - pravostranný interval spolehlivosti,** nebo jenom **dolní hranice - levostranný interval spolehlivosti** pro odhad parametru. Poté používáme **jednostranné intervaly spolehlivosti**.

#### **Rozdělení používaná při intervalových odhadech:**

- **Studentovo t** rozdělení,
- **Chí kvadrát** rozdělení,
- **Asymptotické normální** rozdělení.

#### **Odhad relativní četnosti**

Odhadovaná veličina je rozdělena **alternativně** - může **nabývat 2 stavů** (muž – žena, rub – líc, …). Na základě **výběrového souboru** poté **odhadujeme relativní četnost** výskytu (pravděpodobnost výskytu znaku) **v základním souboru** (např. kolik se za rok narodí holek a kolik kluků podle dat z 1 měsíce).

# Testování hypotéz

Používá se v situacích, kdy **potřebujeme rozhodnout o správnosti nějakého tvrzení**. Např. jestli vede nová technologie výroby k zlepšení kvality vyráběných výrobků.

### Statistická hypotéza (tvrzení)

Jedná se o **tvrzení o parametrech** rozdělení, z něhož pochází **náhodný výběr** (**střední hodnota**, **rozptyl**, **směrodatná odchylka**, …) a o **typu tohoto rozdělení** (normální, exponenciální, rovnoměrné, …). Dva druhy hypotéz:

- **Nulová hypotéza H0** - **předpoklad**, který vyslovíme o určitém parametru či tvaru rozdělení pravděpodobnosti sledované náhodné veličiny.
  - Pacient je nemocný.
- **Alternativní hypotéza H1** - popisuje, jaká situace nastává, **když nulová hypotéza neplatí**.
  - Pacient je zdravý.

**Testování statistických hypotéz** je postup, kterým na základě hodnot náhodného výběru ověřujeme **platnost nulové hypotézy**. Testování může mít **dva závěry**:

- **H0 zamítáme** a tím pádem **platí alternativní hypotéza H1** (s určitou pravděpodobností).
- **H0 nezamítáme**, to znamená, že H0 buď platí, nebo nemáme dostatek informací k tomu, abychom mohli H0 zamítnout. Říkáme, že hypotéza **H1 se neprokázala**.

### Testovací statistika

Jedná se o **testovací kritérium**. Obor hodnot testovací statistiky rozdělíme na dvě části:

- **kritický obor W**: obor **zamítnutí** hypotézy, **T ∈ W → zamítáme H0**,
- **obor přijetí W’**: obor, ve kterém **nezamítáme** hypotézu. **T ∉ W → nezamítáme H0**.

Platnost **H0 posuzujeme** na základě **náhodného výběru** ⇒ **můžeme se dopustit chybných závěrů**. Chyby:

- **Chyba 1. druhu α** (false positive): zamítáme hypotézu, která platí. **α** = **hladina významnosti** testu (obvykle **0,05** → zamítáme H0 a s pravděpodobností alespoň **0.95** (1-α) platí H1).
- **Chyba 2. druhu β** (false negative): nezamítáme hypotézu, která neplatí. **1 − β = síla testu** - pravděpodobnost, že nezamítneme hypotézu, která neplatí.

Chyby 1. a 2. druhu **jdou proti sobě** – nelze minimalizovat obě. (nepřímá úměrnost).

### Testy

- **Studentův t-test**:
  - **test střední hodnoty** rozdělení **se** **známým** **rozptylem**,
  - test zda dvě normální rozdělení mající **stejný** (byť neznámý) **rozptyl**, z nichž pocházejí dva **nezávislé náhodné výběry**, mají **stejné střední hodnoty**.
- **F-test** je jakýkoliv statistický test, ve kterém má testová statistika rozdělení F.

# Regresní a korelační analýza

- **regrese**: Hledáme **funkční závislost** náhodné **veličiny na jiné** veličině (jednostranná závislost). **Umožňuje** **předpovědi**, např. odhad výšky dcery na základě výšky matky.
- **korelace**: Hledáme **sílu** (těsnost) **závislosti dvou náhodných veličin** (vzájemná závislost). **Neslouží** k předpovědím. Např. určujeme, jak těsně spolu souvisí výška matky a výška dcery. Nebo investoři zkoumají, jak jsou nějaké akcie korelované a investují např. do těch, které jsou korelované minimálně, aby v případě, že hodnoty jedněch akcií poklesnou, hodnoty jejich jiných akcií nebyly ovlivněny.

## Regresní analýza

Umožňuje **vyjádřit vztah** mezi proměnnou, kterou chceme popisovat (**vysvětlovaná proměnná**), a množinou **vysvětlujících proměnných**.

- Hledáme vztah mezi množstvím zkonzumované zmrzliny (vysvětlovaná proměnná) a teplotou vzduchu (vysvětlující proměnná).
- Hledáme vztah mezi počtem bodů u zkoušky (vysvětlovaná proměnná) a počtem hodin, které student strávil přípravou na zkoušku (vysvětlující proměnná).

Při regresní analýze odhadujeme:

- **regresní přímku**,
- **regresní parabolu**,
- **regresní rovinu**.

### Metoda nejmenších čtverců

Slouží pro odhad **regresní přímky**, **regresní paraboly** i **regresní roviny**. Pro regresní přímku je model $Y_i = \beta_0 + \beta_1 x_i + e_i$, kde reziduum $e_i = Y_i - (\beta_0 + \beta_1 x_i)$; metoda minimalizuje **součet čtverců reziduí** $\sum_i e_i^2$:

![[media/szz-31/media/image15.png]]

#### **Lineární regrese**

Závislost mezi veličinami je popsána funkcí, která je **lineární v parametrech** (koeficientech).

#### **Nelineární regrese**

Závislost mezi veličinami je popsána funkcí **nelineární v parametrech**.

## Korelační analýza

Úkolem je stanovit **sílu závislosti** mezi sledovanými kvantitativními znaky. Hledáme závislost mezi veličinami, které **spolu (logicky) mohou souviset**. Např. přidávání olova do benzinu a jeho zvýšený výskyt v ovzduší a snižující se IQ a zvyšující se kriminalita. Naopak ale **korelace neimplikuje kauzalitu** - pokud existuje korelace mezi dvěma proměnnými, nelze z toho ještě vyvozovat, že jedna je příčinou a druhá důsledkem (Např. výdaje na podporu rozvoje vědy a počet sebevražd - obě v poslední době rostou, ale podpora vědy nezpůsobuje sebevraždy).

## Zdroje

- SZZ okruh 31 — studijní materiály FIT BUT (`szz-31.docx`). Obrázky a vzorce: `media/szz-31/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/30-vyhledavani-razeni|30. Vyhledávání a řazení]] · další: [[okruhy/32-slozitost-algoritmu|32. Hodnocení složitosti algoritmů]] ▶
