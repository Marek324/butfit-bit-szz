---
title: "15. Číslicové filtry (diferenční rovnice, impulsní odezva, přenosová funkce, frekvenční charakteristika)"
category: okruh
okruh: 15
tags: [dsp, signals, fourier, math]
aliases: [diferenční rovnice, impulsní odezva, konvoluce, FIR, IIR, přenosová funkce, Z-transformace, frekvenční charakteristika, LTI]
relationships:
  - target: "[[okruhy/14-spektralni-analyza]]"
    type: uses
sources: ["_sources/docx/szz-15.docx"]
summary: LTI systémy popsané diferenční rovnicí, impulsní odezvou a přenosovou funkcí; FIR vs. IIR filtry a frekvenční charakteristika (dolní/horní propusť).
provenance:
  extracted: 0.87
  inferred: 0.1
  ambiguous: 0.03
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T15:10:00Z
updated: 2026-06-03T15:40:00Z
---

# 15. Číslicové filtry

> SZZ okruh 15 (FIT BUT). **Filtr** = lineárně časově invariantní (**LTI**) systém, který upravuje signál ve frekvenční oblasti.

## Shrnutí

## Diferenční rovnice

- Diskrétní obdoba diferenciální rovnice; popisuje **LTI systém** (vyžaduje **linearitu** a **časovou invariantnost**).
- Výstup y[n] dán kombinací aktuálních/minulých vstupů a (u rekurzivních) minulých výstupů.
- Příklady: průměr posledních vstupů ≈ dolní propusť, rozdíl ≈ horní propusť.

## Impulsní odezva a konvoluce

- **Impulsní odezva h[n]** — výstup LTI systému na jednotkový impuls; **plně definuje** systém (impuls obsahuje všechny frekvence, ve frekvenční doméně roven 1).
- Libovolný signál = vážený součet posunutých impulsů.
- **Konvoluce** — výstup = konvoluce vstupu s impulsní odezvou; v časové doméně $O(n²)$, ve frekvenční doméně jen **násobení** (viz [[okruhy/14-spektralni-analyza|FFT]]).
- **FIR** — konečná impulsní odezva, **bez rekurze** (zpětné smyčky).
- **IIR** — nekonečná odezva, **min. jedna rekurze**.

![[media/szz-15/media/image21.png]]
*Realizace IIR filtru se zpětnou vazbou (rekurzí).*

## Přenosová funkce a frekvenční charakteristika

- **Přenosová funkce H(z)** = poměr výstupu Y(z) ku vstupu X(z) ve frekvenční oblasti (při nulových počátečních podmínkách); rovná se DTFT/Z-transformaci impulsní odezvy.
- **Z-transformace** — x[n−k] → X(z)·$z^{-k}$; umožní určit **nuly** (z čitatele) a **póly** (ze jmenovatele); **Region of Convergence** určuje stabilitu.

> [!note] Ke kontrole
> Plné znění na jednom místě píše, že „přenosovou funkci lze získat z impulsní odezvy pomocí **Laplaceovy** transformace". Pro **diskrétní** (číslicové) filtry je to **Z-transformace** (Laplaceova transformace patří ke **spojitým** systémům) — zbytek okruhu správně používá Z-transformaci, takže jde o vnitřní nekonzistenci.
- **Frekvenční charakteristika** — přenosová funkce pro z = $e^{jω}$ (DTFT); **amplitudová** |H(ω)| a **fázová** arg(H(ω)).
- Typy: **dolní propusť**, **horní propusť**, **pásmová propusť**, **pásmová zádrž**.

![[media/szz-15/media/image38.png]]
*Frekvenční charakteristika filtru — amplitudová, fázová a skupinové zpoždění.*

## Souvislosti

Frekvenční analýza staví na [[okruhy/14-spektralni-analyza|Fourierově transformaci]]; rekurzivní struktury implementují zpožďovací články (klopné obvody, [[okruhy/03-sekvencni-logicke-obvody]]).

## Související syntéza

