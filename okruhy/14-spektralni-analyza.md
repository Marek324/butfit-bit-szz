---
title: "14. Spektrální analýza spojitých a diskrétních signálů"
category: okruh
okruh: 14
tags: [dsp, signals, fourier, math]
aliases: [signál, vzorkování, Nyquist, Fourierova řada, Fourierova transformace, DFT, DTFT, FFT]
relationships:
  - target: "[[okruhy/15-cislicove-filtry]]"
    type: related_to
sources: ["_sources/docx/szz-14.docx"]
summary: Spojité a diskrétní signály, vzorkování (Nyquist) a rozklad signálu do frekvenční oblasti — Fourierova řada, FT, DTFT, DFT a FFT a jejich vztahy.
provenance:
  extracted: 0.88
  inferred: 0.1
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 14. Spektrální analýza signálů

> SZZ okruh 14 (FIT BUT). **Signál** = fyzikální veličina nesoucí informaci. Spektrální analýza zjišťuje, **které frekvence**, s jakou **amplitudou** a **fází** signál tvoří.

## Shrnutí

## Druhy signálů

- **Spojitý (analogový)** x(t) — reálné hodnoty, souvislá křivka.
- **Diskrétní** x[n] — definovaný v celočíselných okamžicích.
- **Vzorkování** — vzorkovací frekvence musí být **≥ 2× nejvyšší frekvence** složky (**Nyquistův–Shannonův teorém**), jinak nelze signál rekonstruovat.
- **Kvantování** — diskretizace oboru hodnot; ztrátové a nevratné.
- Dále: deterministické × náhodné, periodické, **harmonické** (amplituda, úhlový kmitočet ω, počáteční fáze).

![[media/szz-14/media/image11.png]]
*Rozklad signálu do frekvenční oblasti — výsledkem je spektrum.*

## Fourierův rozklad

| Nástroj | Vstup | Výstup (frekvenční oblast) |
|---|---|---|
| **Fourierova řada (FŘ)** | spojitý periodický | diskrétní neperiodické koeficienty |
| **Diskrétní FŘ (DFŘ)** | diskrétní periodický | diskrétní periodické koeficienty |
| **Fourierova transformace (FT)** | spojitý (neperiodický) | spojitá neperiodická funkce |
| **DTFT** | diskrétní (neperiodický) | spojitá periodická funkce (perioda 2π) |
| **DFT** | N vzorků diskrétního | N komplexních koeficientů |

- **Pomůcka**: periodicita v čase ⇒ diskrétnost ve frekvenci; diskrétnost v čase ⇒ periodicita ve frekvenci.
- **DFT** je pro PC ideální (konečný počet vzorků i koeficientů), pracuje v **O(n²)**.
- **FFT** — rychlá DFT v **O(n·log n)**; jeden z nejpoužívanějších algoritmů (komprese JPEG/MP3, filtrace, **konvoluce** přes násobení ve frekvenční doméně).

> [!note] Ke kontrole
> Plné znění tvrdí, že FFT „lze počítat **pouze** pro počty vzorků = mocnina 2". To platí jen pro **radix-2** FFT (Cooley-Tukey). Obecně FFT existuje pro **libovolné N** (mixed-radix, Bluestein/chirp-z), jen je nejefektivnější pro vysoce složená N. Také pozn.: JPEG ve skutečnosti používá **DCT**, ne přímo FFT.

## Souvislosti

Spektrum je základem pro [[okruhy/15-cislicove-filtry|číslicové filtry]] (frekvenční charakteristika); matematicky navazuje na [[okruhy/17-diferencialni-integralni-pocet|integrální počet]].


## Související syntéza

