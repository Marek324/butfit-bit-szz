---
title: "17. Diferenciální a integrální počet funkcí jedné a více proměnných"
category: okruh
okruh: 17
tags: [math, calculus]
aliases: [derivace, limita, integrál, parciální derivace, gradient, per partes, substituce]
relationships:
  - target: "[[okruhy/24-numericke-metody]]"
    type: related_to
  - target: "[[okruhy/14-spektralni-analyza]]"
    type: related_to
sources: ["_sources/docx/szz-17.docx"]
summary: Limita a spojitost, derivace (geometrický význam, vyšetření průběhu), integrál (určitý/neurčitý, per partes, substituce) a rozšíření na funkce více proměnných (parciální derivace, gradient, vícenásobné integrály).
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T17:10:00Z
updated: 2026-06-03T17:10:00Z
---

# 17. Diferenciální a integrální počet

> SZZ okruh 17 (FIT BUT). Limity, derivace, integrály — jedna i více proměnných.

## Shrnutí

### Diferenciální počet
- **Limita** — hodnoty funkce se libovolně blíží bodu L; funkce má v bodě nejvýše jednu limitu (vlastní/nevlastní, zleva/zprava).
- **Spojitost** — malá změna x → libovolně malá změna f(x); graf „jedním tahem".
- **Derivace** = limita poměru přírůstku funkce ku přírůstku argumentu = **směrnice tečny**; fyzikálně rychlost/zrychlení. Existuje ⇒ funkce je spojitá (naopak ne).
- Použití: 1. derivace → růst/pokles a lokální extrémy (kde = 0 nebo neexistuje); 2. derivace → konvexnost/konkávnost a inflexní body; asymptoty.

### Integrální počet
- **Neurčitý integrál** = primitivní funkce F (F′ = f); opačná operace k derivaci, ale s konstantou +c (info o konstantní složce se derivací ztrácí).
- **Určitý integrál** = plocha pod křivkou; objem, délka křivky.
- Metody: **per partes** (součin), **substituce** (u určitého nutno přepočítat meze).

### Funkce více proměnných
- **Parciální derivace** — derivace podle jedné proměnné, ostatní jako konstanty.
- **Gradient** = vektor parciálních derivací → směr největšího růstu; nulový gradient = stacionární bod (extrém/sedlo).
- **Dvojný/trojný integrál** — převod na dvoj-/trojnásobný (Fubiniova věta); objem, hmotnost.

> [!note] Ke kontrole (ověřeno)
> Zdroj u extrémů funkcí více proměnných píše „gradient druhé parciální derivace … hodnota menší/větší než 0". To je **nepřesné**: typ stacionárního bodu se určuje **definitností Hessovy matice** (druhých parciálních derivací), ne znaménkem jediné hodnoty.