- [[synthesis/fourier-konvoluce-filtry|Spektrální analýza × konvoluce × filtry]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Diferenční rovnice** ↪ [[#Diferenční rovnice]]
- *Obecný tvar, FIR vs. IIR?* → y[n] dáno kombinací vstupů (a u IIR i minulých výstupů). FIR = bez zpětné vazby (konečná odezva), IIR = se zpětnou vazbou/rekurzí (nekonečná odezva).

**Přenosová funkce** ↪ [[#Přenosová funkce a frekvenční charakteristika]]
- *Co je H(z)?* → H(z) = Y(z)/X(z) ze Z-transformace diferenční rovnice; nuly z čitatele, póly ze jmenovatele.
- *Stabilita?* → Všechny póly uvnitř jednotkové kružnice.

**Impulsní odezva** ↪ [[#Impulsní odezva a konvoluce]]
- *Co to je, vztah ke konvoluci?* → Odezva systému na jednotkový impuls; plně definuje LTI systém; výstup = konvoluce vstupu s impulsní odezvou h[n].

**Frekvenční charakteristika a typy filtrů** ↪ [[#Přenosová funkce a frekvenční charakteristika]]
- *Jak ji získat?* → Fourierova transformace impulsní odezvy (H(z) pro z = $e^{jω}$); amplitudová |H(ω)| a fázová charakteristika.
- *Typy filtrů?* → dolní propust, horní propust, pásmová propust, pásmová zádrž.

**Blokové schéma** ↪ [[#Impulsní odezva a konvoluce]]
- *Jak poznat FIR/IIR ze schématu?* → Zpětnovazební smyčka (z⁻¹ z výstupu) = IIR; jen dopředné větve = FIR.

## Plné znění (ke studiu)

## Diferenční rovnice

Diferenční rovnice představují **rovnice o neznámé posloupnosti a jejích diferencích**. Jedná se o **diferenciální rovnice**, které jsou **v diskrétním čase**. Obecná diferenční rovnice vypadá následovně:
![[media/szz-15/media/image36.png]]

Diferenční rovnice stejně jako diferenciální vyžadují počáteční podmínky. Pomocí diferenčních rovnic můžeme popisovat LTI (Linear time-invariant) systémy.

- **linearita**: musí platit aditivita a scaling nebo homogenita:
![[media/szz-15/media/image15.png]]

- **časová invariantnost**: systém **nemění** své **chování v čase**. Pokud systém zareagoval na signál **x** výstupem **y**, zareaguje na stejný signál **x** za deset sekund stejným signálem **y**.

Příklad popisu systému:

- aktuální výstup **y\[n\]** je dán součtem minulého výstupu **1/2y\[n-1\]**, aktuálního vstupu **1/4x\[n\]** a minulého vstupu **1/4x\[n-1\]**.
![[media/szz-15/media/image4.png]]

- Schéma jiného systému daného **diferenční** rovnicí **y\[n\] = 4\*(x\[n\] + 1/6y\[n-1\] + 1/6y\[n-2\])** (POZOR: Zpožďovací články by měly být napojené až za násobičkou, u y\[n\]. V obrázku je tedy chyba. Modrou čarou je naznačeno správné řešení.)
![[media/szz-15/media/image6.png]]

Příklady systémů, které se chovají jako dolní propusť (propouštějí nízké frekvence).

- **průměr** posledních 6 vstupů:
![[media/szz-15/media/image34.png]]

- ‘nabalující se vstup’ (obsahuje **rekurzi** – **aktuální výstup** je **dán** nejen hodnotami vstupů (aktuálních nebo minulých), ale i **hodnotami minulých výstupů**):
![[media/szz-15/media/image35.png]]

Příklady systémů, které se chovají jako horní propusť (propouštějí vysoké frekvence).

- **rozdíl** posledních 6 vstupů:
![[media/szz-15/media/image1.png]]

- ‘nabalující se vstup’:
![[media/szz-15/media/image9.png]]

**Videa:**

[<u>Difference Equation Descriptions for Systems</u>](https://youtu.be/MtHpbGUIGaA)

## Impulsní odezva (Impulse Response, h\[n\])

[<u>The Impulse Response of Systems</u>](https://www.youtube.com/watch?v=GwgAFqK0QgI)

Zkoumá **odezvu** systému na impuls. Impulsní odezva může být spočítána pouze pro LTI systém: impulsní odezva definuje LTI systém (popisuje jeho chování, jeho charakteristiku); impulsní odezva je výstupem LTI systému pro vstup o diskrétním jednotkovém impulsu. **Diskrétní impuls** je definován jako **Jakýkoliv diskrétní signál** může být reprezentován jako **vážený součet** **posunutých** diskrétních **impulsů** v čase:
![[media/szz-15/media/image26.png]]

![[media/szz-15/media/image23.png]]

![[media/szz-15/media/image19.png]]

Impulsní odezva k definici LTI systému používá **konvoluci**. Impulsní odezva definuje systém, protože impuls obsahuje **všechny** frekvence (**ve frekvenční doméně je roven 1 pro všechny frekvence**, tj. po provedení DFT/FFT).

### Konvoluce

**Základní operace** pracující se dvěma signály je definovaná vzorcem
![[media/szz-15/media/image12.png]]

![[media/szz-15/media/image5.png]]

![[media/szz-15/media/image33.png]]

Konvoluce graficky [<u>Discrete Time Convolution Example</u>](https://youtu.be/KAOJsqCyd5Y):
![[media/szz-15/media/image40.jpg]]

Konvoluci lze ve **frekvenční doméně** provést pouze **násobením**.

### FIR - Finite Impulse Response, IIR - Infinite Impulse Response

- **FIR**: impulsní odezva nebo odezva konečného vstupu má **konečnou délku**. Tyto filtry **nesmí** mít ani jednu **zpětnou smyčku (= rekurzi)**.
![[media/szz-15/media/image16.png]]

![[media/szz-15/media/image17.png]]

- **IIR**: impulsní odezva a odezva konečného vstupu má **nekonečnou délku**. Tyto filtry **musí** mít alespoň jednu **zpětnou smyčku (= rekurzi)**.
![[media/szz-15/media/image25.png]]

![[media/szz-15/media/image21.png]]

## Přenosová funkce

Přenosová funkce definuje LTI systém. Pokud chceme na nějaký signál aplikovat filtr, tímto filtrem signál **vynásobíme** (konvoluce v časové doméně) ve frekvenční doméně (např. filtrem, který propouští pouze spodní frekvence). X(z)\*H(z)=Y(z) → Přenosová funkce je definována jako **poměr** (podíl) **výstupu** - Y(z) ku **vstupu** - X(z) ve **frekvenční oblasti**, když jsou **zanedbány počáteční podmínky**. Jinak řečeno při **nulových** počátečních podmínkách, jde o podíl **Fourierovy transformace v diskrétním čase** výstupu a vstupu, respektive **Z-transformace** u signálů, pro které nelze provést **DTFT** (signály, které **nejsou** v +- nekonečnu **0**, mají nekonečnou energii, Z-transformace je násobí tak, aby **byly** v +- nekonečnu **0**). Přenosovou funkci lze také vyjádřit jako **DTFT** **impulsní odezvy** u FIR systémů (výstup je v nekonečnu 0), nebo jako **ZT** [<u>Z Transform Region of Convergence Explained</u>](https://youtu.be/uq_qv3Spzbs) IIR systémů (v nekonečnu nejsou 0). FT/ZT impulsní odezvy z toho důvodu, že X(z) mínus vstup **je 1** (FT jednotkového impulsu).
![[media/szz-15/media/image28.png]]

![[media/szz-15/media/image27.png]]

![[media/szz-15/media/image14.png]]

Přenosovou funkci lze získat z IR pomocí Laplaceovy transformace a IR lze získat z přenosové funkce pomocí inverzní Laplaceovy transformace.

### Region of Convergence
![[media/szz-15/media/image29.png]]

<u>[Z Transform Region of Convergence
Explained](https://youtu.be/uq_qv3Spzbs)[Laplace Transform Region of Convergence Explained](https://youtu.be/SexBL1OlhhU)</u>

### Stabilita
![[media/szz-15/media/image30.png]]

![[media/szz-15/media/image3.png]]

![[media/szz-15/media/image8.png]]

[<u>How do Poles and Zeros affect the Laplace Transform and the Fourier Transform?</u>](https://youtu.be/iP4fckfDNK8)

[<u>Frequency Response Magnitude and Poles and Zeros</u>](https://youtu.be/8jNjVkoZQCU)

## Frekvenční charakteristika
![[media/szz-15/media/image39.png]]

**Frekvenční charakteristika** popisuje/definuje systém **ve frekvenční doméně**, stejně jako **impulsní odezva** jej charakterizuje v **časové doméně**. Graficky ji vynášíme ve dvou grafech jako **amplitudovou charakteristiku** **\|H(⍵)\|** (jak filtr zeslabuje/zesiluje) a **fázovou** **charakteristiku arg(H(⍵))** (jak filtr posouvá). Frekvenční charakteristika je přenosová funkce (z-transformace) vyhodnocená pro **z = $e^{j\*omega}$**, tedy pro DTFT.

### Dělení frekvenčních charakteristik
![[media/szz-15/media/image38.png]]

- **Dolní propusť** - filtr, který **propouští nízké** frekvence.
- **Horní propusť** - filtr, který **propouští vysoké** frekvence.
- **Pásmová propusť** - filtr, který **propouští** signál **jen určitých** frekvencí.
- **Pásmová zádrž** - filtr, který **nepropouští** signál **určitých** frekvencí.

## Filtr
![[media/szz-15/media/image11.png]]

**Filtr** je lineárně časově invariantní (**LTI**) systém, který upravuje signál **ve frekvenční oblasti**. Je charakterizován **impulsní odezvou**. Výstup se získá konvolucí vstupu filtru s jeho impulsní odezvou. Lze implementovat pomocí diferenční rovnice.

![[media/szz-15/media/image2.png]]

**Základní bloky filtrů**

## Z-transformace

Postup:

1. vstupy **x\[n-k\]** se přepíší na $X(z)\,z^{-k}$,
2. výstupy **y\[n-k\]** se přepíší na $Y(z)\,z^{-k}$ (pro k = 0 se jedná o $z^0$, což je 1 a proto se nepíše),
3. všechny **Y(z)** se přepíší na jednu stranu rovnice a všechny **X(z)** na druhou (tento krok chybí v příkladu níže),
4. vytknou se **Y(z)** a **X(z)**, takže vznikne něco jako $Y(z) \cdot (1 + a_1 z^{-1} + \dots) = X(z) \cdot (b_1 z^{-1} + \dots)$,
5. převedeme do tvaru $H(z) = \dfrac{Y(z)}{X(z)} = \dfrac{b_1 z^{-1} + \dots}{1 + a_1 z^{-1} + \dots}$.
6. vzniklý zlomek se **rozšíří** násobením $z^x / z^x$ (což je 1, takže je hodnota zlomku pořád stejná), **x** se rovná největšímu **k** (krok není explicitně uveden v příkladě),
7. převod na PoS (product of sums - např. $z^2 - 4 = (z-2)(z+2)$)
8. určení nul (z Y(z), tedy z čitatele) a pólů (z X(z), tedy ze jmenovatele).

Konkrétní příklad:

Výsledek:
![[media/szz-15/media/image13.png]]

- **Nuly**: z = 1/2,
- **Póly**: z = -1/2.

Komplexní čísla

![[media/szz-15/media/image20.png]]

------------------------------------------------

- **Možné transformace signálu**
  - **Otočení časové osy** - s(-t)
  - **Zpoždění** - s(t-x), kde x \> 0
  - **Předběhnutí** - s(t+x), kde x \> 0
  - **Kontrakce** - s(m\*t), kde m \> 1
  - **Dilatace** - s(t/m), kde m \> 1
- **Komplexní číslo** - Složené z reálné části (osa x) a imaginární části (osa y), kde jednotka je odmocnina z -1, za kterou se substituuje *i* nebo *j*. Komplexní číslo je možné zapsat jako sumu těchto 2 hodnota (42 + 3i) nebo vektorem: z = \|z\|(cosⲪ + i\*sinⲪ), kde \|z\| je délka vektoru a Ⲫ je úhel s kladnou osou x.

![[media/szz-15/media/image10.png]]

![[media/szz-15/media/image18.png]]

- **Exponenciální tvar komplexního čísla** - $z = r \cdot e^{j\varphi}$
- **Komplexně sdružené číslo** - pro číslo

![[media/szz-15/media/image31.png]]
existuje komplexně sdružené číslo

![[media/szz-15/media/image24.png]]
. Vznikne změnou znaménka imaginární části čísla. Např.

![[media/szz-15/media/image22.png]]
. Součtem čísla a jeho komplexně sdruženého čísla vznikne reálné číslo. Funkce $y = e^{jx}$ je komplexní exponenciála; Součtem s komplexně sdruženou získáme kosinusovku.

![[media/szz-15/media/image7.png]]

- **Obecná kosinusovka**

![[media/szz-15/media/image32.png]]

![[media/szz-15/media/image37.png]]

## Zdroje

- SZZ okruh 15 — studijní materiály FIT BUT (`szz-15.docx`). Další obrázky: `media/szz-15/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/14-spektralni-analyza|14. Spektrální analýza]] · další: [[okruhy/16-mnoziny-relace-zobrazeni|16. Množiny, relace a zobrazení]] ▶
