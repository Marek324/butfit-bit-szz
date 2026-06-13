---
title: "13. Principy grafických uživatelských rozhraní (komunikační kanály, módy komunikace, systémy řízené událostmi, standardní prvky)"
category: okruh
okruh: 13
tags: [gui, software-engineering]
aliases: [GUI, WIMP, komunikační kanály, systémy řízené událostmi, MVC, SDI, MDI, TDI, modální okno]
relationships:
  - target: "[[okruhy/06-periferie-preruseni-dma-sbernice]]"
    type: related_to
  - target: "[[okruhy/12-3d-transformace-pipeline]]"
    type: related_to
sources: ["_sources/docx/szz-13.docx"]
summary: Komunikace člověk–stroj, komunikační kanály a módy, systémy řízené událostmi a standardní prvky GUI (WIMP), architektura MVC.
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

# 13. Principy grafických uživatelských rozhraní

> SZZ okruh 13 (FIT BUT). Komunikace člověk–stroj = **obousměrná výměna informací** přes periferie založené na lidských smyslech.

## Shrnutí

## Komunikační kanály

- **Stroj → člověk**: obraz/zrak (nejvyšší propustnost), zvuk/sluch (varovné signály), hmat (vibrace, Braille), čich/chuť (zatím nepoužitelné).
- **Člověk → stroj**: pohyb/hmat (klávesnice, myš — nejobvyklejší), zvuk/řeč (asistenti, problém soukromí), obraz/gesta (VR, rozpoznávání).

## Způsob a módy komunikace

- **Aktivní** komunikace (uživatel řídí) × **pasivní** (odpovídá na dotazy, dialogová okna) — v praxi se kombinují.
- **Mód** = stav, ve kterém PC reaguje na vstup jedinečně (Caps Lock, Insert, Vim režimy). Obecně **čím méně módů, tím lépe**.
- **Přímá manipulace** (Drag & Drop, Look and Feel) — přirozené, intuitivní ovládání.

## Systémy řízené událostmi

- Tok programu řízen **událostmi** (stisk klávesy, pohyb myši); program běží v nekonečné smyčce, čeká na událost, detekuje ji a spustí obsluhu.
- HW realizace přes [[okruhy/06-periferie-preruseni-dma-sbernice|přerušení]]; SW: event listeners, callbacks, Qt signals & slots.

## Standardní prvky (WIMP)

