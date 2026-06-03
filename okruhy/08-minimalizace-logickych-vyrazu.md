---
title: "8. Minimalizace logických výrazů (algebraické metody, Karnaughova mapa, Quine McCluskey)"
category: okruh
okruh: 8
tags: [digital-logic, boolean-algebra, math]
aliases: [Karnaughova mapa, Quine-McCluskey, ÚNDF, ÚNKF, SoP, PoS, minterm, maxterm]
relationships:
  - target: "[[okruhy/02-kombinacni-logicke-obvody]]"
    type: related_to
  - target: "[[okruhy/20-boolovy-algebry]]"
    type: uses
sources: ["_sources/docx/szz-08.docx"]
summary: Metody zjednodušení logických funkcí — algebraická (axiomy Booleovy algebry), grafická (Karnaughova mapa) a algoritmická (Quine-McCluskey).
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

# 8. Minimalizace logických výrazů

> SZZ okruh 8 (FIT BUT). Cíl: menší/rychlejší/levnější obvod — méně hradel a spojů, vyšší spolehlivost.

## Shrnutí

## Metody

- **Algebraické** — aplikace axiomů [[okruhy/20-boolovy-algebry|Booleovy algebry]] (uzavřenost, identita, komutativita, distributivita, komplementárnost) a teorémů (idempotence, absorpce, De Morgan, asociativita, dvojitá negace).
- **Grafické** — Vennovy diagramy, **Karnaughova mapa**, jednotková krychle.
- **Algoritmické** — **Quine-McCluskey** (tabulární).

## Normální formy

- **ÚNDF (SoP, suma součinů)** — z řádků pravdivostní tabulky s výstupem 1 vytvoříme **mintermy** (AND), které sečteme (OR). Proměnná s hodnotou 0 → negovaná.
- **ÚNKF (PoS, součin sum)** — z řádků s výstupem 0 vytvoříme **maxtermy** (OR), které vynásobíme (AND). Proměnná s hodnotou 1 → negovaná.
- **MNDF / MNKF** — minimální formy (z termu už nelze eliminovat proměnnou).

## Karnaughova mapa

- Sestavena v **Grayově kódu** (sousední pole se liší o 1 bit).
- Disjunktivní forma: **jedničky** se sdružují do skupin = mocnin 2 (i přes okraje/rohy). Skupina pokrývající bity 0 i 1 → proměnná vypadne; jen bity 1 → přímo; jen bity 0 → negovaně.
- Konjunktivní forma: analogicky se sdružují **nuly** (přiřazení přímo/negovaně je obrácené).

![[media/szz-08/media/image8.png]]
*Karnaughova mapa sestavená v Grayově kódu.*

![[media/szz-08/media/image20.png]]
*Sdružování jedniček do skupin (mocniny 2) — disjunktivní minimalizace.*

## Quine-McCluskey

1. Seřadit implikanty do skupin dle počtu jedniček.
2. Spojovat ty, které se liší o 1 bit (bit nahradit pomlčkou).
3. Opakovat, dokud lze spojovat → zkrácené implikanty.
4. Mřížkou implikantů najít minimální pokrytí (sloupce s jedním křížkem → nezbytné implikanty).

![[media/szz-08/media/image24.png]]
*Mřížka implikantů pro hledání minimálního pokrytí.*

## Souvislosti

Výsledné minimalizované funkce se realizují jako [[okruhy/02-kombinacni-logicke-obvody|kombinační obvody]].


## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Proč minimalizovat**
- *Cíl minimalizace?* → Méně hradel a spojů → menší, rychlejší, levnější a spolehlivější obvod.

