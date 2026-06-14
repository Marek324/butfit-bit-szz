---
title: "16. Množiny, relace a zobrazení"
category: okruh
okruh: 16
tags: [math, discrete-math]
aliases: [množina, relace, zobrazení, ekvivalence, bijekce, kartézský součin]
relationships:
  - target: "[[topics/20-boolovy-algebry]]"
    type: related_to
  - target: "[[topics/19-vyrokova-predikatova-logika]]"
    type: related_to
sources: ["_sources/docx/szz-16.docx"]
summary: Množiny a operace, spočetnost, binární relace a jejich vlastnosti (ekvivalence, uspořádání) a zobrazení (injekce, surjekce, bijekce).
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T17:10:00Z
updated: 2026-06-03T17:10:00Z
---

# 16. Množiny, relace a zobrazení

> SZZ okruh 16 (FIT BUT). Základ diskrétní matematiky — formální definice a vlastnosti.

## Shrnutí

### Množiny
- Soubor **neopakujících se** prvků, určený svými prvky (nezáleží na pořadí); prázdná ∅, konečná, nekonečná.
- **Spočetná** = existuje bijekce s podmnožinou ℕ (i nekonečná — ℤ, ℚ); **nespočetná** ne (např. ℝ).
- **Potenční množina** P(X) = množina všech podmnožin; $|P(X)| = 2^{|X|}$.
- Operace: průnik ∩, sjednocení ∪, rozdíl \, symetrická diference, doplněk (vůči univerzu).
- **Rozklad** = systém disjunktních neprázdných podmnožin pokrývajících množinu (↔ relace ekvivalence).

### Relace
- Binární relace R ⊆ A×B (podmnožina kartézského součinu).
- Vlastnosti: **reflexivní, symetrická, antisymetrická, asymetrická, tranzitivní, ireflexivní**.
- **Ekvivalence** = reflexivní + symetrická + tranzitivní (odpovídá rozkladu množiny).
- **Uspořádání** = reflexivní + antisymetrická + tranzitivní; **ostré** = ireflexivní + asymetrická + tranzitivní.
- **Uzávěr** (tranzitivní/reflexivní/symetrický) = nejmenší relace s danou vlastností obsahující R.

### Zobrazení
- Speciální relace — každý vzor má **nejvýše jeden** obraz.
- **Injekce** (prosté), **surjekce** (na celé Y), **bijekce** (obojí → existuje inverzní zobrazení).
- Doplňkově: supremum/infimum, **svaz** (∃ sup i inf pro každé dva prvky), **grupa** (uzavřenost, asociativita, neutrální a inverzní prvek).

Souvisí s [[topics/20-boolovy-algebry]] (svazy, uspořádání), s formálním zápisem v [[topics/19-vyrokova-predikatova-logika]] a s [[topics/25-teorie-grafu]] (relace ↔ graf).

## Související syntéza

