---
title: "19. Výroková a predikátová logika (syntaxe, sémantika, splnitelnost, normální formy, PL prvního řádu)"
category: okruh
okruh: 19
tags: [math, logic, discrete-math]
aliases: [výroková logika, predikátová logika, tautologie, DNF, CNF, kvantifikátor, term, formule]
relationships:
  - target: "[[okruhy/16-mnoziny-relace-zobrazeni]]"
    type: related_to
  - target: "[[okruhy/08-minimalizace-logickych-vyrazu]]"
    type: related_to
sources: ["_sources/docx/szz-19.docx"]
summary: Syntaxe a sémantika výrokové logiky, splnitelnost/platnost, logická ekvivalence a důsledek, normální formy (NNF/DNF/CNF) a jazyk predikátové logiky 1. řádu (termy, formule, kvantifikátory, volné/vázané proměnné).
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

# 19. Výroková a predikátová logika

> SZZ okruh 19 (FIT BUT). Formální logika — syntaxe, sémantika, normální formy a predikátová logika 1. řádu.

## Shrnutí

### Výroková logika
- **Syntaxe** = abeceda (proměnné, spojky ¬∧∨→↔, konstanty 0/1) + gramatika; bez precedence → vše se závorkuje.
- **Sémantika** = pravdivostní hodnota pro dané **ohodnocení** I : X → {0,1} (pravdivostní tabulka).
- **Splnitelná** = ∃ ohodnocení dávající 1; **tautologie (platná)** = pravda pro všechna ohodnocení; **kontradikce** = nikdy.
- **Logická ekvivalence** (ϕ ⇔ ψ): stejné modely; **logický důsledek** (ϕ ⇒ ψ): každý model ϕ je modelem ψ. (Neplést s ↔ a → uvnitř formule.)

### Normální formy
- **NNF** — jen ¬∧∨0/1, negace jen u proměnných.
- **DNF** (sum of products) — disjunkce konjunkcí literálů; **CNF** (product of sums) — konjunkce disjunkcí.
- Převod: → NNF (odstranit ↔,→; De Morgan; dvojitá negace) → distributivní zákon.

### Predikátová logika
- Přidává **proměnné, kvantifikátory ∀∃, termy, funkční a predikátové symboly** (s aritou) → bohatší vyjádření.
- **Term** = proměnná / funkční symbol nad termy; **atomická formule** = predikát nad termy.
- **Vázaná** proměnná = v oboru platnosti kvantifikátoru; **volná** = bez něj. Formule bez volných proměnných = **výrok** (uzavřená formule).
- Sémantika vyžaduje **univerzum + interpretaci symbolů + ohodnocení**; základní tvar = **prenexní normální forma**.

