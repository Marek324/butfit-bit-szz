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

> [!note] Ke kontrole
> Zdroj uvádí Studentův **t-test** jako „test střední hodnoty se **známým** rozptylem". Obvyklé vymezení je opačné: **t-test** se používá při **neznámém** rozptylu (odhadovaném z výběru), **z-test** při známém. Ověř formulaci.

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
![[media/szz-31/media/image9.png]]

### Klasická pravděpodobnost

Klasická pravděpodobnost je definována jako **podíl počtu příznivých jevů ku počtu všech možných jevů**. **P(A) = \|A\|/\|Ω\|**, kde:

- **\|A\|** značí počet prvků množiny příznivých jevů,
- **\|Ω\|** značí počet prvků všech možných jevů - velikost základního prostoru.

### Vlastnosti pravděpodobnosti

### Podmíněná pravděpodobnost

O proběhlém pokusu máme doplňující informace a může tak lépe určit jeho pravděpodobnost.
![[media/szz-31/media/image2.png]]

### Bayesův vzorec

Lze jednoduše vyjádřit z podmíněné pravděpodobnosti dosazením za průnik.
![[media/szz-31/media/image44.png]]

### Sčítání pravděpodobností

![[media/szz-31/media/image25.png]]

Pro **nezávislé** jevy jsou průniky **nulové**.

# Náhodná veličina a vektor

Náhodná veličina je číselné ohodnocení náhodného pokusu (který dokážeme číselně ohodnotit). **Náhodnou veličinu** značíme **velkými písmeny X, Y, Z**. **Pravděpodobnost** se značí **malými x, y, z, p**.

Rozlišujeme dva základní typy náhodných veličin:
![[media/szz-31/media/image59.png]]

- **diskrétní** a
- **spojitá**.

### Distribuční funkce

Popisuje **rozdělení** (**pravděpodobnostního chování**) náhodných veličin. Je **neklesající a zprava spojitá**. Distribuční funkce **F(x)** náhodné veličiny **X** přiřazuje každému reálnému číslu **x** pravděpodobnost, že náhodná veličina **X** nabude hodnoty **menší nebo rovné číslu** **x**.

U **diskrétní** náhodné veličiny je distribuční funkce **schodovitá** (vlevo), u spojité náhodné veličiny je distribuční funkce spojitá (vpravo).
![[media/szz-31/media/image30.png]]

Vlastnosti:
![[media/szz-31/media/image20.png]]

![[media/szz-31/media/image24.png]]

Funkce hustoty pravděpodobnosti (Pravděpodobnostní funkce u diskrétní)

Určuje **rozdělení pravděpodobnosti náhodné veličiny** (u **diskrétní** náhodné veličiny lze vyjádřit tak, že se určí pravděpodobnost **P(x)** pro všechna x definičního oboru veličiny **X**). Značíme jí **f(x)** (u diskrétní náhodné veličiny též **p(x)**)a získá se první derivací distribuční funkce: **f(x) = F’(x)**.
![[media/szz-31/media/image58.png]]

![[media/szz-31/media/image21.png]]

Vlastnosti:
![[media/szz-31/media/image39.png]]

![[media/szz-31/media/image65.png]]

![[media/szz-31/media/image37.png]]

## Charakteristiky náhodné veličiny

### Střední hodnota **E(X)**

Střední hodnota **diskrétní** náhodné veličiny (1. obrázek) je **pravděpodobnostně** **vážený průměr všech jejích možných hodnot**. Pro **spojitou** náhodnou veličinu je součet nahrazen **integrálem.**

### Rozptyl **D(X)**
![[media/szz-31/media/image16.png]]

![[media/szz-31/media/image18.png]]

![[media/szz-31/media/image41.png]]

Také **střední kvadratická odchylka**. Jedná se o **charakteristiku** variability rozdělení pravděpodobnosti **náhodné veličiny**, která vyjadřuje variabilitu rozdělení **souboru náhodných hodnot kolem její střední hodnoty**. Jedná se o **součet obsahů čtverců** jednotlivých hodnot dle vzdálenosti od střední hodnoty.

### Směrodatná odchylka **σ(X)**
![[media/szz-31/media/image60.png]]

![[media/szz-31/media/image3.png]]

![[media/szz-31/media/image28.png]]

![[media/szz-31/media/image61.png]]

Směrodatná odchylka vypovídá o tom, **nakolik se od sebe navzájem typicky liší** **jednotlivé případy** v souboru zkoumaných hodnot. Vypočítá se jako odmocnina z rozptylu:
![[media/szz-31/media/image8.png]]

## Náhodný vektor

Často je výsledkem pokusu **n-tice** reálných čísel - **vektor**. Poté můžeme zjednodušeně říct, že se jedná o **vektor více náhodných veličin**, které jsou definované na pravděpodobnostním prostoru.
![[media/szz-31/media/image36.png]]

### Sdružená distribuční funkce

Obdobná distribuční funkci pro jednu náhodnou veličinu s tím rozdílem, že je **n-rozměrná** (**n** je počet veličin náhodného vektoru). Platí také obdobná pravidla.

Příklad **diskrétní vlevo** a **spojité vpravo**:
![[media/szz-31/media/image14.png]]

