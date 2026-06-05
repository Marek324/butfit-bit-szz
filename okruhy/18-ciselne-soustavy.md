---
title: "18. Číselné soustavy a převody mezi nimi"
category: okruh
okruh: 18
tags: [math, number-representation]
aliases: [poziční soustava, polyadická soustava, základ, radix, převody soustav, BCD]
relationships:
  - target: "[[okruhy/09-reprezentace-cisel-ieee754]]"
    type: related_to
sources: ["_sources/docx/szz-18.docx"]
summary: Poziční vs. nepoziční a polyadické soustavy, polynomiální zápis, převody mezi soustavami (dělení/násobení základem, mocninné základy) a kódy záporných čísel.
provenance:
  extracted: 0.93
  inferred: 0.05
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T17:10:00Z
updated: 2026-06-03T17:10:00Z
---

# 18. Číselné soustavy a převody mezi nimi

> SZZ okruh 18 (FIT BUT). Způsoby reprezentace čísel a převody mezi soustavami.

## Shrnutí

### Číselné soustavy
- **Poziční** — hodnota číslice závisí na její pozici (dnes převažují); **nepoziční** — nezávisí (římské, dnes zastaralé).
- **Polyadické** = poziční se základem r; hodnota = polynomiální zápis (Σ aᵢ·rⁱ). Musí mít symbol pro **0**.
- Základy: dvojková (r=2), osmičková (8), desítková (10), dvanáctková (12), šestnáctková (16, číslice A–F), šedesátková (60, čas).