- **Window** — primární (hlavní, menu), sekundární/**modální** (mění režim, blokuje), systémově modální, nemodální.
- **Icon**, **Menu**, **Pointer** + tlačítka, checkboxy, slidery, vstupní pole.
- Režimy oken: **SDI** (jedno primární okno), **MDI** (více oken v aplikaci), **TDI** (záložky — prohlížeče, editory).

![[media/szz-13/media/image3.png]]
*Single-Document Interface (SDI) — každý dokument ve vlastním okně s vlastním menu (Excel 2013).*

## MVC (Model-View-Controller)

Architektura oddělující **model** (data), **view** (prezentace) a **controller** (reakce na události); změna jedné komponenty má minimální vliv na ostatní.

![[media/szz-13/media/image1.png]]
*Vzor Model-View-Controller.*

## Souvislosti

Vykreslení prvků staví na [[okruhy/12-3d-transformace-pipeline|grafické pipeline]]; MVC a události se uplatňují i ve [[okruhy/37-webova-rozhrani-autentizace|webových rozhraních]].

## Související syntéza

- [[synthesis/preruseni-udalosti-signaly|Přerušení × události × signály]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Principy GUI** ↪ [[#Komunikační kanály]]
- *Komunikační kanály?* → Způsoby komunikace přes lidské smysly: stroj→člověk (obraz, zvuk, hmat), člověk→stroj (pohyb, řeč, gesta).
- *Aktivní vs. pasivní komunikace?* → Aktivní: uživatel řídí činnost; pasivní: odpovídá na dotazy systému (dialogová okna).

**Módy a modalita** ↪ [[#Způsob a módy komunikace]]
- *Co je mód komunikace?* → Stav, ve kterém systém reaguje na vstup jedinečně (Caps Lock, režimy Vim); obecně čím méně módů, tím lépe.

**WIMP a metafora** ↪ [[#Standardní prvky (WIMP)]]
- *Co je WIMP?* → Windows, Icons, Menus, Pointer — standardní prvky GUI.
- *Metafora v GUI?* → Vychází z reálného světa (plocha, složky, koš) → intuitivní pochopení a ovládání.

**Události a MVC** ↪ [[#Systémy řízené událostmi]]
- *Systém řízený událostmi?* → Smyčka čeká na události (klávesa, myš), detekuje je a spustí obsluhu; HW přes přerušení, SW přes event listeners/callbacks.
- *MVC?* → Model (data) – View (prezentace) – Controller (reakce na události); oddělení komponent → minimální vzájemný vliv změn.

## Plné znění (ke studiu)

Komunikaci člověka se strojem lze definovat jako **obousměrnou výměnu informací** mezi člověkem a strojem. Tok informací od počítače k člověku lze uskutečnit pomocí **periferních** výstupních zařízení generujících výstupy, na které mohou reagovat **smysly člověka**. Tok údaj od člověka k počítači lze naopak uskutečnit pomocí vstupních periferních zařízení, která mohou **reagovat na podněty** generované člověkem.

## Komunikační kanály

Komunikační kanály jsou způsoby **komunikace člověka a stroje** pomocí periferních zařízení - **monitor**, **klávesnice**, **tiskárna**, **myš**, **kamera**, … Jsou **založené** na **lidských smyslech**.

### Komunikační kanály od stroje k človeku

- **Obraz (zrak)** - Nejvýhodnější pro přenos informace. **Nejvyšší informační propustnost**.
- **Zvuk (sluch)** - Vhodný pro přenos menšího počtu informací. Nižší propustnost a “sériový” přístup (je obtížné poslouchat 2 věci zároveň). Zvuk na sebe však může **lépe upozorňovat** - varovné signály.
- **Hmat** - Využívá se pro komunikaci **nevidomých** a stroje (braillovo písmo). Běžní uživatelé se nejčastěji setkávají s tímto druhem komunikace na mobilních zařízeních, formou **vibrací** (náhrada za pocit stisknutí tlačítka) a také na ovladačích her (např. signalizace překážky, **silový odpor** u závodního volantu).
- **Čich, chuť** - V současnosti **nejsou** pro komunikaci **použitelné**. Problémy s umělým syntezováním chuti a vůně v reálném čase.

### Komunikační kanály od člověka ke stroji

- **Pohyb (Hmat)** - Nejobvyklejší prostředek - **klávesnice**, tlačítka, přepínače, … a **mechanické polohovací zařízení** - **myš**, páčky. (Dnes nejpoužívanější, ale neznamená to, že je nejlepší, pouze je obvykle nejjednodušší na implementaci - např. diktování textu může být pro většinu uživatelů příjemnější, než psaní na klávesnici).
- **Zvuk (Řeč)** - Rychle se vyvíjí, dnes už prakticky **použitelný** způsob ovládání, zejména v anglickém jazyce (asistenti na mobilu, speech to text apod.). **Problém** s rozpoznáváním řeči a náročnost zpracování, **soukromí**. Není vhodné pro sdělování citlivých informací (hesla, číslo OP., …)
- **Obraz (gesta)** - Sdělování informací **gesty,** **pohyby** a **mimikou v obličeji** (filtry na Instagramu). Lze využít ve **virtuální realitě** a hrách (Just dance, Wii games…), gesta ruky pro přeskočení písničky na Android 10 (Google Pixel). Rozpoznávání osob a objektů - pro bezpečnost nebo klasifikaci.

## Způsob komunikace

Nejzákladnějším dělením obrazové komunikace člověka s počítačem je dělení podle aktivity uživatele:

- **Aktivní komunikace** - **Uživatel řídí** činnost počítače - činnost počítače záleží na **vůli uživatele**. Například panel nástrojů v grafickém editoru, unixový terminál…
- **Pasivní komunikace** - Uživatel **odpovídá** na dotazy počítače. **Dialogová**/modální okna.

Je zřejmé, že komunikace s počítačem se **nebude trvale** odehrávat jen **pasivně** nebo jen **aktivně**, a že je vhodné oba způsoby **kombinovat**. **Aktivní** komunikaci je nutné používat tam, kde uživatel **musí rozhodnout**, jakou činnost má počítač vykonávat a kdy není možné rozhodnutí obsluhy předvídat. **Pasivní** komunikace je naopak vhodná tehdy, je-li příští **činnost** počítače **známá**, a obsluha jen zadává údaje nebo rozhoduje mezi několik málo možnými variantami, které lze přesně určit.

![[media/szz-13/media/image4.png]]
style="width:4.75in;height:2.01042in" />

## Módy komunikace

**Mód komunikace** = Stav, ve kterém počítač reaguje jedinečným způsobem na vstup od uživatele (změny módů - změny chování počíteče na vstupy, na klávesnici **Caps Lock, Insert**, grafický editor a levé tlačítko myši může kreslit, mazat, přesouvat objekty). Obecně čím méně modů tím lípe. Typické mody (např. Vim - **i** pro editaci):

- Zadání příkazu v příkazovém jazyce
- Odpověď na dotaz (potvrzení akce - např. smazání).
- Editace textu
- Reakce na chybu

### Přímá manipulace (Drag and Drop, Look and Feel)

Umožňuje interakci mezi uživatelem a objekty zobrazenými na obrazovce - podporuje **přirozené chování** uživatele. **Zjednodušuje ovládání** počítače pro neškolené uživatele a zlepšuje jejich dojem při práci s PC. Zjednodušuje nároky na zkušeného uživatele, který nemusí vynakládat úsilí např. pro přesun souboru, ale provede jej intuitivně pomocí **Drag and Drop**. **Look and Feel** - uživatelské rozhraní se dá používat **intuitivním způsobem** vycházejícím z podobnosti s prací s předměty v běžném životě.

## Systémy řízené událostmi

