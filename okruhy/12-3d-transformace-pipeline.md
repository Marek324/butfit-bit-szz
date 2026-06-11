---
title: "12. Transformace a zobrazení 3D polygonálních modelů, principy programovatelného vykreslovacího řetězce"
category: okruh
okruh: 12
tags: [computer-graphics, math]
aliases: [homogenní souřadnice, afinní transformace, projekce, ray tracing, radiozita, vertex shader, fragment shader, rendering pipeline]
relationships:
  - target: "[[okruhy/11-2d-vektorova-grafika]]"
    type: related_to
sources: ["_sources/docx/szz-12.docx"]
summary: Geometrické transformace 3D modelů přes homogenní souřadnice, projekce (paralelní/perspektivní), realistické zobrazení (ray tracing, radiozita) a programovatelná zobrazovací pipeline.
provenance:
  extracted: 0.9
  inferred: 0.08
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 12. 3D transformace a vykreslovací řetězec

> SZZ okruh 12 (FIT BUT). Transformace = změna pozice vrcholů nebo souřadnicového systému.

## Shrnutí

## Transformace

- **Lineární** (zachovává lineární kombinaci i **počátek**): měřítko, rotace, zkosení, zrcadlení.
- **Afinní** (zachovává kolinearitu, dělicí poměr i rovnoběžnost): + posunutí; lineární následovaná posunem.
- **Homogenní souřadnice** — přidaná váha **w** (u afinních w = 1) → jednotný **maticový zápis** všech transformací, snadné **skládání** a perspektivní projekce.
- Skládání závisí na pořadí; první transformace musí být **nejblíže** transformovanému bodu.

## Projekce

- **Paralelní (ortografická)** — zachovává rovnoběžnost, vzdálenost neovlivní velikost; CAD.
- **Perspektivní (středová)** — paprsky se sbíhají do středu projekce, vzdálenost zmenšuje objekt; hry, VR. Kamera se obvykle zafixuje do počátku a hýbe se scénou.

## Realistické zobrazení

- **Ray tracing** — zpětné sledování paprsku od kamery; primární, stínové, sekundární paprsky; výpočetně náročné, závisí na poloze kamery.
- **Radiozita** — globální osvětlení, šíření energie mezi ploškami (BRDF, konfigurační faktory); **nezávisí** na poloze kamery; lze kombinovat s ray tracingem.

## Programovatelná zobrazovací pipeline

1. **Vertex Assembly** — sestavení atributů vrcholů (stride, offset).
2. **Vertex Shader** (programovatelný) — model × view × projekční matice (model space → clip space).
3. **Primitive Assembly** — sestavení trojúhelníků ze 3 vrcholů.
4. **Clipping/Culling** — ořez na view frustum, zahození neviditelných.
5. **Perspective Division** — z homogenních na kartézské podle hloubky.
6. **Viewport Transformation** — NDC (−1,+1) → rozlišení okna.
7. **Rasterization** — produkuje **fragmenty**.
8. **Fragment Shader** (programovatelný) — obarvení/textura, interpolace přes **barycentrické souřadnice**.
9. **Per-Fragment Operations** — **hloubkový test** (z-buffer) a **blending** (např. alpha).

![[media/szz-12/media/image4.png]]
*Programovatelný vykreslovací řetězec (rendering pipeline).*

## Souvislosti

Rasterizace trojúhelníků navazuje na [[okruhy/11-2d-vektorova-grafika|2D rasterizaci]]; prvky GUI staví na této pipeline viz [[okruhy/13-graficka-uzivatelska-rozhrani]]; matice a vektory řeší lineární algebra.


## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Vykreslovací řetězec** ↪ [[#Programovatelná zobrazovací pipeline]]
- *Části pipeline?* → vertex assembly → vertex shader → primitive assembly → clipping → perspective division → viewport → rasterizace → fragment shader → per-fragment (depth test, blending).