Souvisí s [[okruhy/16-mnoziny-relace-zobrazeni]] (formální definice), [[okruhy/20-boolovy-algebry]] (algebra výroků) a [[okruhy/08-minimalizace-logickych-vyrazu]] (DNF/CNF, De Morgan).

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Výroková vs. predikátová** ↪ [[#Predikátová logika]]
- *Co navíc přináší PL?* → proměnné, kvantifikátory (∀,∃), termy, funkční a predikátové symboly.

**Sémantika VL** ↪ [[#Výroková logika]]
- *Splnitelnost vs. platnost (tautologie)?* → Splnitelná = ∃ ohodnocení s hodnotou 1; tautologie = platí pro všechna ohodnocení.
- *Ekvivalence vs. důsledek?* → Ekvivalence: stejné modely; důsledek: každý model ϕ je modelem ψ.
- *Počet řádků prav. tabulky pro N proměnných?* → $2^N$.

**Normální formy** ↪ [[#Normální formy]]
- *DNF vs. CNF?* → DNF = disjunkce konjunkcí (SoP); CNF = konjunkce disjunkcí (PoS); převod přes NNF + distributivita.

**Predikátová logika** ↪ [[#Predikátová logika]]
- *Term vs. formule?* → Term = proměnná / f(termy); formule = predikát nad termy + logické spojky/kvantifikátory.
- *Volné vs. vázané proměnné?* → Vázaná = pod kvantifikátorem; volná = bez něj; bez volných = výrok.
- *Co určuje pravdivost formule?* → univerzum + interpretace symbolů + ohodnocení proměnných.

**Dokazování**
- *Tautologie ↔ dokazatelnost?* → V korektním a úplném kalkulu: dokazatelné ⇔ tautologie.

## Plné znění (ke studiu)

# Výroková logika

Výroková logika tvoří formální odvozovací systém, ze syntaktických a odvozovacích pravidel.

[<u>https://www.fit.vut.cz/person/lengal/public/iam-2025/izlo-opora.pdf</u>](https://www.fit.vut.cz/person/lengal/public/iam-2025/izlo-opora.pdf)

## Syntaxe výrokové logiky

Syntaxe je dána abecedou a gramatikou:

- **abeceda**: Je tvořena spočetně nekonečnou množinu výrokových proměnných, logickými spojkami (logické symboly **{¬,∧,∨,→,↔}**) a logickými konstantami (**0** a **1**). **X = { x, y, z, … , x1, x2, … , 0, 1, ¬, ∧, ∨, →, ↔, (, ) }**

- **gramatika**: vyjadřuje pravidla, jak můžeme tvořit formule výrokové logiky.

  - Je-li **x** výroková proměnná, tj. **x** ∈ **X**, pak **x**, **0** a **1** **jsou formule**.

  - Jsou-li **ϕ** a **ψ** formule, pak jsou formule i **(¬ϕ)**, **(ϕ ∧ ψ)**, **(ϕ ∨ ψ)**, **(ϕ → ψ)** a **(ϕ ↔ ψ)**.

  - Formule výrokové logiky jsou právě všechny konečné řetězce získané pomocí předchozích dvou pravidel.

> **Pozor**, výroková logika **neuvažuje** bez rozšíření **precedenci** jednotlivých **logických symbolů**, vše se musí závorkovat.

## Sémantika výrokové logiky

Sémantika formule určuje její **význam** a určuje, jakou **pravdivostní hodnotu** formule nabude pro **jednotlivá ohodnocení proměnných**. Tato hodnota se často definuje pomocí pravdivostní tabulky. Pravdivostní tabulka pro dvě formule **ϕ** a **ψ** říká, jaká bude výsledná hodnota formule získané aplikací dané **logické spojky** na **ϕ** a **ψ**.
![[media/szz-19/media/image2.png]]


## Splnitelnost, platnost

V následujících bodech uvažujeme ohodnocení proměnných **I : X → {0, 1}**.
![[media/szz-19/media/image8.png]]


- **I splňuje ϕ** (**I \|= ϕ**): Zjišťujeme na základě daného ohodnocení proměnných **I** formule **ϕ**. Pokud je pro toto ohodnocení hodnota **ϕ 1**, je **I** **modelem** formule **ϕ** a formuli splňuje.

- **splnitelnost**: Formule je splnitelná, pokud existuje nějaké ohodnocení proměnných **I** takové, že **I \|= ϕ** (**I** splňuje **ϕ** pro nějaké ohodnocení **I**). Z pravdivostní tabulky poznáme **splnitelnou formuli** tak, že se ve sloupci značící **ϕ** vyskytuje **alespoň jednou hodnota 1**.
![[media/szz-19/media/image20.png]]


- **platnost, tautologie, \|= ϕ**: formule je platná (tautologie) pokud je splněna libovolným ohodnocením proměnných. Pomocí pravdivostní tabulky můžeme platnou formuli poznat tak, že v **posledním sloupci** (sloupec s **ϕ**) tabulky jsou **samé hodnoty 1**.
![[media/szz-19/media/image30.png]]


- **I nesplňuje ϕ** (**I \\= ϕ**): zjišťujeme na základě daného ohodnocení proměnných **I** formule **ϕ**. Pokud je pro toto ohodnocení hodnota **ϕ 0**, není **I** modelem formule **ϕ** a formuli nesplňuje.
![[media/szz-19/media/image24.png]]


- **neplatnost** (**\\= ϕ**)**:** formule **ϕ** je neplatná, pokud existuje **ohodnocení** proměnných, které ji **nesplňuje**. Pomocí pravdivostní tabulky takovou formuli poznáme tak, že by v posledním sloupci (sloupec s **ϕ**) je **alespoň** **jedna hodnota 0**.

- **nesplnitelnost, kontradikce**: formule je nesplnitelná, pokud **není splnitelná**, tj. ve sloupci s **ϕ** pravdivostní tabulky jsou **samé** **0**.

## Logická ekvivalence a logický důsledek
![[media/szz-19/media/image9.png]]

![[media/szz-19/media/image10.png]]

![[media/szz-19/media/image23.png]]


- **logická ekvivalence**: Dvě formule **ϕ** a **ψ** jsou (logicky) **ekvivalentní**, zapisováno **ϕ ⇔ ψ**, pokud pro **všechna ohodnocení** proměnných **I** platí, že **I** je modelem (splňuje) **ϕ** právě tehdy, když **I** je modelem (splňuje) **ψ**.
![[media/szz-19/media/image33.png]]


- **logický důsledek**: Formule **ψ** je **logickým důsledkem** formule **ϕ**, zapisováno **ϕ ⇒ ψ**, když pro **každé ohodnocení** proměnných **I** platí, že je-li **I** modelem (splňuje) **ϕ**, pak je **I** rovněž modelem (splňuje) **ψ**.
![[media/szz-19/media/image28.png]]


**Neplést** si s **logickými spojkami implikace** a **bikondicionál**, i když je význam podobný. Implikace a bikondicionál se používají uvnitř formulí, logická ekvivalence a logický důsledek mezi formulemi.

## Algebraické úpravy formulí

S formulemi můžeme pracovat jako s výrazy, tedy je upravovat jako výrazy pomocí algebraických úprav formulí.

## Normální formy
![[media/szz-19/media/image32.png]]

![[media/szz-19/media/image17.png]]


Jedná se o formule, které splňují jistá syntaktická omezení.

### Negační normální forma (NNF)

Formule je v NNF, pokud:

1.  obsahuje jen následující logické spojky: **0, 1, ¬, ∧, ∨** a

2.  **negace ¬** se vyskytuje jen **před proměnnými**.

Jedná se o literály (proměnné nebo negace proměnných) spojené konjunkcemi a disjunkcemi. Formule v NNF:
![[media/szz-19/media/image15.png]]


Postup převodu obecné formule na formuli v NNF:

1.  **Přepíšeme** postupně všechny **bikondicionály ↔** ve formuli **za implikace**.

2.  **Přepíšeme** postupně všechny **implikace →** ve formuli **za negaci a disjunkci**.
![[media/szz-19/media/image3.png]]

![[media/szz-19/media/image26.png]]


3.  Pomocí **De Morganových** zákonů postupně **přesuneme negaci** co **nejhlouběji**.
![[media/szz-19/media/image7.png]]


4.  Kdykoliv to jde, **eliminujeme dvojitou negaci** (dvojitá negace v NNF není povolena).
![[media/szz-19/media/image13.png]]


### Disjunktivní normální forma (DNF)

Formule je v DNF (sum of products, SoP) v případě, že je zapsána jako disjunkce konjunkcí literálů (konjunkce jsou uvnitř závorek, disjunkce na nejvyšší úrovni). V případě DNF se **konjunkci** literálů říká **klauzule**. Používá se následující značení, kde $l_{i,j}$ je literál:
![[media/szz-19/media/image31.png]]


Příklady formulí v DNF:
![[media/szz-19/media/image22.png]]


Postup převodu obecné formule na formuli v DNF:

1.  Převedeme obecnou formuli na formuli v NNF.

2.  Formuli v NNF převedeme do tvaru, kde jsou **všechny konjunkce pod disjunkcemi** pomocí **distributivního zákona**.
![[media/szz-19/media/image16.png]]


### Konjunktivní normální forma (CNF)

Formule je v CNF (product of sums, PoS) v případě, že je zapsána jako konjunkce disjunkcí literálů (disjunkce jsou uvnitř závorek, konjunkce na nejvyšší úrovni). V případě CNF se **disjunkci** literálů říká **klauzule**. Používá se následující značení, kde $l_{i,j}$ je literál:
![[media/szz-19/media/image14.png]]


Příklady formulí v CNF:

Postup převodu obecné formule na formuli v CNF:
![[media/szz-19/media/image21.png]]


1.  Převedeme obecnou formuli na formuli v NNF.

2.  Formuli v NNF převedeme do tvaru, kde jsou všechny **disjunkce pod konjunkcemi** pomocí **distributivního zákona**.

## Systémy logických spojek
![[media/szz-19/media/image6.png]]


Další logické spojky:

- ⊕: exkluzivní disjunkce (často se jí též říká „xor“ (z anglického „exclusive or“) nebo „nonekvivalence“), kterou lze definovat např. jako:

> x ⊕ y ⇐def⇒ ¬(x ↔ y).

- ↓: negovaná disjunkce (často se používá označení „nor“ z anglického „not or“, můžeme se ale také setkat s termínem **Piercova** šipka):

> x ↓ y ⇐def⇒ ¬(x ∨ y).

- ↑: negovaná konjunkce (často se používá označení „nand“ z anglického „not and“, můžeme se ale také setkat s termínem **Shefferův** operátor):

> x ↑ y ⇐def⇒ ¬(x ∧ y).

Ne všechny zavedené logické spojky jsou nezbytné. Systém logických spojek S je nějaká podmnožina logických spojek, např. S = {→, ∧, 1}. Budeme používat označení $\Phi_S$ pro množinu všech formulí, které lze vytvořit pomocí spojek z S (a proměnných z X a závorek). Systém spojek S je úplný, pokud pro každou formuli výrokové logiky $\varphi \in \Phi_{VL}$ existuje formule $\varphi_S \in \Phi_S$ taková, že $\varphi \Leftrightarrow \varphi_S$.
![[media/szz-19/media/image29.png]]


Příklady úplných a neúplných systémů spojek:

- úplné: {∧, ¬}, {∨, ¬}, {→, ¬}, {↑}, {↓}, {⊕, 1}, {→, 0} (a jejich nadmnožiny),

- neúplné: {∧, ∨, →, ↔, 1} (a libovolná podmnožina).

\
=

# Predikátová logika

Oproti výrokové logice **poskytuje** predikátová logika mnohem bohatší vyjadřovací prostředky. [<u>https://www.fit.vutbr.cz/~lengal/idm-2021/predikatova-logika.pdf</u>](https://www.fit.vutbr.cz/~lengal/idm-2021/predikatova-logika.pdf)

## Abeceda predikátové logiky

1.  **logické spojky**: ¬, ∧, ∨, →, ↔,

2.  **proměnné**: x, y, z, . . . , x1, x2, . . . ∈ X, kde X je spočetně nekonečná množina proměnných

3.  **kvantifikátory**: ∃, ∀,

4.  **závorky**: ),(,

5.  **funkční symboly**: f1, f2, . . . ∈ F (+/2, sin/1, e/0); přiřazují jednu hodnotu každé kombinaci svých argumentů, vracejí konkrétní hodnoty

6.  **predikátové symboly**: p1, p2, . . . (\</2, isnan/1); vyjadřují vztah, vracejí True (1) nebo False (0)

7.  **predikátový symbol rovnosti**: =/2.

**Funkční** a **predikátové** symboly mají **aritu**, která říká, s kolika parametry (operandy) daný symbol pracuje.

## Gramatika predikátové logiky

- **termy**:

  - Je-li **x** proměnná (**x ∈ X**), pak řetězec **“x”** je **term**.

  - Je-li **f** funkční symbol s aritou **n** a **t1, . . . ,tn** jsou **termy**, pak i řetězec **„f(t1, . . . ,tn)“** je term.

- **formule**:
![[media/szz-19/media/image19.png]]


  - Je-li **p** predikátový symbol s aritou **n** a **t1, . . . ,tn** jsou **termy**, potom je řetězec **„p(t1, . . . ,tn)“** **formule** (toto platí i pro „vestavěný“ binární predikátový symbol **=**). Formuli tohoto tvaru říkáme **atomická formule**.

  - Jsou-li **ϕ** a **ψ** **formule**, pak jsou **formule** i řetězce **„(¬ϕ)“**, **„(ϕ ∧ ψ)“**, **„(ϕ ∨ ψ)“**, **„(ϕ → ψ)“** a **„(ϕ ↔ ψ)“**.

  - Je-li **ϕ** formule a **x ∈ X** **proměnná**, pak jsou formule i řetězce **„(∃xϕ)“** a **„(∀xϕ)“**.

## Syntaxe predikátové logiky
![[media/szz-19/media/image18.png]]


Syntax predikátové logiky tvoří abeceda a gramatika (viz výše). Navíc funkční a predikátové symboly nejsou **pevně zafixovány**, ale lze je chápat jako *parametr* jazyka, který si volíme podle toho, co **chceme** v logice **vyjádřit**. Jedná se o signaturu jazyka predikátové logiky, která je dána jako dvojice **\<množina funkčních symbolů, množina predikátových symbolů\>**. Příklady jazyků predikátové logiky.

## Vázané proměnné
![[media/szz-19/media/image1.png]]


Výskyt proměnné je ve formuli vázaný, pokud se nachází v **oboru platnosti** kvantifikátoru ∃ nebo ∀. Pokud je výskyt proměnné vázaný, pak je vázaný **nejbližším** kvantifikátorem nad sebou. Příklad oborů platnosti jednotlivých kvantifikátorů:
![[media/szz-19/media/image12.png]]


## Volné proměnné

Volné proměnné jsou takové, které **nejsou vázané žádným kvantifikátorem**. Z předchozí formule jsou to následující proměnné:
![[media/szz-19/media/image5.png]]


Proměnná je ve formuli **volná**, pokud je ve formuli **alespoň jeden volný výskyt dané proměnné**. Formuli s **volnými** **proměnnými** říkáme **výroková forma** ($x^2 - y > z$), formuli **bez volných proměnných** říkáme **uzavřená formule** nebo také **výrok** ($\forall x\, \exists y\, (x < 2y)$).

## Sémantika predikátové logiky

Sémantika predikátové logiky je podstatně **komplikovanější** než u výrokové logiky. V predikátové logice musíme proměnným **přiřazovat hodnoty** z nějakého univerza a musíme **interpretovat funkční** a **predikátové symboly** (provádět **realizaci** jazyka). Např. abychom určili, jestli formule platí, musíme znát:
![[media/szz-19/media/image25.png]]


- jakou hodnotu bude mít proměnná **y**,

- jaké všechny prvky bude uvažovat **kvantifikátor „∀x“**,

- jaká je **sémantika** funkčního symbolu **„f/1 “** a

- jaká je **sémantika** predikátového symbolu **„\</2 “**.

Příklady různých realizací jazyka:
![[media/szz-19/media/image27.png]]


## Algebraické úpravy formulí

V predikátové logice, obdobně jako ve výrokové logice, můžeme provádět následující algebraické úpravy zachovávající ekvivalenci.

pokud **x** nenáleží FREE\[φ\] znamená, že operaci lze provést jen tehdy, když **x** se **nevyskytuje** jako volná proměnná ve formuli **φ**.
![[media/szz-19/media/image34.png]]


## Prenexní normální forma

Základní normální forma v predikátové logice je tzv. **prenexní normální**

**forma**. Tato forma slouží jako **základ** pro mnoho dalších úprav formulí, jako

je například Skolemizace (odstranění existenčních kvantifikátorů zavedením nových funkčních symbolů).

Formule φ je v prenexní normální formě (PNF), pokud začíná prefixem

kvantifikátorů, za nímž následuje formule bez kvantifikátorů, tj. má

následující tvar:

kde $Q_1, \dots, Q_k \in \{\exists, \forall\}$, $x_1, \dots, x_k \in X$ a $\psi$ je formule bez kvantifikátorů. Postup:
![[media/szz-19/media/image4.png]]

![[media/szz-19/media/image11.png]]


## Zdroje

- SZZ okruh 19 — studijní materiály FIT BUT (`szz-19.docx`). Obrázky: `media/szz-19/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/18-ciselne-soustavy|18. Číselné soustavy]] · další: [[okruhy/20-boolovy-algebry|20. Boolovy algebry]] ▶
