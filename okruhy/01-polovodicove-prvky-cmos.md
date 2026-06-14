---
title: "1. Princip činnosti polovodičových prvků (dioda, BJT a unipolární tranzistor ve spínacím režimu, NAND a NOR v CMOS)"
category: okruh
okruh: 1
tags: [hardware, electronics, digital-logic]
aliases: [dioda, tranzistor, MOSFET, CMOS, BJT, NAND, NOR]
relationships:
  - target: "[[okruhy/02-kombinacni-logicke-obvody]]"
    type: related_to
  - target: "[[okruhy/03-sekvencni-logicke-obvody]]"
    type: related_to
sources: ["_sources/docx/szz-01.docx"]
summary: Princip činnosti diody, bipolárního (BJT) a unipolárního (MOSFET) tranzistoru ve spínacím režimu a realizace hradel NAND/NOR v technologii CMOS.
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

# 1. Princip činnosti polovodičových prvků

> SZZ okruh 1 (FIT BUT). Báze elektroniky číslicových obvodů — od PN přechodu po realizaci logických hradel.

## Shrnutí

## Polovodiče a PN přechod

- Základem je **křemík**; dva typy příměsí: **N** (volný elektron, dotace fosforem, majoritní = elektrony) a **P** (díra, dotace borem, majoritní = díry).
- Při spojení N a P dojde k **rekombinaci** a vznikne **potenciálová bariéra** ~0,7 V (křemík).

## Dioda

Jeden PN přechod, propouští proud jen v **propustném** směru (po překonání 0,7 V); v **závěrném** směru nevede až do **průrazného napětí** (pak proud strmě roste — obvykle zničení, výjimka Zenerovy diody).

![[media/szz-01/media/image2.png]]
*Polovodičová dioda — schématická značka a PN přechod.*

![[media/szz-01/media/image10.png]]
*Voltampérová (přechodová) charakteristika diody.*

## Tranzistor ve spínacím režimu

Tranzistor zesiluje proud; ve **spínacím režimu** malým proudem/napětím spínáme velký proud.

![[media/szz-01/media/image11.png]]
*Tranzistor jako spínač — malým proudem do báze spínáme velký proud spotřebičem.*

- **BJT (bipolární)** — dva PN přechody (NPN/PNP), vývody E/B/C. Proud do **báze** (~0,7 V nad emitorem) otevře cestu kolektor–emitor. Vede oba typy nosičů.
- **MOSFET (unipolární)** — řízen **napětím** na izolované elektrodě **Gate** (přes dielektrikum). Vede jen jeden nosič (N-channel / P-channel); typy *enhancement* (vede až po zapnutí) a *depletion* (vede ve výchozím stavu).

![[media/szz-01/media/image5.png]]
*Struktura N-channel MOSFET (Source, Gate přes oxid, Drain, P-substrát).*

## CMOS

**CMOS** = komplementární dvojice **NMOS + PMOS** tranzistorů. Výhody: **nízká spotřeba**, odolnost proti šumu, malé zahřívání.

- **NMOS** sepne kladné (log. 1) napětí na gate; **PMOS** sepne nízké (log. 0) napětí.
- Invertor je nejjednodušší případ; **NAND** a **NOR** vzniknou párovou kombinací PMOS/NMOS.

![[media/szz-01/media/image7.png]]
*Realizace hradel NAND a NOR v technologii CMOS.*

- **NAND (Shefferova)** i **NOR (Peirceova)** funkce jsou **funkčně úplné** — z každé lze sestavit libovolnou booleovskou funkci. ^[inferred]

> [!note] Ke kontrole (ověřeno)
> Plné znění tvrdí, že „z hradla NAND lze záměnou PMOS↔NMOS vytvořit OR a z NOR vytvořit AND". To je **chybně**: **statické CMOS hradlo je vždy invertující** (jednostupňově jen NAND/NOR/NOT). **OR a AND** v CMOS vznikají až **přidáním invertoru**; pouhá záměna tranzistorů dá opět invertující funkci, ne OR/AND.

## Souvislosti