- [[synthesis/fourier-konvoluce-filtry|Spektrální analýza × konvoluce × filtry]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Typy signálů a vzorkování** ↪ [[#Druhy signálů]]
- *Spojitý vs. diskrétní?* → Spojitý x(t) (reálné hodnoty), diskrétní x[n] (v celočíselných okamžicích); + deterministický/náhodný, periodický/neperiodický.
- *Vzorkovací teorém?* → f_vz ≥ 2× nejvyšší frekvence (Nyquist/Shannon); při porušení **aliasing** (přeložení spektra). Proto dolní propust před vzorkováním.

**Fourierova analýza** ↪ [[#Fourierův rozklad]]
- *FŘ vs. FT vs. DTFT vs. DFT?* → FŘ: spojitý periodický → diskrétní koeficienty; FT: spojitý → spojité spektrum; DTFT: diskrétní → spojité periodické; DFT: N vzorků → N koeficientů (vhodné pro PC).
- *Vztah čas–frekvence?* → Periodicita v čase ⇒ diskrétnost ve frekvenci a naopak.
- *FFT?* → Rychlá DFT, O(n·log n), n = mocnina 2; využití komprese (JPEG/MP3), filtrace, konvoluce.
- *Konvoluční teorém?* → Konvoluce v čase = násobení ve frekvenci (a naopak).

## Plné znění (ke studiu)

**Signál** je záměrný fyzikální jev nesoucí informaci o aktuální
události. Jedná se o časovou či prostorovou proměnnou prostředí
(**fyzikální veličinu)**.

### Spojitý (analogový) signál

Vyskytují se **v reálném světě** (například zvukové vlny), mají pro
každý časový okamžik určitou hodnotu, což tvoří souvislou (spojitou)
křivku. Lze je zapsat funkcí. Značíme je ***x(t)*** a hodnoty spojitého
signálu jsou z množiny **reálných čísel**.

### Diskrétní signál

Jeho okamžitá hodnota se s časem nemění spojitě, ale skokově. Lze je
ukládat a zpracovávat na **číslicových** počítačích. Značíme je
***x\[t\]*** a hodnoty diskrétních signálů jsou definovány pouze v
**celočíselných hodnotách**. Samotné hodnoty diskrétních signálů mohou
nabývat reálných hodnot. Pro získání diskrétních signálů **vzorkujeme**
signály kolem nás, které jsou spojité. Následně signály **kvantujeme** -
zaokrouhlujeme na čísla z oboru hodnot signálu (respektive na čísla,
která dokáže reprezentovat v PC).

- **Vzorkování:** Periodicky zaznamenáváme hodnotu spojitého signálu.
  Perioda zaznamenávání spojitého signálu musí být aspoň dvakrát menší,
  než nejmenší perioda některé ze složek spojitého signálu, neboli
  vzorkovací frekvence musí být minimálně dvakrát větší než největší
  frekvence některé ze složek signálu (**Nyquistův–Shannonův vzorkovací
  teorém**, jinak nelze signál rekonstruovat).\
  
![[media/szz-14/media/image19.png]]


- **Kvantování:** diskretizace oboru hodnot signálu (převod z reálných
  čísel na celá čísla). Je to obecně proces ztrátový a nevratný.\
  
![[media/szz-14/media/image14.png]]


### Deterministické signály 

Pro **každý spojitý čas** či **diskrétní čas** přesně víme, jakou
**hodnotu** bude signál **mít**. Lze je definovat funkcí.

### Náhodné signály

Nelze je popsat rovnicí. Pro část (t) nebo \[n\] **nikdy** přesně
**nevíme**, jaká bude jejich **hodnota**. Popisují se pomocí parametrů
jako **střední hodnota** nebo **rozptyl**.

### Periodické signály

Průběh signálu se opakuje s určitou periodou T: s(t) = s(t+T).

- **Harmonické signály:** Nejjednodušeji definované periodické signály o
  frekvenci, která je celočíselným kladným **násobkem** **základní
  frekvence** (nejmenší frekvence periodického signálu) nějakého
  periodického signálu, například sinusovky nebo cosinusovky. Mají tvar:
  
![[media/szz-14/media/image20.png]]
 (místo cos může být sin),
  kde

  - A - Amplituda. Maximální hodnota periodické funkce,

  - ω - úhlový nebo kruhový kmitočet, \[rad/s\] pro spojitý a \[rad\]
    pro diskrétní signál,

  - Ⲫ<sub>0</sub> - počáteční fáze \[rad\]. Posunutí funkce po ose x.

## Spektrální analýza

Spektrální analýzou signálů zjišťujeme jejich **frekvenční
charakteristiku** (zajímají nás):

- **kde** jsou frekvenční komponenty signálu (na jakých **frekvencích**
  se signál nachází),

- **kolik** je na které frekvenci signálu (**amplituda** na dané
  frekvenci) a

- jak je na které frekvenci signál **posunutý** (**fázový posun** na
  dané frekvenci).

**Rozklad** signálu na **sinusovky** a **cosinusovky**. Převod signálu z
časové do frekvenční oblasti. Výsledkem spektrální analýzy signálu je
**spektrum**. 
![[media/szz-14/media/image11.png]]


### Fourierova řada (Fourier Series)

Každý periodický signál lze vyjádřit jako součet sinusovek a
cosinusovek. **Frekvence** jednotlivých sinusovek a cosinusovek jsou
**celočíselným násobkem** frekvence **původního** signálu. **Fázi** a
**amplitudu** každé harmonické složky (sinusovky a cosinusovky) lze
získat **Furiérovým rozkladem** (výpočet koeficientů a<sub>n</sub> a
b<sub>n</sub>). Furierova řada tedy **umožňuje popsat původní periodický
signál součtem sinusovek a kosinusovek**.

Fourierova řada může být také zapsána jako součet komplexních
exponenciál.
![[media/szz-14/media/image5.png]]

![[media/szz-14/media/image10.png]]

![[media/szz-14/media/image16.png]]


- **Vstup**: **Spojitý periodický** signál
  (funkce).
![[media/szz-14/media/image8.png]]


- **Výstup:** Koeficienty určující **amplitudy** a **fáze** komplexních
  exponenciál na **násobcích** základní **frekvence** - jsou to tedy
  **diskrétní hodnoty**, ale neperiodické.

**FŘ** reprezentuje pořád ten **samý signál**, my ale z toho původního
potřebujeme znát právě jeho **koeficienty**, které nám o něm dávají
informace. Z **koeficientů** můžeme původní signál **znovu sestavit**
pomocí vzorce pro **FŘ**.

### Diskrétní Fourierova řada (Discrete Fourier Series)
![[media/szz-14/media/image1.png]]


**Diskrétní Fourierova řada je tvořena konečným počtem součtů sinusových
a kosinusových funkcí.** Jedná se o aproximaci FŘ (její zobecnění) pro
**diskrétní periodické** signály. **Signál musí** být stále
**periodický**. Umožňuje nám provádět výpočty v praxi, protože data na
počítačích nejsou **nikdy spojitá** a navíc nedokážeme provést nekonečné
množství součtů.

- **Vstup**: **Diskrétní periodický** signál s periodou **N**.

- **Výstup**: **Diskrétní periodické** koeficienty určující
  **amplitudy** a **fáze** komplexních exponenciál na **násobcích**
  základní **frekvence**, které se **periodicky** opakují s periodou
  **N**. Ideální pro zpracování v počítači, ale jen pro periodické
  signály…
![[media/szz-14/media/image23.png]]

![[media/szz-14/media/image3.png]]

![[media/szz-14/media/image22.png]]


### Fourierova transformace (Fourier Transform)

**Zobecnění** **FŘ** pro **neperiodické** signály. Slouží pro **převod**
(transformaci) signálů z **prostorové** nebo **časové** oblasti **do**
oblasti **frekvenční**. Umožňuje dekomponovat signál na **jednotlivé
frekvence**, které ho tvoří.

- **Vstup** - Obecný spojitý signál (**nemusí** být periodický).

- **Výstup** - je **spojitá funkce definovaná na celém intervalu (tedy
  řada komplexních čísel)**, z nichž každé **odpovídá frekvenci,
  amplitudě a fázi** ve výsledném **frekvenčním spektru**. (někdy lze
  využít pro získání koeficientů FŘ
  [<u>https://lpsa.swarthmore.edu/Fourier/Xforms/FXFS.html</u>](https://lpsa.swarthmore.edu/Fourier/Xforms/FXFS.html),
  pokud obsahuje **jednu periodu signálu a jinak 0** - lze ztotožnit se
  získáváním koeficientů FŘ). Problém: **Výstup je spojitý a
  neperiodický**, PC
  nezpracuje.
![[media/szz-14/media/image13.png]]

![[media/szz-14/media/image4.png]]

![[media/szz-14/media/image21.png]]


### Fourierova transformace s diskrétním časem - Discrete Time Fourier Transform

**Zobecňuje DFŘ** pro **neperiodické** signály. Slouží pro **převod**
(transformaci) signálů z **prostorové** nebo **časové** oblasti **do**
oblasti **frekvenční**. DTFT je **periodická** s periodou **2\*pi**.

- **Vstup**: Nekonečno vzorků obecného **diskrétního** signálu (nemusí
  být periodický).

- **Výstup**: **Spojitá periodická** funkce ve frekvenční oblasti, což
  stále není na PC použitelné. **Diskrétní** je pouze v případě
  **periodického** signálu.

### Diskrétní Fourierova transformace - Discrete Fourier Transform 
![[media/szz-14/media/image2.png]]


Slouží pro **převod** (transformaci) signálů z **prostorové** nebo
**časové** oblasti **do** oblasti **frekvenční**. **Vzorkuje výstup
DTFT** (Fourierova transformace s diskrétním časem), který je spojitý.
Pracuje s **kvadratickou O(n^2)** časovou složitostí.

- **Vstup**: **N vzorků** obecného neperiodického diskrétního signálu
  (DFT bere těchto N vzorků, jako by se periodicky opakovaly)

- **Výstup**: **N komplexních koeficientů** (komplexních exponenciál),
  které určují **amplitudy** a **fáze frekvence.** Pro PC tedy ideální
  situace.

### Fast Fourier Transform
![[media/szz-14/media/image6.png]]


Modifikace DFT, která je rychlejší: pracuje s **linearitmickou
O(n\*logn)** časovou složitostí. Lze počítat pouze pro **počty vzorků**,
které jsou rovny **mocnině 2** (2^n). Jedná se dnes o jeden z
**nejpoužívanějších algoritmů vůbec**. Např.:

- **Komprese** JPEG, MP3, …: Fungují na principu výpočtu FFT a následně
  **odstranění frekvencí**, které jsou zastoupeny **minimálně** - což je
  většina, třeba i **99%**. Jedná se o ztrátovou kompresi (nelze
  praktici rozeznat), ale **nezbytnou**.

- **derivace**

- **filtrace dat**: pomocí FFT nalezneme frekvence, které tvoří rušení a
  odstraníme je.

- **konvoluce**: pomocí FFT se převedou signály **do frekvenční
  domény**, **vynásobí** **se** a **převedou se zpět** pomocí IFFT
  (inverzní FFT). Běžná konvoluce je v **O(n^2)**, konvoluce pomocí FFT
  v **O(n\*logn)**.

### Pomůcka

Platí, že **periodicita v časové** doméně způsobuje **diskrétnost ve
frekvenční** doméně a **diskrétnost v časové** doméně způsobuje
**periodicitu ve frekvenční** doméně.

FŘ je **periodická spojitá** (v čase) → její koeficienty jsou
**diskrétní neperiodické** (ve frekvenci),

DFŘ je **periodická diskrétní** (v čase) → její koeficienty jsou
**diskrétní periodické** (ve frekvenci), perioda u obou je **stejná**.

FT je **neperiodická** **spojitá** (v čase) → koeficienty jsou vyjádřeny
**spojitou neperiodickou funkcí** (ve frekvenci),

DTFT je **neperiodická diskrétní** (v čase) → koeficienty jsou vyjádřeny
**spojitou periodickou funkcí** (ve frekvenci)

DFT je **pseudo-periodická diskrétní** (v čase) → koeficienty jsou
**diskrétní** **a periodické** (ve frekvenci), ale vždy je jich **stejný
počet jako v čase** (takže délka jedné periody - původního signálu).

Signály **pomalu** měnící se v čase budou mít **úzké** spektrum ve
frekvenci, signály **rychle** měnící se v čase budou mít **široké**
spektrum ve frekvenci

### Užitečné signály

- **několik cosinusovek**:

koeficienty získáme z převodního vzorečku (**půlka amplitudy a stejná,
resp. opačná fáze**)
![[media/szz-14/media/image12.png]]



![[media/szz-14/media/image9.png]]

![[media/szz-14/media/image15.png]]

![[media/szz-14/media/image7.png]]


- **Periodický obdelník:** Velikost impulsů bude D = 6, základní perioda
  T1 = 1 µs, šířka impulsu ϑ = 0.5 µs. ω = 2π/ϑ = 2π/(0.5×10−6) = 4π ×
  10−6 = 4Mπ. ω = 4Mπ.
![[media/szz-14/media/image17.png]]


- **Diracův impuls** δ(t): „Za 0 sekund (v nulovém čase) dokáže vyskočit
  do nekonečna a zase se vrátit
  zpět.“
![[media/szz-14/media/image24.png]]

![[media/szz-14/media/image18.png]]


**Frekvence**

- **Normální nenormovaná frekvence** - f \[Hz\]

- **Normální normovaná frekvence** - f / Fs \[-\]

- **Kruhová nenormovaná frekvence** - ω = 2\*pi\*f \[rad/s\]

- **Kruhová normovaná frekvence** - (2\*pi\*f)/Fs \[rad\]

**Videa:**

[<u>But what is the Fourier Transform? A visual
introduction.</u>](https://youtu.be/spUNpyF58BY)

[<u>How are the Fourier Series, Fourier Transform, DTFT, DFT, FFT, LT
and ZT Related?</u>](https://youtu.be/2kMSLqAbLj4)

[<u>The Discrete Fourier Transform
(DFT)</u>](https://youtu.be/nl9TZanwbBk)

[<u>Image Compression and the FFT</u>](https://youtu.be/gGEBUdM0PVc)

[<u>3 Applications of the (Fast) Fourier Transform (ft. Michael
Kapralov)</u>](https://youtu.be/aqa6vyGSdos)

## Zdroje

- SZZ okruh 14 — studijní materiály FIT BUT (`szz-14.docx`). Další obrázky: `media/szz-14/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/13-graficka-uzivatelska-rozhrani|13. Grafická uživatelská rozhraní]] · další: [[okruhy/15-cislicove-filtry|15. Číslicové filtry]] ▶