### Převody
- Obecně **přes desítkovou** soustavu; je-li jeden základ **mocninou** druhého, lze **přímo**.
- **Dělení základem** — pro celá čísla (zbytky tvoří číslice odzadu).
- **Násobení základem** — pro desetinná čísla (celé části tvoří číslice; konec při 0 nebo dosažené přesnosti).
- **Mocninné základy**: 2↔8 po trojicích bitů, 2↔16 po čtveřicích (niblech).
- Záporná čísla: přímý / inverzní (jedničkový) / **doplňkový (dvojkový)** kód — viz [[okruhy/09-reprezentace-cisel-ieee754]].

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Typy soustav** ↪ [[#Číselné soustavy]]
- *Poziční vs. nepoziční?* → Poziční: hodnota dle pozice (desítková, binární); nepoziční: nezávisí (římské).
- *Polyadická soustava?* → Poziční se základem r; hodnota = Σ aᵢ·rⁱ; nutný symbol pro 0.

**Zápis a převody** ↪ [[#Převody]]
- *Polynomiální zápis?* → Číslo jako vážený součet mocnin základu (aₙrⁿ + … + a₀r⁰).
- *Dec→bin a zpět?* → Dec→bin dělením 2 (zbytky odzadu); bin→dec polynomiálně (součet mocnin 2).
- *Bin↔hex / bin↔oct?* → Po 4 bitech (hex) / 3 bitech (oct), protože 16=2⁴, 8=2³.
- *Desetinná čísla?* → Násobení základem, sepisování celých částí.

**Záporná čísla** ↪ [[#Převody]]
- *Kódy?* → přímý, inverzní (jedničkový doplněk), doplňkový (dvojkový) — detail v okruhu 9.

**Obecné**
- *Proč hex v informatice?* → Kompaktní zápis binárních hodnot (1 hex číslice = 4 bity).

## Plné znění (ke studiu)

**Číselné soustavy** vyjadřují **způsob reprezentace čísel**. Podle způsobu určení hodnoty čísla z dané reprezentace rozlišujeme dva hlavní druhy číselných soustav: poziční číselné soustavy a nepoziční číselné soustavy. **Dnes** se obvykle používají **soustavy poziční**. Zápis čísla dané soustavy je posloupností symbolů, které se nazývají číslice.

## Poziční

Číselné soustavy, u kterých **závisí na pozici číslic**. Spadají sem polyadické soustavy (viz dále)

## Nepoziční

Číselné soustavy, ve kterých **není** hodnota číslice **dána jejím umístěním** v dané sekvenci číslic. Tyto způsoby zápisu čísel se **dnes** již téměř **nepoužívají** a jsou považovány za zastaralé.

Např. egyptské nebo řecké číslice

### Římská číselná soustava (římské číslice)
![[media/szz-18/media/image5.png]]


Římané psali číslici **4 jako IIII**, **40 jako XXXX** atd. tento zápis opravdu umožňuje zápis **číslic na libovolné pozice**. Pravidlo pro odečtení, že 4 se zapisuje jako IV, 40 jako XL atd., se začalo používat až ve středověku, komplikuje ale umístění číslic (největší se tak psala vlevo, nejmenší vpravo). Např. číslo **78** se běžně zapisuje jako **LXXVIII**. Lze ale zapsat také např. jako XXVLIII, XXIIILV - uvažujeme pravidlo odečtení a libovolně, pokud jej neuvažujeme např. IXLXIVI, IIVILXL, … Poziční zápis v římské číselné soustavě není možný, protože neexistuje symbol pro **nulu**.

- **Převod z římské do desítkové**: jednotlivé číslice nahradíme za jejich hodnotou a jednotlivé hodnoty sečteme. Např.:

> **LXVXI = 50 + 10 + 5 + 10 + 1 = 76**.

- **Převod z desítkové do římské**: musíme najít první číslici, jejíž hodnota je menší, než hodnota čísla v desítkové soustavě. Zapsat ji tolikrát, kolikrát se do čísla vejde, od čísla odečíst zapsanou hodnotu a pokračovat další číslicí. Např. převod čísla **32**: L - nevleze se, X - vleze se (3x), V - nevleze se, I - vleze se (2x) → **XXXII**.

- Původní zápis je nepoziční, ale pokud vezmeme v potaz odečítání (IV = 4) a nějaká pravidla zápisu (menší před větším může být jenom pokud se odečítá), tak už na pozici záleží (a není polyadická, ale má svoje vlastní pravidla pro zápis).

## Polyadické

Převládající způsob písemné reprezentace čísel. V tomto způsobu zápisu čísel je **hodnota** každé **číslice** dána její **pozicí v sekvenci symbolů**. Všechny poziční soustavy **musí** mít symbol pro **nulu**. Celá část je oddělena od zlomkové speciálním znakem (zpravidla řádovou čárkou či tečkou). Nejběžnější poziční číselnou soustavou je soustava **desítková**. Pro zápis hodnoty čísla v libovolné soustavě můžeme použít polynomiální zápis.

### Základ (báze, radix) číselné soustavy
![[media/szz-18/media/image1.png]]

![[media/szz-18/media/image7.png]]


Číslo definující **maximální** počet **číslic**, které jsou v dané soustavě k **dispozici**.

- **dvojková** (binární, **r=2**) – přímá implementace v digitálních elektronických obvodech (použitím logických členů).

- **osmičková** (oktální, oktalová, **r=8**)

- **desítková** (decimální, dekadická, **r=10**) – nejpoužívanější v běžném životě

- **dvanáctková** (**r=12**) – dnes málo používaná, ale dodnes z ní zbyly názvy prvních dvou řádů – **tucet** a veletucet.

- **šestnáctková** (hexadecimální, **r=16**) – používá se v oblasti informatiky, pro číslice 10 až 15 se používají písmena **A** až **F**.

- **šedesátková** (**r=60**) – používá se k měření času pro zlomky hodiny; číslice se obvykle zapisují desítkovou soustavou jako 00 až 59 a řády se oddělují **dvojtečkou.** Staré názvy prvních dvou řádů jsou **kopa** a velekopa.

## Převody mezi pozičními soustavami

Běžný postup při převodu čísel mezi dvěma číselnými soustavami je **převod přes desítkovou soustavu**. Pokud však **základ jedné** soustavy je **mocninou základu** soustavy **druhé**, lze postupovat i **přímo**.

### Substituční metoda převodu soustav

Lze použít pro libovolnou soustavu, pro člověka je však nejjednodušší pro převod do desítkové soustavy.

- Číslo se vyjádří polynomiálním zápisem v cílové soustavě (dekadická).

- Vypočítají se členy polynomu a sečtou.

> 
![[media/szz-18/media/image4.png]]


### Metoda dělení základem

Vhodná pro převod celých čísel.\

![[media/szz-18/media/image2.png]]


Protože dělení je pro člověka náročná operace, lze použít způsob, kdy hledáme největší mocninu cílové soustavy, která je menší než převáděná hodnota, zjistíme, kolikrát se do převáděného čísla vejde a odečteme tento násobek od převedeného čísla - získanou číslici zapíšeme na správné pozici čísla v soustavě, do které převádíme. Postup opakujeme, dokud nevyčerpáme všechny pozice cílového čísla.

- Vhodné zejména u **dvojkové** soustavy, ve které známe hodnoty jednotlivých mocnin 2 a víme, že možné hodnoty ve dvojkové soustavě jsou jen 0 a 1, tedy mocnina 2 v převáděném čísle buď je (jednou), nebo vůbec není.

### Metoda násobení základem

Vhodná pro **převod desetinných čísel**. Číslo se násobí základem soustavy, do které ho převádíme. Po každém kroku se sepíše celočíselná část. Končíme po **dosažení 0** nebo **požadované přesnosti**.\

![[media/szz-18/media/image6.png]]


### Substituční převod desetinných čísel

Postupuje se stejně jako s celými čísly, ale tentokrát je lepší čísla odečítat a jak se dostaneme na desetinnou čárku, použijí se **záporné mocniny**.\

![[media/szz-18/media/image3.png]]


### Převod mezi soustavami s mocninným rozdílem základů

- **Převod mezi dvojkovou a osmičkovou soustavou:** na zapsání všech osmičkových číslic stačí přesně **3 bity.** Stačí číslo rozdělit na **trojice** (číslo se doplní na násobek 3 přidáním nul před číslo - nezmění hodnotu) a každou zapsat jako **osmičkovou číslici**, respektive z osmičkové číslice vytvářet **trojice binárních číslic**. Např. převod binárního čísla:
![[media/szz-18/media/image8.png]]


> (001010111100)2 = (001\|010\|111\|100)2 = (1\|2\|7\|4)8 = (1274)8
>
> (736)8 = (7\|3\|6)8 = (111\|011\|110)2 = (111011110)2

- **Převod mezi dvojkovou a šestnáctkovou soustavou:** na zapsání všech šestnáctkových číslic stačí přesně **4 bity**. Stačí číslo rozdělit na **nibly** (čtveřice) a každý zapsat jako **šestnáctkovou číslici**, respektive z šestnáctkové číslice vytvářet **nibly** (čtveřice binárních číslic).\
  (0001\|0011\|0010\|1010)₂ = (1\|3\|2\|A)₁₆\
  (8\|A\|F)₁₆ = (1000\|1010\|1111)₂

## Zdroje

- SZZ okruh 18 — studijní materiály FIT BUT (`szz-18.docx`). Obrázky: `media/szz-18/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/17-diferencialni-integralni-pocet|17. Diferenciální a integrální počet]] · další: [[okruhy/19-vyrokova-predikatova-logika|19. Výroková a predikátová logika]] ▶