Tato hardwarová báze stojí pod [[okruhy/02-kombinacni-logicke-obvody]] i [[okruhy/03-sekvencni-logicke-obvody]]. Statická paměť (SRAM) z okruhu 3 a paměťová [[okruhy/04-hierarchie-pameti|hierarchie]] jsou rovněž tvořeny MOSFET tranzistory.

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají (zdroj: „Časté otázky k okruhům"). Plné odpovědi níže v Plném znění.*

**Dioda** ↪ [[#Dioda]]
- *Anoda/katoda, propustný vs. závěrný směr?* → Proud teče z anody (+) na katodu (−); v propustném směru vede po překonání ~0,7 V, v závěrném nevede až do průrazného napětí.
- *VA charakteristika?* → V propustném směru proud strmě roste po prahovém napětí (~0,7 V Si); v závěrném ~0 do průrazu U_BR.
- *Účel rezistoru před diodou?* → Omezuje proud, jinak se dioda zničí.
- *Zenerova dioda?* → Záměrně pracuje v závěrném průrazu při definovaném napětí → stabilizace napětí.
- *Jednocestný vs. dvoucestný usměrňovač?* → Jednocestný propustí jednu půlvlnu; dvoucestný (Graetzův můstek) obě → hladší DC (vyhladí kondenzátor).

**PN přechod a polovodiče** ↪ [[#Polovodiče a PN přechod]]
- *P a N typ?* → N = volné elektrony (majoritní elektrony, dotace fosforem); P = díry (majoritní díry, dotace borem).
- *PN přechod?* → Rekombinace na rozhraní vytvoří ochuzenou vrstvu a potenciálovou bariéru (~0,7 V Si).

**Bipolární tranzistor (BJT)** ↪ [[#Tranzistor ve spínacím režimu]]
- *Princip NPN, spínací režim?* → Malý proud do báze (U_BE ≳ 0,7 V) otevře velký proud kolektor→emitor; malým proudem spínáme velký.
- *Tranzistor jako invertor?* → Sepnutý (báze v 1) stáhne výstup (kolektor) k 0; rozepnutý → výstup v 1 → logická inverze.

**Unipolární tranzistor (MOSFET)** ↪ [[#Tranzistor ve spínacím režimu]]
- *NMOS vs. PMOS, oxid na gate?* → NMOS sepne kladným napětím na gate (vede elektrony), PMOS nízkým (vede díry); gate je izolován vrstvou oxidu (SiO₂).

**CMOS** ↪ [[#CMOS]]
- *Co je CMOS, proč NMOS+PMOS?* → Komplementární dvojice; v ustáleném stavu neteče klidový proud → nízká spotřeba, malý ohřev, odolnost proti šumu.
- *NAND/NOR v CMOS?* → Pull-up síť z PMOS + pull-down síť z NMOS (viz schéma níže).

**Obecné**
- *Ohmův zákon / napěťový dělič?* → U = R·I; dělič U_out = U·R₂/(R₁+R₂).

## Plné znění (ke studiu)

- elektrony tečou od **-** k **+**, proud značíme, že teče od **+** k **-**.
- Základem jsou polokovy, hlavně **křemík**.
- Existují 2 typy **polovodičových materiálů** založených na příměsích:
  - **N** (negativní) - Při vazbě atomů vzniká v polokovu **volný elektron**, který je schopný vést proud - elektronová vodivost. Dotování **fosforem**.
    - majoritní: elektrony
    - minoritní: díry
  - **P** (pozitivní) - Při vazbě vzniká “díra” (**místo, kde chybí elektron**) pro vedení proudu. Dotování **borem**.
    - majoritní: díry
    - minoritní: elektrony
- Oba typy polovodičových materiálů **nemají na venek elektrický náboj** (uvnitř materiálů je stejný počet protonů jako elektronů), pokud se spojí na mikroskopické úrovni, dojde k přesunu části (maličko) elektronů z **N** do **P**. V **P** vznikne záporný náboj a v **N** kladný náboj. Tomuto jevu se říká **rekombinace**.
- V místě dotyku vzniká **potenciálová bariéra** (~0.7 V u křemíku).
- Přechod v propustném směru (anoda = kladná, katoda = záporná)
- Připojíme-li napětí podle obrázku, nosiče náboje se odpuzují a jsou vytlačovány do vyprázdněné vrstvy, která se tím zužuje.

## **Polovodičová dioda**
![[media/szz-01/media/image2.png]]

obsahuje PN přechod, propouští proud *pouze v jednom směru*. Ideální dioda by propouštěla proud pouze v jednom směru, reálná dioda propouští v jednom lépe než v druhém. V závěrném směru prakticky nepropouští proud (Reverse Saturation Current) až do tzv. **průrazného napětí**, poté začne procházející proud strmě narůstat (Avanalche Breakdown, Tunneling Breakdown), což obvykle vede na zničení diody (přehřátí a spálení). Pokud k tomu není dioda určená (zenerovy diody), ale i ty lze spálit příliš velkým proudem, musí být omezen prvky v obvodu (rezistor). V propustném směru začne proud strmě narůstat po **překonání potenciálové bariéry** (0.7V pro křemík, méně pro germanium). [<u>How Diodes Work - The Learning Circuit</u>](https://youtu.be/-SSkjWuUri4)

- **Přechodová (voltampérová) charakteristika diody** - (obr.)
![[media/szz-01/media/image10.png]]

- Existuje více druhů diod (usměrňovací, spínací, fotodiody, luminiscenční…)

## **Tranzistor**

Elektronická součástka, která má schopnost zesilovat proud.

**Tranzistor jako spínač (spínací režim)** - Dokáže spínat velké proudy a pracuje velmi rychle. Pokud do báze teče proud (stačí malý) tak začne mezi kolektorem a emitorem a tedy i spotřebičem procházet velký proud. Malým proudem spínáme proud velký.

![[media/szz-01/media/image11.png]]

### **Bipolární tranzistor BJT (Bipolar Junction Transistor)**

Přenos proudu uskutečňují oba nosiče: N i P. Jedná se o **2 PN** přechody vedle sebe - **PNP** nebo **NPN** tranzistor.

- **E - Emitor** je hodně nadopovaný, **B - Báze** je málo nadopovaná a velmi **tenká**, **C - Kolektor** je středně nadopovaný
- **Princip NPN** - emitor je připojen na katodu (elektrodu uvolňující elektrony) a společně s bází tvoří diodu v propustném směru. Pokud je na **bázi** přivedeno napětí o **~0.7V** větší než na **emitor**, začne touto diodou procházet proud. Díky tomu, že emitor je daleko více dopován než báze, dostává se do báze mnohonásobně větší množství elektronů, než je zde děr. Protože báze je navíc tenká, jsou tyto elektrony přitahovány kladným elektrickým nábojem vznikajícím na kolektoru, který je připojen na **anodu**, a tranzistorem tak **prochází** proud. Pokud není napětí na bázi vyšší alespoň o ~0.7V oproti emitoru, nedojde k překonání **potenciálové bariéry** a celým tranzistorem proud neteče. [<u>https://youtu.be/DXvAlwMAxiA</u>](https://youtu.be/DXvAlwMAxiA)
- **Princip PNP** - emitor musí být připojen na anodu, kolektor na katodu a napětí mezi bází a emitorem musí být **-~0.7V** (mezi emitorem a bází ~0.7V), jinak je princip obdobný s tím, že uvažujeme pohyb děr…

![[media/szz-01/media/image14.png]]

![[media/szz-01/media/image8.png]]
style="width:6.26772in;height:2.40278in" />

### **Unipolární tranzistor MOSFET** (Metal Oxide Semiconductor Field Effect Transistor)

Přenos proudu uskutečňuje pouze jeden nosič - **N-channel** nebo **P-channel**, dále jsou děleny na **enhancement** (**nevedou** proud a musí se **zapnout**) a **depletion** (**vedou** proud a musí se **vypnout**). Jsou řízeny napětím.

- **Gate** - řídící elektroda - přes **vrstvu dielektrika** (oxid - izolace) připojena k substrátu, **Source** - zdrojová elektroda - silně dopovaná, **Drain** - výstupní elektroda - silně dopovaná, **Body/Substrate** - málo dopován.
- **Princip NPN enhancement** - na Source je přivedeno záporné napětí (stejné jako na Bulk/Body) a na Drain je přivedeno kladné napětí (Drain a Source lze zaměnit). Aby tekl ze Source do Drain proud, musí být na Gate dovedeno kladné napětí (řádově menší, než mezi Source a Drain). Kolem Gate tak vznikne kladný náboj a začne přitahovat elektrony ze Substrate/Body (díry se přesunují dolů) a zároveň přitahovat elektrony ze Source. Začne se vytvářet postupně od Source k Drain kanál (trojúhelníkový tvar). Při dostatečném napětí na Gate je elektrické pole natolik velké, že kanál propojí Source s Drain a začne téct proud (s vyšším Gate napětím se dále zvyšuje). Zvyšování napětí mezi Source a Drain způsobní i zvyšování **potenciálové bariéry** kolem Drain, což způsobí saturační fázi (Saturation Region - nezvyšuje se prakticky protékající proud).

![[media/szz-01/media/image5.png]]

  - Source a Bulk jsou spojené, aby neměly různé potenciály, jinak záporné napětí může být různé, ale právě Source a Bulk musí mít to **stejné záporné napětí**, aby nevznikl žádný tok proudu (aby tranzistor nefungoval jako dioda).
  - Bulk a Drain vytváří tzv. parazitní diodu.

![[media/szz-01/media/image9.png]]
style="width:3.52604in;height:2.98908in" />[<u>How
> Does a MOSFET Work?</u>](https://youtu.be/rkbjHNEKcRw)

### CMOS

CMOS (Complementary metal–oxide–semiconductor) je technologie výroby logických členů za pomoci párů P-channel (PMOS) a N-channel (NMOS) MOSFET tranzistorů. **Nízká spotřeba, odolnost proti šumu a méně se zahřívá**. Dělí se na **(a)** **PMOS** a **(b)** **NMOS.**

-
![[media/szz-01/media/image13.png]]
**PMOS** - záporné (**low - 0**) napětí na gate sepne tranzistor - **děrová vodivost**. Source a Body/Substrate se zapojují na **kladný** pól zdroje, Drain se zapojuje na **záporný** pól zdroje. Source a Drain jsou typu **P**, Substrate je typu **N**. Na Source je menší napětí než na drain.

![[media/szz-01/media/image1.png]]

- **NMOS** - kladné (**high - 1**) napětí na gate sepne tranzistor - **elektronová vodivost**. Source a Body/Substrate se zapojují na **záporný** pól zdroje, Drain se zapojuje na **kladný** pól zdroje. Source a Drain jsou typu **N**, Substrate je typu **P**. Na Source je větší napětí než na Drain.
![[media/szz-01/media/image12.png]]

Proces výroby CMOS je takový, že se celý čip nadopuje na typ **P**. NMOS tranzistory lze pak vytvořit přímo přidání **N** kanálů. PMOS se musí vytvořit tak, že se nadopuje oblast v čipu (well - studna) na typ **N** a až do ní se vkládají **P** kanály. Výhodné je to proto, že obvykle je potřeba více NMOS tranzistorů (např. SRAM používá 4x NMOS a 2x PMOS, DRAM používá 1x NMOS, …) [<u>https://www.montana.edu/aolson/eele414/lecture_notes/eele414_module_04_CMOS_FAB.pdf</u>](https://www.montana.edu/aolson/eele414/lecture_notes/eele414_module_04_CMOS_FAB.pdf)

![[media/szz-01/media/image4.png]]

- **NAND, NOR A INVERTOR (Technologie CMOS)**
![[media/szz-01/media/image6.png]]

![[media/szz-01/media/image7.png]]

> Z hradla **NAND** lze záměnou **PMOS** za **NMOS**
> a naopak vytvořit **OR,** z hradla **NOR** lze záměnou **PMOS** za
> **NMOS** a naopak vytvořit **AND**.

![[media/szz-01/media/image3.png]]
NAND (Shefferova funkce) logika **¬p ≡ ¬(p∧p)**

**p∧q ≡ ¬(¬(p∧q)) ≡ ¬(¬(p∧q)∧¬(p∧q)))**

**p∨q ≡ ¬(¬p∧¬q) ≡ ¬(¬(p∧p)∧¬(q∧q)))**

**p→q ≡ ¬p∨q ≡ ¬(p∧¬q) ≡ ¬(p∧¬(q∧q)))**

## NOR (Peirceova funkce) logika

**¬p ≡ ¬(p∨p)**

**p∧q ≡ ¬(¬p∨¬q) ≡ ¬(¬(p∨p)∨¬(q∨q)))**

**p∨q ≡ ¬(¬(p∨q)) ≡ ¬(¬(p∨q)∨¬(p∨q)))**

**p→q ≡ ¬p∨q ≡ ¬(p∨p)∨q ≡ ¬(¬(¬(p∨p)∨q)∨¬(¬(p∨p)∨q)))**

**Odkazy:**

- Jak funguje tranzistor - [<u>Transistors, How do they work ?</u>](https://www.youtube.com/watch?v=7ukDKVHnac4)
- VA charakteristika - [<u>https://upload.wikimedia.org/wikipedia/commons/4/43/Threshold_formation_nowatermark.gif</u>](https://upload.wikimedia.org/wikipedia/commons/4/43/Threshold_formation_nowatermark.gif)
- [<u>Working of Transistor as a Switch - NPN and PNP Transistors</u>](https://www.electronicshub.org/transistor-as-a-switch/)
- [<u>http://old.spsemoh.cz/vyuka/zel/tranzistory-bip.htm</u>](http://old.spsemoh.cz/vyuka/zel/tranzistory-bip.htm)
- [<u>Transistor Logic NOT Gate - Inverter</u>](https://www.petervis.com/Education/logic-gates/transistor-logic-not-gate-inverter.html)
- Prakticky polovodiče a tranzistory - kapitola 7
  - [<u>https://elektrokniha.cz/ebook/index.html</u>](https://elektrokniha.cz/ebook/index.html)

## Zdroje

- SZZ okruh 1 — studijní materiály FIT BUT (`szz-01.docx`). Další obrázky: `media/szz-01/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · předchozí: — · další: [[okruhy/02-kombinacni-logicke-obvody|2. Kombinační logické obvody]] ▶