**Homogenní souřadnice** ↪ [[#Transformace]]
- *Co a proč?* → Kartézské souřadnice + váha w; umožní vyjádřit i posun maticí a skládat transformace násobením; u bodů w = 1.
- *Skládání transformací?* → Násobení matic; záleží na pořadí (nekomutativní), první transformace nejblíž bodu (např. rotace kolem bodu = posun → rotace → posun zpět).
- *Lineární vs. afinní?* → Lineární zachovává sčítání a násobení skalárem (měřítko, rotace, zkosení); posun není lineární → afinní (proto homogenní souřadnice).

**Projekce a reprezentace** ↪ [[#Projekce]]
- *Paralelní vs. perspektivní?* → Paralelní zachovává rovnoběžnost, velikost nezávisí na vzdálenosti (CAD); perspektivní sbíhá do středu, vzdálené se zmenšuje (hry, VR).
- *Proč polygony (trojúhelníky)?* → Vždy konvexní, efektivní v HW; alternativy CSG, voxely.

## Plné znění (ke studiu)

## Geometrická transformace

**změna** pozice **vrcholů** objektů v **aktuálním**
souřadnicovém systému nebo **změna** **souřadnicového** systému

### Lineární transformace

Lineární transformace **zachovává lineární kombinaci** — vektory lze aplikovat
**zároveň nebo po jednom** a výsledek je vždy stejný. Pro libovolné dva vektory
a skalár platí:

$$f(\vec{x}_1+\vec{x}_2) = f(\vec{x}_1)+f(\vec{x}_2), \qquad f(\alpha\,\vec{x}_1) = \alpha\,f(\vec{x}_1).$$

Důsledek: lineární transformace **vždy zachovává počátek** ($f(\vec{0})=\vec{0}$).
Patří sem **měřítko** (zvětšení, zmenšení), **rotace**, **zkosení** a **zrcadlení**.
**Posunutí (translace) lineární není** — posunulo by počátek — proto se zavádějí
homogenní souřadnice.

### Afinní transformace

Afinní transformace = **lineární následovaná posunutím**, $f(\vec{x})=A\vec{x}+\vec{b}$.
Zachovává **kolinearitu a dělící poměr** (body ležící na přímce zůstanou na přímce
a poměr jejich vzdáleností se nezmění), dále **rovnoběžnost** a **konvexnost**.
Obecně nezachovává délky ani úhly (zkosení a nestejnoměrné měřítko je deformují,
přímku ale nechají přímkou). Všechny základní geometrické operace (**měřítko Sc**,
**rotace R**, **zkosení Sh** i **posunutí T**) jsou afinní. Každá lineární
transformace je současně afinní (s $\vec{b}=\vec{0}$); afinní množina je striktně
větší.

> [!note] Proč afinní zachovává kolinearitu
> Přímku zapíšeme parametricky jako $P + t\,\vec{d}$ (bod + skalár × směr) a dosadíme do $f(\vec{x})=A\vec{x}+\vec{b}$:
> $$f(P+t\vec{d}) = A(P+t\vec{d})+\vec{b} = (AP+\vec{b}) + t\,(A\vec{d}) = f(P) + t\,(A\vec{d}),$$
> což je opět **bod + $t\cdot$ směr**, tedy přímka (pokud $A\vec{d}\neq\vec{0}$). Projektivní (perspektivní) transformace přímky na přímky také zobrazí, ale poruší rovnoběžnost a poměry (rovnoběžky se protnou v úběžníku); nelineární zkreslení (např. zkreslení objektivu) přímky ohýbá na křivky — afinní už není.

### Homogenní souřadnice (váha)

Ke standardním **kartézským** souřadnicím (x, y ve 2D, x, y, z ve 3D) se přidá
souřadnice **w** (váha bodu, u **afinních je w = 1**). Umožňují pracovat se
**všemi** základními **transformacemi** jednotně pomocí **maticového zápisu**.

**Tři důvody použití** (přibližně dle důležitosti):

1. **Posunutí jako násobení maticí.** Posunutí je afinní, ne lineární, takže běžnou
   $n\times n$ maticí ho jako násobení nevyjádříme. Přidáním jedné dimenze se
   přičtení $\vec{b}$ "schová" do matice — pak je *každá* afinní transformace jediné
   maticové násobení.

2. **Jednotné skládání.** Když je vše "násobení maticí", celý řetězec složíme
   vynásobením matic do jediné. Tu předpočítáme jednou a aplikujeme na tisíce
   vrcholů (bez homogenních souřadnic by se střídalo násobení s přičítáním a nešlo
   by to sloučit do jediné operace).

3. **Perspektiva a body v nekonečnu.** Souřadnice $w$ není vždy 1: perspektivní
   projekce zapisuje nenulové hodnoty do spodního řádku a **perspektivní dělení**
   (dělení $w$) zmenšuje vzdálené objekty. $w$ navíc odlišuje **body** ($w=1$) od
   **směrů/vektorů** ($w=0$); $w=0$ reprezentuje bod v nekonečnu (úběžník).

Důvody 1–2 jsou pohodlí a jednotnost, důvod 3 je skutečná nová schopnost.

#### Maticový zápis základních transformací

Níže ve **sloupcové konvenci** (bod jako sloupec, matice vlevo): $P' = M\cdot P$.

- **Posunutí** (translace), 2D — posun je v posledním sloupci; inverze neguje $d_x, d_y$:

$$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}1&0&d_x\\0&1&d_y\\0&0&1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix},\qquad T^{-1}=\begin{bmatrix}1&0&-d_x\\0&1&-d_y\\0&0&1\end{bmatrix}.$$

  Ve **3D** stačí matici rozšířit o řádek a sloupec s $d_z$ (resp. $-d_z$):

$$T_{3D}=\begin{bmatrix}1&0&0&d_x\\0&1&0&d_y\\0&0&1&d_z\\0&0&0&1\end{bmatrix}.$$

- **Změna měřítka** (scale), $P'=P\cdot S$; ve 3D přibude $S_z$ (inverze $1/S_z$):

$$S=\begin{bmatrix}S_x&0&0\\0&S_y&0\\0&0&1\end{bmatrix},\qquad S^{-1}=\begin{bmatrix}1/S_x&0&0\\0&1/S_y&0\\0&0&1\end{bmatrix}.$$

- **Zkosení** (shear): **1** matice ve **2D**, **3** matice ve **3D** (směry YZ, XZ, XY):

$$S_H=\begin{bmatrix}1&S_{hx}&0\\S_{hy}&1&0\\0&0&1\end{bmatrix},\qquad S_H^{-1}=\begin{bmatrix}1&-S_{hx}&0\\-S_{hy}&1&0\\0&0&1\end{bmatrix}.$$

$$S_{HYZ}=\begin{bmatrix}1&0&0&0\\S_{hy}&1&0&0\\S_{hz}&0&1&0\\0&0&0&1\end{bmatrix},\quad S_{HXZ}=\begin{bmatrix}1&S_{hx}&0&0\\0&1&0&0\\0&S_{hz}&1&0\\0&0&0&1\end{bmatrix},\quad S_{HXY}=\begin{bmatrix}1&0&S_{hx}&0\\0&1&S_{hy}&0\\0&0&1&0\\0&0&0&1\end{bmatrix}.$$

- **Rotace kolem počátku**, 2D — $P'=R\cdot P$ (inverze = rotace o $-\alpha$, tj. transpozice):

$$R=\begin{bmatrix}\cos\alpha&-\sin\alpha&0\\\sin\alpha&\cos\alpha&0\\0&0&1\end{bmatrix},\qquad R^{-1}=\begin{bmatrix}\cos\alpha&\sin\alpha&0\\-\sin\alpha&\cos\alpha&0\\0&0&1\end{bmatrix}.$$

  Ve **3D** jsou **3 matice** (rotace kolem os X, Y, Z):

$$R_x=\begin{bmatrix}1&0&0&0\\0&\cos\alpha&-\sin\alpha&0\\0&\sin\alpha&\cos\alpha&0\\0&0&0&1\end{bmatrix},\quad R_y=\begin{bmatrix}\cos\alpha&0&\sin\alpha&0\\0&1&0&0\\-\sin\alpha&0&\cos\alpha&0\\0&0&0&1\end{bmatrix},\quad R_z=\begin{bmatrix}\cos\alpha&-\sin\alpha&0&0\\\sin\alpha&\cos\alpha&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}.$$

> [!note] Proč má $R_y$ obrácená znaménka sinů
> Všechny tři rotace točí **proti směru hodinových ručiček při pohledu z kladné poloosy** (pravidlo pravé ruky) a každá pracuje v rovině zbývajících dvou os v pořadí cyklu $x\to y\to z\to x$. $R_x$ (rovina y,z) i $R_z$ (rovina x,y) mají osy v matici ve stejném pořadí jako cyklus, kdežto $R_y$ má pořadí $z\to x$ obrácené — blok 2×2 se proto vloží "transponovaně" a znaménka u sinů se prohodí. Tím $R_y$ zůstává správnou pravotočivou rotací. (Ve **řádkové** konvenci $P'=P\cdot M$ jsou všechny matice transpozicí zde uvedených.)

- **Rotace ve 3D kolem obecné osy** (dané směrovým vektorem $\vec{v}$ a bodem $P$) se rozloží na posloupnost:

  1. posunutí osy rotace do počátku souřadného systému,
  2. sklopení posunuté osy do jedné ze souřadných rovin,
  3. otočení sklopené osy do jedné ze souřadných os (např. X),
  4. provedení požadované rotace o úhel ω kolem této osy (zde X),
  5. vrácení osy rotace do původní polohy.

  Souhrnná matice:

$$M = T\cdot R_x\cdot R_z\cdot R_{x(\omega)}\cdot R_z^{-1}\cdot R_x^{-1}\cdot T^{-1}.$$

  Zkráceně: **obecnou osu dostat do pozice jedné z os**, provést otočení a vrátit osu na původní místo.

### Skládání transformací

U skládání závisí na **pořadí** (násobení matic je asociativní, ale
**nekomutativní**; ani rotace mezi sebou nekomutují, $R_x R_y \neq R_y R_x$).
Souhrnnou matici $M$ předpočítáme jednou a každý vrchol je pak jediné násobení.

- **zápis bodu ve sloupci** (sloupcová konvence): $P' = T\cdot R\cdot S\cdot P$, matici $M = T\cdot R\cdot S$; aplikuje se **zprava doleva**, tj. nejprve $S$ (nejblíž bodu).
- **zápis bodu v řádku** (řádková konvence): $P' = P\cdot S\cdot R\cdot T$, matici $M = S\cdot R\cdot T$; aplikuje se **zleva doprava**, opět nejprve $S$.

V obou případech musí být **první transformace v pořadí nejblíž transformovanému
bodu**. Typicky **měřítko → rotace → posunutí**: objekt nejdřív zvětšíme a otočíme
kolem vlastního počátku a teprve pak posuneme na místo (posunutí jako první by
rotaci provedlo kolem počátku světa).

> [!note] Řádkové vs. sloupcové vektory
> Jde o **dvě konvence téhož**: řádkové vektory ($P'=P\cdot M$, matice vpravo) vs. sloupcové ($P'=M\cdot P$, matice vlevo — standard v matematice a OpenGL). Matice jedné konvence jsou **transpozicí** druhé ($M_{\text{sloupec}} = M_{\text{řádek}}^{\mathsf{T}}$), proto se i pořadí ve skládání obrací ($(AB)^{\mathsf{T}}=B^{\mathsf{T}}A^{\mathsf{T}}$). Pozor: konvence vektoru **není totéž** co řádkové/sloupcové uložení v paměti (row-/column-major) — to jsou nezávislé volby (OpenGL: sloupcové vektory + column-major; DirectX tradičně: řádkové vektory + row-major, obě volby se "vyruší").

## Zobrazení 3D polygonálních modelů

Zobrazení **3D** objektů provádíme většinou na **2D**
obrazovku **projekcí** (transformací z 3D do 2D, to znamená ztrátu dat),
obrazovka je tedy **průmětna**. Promítání provádíme pomocí paprsků, tzv.
**projekčních paprsků**. V počítačové grafice se většinou rasterizují
všechny objekty **pomocí trojúhelníku** (konvexnost, lze dobře
akcelerovat v HW).

### Prvky 3D scény

- **near clip plane**: určuje minimální hloubku
  zobrazovaných objektů,

- **far clip plane**: udává maximální hloubku
  zobrazovaných objektů,
![[media/szz-12/media/image12.png]]


- **viewing frustum**: prostor v modelovaném
  prostředí, který se objeví na obrazovce,

- **viewpoint:** místo, ze kterého scénu pozorujeme
  (kamera)

- **světlo**: bodové nebo plošné, umístění rozhoduje
  o viditelnosti objektů (barvy, stíny, …),

- **modelované objekty**.


![[media/szz-12/media/image10.png]]


### Paralelní projekce (**rovnoběžná**, ortografická)
- **zachovává rovnoběžnost hran**
- **vzdálenost** průmětny **neovlivňuje**
  **velikost** průmětu (při změně vzdálenosti objektu se nemění jeho
  velikost)
- **kolmé promítání** - paprsky jsou **kolmé na
  průmětnu**
- použití: technické **CAD** aplikace, výkresová
  dokumentace

**Ortografická matice** (kolmé promítání do roviny $z=0$, sloupcová konvence
$P'=M\cdot P$) jen zahodí hloubku $z$ a ponechá $w=1$ — proto velikost na
vzdálenosti nezávisí (žádné dělení $w$):

$$\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&0\\0&0&0&1\end{bmatrix}\cdot\begin{bmatrix}x\\y\\z\\1\end{bmatrix}=\begin{bmatrix}x\\y\\0\\1\end{bmatrix}.$$

Je to **afinní** (lineární) transformace — spodní řádek zůstává $[0\;0\;0\;1]$,
na rozdíl od perspektivní matice níže.
![[media/szz-12/media/image9.png]]

### Perspektivní projekce (**středová**)
- **nezachovává** **rovnoběžnost** hran
- použití ve **hrách**, **VR** a jinde
- **vzdálenost průmětny** od objektu **ovlivňuje
  velikost průmětu** (se vzdáleností objektu se objekt zmenšuje)
- nelineární středová projekce: paprsky **vycházejí z
  1 bodu** - **středu projekce**
- pro jednodušší manipulaci se **kamera** obvykle
  **zafixuje** do počátku souřadného systému a **hýbe** se (pomocí
  transformačních matic) se **scénou**.
  - **Geometrický princip projekce**: z vrcholů
    trojúhelníku se do středu projekce (tj. střed souřadného systému,
    kam je umístěna i kamera) vrhnou paprsky (u perspektivní projekce se
    všechny paprsky sbíhají do středu projekce). V tom místě, kde
    paprsek protnul projekční rovinu, se promítne bod, ze kterého
    paprsek původně
    vyšel.
![[media/szz-12/media/image5.png]]

**Perspektivní matice** (promítnutí na rovinu $z=d$, střed projekce v počátku;
sloupcová konvence $P'=M\cdot P$) zapisuje do spodního řádku, čímž $w$ závisí na
hloubce:

$$\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1/d&0\end{bmatrix}\cdot\begin{bmatrix}x\\y\\z\\1\end{bmatrix}=\begin{bmatrix}x\\y\\z\\z/d\end{bmatrix}\;\xrightarrow{\text{/ }w}\;\left(\frac{dx}{z},\,\frac{dy}{z}\right).$$

Je to jediná **projektivní (neafinní)** matice — má nenulový spodní řádek. Až
**perspektivní dělení** souřadnicí $w=z/d$ zajistí, že se vzdálené objekty zmenší.


### RayTracing

Metoda pro realistické zobrazování. Funguje na
principu zpětného sledování cest paprsku od kamery ke zdroji světla.
Hledá se množství světla, které paprsek přináší.

Paprsky dělíme na:

- **Primární**: Vychází z kamery, mají společný
  počátek nebo jsou rovnoběžné

- **Stínové**: Z místa dopadu paprsku do každého
  světla, zajímá nás, jestli jej **vidíme nebo nevidíme**, podle toho
  následně spočítáme **stín**.

- **Sekundární**: Vznikají **odrazem a lomem** z míst
  **dopadů primárních** a sekundárních paprsků. Jsou chaotičtější než
  primární paprsky.

Výpočetně je RayTracing velmi náročný, lze
optimalizovat například ohledem na to, že **sekundární** paprsky mají
**menší vliv** na výsledný obraz, **intenzita světla** se snižuje se
**čtvercem** vzdálenosti, **snížit rozlišení**. Výpočet scény je
**závislý na poloze kamery**.

### Radiozita

Metoda **globálního osvětlení scény**. Řeší **šíření
energie**, objekty mohou být sekundárními zdroji světla (odraz).

- Vychází ze zákona zachování energie, vyžaduje
  energeticky uzavřenou scénu.

- Scéna musí být reprezentovaná **polygonálním
  modelem** (jiné modely - CSG, B-rep, Drátové modely).

- Vychází z dvousměrové distribuční **funkce
  BRDF**.

- Před vlastním výpočtem je třeba **polygony** ve
  scéně **rozdělit** na **malé plošky** a spočítat **konfigurační
  faktory** (**vliv** každé **plošky** na každou **jinou plošku** ve
  scéně).

- Nedokáže pracovat s průhlednými objekty.

- Výpočet scény **není závislý na poloze
  kamery**.

- V praxi lze **kombinovat s RayTracing**.

## Principy programovatelného vykreslovacího řetězce (zobrazovací pipeline)

zobrazovací pipeline je tvořena těmito částmi:

1.  **Vertex Assembly (Vertex Puller)**: je zařízení
    na grafické kartě, které se stará o **sestavení vrcholů**. Vertex
    puller je tvořen **čtecími hlavami**, každá konstruuje jeden atribut
    vrcholu (pozice, normála, souřadnice textury, barva, …). Čtecí hlavy
    se pohybují s krokem (**stride**) a mají nějaký posun (**offset**).
    Data čtou z pole bytů.

2.  **Vertex Shader** (programovatelný): Provádí
    zpracování vrcholů z Vertex Assembly. Jedná se o násobení
    **modelovou maticí**, **view maticí** a **projekční maticí**.
    Vstupem jsou vrcholy v **model space**, výstupem vrcholy v **clip
    space**.

3.  **Primitive Assembly**: je jednotka, která
    sestavuje trojúhelníky. **Čeká na 3** po sobě jdoucí **vrcholy** z
    vertex shaderu a **sestaví trojúhelník**. Lze na to také nahlížet
    tak, že Primitive Assembly dostane příkaz vykreslit třeba 4
    trojúhelníky. Jednotka tak spustí Vertex Shader 12x, který takto
    spustí 12x Vertex Assembly.

4.  **Clipping/Culling**: provádí **ořez prostoru**
    na view frustum. Trojúhelníky na **hranicích** musí ořezat (může
    vést na rozdělení na 2) a zahazuje trojúhelníky, které nejsou vůbec
    vidět (odvrácené, překryté).

5.  **Perspective Division**: provádí převod z
    homogenních souřadnic na kartézskéch na základě hloubky trojúhelníků
    (dělením - co je daleko se zmenší více, co je blízko se zmenší
    méně).

6.  **Viewport Transformation**: Převádí souřadnice z
    NDC (normalized device coordinates, **-1, +1**) na rozlišení okna,
    aby se mohla provést rasterizace.

7.  **Rasterization**: rasterizuje připravené
    trojúhelníky a produkuje **fragmenty** (čtvercové úlomky
    trojúhelníku - **pixely**, které se nakonec **zapíší** do
    **framebufferu**).

8.  **Fragment Shader** (programovatelný): **obarvuje
    fragmenty** (aplikuje textury na fragmenty) uvnitř trojúhelníka
    (střed pixelu musí ležet uvnitř). Pro konkrétní fragment (pixel)
    trojúhelníku se spočítají **barycentrické souřadnice** a použijí se
    pro **interpolaci** všech atributů z **vrcholů**.

9.  **Per-Fragment Operations**: jedná se o dvě
    operace: **hloubkový test** a **blending** (a další testy a
    operace).

    - **Hloubkový test** (depth test) se stará o
      **zahazování fragmentů**, které jsou **hlouběji** než to, co už se
      **vyrasterizovalo, naopak** pokud je **hloubka** nového fragment
      **menší,** je jeho **barva a hloubka zapsána do
      framebufferu**.

    - **Blending** místo přepsání barvy ve
      framebufferu je míchá. Existuje mnoho způsobů realizace, např.
      pomocí **průhlednosti** (**alpha blending**).

Obsah framebufferu je poté
zobrazen.
![[media/szz-12/media/image4.png]]


> 
![[media/szz-12/media/image1.png]]
 style="width:6.25in;height:2.17708in" />

## Jiná reprezentace objektů

- **CSG** (Constructive solid geometry) - skládání jednoduchých 3D
  primitiv (koule, krychle, kvádry, válce, …).

- Pomocí objemových jednotek - **voxely** (analogie pixelu ve 3D).

- **Implicitní plochy** - potenciální pole kolem nějaké kostry.

## Zdroje

- SZZ okruh 12 — studijní materiály FIT BUT (`szz-12.docx`). Další obrázky: `media/szz-12/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/11-2d-vektorova-grafika|11. 2D vektorová grafika]] · další: [[okruhy/13-graficka-uzivatelska-rozhrani|13. Grafická uživatelská rozhraní]] ▶