- [[synthesis/relace-napric-obory|Relace × graf × tabulka]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Množiny** ↪ [[#Množiny]]
- *Operace s množinami?* → průnik, sjednocení, rozdíl, symetrická diference, doplněk.
- *Spočetná vs. nespočetná?* → Spočetná = bijekce s podmnožinou ℕ; nespočetná ne (ℝ).
- *Potenční množina a mohutnost?* → P(X) = všechny podmnožiny, $|P(X)| = 2^n$.

**Relace** ↪ [[#Relace]]
- *Definice binární relace?* → Podmnožina kartézského součinu R ⊆ A×B.
- *Vlastnosti?* → reflexivita, symetrie, antisymetrie, tranzitivita, ireflexivita.
- *Ekvivalence ↔ rozklad?* → Ekvivalence (R+S+T) jednoznačně odpovídá rozkladu množiny na třídy.

**Zobrazení** ↪ [[#Zobrazení]]
- *Injekce / surjekce / bijekce?* → Injekce: každý obraz má max. 1 vzor; surjekce: pokrývá celé Y; bijekce: obojí → existuje inverzní zobrazení.

**Tranzitivní uzávěr** ↪ [[#Relace]]
- *Co to je?* → Nejmenší tranzitivní relace obsahující R; doplňuje (a,c) kdykoliv (a,b),(b,c)∈R, dokud nepřibývají nové dvojice (Warshall).

**Kartézský součin**
- *Definice?* → A×B = {(a,b) | a∈A, b∈B}; základ pro definici relací.

## Plné znění (ke studiu)

## Množina

Matematická struktura **neopakujících** se objektů (prvků množiny), chápaných jako celek. Množina je **jednoznačně** **určena** svými **prvky**, ale **nezáleží na** jejich **pořadí**. Množiny mohou být **prázdné**, **konečné** a **nekonečné**.

### Spočetnost množin

- **Spočetná** množina (konečné množiny i nekonečné množiny – spočetně nekonečné množiny; samozřejmě, konečná množina je vždy nutně také spočetná): Taková množina, která je vzájemně **jednoznačná** (**bijektivní** zobrazení) s některou **podmnožinou množiny přirozených čísel** (má stejný počet prvků jako nějaká podmnožina množiny přirozených čísel; každý prvek množiny lze přiřadit jinému přirozenému číslu z dané podmnožiny množiny přirozených čísel). Viz např. Hilbertův hotel [<u>The Infinite Hotel Paradox - Jeff Dekofsky</u>](https://youtu.be/Uj3_KqkI9Zo)
- **Nespočetná** množina (nespočetně nekonečná množina): Množina, kterou nelze jednoznačně vzájemně zobrazit na žádnou podmnožinu přirozených čísel. Neexistuje tedy prosté zobrazení z dané množiny na množinu přirozených čísel. Nespočetná množina má více prvků než množina přirozených čísel. Například **reálná čísla**.

### Prázdná množina (∅ nebo {})

Množina, která neobsahuje žádné prvky.

### Popis množiny a značení

Množiny obvykle značíme velkými písmeny a jejich prvky písmeny malými. Je-li prvek **a** prvkem množiny **B**, píšeme: **a** **∈** **B**. Způsoby zadávání:

- **Výčtem prvků**: $A = \{42, 1337, 94, 0\}$,
- **Predikátem**: $B = \{2^k \mid k \in \mathbb{N}\}$,
- **Intervalem**: $(a, b)$, $(a, b\rangle$, $\langle a, b)$, $\langle a, b\rangle$ — $a < b$,
- **Dobře známé množiny**: **N**, **Z**, **Q**, **R**, **C**, **∅**.

### Potenční množina

Potenční množina **P(X)** množiny **X** je taková množina, která obsahuje všechny podmnožiny množiny **X**. Pokud je množina **X** konečná a její mohutnost **\|X\|** = **n**, pak je mohutnost **P(X)** rovna **\|P(X)\|** = $2^n$.

- Množina samotná je také podmnožinou sama sebe.
- Prázdná množina je podmnožinou každé množiny, včetně prázdné množiny.

Např.:

> *A = {1,2,3}*
>
> *P(A) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}*
>
> *A = ∅, tedy n = 0: $2^n = 1$*
>
> *P(A) = {∅}*

### Podmnožina

Množina **B** je podmnožinou množiny **A**: **B ⊆ A**, pokud platí, že všechny prvky množiny B se **nachází** v množině **A**. Pak je možné množinu **A** označit také za **nadmnožinu**. Stav “bytí podmnožinou” se také nazývá **inkluze**.

- **Vlastní podmnožina**: Podmnožina **B** množiny **A**, která se **nerovná** množině **A: B ⊂ A.**

### Uzavřenost množiny na operaci

Množina **M**, kde **M ⊂ U**, je **uzavřená** vůči algebraické operaci pokud tato operace **vrátí** hodnotu z **M (**a nikoliv hodnotu z **U** mimo **M)**. Tedy provedením operace s **uzavřenou množinou** **k této operaci** získáme opět prvek **z této množiny**.

### Rozklad množiny

Rozkladem množin vznikne **systém množin** (množina množin), kde sjednocením jejích prvků získáme původní rozloženou množinu. Zároveň pokud pro libovolné dva prvky rozkladu platí **X ∩ Y != ∅, pak X = Y**.

![[media/szz-16/media/image13.png]]

### Operace s množinami

- **Průnik**: průnik dvou nebo více množin označuje taková množina, která obsahuje pouze ty prvky, které se nalézají ve všech těchto množinách.
- **Sjednocení**: sjednocení dvou nebo více množin označuje taková množina, která obsahuje každý prvek, který se nachází alespoň v jedné ze sjednocovaných množin, a žádné další prvky.
- **Rozdíl**: rozdíl dvou množin označuje taková množina, která obsahuje každý prvek, který se nachází v první z množin, ale nenachází se ve druhé z nich, a žádné další prvky.
- **Symetrická diference** (**symetrický rozdíl**): symetrická diference nebo symetrický rozdíl dvou množin označuje taková množina, která obsahuje všechny prvky z obou množin, které nejsou v jejich průniku.
![[media/szz-16/media/image4.png]]= (A ∪ B) \\ (A ∩ B)

- **Doplněk**: doplněk množiny A nebo **komplement** množiny A označuje množina $A^C$ všech prvků, které nejsou v A a přitom v nějaké jiné (předem dané) množině jsou obsaženy (na obrázku v U). Aby bylo možné doplněk definovat, je třeba znát množinu (universum), vzhledem ke které se doplněk počítá.
![[media/szz-16/media/image17.png]]

### Vlastnosti operací

- **Komutativnost** - Vlastnost binární operace, která říká, že nezáleží na pořadí argumentů - A ∩ B = B ∩ A. U komutativní operace můžeme **zaměnit** **pořadí** hodnot a **nezměníme** tím **výsledek**.
- **Asociativita** - Vlastnost **binární operace**, která říká, že **nezáleží** na tom, jak použijeme **závorky** u výrazu, kde je více operandů. Nezáleží, v jakém pořadí budeme tedy tento výraz počítat - **(A ∩ B) ∩ C = A ∩ (B ∩ C)**.
- **Distributivita** - Vlastnost **binární operace vůči jiné binární operaci**, říkající, že můžeme tuto **operaci distribuovat** přes jinou operaci - **x\*(y + z) = (x \* y) + (x \* z)**. Nebo **(A ∩ B) ∪ C = (A ∪ C) ∩ (B ∪ C)**.

## Relace

Jako relaci nebo n-ární relaci nazveme v matematice libovolný vztah mezi skupinou prvků jedné nebo více množin. Podle **arity** dělíme relace na **unární**, **binární**, **ternární** (obecně **n-ární**).

Relace mezi množinami **A1, A2, · · · , Ak**, pro **k ∈ N**, je libovolná podmnožina kartézského součinu **R ⊆ A1 × A2 × · · · × Ak** . Pokud **A1 = A2 = · · · = Ak = A**, hovoříme o **k-ární** relaci **R** na **A.**

### Unární relací

V relaci se nachází jeden prvek, např.:

- relace: **Být kladné číslo**. Ptáme se, je číslo kladné?
- relace: **Být pravdivý výrok**. Ptáme se, je výrok pravdivý?

### Binární relace

Binární relace jsou relace, do kterých vstupují **dva** prvky množiny (množiny mohou být různé). Binární relace **R** mezi množinami **A, B** je libovolná podmnožina **R** **kartézského součinu** množin **A, B**. Označení: **\[x, y\]** **∈** **R** nebo ***(xRy)***. Pokud **A = B**, hovoříme o binární relaci na množině **A**. Množina **A** se nazývá **definičním oborem** relace **R** a množina **B** **oborem hodnot** relace **R**. Pro zápis relací používáme popis predikátem: **R = {(a, b) ∈ A × B \| student a má zapsán předmět b}** nebo **R =** **{(a, b) ∈ A × B \| a + b \> 5}**.

### Vlastnosti relací

- **Symetrická**: pokud platí ***(pRq)***, tak platí i ***(qRp)***. Relace je symetrická pokud pro ***p*** a ***q*** z **X** platí, že ***p*** je v relaci s ***q*** a ***q*** je současně v relaci s ***p***.
	- např. relace **R** = ‘je sourozenec’ - **Prázdná relace je symetrická**, tzn. platí to i když někdo nemá sourozence.

$$\forall a,b \in X:\ [a,b] \in R \implies [b,a] \in R$$

- **Antisymetrická** (slabě antisymetrická): Relace, ve které nemůže nastat, že by ***p*** bylo v relaci s ***q*** a zároveň ***q*** v relaci s ***p***. Pokud tak nastane, **p** se rovná **q**. Jedná se např. o R = ‘je menší nebo rovno’ ((neostré) uspořádání). **Nejedná se o opak symetrie**. Relace může být **současně symetrická i antisymetrická**, např. rovnost.

$$\forall a,b \in X:\ \big([a,b] \in R \wedge [b,a] \in R\big) \implies a = b$$

- **Asymetrická** (Silně antisymetrická): relace, která je **současně antisymetrická** a **ireflexivní**. Jedná se např. o R = ‘je menší než’ (ostrá nerovnost). Jediná relace, která je **současně symetrická a asymetrická, je prázdná** relace.

$$\forall a,b \in X:\ [a,b] \in R \implies \neg\big([b,a] \in R\big)$$

- **Reflexivní**: pokud pro všechna x patřící do X platí ***(xRx)***, jinak řečeno, pokud je každý prvek **v relaci sám se sebou**. **Prázdná** relace nad **prázdnou** množinou **je reflexivní**, ale **prázdná** relace nad **neprázdnou** množinou **není reflexivní**.
	- např. R = ‘je stejný’, R = ‘je větší nebo rovno’, R = ‘je podmnožinou’

$$\forall a \in X:\ [a,a] \in R$$

- **Tranzitivní** - Pokud ***(pRq)*** a současně ***(qRr)***, pak platí ***(pRr)***. Pokud pro každé **p, q, r** z množiny **X** platí, že pokud je **p** v relaci s **q** a **q** v relaci s **r**, tak je i **p** v relaci s **r**. **Prázdná relace je tranzitivní**.
	- např. R = ‘je sourozenec’, R = ‘je vyšší’
	- relace R = ‘je kamarád’ **není tranzitivní**.

$$\forall a,b,c \in X:\ \big([a,b] \in R \wedge [b,c] \in R\big) \implies [a,c] \in R$$

### Známé binární relace

- **Ekvivalence**: relace, která je současně **reflexivní**, **symetrická** a **tranzitivní**. Např. **rovnoběžnost, rovnost, podobnost trojúhelníků**.
- **Uspořádání**: relace, která je současně **reflexivní**, (slabě) **antisymetrická** a **tranzitivní**. Např. R = ‘větší nebo rovno než’ nebo R = ‘je podmnožinou’
- **Ostré uspořádání**: relace, která je současně **ireflexivní**, **asymetrická** a **tranzitivní**. Např. R = ‘větší než’ nebo R = ‘je vlastní podmnožinou’ (podmnožina množiny, která ji není rovna).

### Inverzní relace

Inverzní binární relace je množina uspořádaných párů, která je přesnou inverzí (obrácením pořadí) množiny uspořádaných párů původní binární relace. Např.: pro R = {(1, a), (2, b), (3, c)} je inverzní relace $R^{-1}$ = {(a, 1), (b, 2), (c, 3)}

### Uzávěry relací

- **Tranzitivní**: [<u>Warshall's Algorithm (Finding the Transitive Closure)</u>](https://youtu.be/_-p8zhizock)Např. pro
![[media/szz-16/media/image14.png]]
je tranzitivní uzávěr R+ = {(2, 1), (2, 3), (2, 4), (3, 1), (3, 3), (3, 4), (4, 1), (4, 3), (4, 4)}

- **Reflexivní**: reflexivní uzávěr binární relace **R** na množině **X** je nejmenší reflexivní relace **S** na množině X obsahující relaci **R** . Např.: X = {1, 2, 3}, R = {(1, 1), (2, 3)}, S = {(1, 1), (2, 2), (3, 3), (2, 3)}
![[media/szz-16/media/image2.png]]

- **Symetrický**: symetrický uzávěr binární relace **R** na množině **X** je nejmenší symetrická relace **S** na množině **X** obsahující relaci **R**. Např.: X = {1, 2, 3}, R = {(1, 1), (2, 1), (2, 3)}, S = {(1, 1), (1, 2), (2, 1), (2, 3), (3, 2)}
![[media/szz-16/media/image8.png]]

### Ternární relace

Ternární relace jsou relace, do kterých vstupují **tři** prvky množiny (množiny mohou být různé). Ternární relace **R** mezi množinami **A, B, C** je libovolná podmnožina **R** **kartézského součinu** množin **A, B, C**. Označení: **\[x, y, z\]** **∈** **R** nebo **R(x, y, z)**. Pokud **A = B = C**, hovoříme o ternární relaci na množině **A**.

- např. R = ‘je mezi’

### Skládání relací

Používá se operátor “kolečko”, který má význam **po**. To znamená, že relace z první množiny navazujeme na relace z druhé množiny.

![[media/szz-16/media/image3.png]]

### Algebra

Množina, na které jsou definované nějaké **operace** a daná množina je vzhledem k těmto operacím **uzavřená**, tzn. že výsledkem operace nad prvky této množiny je vždy také prvek této množiny. Např. sčítání na množině přirozených čísel.

### Kongruence

Kongruence je ekvivalence (reflexivní, symetrická a tranzitivní relace) na algebře (množina uzavřená vůči operacím). Jedná se např. o množinu **zbytkových tříd**.

### Kartézský součin

Kartézským součinem množin **X** a **Y** vznikne množina všech **uspořádaných dvojic**, ve kterých je první položka prvkem množiny **X** a druhá prvkem množiny **Y**.

![[media/szz-16/media/image19.png]]

## Zobrazení

Předpis, který prvkům množiny **X** (vzory) přiřazuje **nejvýše jeden** prvek množiny **Y** (obraz). Tedy zobrazení z množiny **X** do množiny **Y**. Prvky **X** se nazývají **vzory** a prvky **Y** se nazývají **obrazy**. Podobně jako u funkce musí každému prvku z **X** být přiřazena nanejvýš jedna hodnota. **Zobrazení je speciálním případem binární relace, u které má každý vzor nejvýše jeden obraz**.

Typy zobrazení:

- **Injektivní (prosté) zobrazení**: Každý prvek z Y má namapován nejvíce 1 prvek z X (každý vzor má obraz, může ale existovat i obraz bez vzoru).

![[media/szz-16/media/image11.png]]

- **Surjektivní zobrazení (zobrazení na)**: Zobrazuje **na celou cílovou množinu** (**nezůstane volný prvek v Y**, tedy každý prvek **Y** má namapovaný alespoň 1 prvek z **X**, každý obraz má alespoň jeden vzor).

![[media/szz-16/media/image9.png]]

- **Bijektivní (vzájemně jednoznačné) zobrazení**: Zároveň **injektivní** a **surjektivní** zobrazení. Každý obraz má právě jeden vzor.

![[media/szz-16/media/image12.png]]

![[media/szz-16/media/image6.png]]

### Inverzní zobrazení

Inverzní zobrazení k nějakému zobrazení **f: A → B** přiřazuje prvkům z množiny **B** prvky množiny **A**, tedy **obrazům** zobrazení **f** přiřazuje **vzory** zobrazení **f**. Zobrazení **f** musí být **prosté** (injektivní).

### Supremum a maximum

Nechť **A** je neprázdná **shora ohraničená** množina (množina, která nejde do nekonečna) reálných čísel. Číslo **sup(A)** se nazývá **supremum** množiny **A**, jestliže je **nejmenší** **horní závorou** množiny A. **Sup(A)** musí být **větší** **nebo rovno** všem prvkům množiny **A**, nemusí být ale maximem. Např.: interval **X = (2, 3)** má **supremum** **3** (**sup(X) = 3**), ale nemá maximum, protože se jedná o otevřený interval. Y = (2, 3\> má **supremum 3**, které je současně **maximem**.

### Infimum a minimum

Nechť **A** je neprázdná **zdola ohraničená** množina (množina, která nezačíná v mínus nekonečnu) reálných čísel. Číslo **inf(A)** se nazývá **infimum** množiny **A**, jestliže je **největší dolní závorou** množiny **A**. **Inf(A)** musí být **menší nebo rovno** všem prvkům množiny **A**, nemusí být ale minimem. Např.: interval **X = (2, 3)** má **infimum** **2** (**inf(X) = 2**), ale nemá minimum, protože se jedná o otevřený interval. Y = \<2, 3) má **infimum 2**, které je současně **minimem**. Tzn. infimum nemusí být prvek z dané množiny, minimum ale musí.

### Svaz

Svaz je **uspořádaná množina**, kde pro **každé dva prvky** z daného svazu musí existovat **supremum** a **infimum**, které také náleží danému svazu.

### Grupa

Grupou nazýváme množinu **G** spolu s binární operací (v tomto případě značenou +). Musí platit:

- Operace **+** musí být na množině **G** **uzavřená**, tj. musí vracet prvek z množiny **G**.
- Operace **+** musí být na množině **G** **asociativní**.
- **Existence neutrálního prvku**: Existuje prvek **e** **∈ G** (neutrální prvek) takový, že pro všechny ostatní prvky **a** **∈ G** platí: **a + e = e + a = a**.
- **Existence inverzních prvků**: Pro každý prvek **a** **∈ G** existuje prvek **b** **∈ G** takový, že **a + b = b + a = e**, kde **e** **∈ G** je **neutrální prvek**.

## Zdroje

- SZZ okruh 16 — studijní materiály FIT BUT (`szz-16.docx`). Obrázky: `media/szz-16/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[topics/15-cislicove-filtry|15. Číslicové filtry]] · další: [[topics/17-diferencialni-integralni-pocet|17. Diferenciální a integrální počet]] ▶