**Karnaughova mapa** ↪ [[#Karnaughova mapa]]
- *Princip?* → Tabulka v Grayově kódu (sousední pole se liší o 1 bit); jedničky se sdružují do skupin = mocnin 2 (i přes okraje/rohy).
- *Pravidla zakroužkování?* → Skupina pokrývající bity 0 i 1 dané proměnné → proměnná vypadne; jen bity 1 → přímo; jen bity 0 → negovaně.
- *Booleovská sousednost?* → Sousední termy se liší v jediné proměnné → lze je sloučit.

**Algebraické metody** ↪ [[#Metody]]
- *De Morganovy zákony?* → (a+b)' = a'·b' ; (a·b)' = a'+b'.

**Quine–McCluskey** ↪ [[#Quine-McCluskey]]
- *Co to je, kdy použít?* → Tabulková (algoritmická) metoda pro mnoho proměnných a strojové zpracování; spojuje implikanty lišící se o 1 bit, pak hledá minimální pokrytí.

**Normální formy** ↪ [[#Normální formy]]
- *ÚNDF vs. ÚNKF?* → SoP = suma mintermů (z řádků s výstupem 1); PoS = součin maxtermů (z řádků s výstupem 0).

## Plné znění (ke studiu)

Minimalizaci logických výrazů provádíme z
důvodů:

- **menší, jednodušší logický výraz,**

- **menší počet logických hradel**,

- **menší počet spojů hradel**,

- **rychlejší výpočet**,

- **levnější výroba**,

- méně integrovaných obvodů,

- delší doba bez poruch,

- jednodušší servis,

- větší spolehlivost při praktickém využívání.

## Metody minimalizace

- **Algebraické** - Aplikace **axiomů** Booleovy
  algebry. Náročné pro velké příklady.

- **Grafické** - Vennovy diagramy, **Karnaughova
  mapa**, jednotková krychle…

- **Algoritmické** - **Quine-McCluskey**.

### Algebraická minimalizace

Algebraickou minimalizaci provádíme aplikací **axiomů
Booleovy algebry**, které jsou:

- **uzavřenost**: pokud a, b ∈ B: **(a+b) ∈ B**,
  **(aᐧb)** **∈ B**

- **identita**: **a+0=a**, **aᐧ1=a** - z hlediska
  implementace není nutno tuto operaci provádět,

- **komutativita**: **a+b=b+a**, **aᐧb=bᐧa** - z
  hlediska implementace umožňuje volbu zapojení do hradel,

- **distributivita**: **a+bᐧc = (a+b)ᐧ(a+c)**,
  **aᐧ(b+c)=aᐧb+aᐧc** - kratší výrazy jsou z hlediska implementace
  výhodnější,

- **komplementárnost**: **aᐧa’=0**, **a+a’=1** - z
  hlediska implementace lze předem určit výsledek

- v množině B existují alespoň dva různé prvky

### Teorémy

Jsou odvozeny na základě **axiomů Booleovy algebry**
a definují další užitečné vlastnosti využívané při **minimalizaci**
logických výrazů, jsou to:

- **jedinečnost 0 a 1**,

- idempotence: **a+a=a**, **aᐧa=a**,

- agresivita 1 a 0 (anihilace): **a+1=1**,
  **aᐧ0=0**,

- absorpce: **a+aᐧb=a, aᐧ(a+b)=a**,

- De Morganovy zákony: **(a+b)'= a'ᐧb'**, **(aᐧb)'=
  a'+b'**,

- asociativita: **(a+b)+c=a+(b+c)**,
  **(aᐧb)ᐧc=aᐧ(bᐧc)**,

- dvojitá negace: **a’’=a**,

- absorpce negace: **a+a'ᐧb=a+b**,
  **aᐧ(a'+b)=aᐧb**.

### Normální formy

- **úplná normální disjunktní forma** **ÚNDF** (SoP:
  Sum of Products): Výraz je sepsán jako **suma součinů**. Z
  pravdivostní tabulky ji získáme tak, že vytvoříme **součiny** (AND)
  **vstupních** proměnných v řádcích, kde má výstupní funkce hodnotu
  **log. 1**, tzv. **mintermy**. Všechny tyto mintermy pak **sečteme**
  (OR). Každá proměnná v součinu je zapsána tak, že pokud nabývá hodnoty
  **log. 0**, pak ji píšeme s **negací**, pokud **log. 1**, pak píšeme
  **bez negace**. U zkráceného zápisu jsou uvedeny **stavové indexy**,
  pro které nabývá funkce hodnoty **log. 1**, viz tabulka s červeným
  písmem.

- **úplná normální konjunktní forma ÚNKF** (PoS:
  Product of Sums): Výraz je sepsán jako **součin sum**. Z pravdivostní
  tabulky ji získáme tak, že vytvoříme ze **součtů** vstupních
  proměnných v řádcích, kde má výstupní funkce hodnotu **log. 0** tzv.
  **maxtermů**, a všechny tyto **maxtermy** pak **vynásobíme**. Každá
  proměnná v součtu je zapsána tak, že pokud nabývá hodnoty **log. 0**,
  pak ji píšeme **bez negace**, pokud **log. 1**, pak píšeme s
  **negací**. U zkráceného zápisu jsou uvedeny **stavové indexy**, pro
  které nabývá funkce hodnoty **log. 0**, viz tabulka s červeným
  písmem.
![[media/szz-08/media/image11.png]]

![[media/szz-08/media/image3.png]]

![[media/szz-08/media/image10.png]]

![[media/szz-08/media/image14.png]]


  - **ÚNDF: aᐧbᐧc’ + aᐧb’ᐧc + a’ᐧbᐧc + aᐧbᐧc**

  - **ÚNKF:
    (a+b+c)ᐧ(a’+b+c)ᐧ(a+b’+c)ᐧ(a+b+c’)**

- **minimální normální disjunktní forma MNDF**:
  Minimální možné řešení **termu** (uspořádaná skupina proměnných a
  operátorů) v normální disjunktní formě. Již nelze eliminovat žádnou
  proměnnou z termu.

- **minimální normální konjunktní forma MNKF**:
  Minimální možné řešení **termu** v normální konjunktní formě. Již
  nelze eliminovat žádnou proměnnou z termu.

## Karnaughova mapy

Karnaughovy mapy vytváříme s pomocí **Grayova**
(sousední hodnoty se liší o jediný bit) kódu tak, aby se každé políčko
se všemi sousedními lišilo pouze o **jediný** bit (přehození 3. sloupce
a 3. řádku se 4.). Hodnota proměnné má být **1** v polích, kde je její
odpovídající **bit** **1**, v ostatních polích má být v **0**. V polích
pod **podtržením** má proměnná **nabývat 1, v ostatních 0**.\

![[media/szz-08/media/image8.png]]


### Minimalizace Karnaughovy mapy v disjunktivní formě

**Jedničky** (popř. x) se sdružují do **skupin**,
které jsou **mocniny 2** - lze i přes okraje a rohy. Pokud daná skupina
zasahuje do **bitů** **0 i 1** dané proměnné, proměnná **nebude** ve
výsledném termu. Pokud daná skupina zasahuje pouze do **bitů 1** dané
proměnné, **bude** proměnná ve výsledném termu **přímo**. Pokud daná
skupina zasahuje pouze do **bitů 0**, **bude** proměnná ve výsledném
termu **negovaně**.
![[media/szz-08/media/image5.png]]

![[media/szz-08/media/image20.png]]


### Minimalizace Karnaughovy mapy v konjunktivní formě
![[media/szz-08/media/image1.png]]

![[media/szz-08/media/image17.png]]


**Nuly** (popř. x) se sdružují do skupin, které jsou
**mocniny 2** - lze i přes okraje a rohy. Pokud daná skupina zasahuje do
**bitů** **0 i 1** dané proměnné, proměnná **nebude** ve výsledném
termu. Pokud daná skupina zasahuje pouze do **bitů 1** dané proměnné,
**bude** proměnná ve výsledném termu **negovaně**. Pokud daná skupina
zasahuje pouze do **bitů 0**, **bude** proměnná ve výsledném termu
**přímo**. 
![[media/szz-08/media/image21.png]]

![[media/szz-08/media/image9.png]]

![[media/szz-08/media/image6.png]]

![[media/szz-08/media/image12.png]]


## Quine McCluskey

Tabulární minimalizační metoda. Vhodná pro funkce s
více proměnnými. Postup pro **ÚNDF (SOP)** [<u>Quine-McCluskey
Minimization Technique (Tabular
Method)</u>](https://youtu.be/l1jgq0R5EwQ):

1.  Seřaď do **skupin** jednotlivé implikanty v
    pořadí dle **počtu jedniček** v jejich binárních
    reprezentaci.

2.  Eliminuj proměnné, jejichž implikanty se liší v
    sousedních skupinách **jediným** bitem, místo tohoto bitu piš
    **pomlčku**. Pokud implikant nemá sousedné termy a nelze u něj
    eliminovat žádný bit, jedná se o zkrácený
    implikant.
![[media/szz-08/media/image19.png]]

![[media/szz-08/media/image16.png]]


> 
![[media/szz-08/media/image22.png]]
 style="width:3.20658in;height:4.90981in" />

3.  Pokud byly eliminovány některé implikanty,
    pokračuj bodem 1 s takto eliminovanými
    implikanty.
![[media/szz-08/media/image4.png]]


4.  Hledej minimální řešení pokrytí dané funkce
    pomocí mřížky implikantů.

    1.  zapsat zkrácené implikanty do
        mřížky,
![[media/szz-08/media/image24.png]]


    2.  vybrat sloupce, kde je pouze jeden
        křížek,
![[media/szz-08/media/image7.png]]

![[media/szz-08/media/image18.png]]


    3.  zapsat logický výraz na základě řádků, ve
        kterých se zakroužkované křížky.

**N-rozměrná jednotková krychle** - Model pro 3-4
proměnné, velmi názorný.\

![[media/szz-08/media/image15.png]]



![[media/szz-08/media/image13.png]]

![[media/szz-08/media/image23.png]]


**Vennovy diagramy** - graficky zobrazují booleovskou
sousednost.\

![[media/szz-08/media/image2.png]]


**Odkazy:**

- [<u>Disjunktivní a konjunktivní normální
  forma</u>](https://is.mendelu.cz/eknihovna/opory/zobraz_cast.pl?cast=65564)

## Zdroje

- SZZ okruh 8 — studijní materiály FIT BUT (`szz-08.docx`). Další obrázky: `media/szz-08/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/07-princip-cinnosti-pocitace-pipelining|7. Princip činnosti počítače]] · další: [[okruhy/09-reprezentace-cisel-ieee754|9. Reprezentace čísel]] ▶