![[media/szz-31/media/image10.png]]

![[media/szz-31/media/image42.png]]

### Marginální distribuční funkce
![[media/szz-31/media/image38.png]]

![[media/szz-31/media/image5.png]]

Jedná se o distribuční funkci **jedné z náhodných proměnných náhodného vektoru**, pokud jsou náhodné jevy popsané **zbylými proměnnými** jisté (100%).
![[media/szz-31/media/image32.png]]

### Sdružená pravděpodobnostní funkce (sdružená hustota pst.)
![[media/szz-31/media/image19.png]]

### Marginální pravděpodobnostní funkce
![[media/szz-31/media/image6.png]]

Všechny ostatní náhodné veličiny až na jednu (tu, u které zjišťujeme marginální pravděpodobnostní funkci), jsou jisté (100%)

### Podmíněné rozdělení
![[media/szz-31/media/image26.png]]

![[media/szz-31/media/image34.png]]

![[media/szz-31/media/image17.png]]

![[media/szz-31/media/image54.png]]

### Nezávislost
![[media/szz-31/media/image7.png]]

### Střední hodnota a rozptyl
![[media/szz-31/media/image40.png]]

![[media/szz-31/media/image29.png]]

![[media/szz-31/media/image27.png]]

![[media/szz-31/media/image52.png]]

# Rozdělení pravděpodobnosti
![[media/szz-31/media/image56.png]]

### Rovnoměrné rozložení
![[media/szz-31/media/image46.png]]

![[media/szz-31/media/image53.png]]

![[media/szz-31/media/image4.png]]

![[media/szz-31/media/image23.png]]

### Normální rozdělení
![[media/szz-31/media/image45.png]]

Jeho důležitost ukazuje **centrální limitní věta** (CLV), jež zhruba řečeno tvrdí, že součet či aritmetický průměr **velkého počtu libovolných** vzájemně nezávislých a nepříliš „divokých“ náhodných veličin se vždy **podobá normálně rozdělené** náhodné veličině.
![[media/szz-31/media/image35.png]]

![[media/szz-31/media/image50.png]]

![[media/szz-31/media/image64.png]]

### Exponenciální rozdělení

Určuje **dobu mezi dvěma následnými výskyty dané náhodné události**.

### Poissonovo rozdělení
![[media/szz-31/media/image63.png]]

![[media/szz-31/media/image49.png]]

![[media/szz-31/media/image55.png]]

Jedná se o **diskrétní rozdělení**. Udává **počet výskytů dané náhodné události za jednotku času**. Jedná se o opak exponenciálního rozdělení.
![[media/szz-31/media/image48.png]]

![[media/szz-31/media/image43.png]]

![[media/szz-31/media/image11.png]]

![[media/szz-31/media/image51.png]]

### Binomické rozdělení

Opět se jedná o **diskrétní rozdělení**.

![[media/szz-31/media/image62.png]]

![[media/szz-31/media/image13.png]]

![[media/szz-31/media/image33.png]]

# Generování pseudonáhodných čísel

- **fyzikální zdroje náhodnosti**: využívají **senzory** zařízení (teplota, akcelerace, poloha, …), vygenerovaná čísla jsou opravdu **náhodná** (**nedeterministické** generování). Problémem je rychlost, generují jen málo bitů za sekundu.
- **algoritmické generátory**: **pseudonáhodné** (**deterministické**), generují řádově miliardy bitů za sekundu.

### Kongruentní generátor
![[media/szz-31/media/image31.png]]

konstanty a, b, m musí být vhodně zvolené, jinak budou generovaná čísla nekvalitní (závislost mezi čísly).

- generují **rovnoměrné rozložení**,
- generují **konečnou posloupnost** čísel - perioda generátoru.
![[media/szz-31/media/image22.png]]

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

[<u>Inverse Transform Sampling : Data Science Concepts</u>](https://www.youtube.com/watch?v=9ixzzPQWuAY)

### Vylučovací metoda
![[media/szz-31/media/image47.png]]

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
![[media/szz-31/media/image12.png]]

Jedná se o **aritmetický průměr**.

#### **Výběrový rozptyl**
![[media/szz-31/media/image1.png]]

### Intervalové odhady

Protože bodové odhady jsou poměrně nepřesné, používají se v praxi spíše intervalové odhady, u kterých můžeme říct, že s **určitou pravděpodobností** (vysokou **95–99 %** – **interval spolehlivosti**) se zde **neznámý parametr základního souboru bude vyskytovat**.

- Spolehlivost odhadu je dána zvolenou **pravděpodobností** intervalu spolehlivosti, **čím** je pravděpodobnost **větší**, **tím** je daný odhad **spolehlivější**. **Čím** je ale **odhad spolehlivější**, **tím** se **zvětšuje** i příslušný **interval spolehlivosti**. Tj. **čím širší** interval spolehlivosti, tím je odhad **spolehlivější**, ale **méně přesný**, což je **nepraktické**. Mezi spolehlivostí a přesností je **nepřímá úměrnost**.
![[media/szz-31/media/image57.png]]

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

Slouží pro odhad **regresní přímky**, **regresní paraboly** i **regresní roviny**.

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