Numerické postupy (Euler, Monte Carlo) viz [[okruhy/24-numericke-metody]]; integrály a derivace stojí pod [[okruhy/14-spektralni-analyza|Fourierovou analýzou]].

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Derivace** ↪ [[#Diferenciální počet]]
- *Definice a geometrický význam?* → Limita poměru Δf/Δx; směrnice tečny grafu v bodě.
- *Vztah spojitost ↔ derivovatelnost?* → Má-li funkce derivaci, je spojitá; opačně neplatí (např. |x| v 0).

**Extrémy** ↪ [[#Diferenciální počet]]
- *Jak hledat?* → Kritické body (1. derivace = 0 nebo neexistuje) + krajní body; typ rozhodne 2. derivace (jedna proměnná) / Hessián (více proměnných).

**Funkce více proměnných** ↪ [[#Funkce více proměnných]]
- *Parciální derivace, gradient?* → Derivace podle jedné proměnné (ostatní konstanty); gradient = vektor parciálních derivací, směr největšího růstu.

**Integrál** ↪ [[#Integrální počet]]
- *Určitý vs. neurčitý?* → Neurčitý = primitivní funkce (+c); určitý = plocha pod křivkou mezi mezemi.
- *Metody?* → per partes, substituce; numericky lichoběžníkové pravidlo, Monte Carlo.

**Limita a spojitost** ↪ [[#Diferenciální počet]]
- *Spojitost (ε–δ)?* → Pro každé ε-okolí f(a) existuje δ-okolí a tak, že f(x) padne do ε-okolí.

## Plné znění (ke studiu)

## Diferenciální počet

Matematická disciplína, která zkoumá **změny funkčních hodnot** v závislosti na změně nezávislé proměnné.

### Spojitost funkce

**Definice**: Funkce je spojitá v bodě **a**, pokud pro libovolně velké **epsilon** okolí bodu **f(a)** (funkční hodnoty funkce v bodě a) existuje **delta** okolí bodu **a** a pro všechna **x** z **delta** okolí platí, že **f(x)** náleží do **epsilon** okolí.

Spojitost funkce je její důležitá vlastnost pro určování limit a derivací. Spojitá funkce je funkce, jejíž hodnoty se **mění plynule**, tedy při dostatečně malé změně hodnoty **x** se hodnota **f(x)** změní libovolně málo. Intuitivní (ne zcela přesná) představa spojité funkce spočívá ve funkci, jejíž graf lze nakreslit jedním tahem, aniž by se tužka zvedla z papíru. Pokud funkce není v bodě spojitá, může tato nespojitost být dvojího druhu:
![[media/szz-17/media/image5.png]]

- **Nespojitost prvního druhu**: Limity **zleva a zprava jsou vlastní, ale nerovnají se.**
- **Nespojitost druhého druhu**: Bod má alespoň jednu **nevlastní** jednostrannou limitu nebo pokud alespoň jedna **limita neexistuje**.

### Limita

Limita je matematická konstrukce vyjadřující, že se hodnoty zadané funkce blíží **libovolně blízko** k nějakému bodu. Právě tento bod je pak označován jako limita.

**Definice**: Funkce **f(x)** má v bodě **a** limitu **L**, jestliže k libovolně zvolenému **epsilon** okolí bodu **L** existuje **delta** okolí bodu **a** takové, že pro všechna reálná **x != a** tohoto okolí **náleží hodnoty f(x)** epsilon okolí **bodu L**. Značíme jako Funkce má v bodě **maximálně jednu limitu**. Druhy limit:
![[media/szz-17/media/image45.png]]

![[media/szz-17/media/image38.png]]

- **Vlastní** - Pokud hodnota neroste do +- nekonečna.
- **Nevlastní** - Limita roste do +- nekonečna.
- **Zprava** - Pokud se blížíme k bodu zprava na ose (z kladných čísel).
- **Zleva** - Pokud se blížíme k bodu zleva na ose (ze záporných čísel). Např. funkce signum má v bodě 0 limitu zleva rovnu -1 a limitu zprava rovnu +1.

### Derivace

Derivace funkce je **změna** (růst či pokles) její funkční hodnoty **v poměru** ke **změně** jejího **argumentu**, pro velmi malé změny argumentu. V případě dvourozměrného grafu funkce **f(x)** je **derivace této funkce** v libovolném bodě (pokud existuje) rovna **směrnici tečny tohoto grafu v daném bodě**. Například pokud funkce popisuje **dráhu tělesa v čase**, bude její **derivace** v určitém bodě udávat **okamžitou rychlost**. Pokud popisuje **rychlost**, bude **derivace udávat zrychlení**. Derivaci definujeme pomocí limity. Funkce **f(x)** je v bodě **x** **diferencovatelná**, pokud v tomto bodě derivace existuje. Pokud limita v bodě **x** neexistuje nebo **je nevlastní**, pak **není** **derivace** funkce f(x) v bodě x **definována**. Aby existovala derivace v bodě, musí být **limity** v tomto bodě zprava i zleva vlastní a navzájem si rovny. Má-li funkce v daném bodě derivaci, pak je v tomto bodě i spojitá (naopak to **neplatí**).
![[media/szz-17/media/image20.png]]

![[media/szz-17/media/image25.png]]

![[media/szz-17/media/image9.png]]

![[media/szz-17/media/image36.png]]

![[media/szz-17/media/image49.png]]

Derivaci používáme k **vyšetření průběhu funkce**. První derivací určujeme, jestli funkce v daném bodě roste, nebo klesá. V bodech, kde je **první derivace nulová** nebo **neexistuje** hledáme **lokální extrémy** (minima a maxima). **Druhou derivací** určujeme **konvexnost** (druhá derivace je kladná) a **konkávnost** (druhá derivace je záporná) funkcí. Body, ve kterých je druhá **derivace nulová nebo neexistuje**, jsou **inflexní** body. **Asymptoty grafu funkce** jsou přímky, ke kterým se graf funkce blíží v +/- nekonečnu (výpočet viz [<u>Asymptota funkce</u>](https://maths.cz/clanky/213-asymptota-funkce))

- **Bez směrnice**: podezřelé jsou hodnoty **vyloučené** z definičního oboru. Pro ověření je potřeba **spočítat limitu** **zleva** a **zprava** pro daný bod a pokud vyjdou **+/- nekonečno**, jedná se o **asymptotu bez směrnic**.
- **Se směrnicí**: Jedná se o asymptotu, která **není rovnoběžná s osou y**. Mohou existovat **maximálně 2** pro jednu funkci. (y = ax + b).

### Derivace elementárních funkcí

viz tabulka
![[media/szz-17/media/image40.png]]

## Integrální počet

Integrální počet je část matematiky, která se zabývá především **integrací**. Integrály se využívají pro hledání **ploch**, **objemů** a délek **křivek**. Integraci můžeme také považovat **za proces sčítání**, dokonce tak lze definovat **určitý integrál**.

**Neurčitý integrál** definujeme pomocí derivace takto: Nechť **I** je otevřený interval, **f(x)** a **F(x)** funkce na něm definované, pokud **F′(x) = f(x)**, pak se funkce **F(x)** nazývá primitivní funkcí k funkci **f(x)**, nebo též **neurčitý integrál funkce** **f(x)** na intervalu **I**.
![[media/szz-17/media/image11.png]]

### Neurčitý integrál
![[media/szz-17/media/image8.png]]

Operace integrování je **opačná** k operaci derivování. Integrál ale **není inverzní** funkcí k derivaci, protože **derivováním ztrácíme** informaci o **konstantní** (stejnosměrné) složce derivované funkce. Abychom integrováním zderivované funkce získali funkci původní, musíme znát její hodnotu **alespoň v jednom bodě**. Pomocí této hodnoty můžeme **vypočítat konstantní** (**c**) složku.

### Určitý integrál

Slouží pro výpočet **povrchu**, **objemu** nebo **obvodu** geometrického útvaru (výpočet je omezen na určitou část). Aby byla funkce integrovatelná nemusí být **spojitá** na celém intervalu nebo **spojitá po částech** (měla **konečně** mnoho bodů nespojitosti).
![[media/szz-17/media/image35.png]]

![[media/szz-17/media/image51.png]]

### Postupy integrace

- **Metoda per partes**: využívá se pro integraci funkcí v součinovém tvaru dle vzorce (pro úspěšnou integraci velmi **záleží** **na** správném výběru **u** a **v**):
![[media/szz-17/media/image16.png]]

> Příklad integrace metodou per partes:
![[media/szz-17/media/image26.png]]

![[media/szz-17/media/image10.png]]

![[media/szz-17/media/image33.png]]

![[media/szz-17/media/image18.png]]

- **Substituční metoda**: Během integrování nahrazujeme část integrované funkce za jinou, provedeme integraci a vrátíme funkci zpět do původního tvaru. U **určitého** integrálu je **nutné přepočítat meze integrace**.
![[media/szz-17/media/image42.png]]

> Příklad integrace substituční metodou:
![[media/szz-17/media/image47.png]]

![[media/szz-17/media/image12.png]]

![[media/szz-17/media/image28.png]]

![[media/szz-17/media/image6.png]]

![[media/szz-17/media/image30.png]]

> Příklad integrace určitého integrálu:
![[media/szz-17/media/image34.png]]

![[media/szz-17/media/image15.png]]

### Integrace elementárních funkcí

Viz tabulka
![[media/szz-17/media/image22.png]]

## Více proměnných

Derivace i integrace více proměnných je založená na postupné derivaci/integraci podle jednotlivých proměnných.

### Parciální derivace

Parciální derivace funkce o **více proměnných** je její derivace vzhledem **k jedné** z těchto proměnných, přičemž s **ostatními** proměnnými se zachází jako s **konstantami**. **Většinou** platí: Pomocí parciálních derivací se např. určuje tečná rovina grafu dvou proměnných
![[media/szz-17/media/image41.png]]

![[media/szz-17/media/image3.png]]

### Gradient (parciálních derivací)

Jedná se o **vektor prvních parciálních derivací** dle **všech** proměnných funkce, který určuje směr **největšího růstu** funkce (respektive největšího poklesu, pokud jej vezmeme záporně). Délka vektoru gradientu je nárůst veličiny **f** na intervalu jednotkové délky.

Umožňuje vypočítat **derivaci** funkce více proměnných ve **směru nějakého vektoru**, viz [<u>19 - Gradient a jeho využití (MAT - Diferenciální počet funkcí více proměnných)</u>](https://youtu.be/wEItObA6Ozs). Směrová derivace se vypočítá jako skalární součin vektoru **u** (vektor udávající směr) a gradientu v bodě **A** (lze vyjádřit i obecně a poté dosadit libovolný bod). Gradient je kolmý na křivky (u funkcí 2 proměnných) a plochy (u funkcí 3 proměnných) o **stejné funkční hodnotě - hladiny funkce**. Jedná se např. o **vrstevnice** na mapách. V bodech, kde je gradient **nulový vektor**, se mohou nacházet **lokální extrémy** funkce více proměnných nebo **sedlové body**. Jedná se o stacionární body. Lokální **maximum** se v bodě nachází, pokud existuje i gradient druhé parciální derivace a jeho **hodnota je menší než 0**, respektive je zde lokální **minimum**, pokud je **hodnota větší než 0**.
![[media/szz-17/media/image48.png]]

![[media/szz-17/media/image23.png]]

Lze využít I Hessovu matici a Hessián (její determinant) viz: [<u>https://is.muni.cz/el/sci/jaro2021/C1471/um/extremy.pdf</u>](https://is.muni.cz/el/sci/jaro2021/C1471/um/extremy.pdf)
![[media/szz-17/media/image27.png]]

![[media/szz-17/media/image32.png]]

![[media/szz-17/media/image43.png]]

### Integrace více proměnných

U integrace více proměnných můžeme využít na základě vlastností integrované funkce a hranic integrování 3 různé postupy:

- Funkci lze rozdělit na **součin** funkcí jedné proměnné → dvojný/trojný integrál lze rozdělit na **součin jednoduchých** integrálů.
- Hranice, na kterých máme integrovat jsou známé pro všechny proměnné - **konstanty** (integrace na obdélníku, kvádru) → sestavení **dvojnásobného/trojnásobného** integrálu, na způsobu zanoření integrálů nezáleží, je nutné ale zachovat meze.
- Hranice jsou vyjádřeny **funkcí** zbylých **proměnných** (konstantou, poté funkcí jedné proměnné a u trojného integrálu funkcí dvou proměnných), zde již záleží i na způsobu zanoření integrálů - ten s hranicemi definovanými funkcí nejvíce proměnných musí být nejvíce vnořený.

### Dvojný integrál

Jedná se o integrál funkce **dvou proměnných**. Používá se např. pro výpočet **objemu**, výpočet **hmotnosti nehomogenní plochy**, výpočet **povrchu**. Při výpočtu se snažíme **dvojný** integrál převést **na integrál dvojnásobný**, tj. **dva jednoduché** integrály a integraci provádět postupně (Fubiniova věta). Hranicí vnitřního integrálu budou tvořit funkce.
![[media/szz-17/media/image50.png]]

![[media/szz-17/media/image19.png]]

### Trojný integrál

Jedná se o integrál funkce **tří proměnných**. Používá se např. pro výpočet **objemu** tělesa ohraničeného třemi křivkami, výpočet jeho **hmotnosti** na základě proměnlivé hustoty, **statické momenty**, aj.
![[media/szz-17/media/image4.png]]

![[media/szz-17/media/image2.png]]

Výpočet **trojného integrálu** opět provádíme jeho **převodem na trojnásobný** integrál.
![[media/szz-17/media/image7.png]]

### Příklady dvojného a trojného integrálu

- **dvojný integrál na obdelníku**:
![[media/szz-17/media/image1.png]]

![[media/szz-17/media/image37.png]]

- **dvojný integrál - Fubiniova věta**:
![[media/szz-17/media/image21.png]]

- **trojný integrál na kvádru**:
![[media/szz-17/media/image39.png]]

![[media/szz-17/media/image13.png]]

- **trojný integrál - Fubiniova věta**:
![[media/szz-17/media/image46.png]]

### Limity funkcí více proměnných

Limity funkcí více proměnných fungují na **podobném** principu jako limity funkce jedné proměnné. Limita funkce **existuje**, když hodnoty **libovolně malého okolí** bodu **spadají do ohraničeného pásu funkčních hodnot**. U funkce **dvou** proměnných bude okolím **kruh**, u tří proměnných **koule**. Limitu funkce více proměnných v bodě **p ∈ U** lze počítat pouze, pokud je tento bod **bodem** **hromadným** (X a Y na obr.) - bod, jehož **každé prstencové** okolí má s množinou **U neprázdný průnik**. Body, které toto nesplňují, jsou body **izolované** (Z na obr.) a v nich **limitu** funkce více proměnných počítat **nelze**.

- **Otevřená množina** - Neobsahuje žádný bod ze své hranice.
- **Uzavřená množina** - Obsahuje všechny body své hranice.
- **Vnitřní** **bod** - Bod uvnitř množiny.
- **Hraniční** **bod** - Bod na hranici množiny.
- **Hranice** **množiny** - Množina všech hraničních bodů.
![[media/szz-17/media/image14.png]]

![[media/szz-17/media/image44.png]]

## Další info

### L'Hôpitalovo pravidlo

Umožňuje v některých případech vypočítat limitu podílu dvou funkcí. Říká, že limita podílu dvou funkcí, které splňují jisté předpoklady, je rovna limitě podílu derivací těchto funkcí. Pokud potom
![[media/szz-17/media/image29.png]]

![[media/szz-17/media/image31.png]]

![[media/szz-17/media/image24.png]]

### Taylorova řada

Mocninná řada, vyjádřená jako **suma derivací funkce v bodě**. Pokud se jedná o rozvoj v **okolí bodu 0**, mluvíme o **Maclaurinově řadě**. **Taylorovy** a **Maclaurinovy řady** se využívají k **aproximaci funkcí**.
![[media/szz-17/media/image17.png]]

**Odkazy:**

- [<u>Neurcity integral</u>](http://user.mendelu.cz/marik/mat-web/mat-webse9.html)
- [<u>Integrace substitucí</u>](https://matematika.cz/integrace-substituci)
- [<u>Spojitost funkce</u>](https://kag.upol.cz/mat1/texty/ch08/kapitola8.pdf)
- [<u>Funkce více proměnných</u>](https://math.feld.cvut.cz/tiser/web2.pdf)
- [<u>VZORCE PRO INTEGROVÁNÍ</u>](http://www.matematika-lucerna.cz/graph/vzorce-integrovani.pdf)
- Derivace: [<u>Tabulky</u>](https://www.karlin.mff.cuni.cz/~rokyta/vyuka/general/tahaky/derivace.htm)

## Zdroje

- SZZ okruh 17 — studijní materiály FIT BUT (`szz-17.docx`). Obrázky a vzorce: `media/szz-17/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/16-mnoziny-relace-zobrazeni|16. Množiny, relace a zobrazení]] · další: [[okruhy/18-ciselne-soustavy|18. Číselné soustavy]] ▶