Systémy, které se zabývají **detekcí**, **zpracováním** a **reakcí** na události. Tok programu je řízen různými událostmi (vstup z periferií - **zmáčknutí klávesy**, **pohyb** **myši**). Program naslouchá na tyto akce, a nějak reaguje (např. v JS pomocí **event listeners**: onclick, onhover, onkeypress). U hardware je toto prováděno pomocí **přerušení**. Tento přístup je velmi využívaný. Programy, které takto pracují, běží v nekonečné smyčce (z té vystoupí po události signalizující ukončení) a čekají na příchod události (HW přerušení) nebo sami kontrolují její vznik (Polling), nebo probíhá formou zasílání zpráv. **Detekuje se, o jakou se jedná událost, a spustí se její obsluha. Po dokončení obsluhy se program dostává zpět do stavu, ve kterém čeká na další událost.**

- QT: signal and slots,
- callbacks

## Standardní prvky rozhraní

Standardní prvky GUI obvykle označujeme pod zkratkou **WIMP**:

- **Window - okno**: reprezentují spuštěné programy (Douglas Engelbart; Xerox PARC):
  - **primární**: hlavní okno aplikace, obsahuje menu, více nezávislých funkcí,
  - **sekundární**: okno pro zpracování vedlejších, rozšiřujících či doplňkových funkcí, pevný rozměr, nemá min/maximalizaci, menší než primární okno. Může být nazývané jako **modální**, protože **mění mód/režim** chování aplikace/systému, mění pracovní postup. Může vyžadovat interakci uživatele, než vrátí řízení rodičovskému oknu (např. dialogová okna). Slouží k upozornění uživatele a blokování aplikace/systému pro získání klíčových informací (uživatel musí dokončit práci v modálním okně)
    - **modální** - dialog v rámci aplikace,
    - **systémově modální** - Mají prioritu nad aplikacemi (např. nedostatečná práva pro provedení akce, **potvrzení instalace**).
    - **nemodální** - Neprioritní. Uživatel může mít okno otevřené a stále pracovat s aplikací (výběr barvy štětce v malování například).
- **Icon - ikona**: reprezentují zkratky sloužící k provedení určité činnosti (například spuštění programu).
- **Menu**: textové nebo z ikon složené **nabídky**, ze kterých je možné jednu vybrat a provést tak určitou akci.
- **Pointer - ukazatel**: pohybující se grafický symbol reprezentující pohyb fyzického zařízení (myš), pomocí něhož uživatel vybírá ikony, položky v menu nebo data.

### Další prvku UI

- tlačítka,
- přepínače,
- popisky,
- checkboxy,
- seznamy,
- slidery,
- výběr souboru,
- vstupní pole pro text

### Režim oken aplikace

- **Single-Document Interface** (SDI): Jedno primární okno, několik sekundárních. Jednoznačný vztah okna s objektem. **Přehledné, srozumitelné**. **Každé okno má své menu**. Několik instancí aplikace v liště OS. (Excel 2013)
![[media/szz-13/media/image3.png]]
- **Multiple-Document Interface** (MDI): Jedna aplikace **obsahuje více oken.** Práce s jedním objektem z více pohledů (otevřený ve více oknech) nebo práce s více objekty současně (možnost při práci s jedním nahlížet na druhý). Menší přehlednost a obtížnější zvládnutí. (Excel 2010)
![[media/szz-13/media/image2.png]]
- **Tabbed Document Interface** (TDI) - prohlížeče, editory zdrojových kódů, … Dnes často používané. Řízené SDI - SDI doplněné o řídící okno, které obsahuje menu a seznam otevřených objektů (záložek). Kooperativní SDI - některé funkce mohou ovlivnit obsah i jiných oken. (jednotlivé dokumenty v záložkách)

Vzor MVC (model-view-controller)

je softwarová architektura, která rozděluje datový model aplikace, uživatelské rozhraní a řídicí logiku do tří nezávislých komponent tak, že modifikace některé z nich má jen minimální vliv na ostatní

- model - reprezentace informací (dat), s nimiž aplikace pracuje
- view (pohled) - převádí data reprezentovaná modelem do podoby vhodné k interaktivní prezentaci uživateli
- controller (řadič) - reaguje na události (typicky od uživatele) a zajišťuje změny v modelu, na základě těchto změn se aktualizuje samotný pohled

![[media/szz-13/media/image1.png]]

**Odkazy:**

[<u>https://www.fit.vutbr.cz/study/courses/ITU/private/lectures/zaklady/itu-zaklady_GUI_a_historie.pdf</u>](https://www.fit.vutbr.cz/study/courses/ITU/private/lectures/zaklady/itu-zaklady_GUI_a_historie.pdf)

https://cs.wikipedia.org/wiki/Model-view-controller

## Zdroje

- SZZ okruh 13 — studijní materiály FIT BUT (`szz-13.docx`). Další obrázky: `media/szz-13/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/12-3d-transformace-pipeline|12. Transformace 3D modelů]] · další: [[okruhy/14-spektralni-analyza|14. Spektrální analýza]] ▶
