---
title: "21. Regulární jazyky a jejich modely (konečné automaty, regulární výrazy)"
category: okruh
okruh: 21
tags: [theory, formal-languages, automata]
aliases: [regulární jazyk, konečný automat, DFA, NFA, regulární výraz, determinizace, pumping lemma]
relationships:
  - target: "[[topics/22-bezkontextove-jazyky]]"
    type: related_to
  - target: "[[topics/03-sekvencni-logicke-obvody]]"
    type: related_to
sources: ["_sources/docx/szz-21.docx"]
summary: Regulární jazyky a tři ekvivalentní modely — konečné automaty (DFA/NFA, determinizace, minimalizace), regulární výrazy a regulární gramatiky; pumping lemma.
provenance:
  extracted: 0.92
  inferred: 0.06
  ambiguous: 0.02
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
tier: supporting
created: 2026-06-03T17:30:00Z
updated: 2026-06-03T17:30:00Z
---

# 21. Regulární jazyky a jejich modely

> SZZ okruh 21 (FIT BUT). Nejjednodušší třída Chomského hierarchie — tři ekvivalentní modely.

## Shrnutí

### Jazyky a regulární jazyk
- **Abeceda** Σ (konečná množina symbolů), **řetězec** (i prázdný ε), **jazyk** L ⊆ Σ*.
- Operace nad jazyky: sjednocení, průnik, rozdíl, doplněk, **konkatenace**, **iterace** (*), reverzace.
- **Regulární jazyk** je ekvivalentně: přijímán **konečným automatem**, značen **regulárním výrazem**, generován **regulární gramatikou**.

### Konečné automaty
- KA = pětice **M = (Q, Σ, R, s, F)**.
- **NFA** (ε-přechody, více přechodů na stejný symbol) × **DFA** (max. 1 přechod) × **úplný DFA** × **minimální** DFA.
- **Determinizace** (NFA→DFA) podmnožinovou (powerset) konstrukcí: až 2ⁿ stavů.

### Regulární výrazy a gramatiky
- RV s operátory **konkatenace (.), sjednocení (+), iterace (*)**; priorita * > . > +.
- **Regulární gramatika** (N,T,P,S) — pravá/levá, generuje regulární jazyk; převoditelná na/z KA.
- **Pumping lemma** — dokazuje (sporem), že jazyk **NENÍ** regulární (nikdy ne že je).

Navazuje na [[topics/22-bezkontextove-jazyky]] (silnější třída), automaty viz [[topics/03-sekvencni-logicke-obvody]], využití v [[topics/23-struktura-prekladace|lexikální analýze]].

## Související syntéza

- [[synthesis/konecne-automaty-napric-obory|Konečné automaty napříč obory]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Konečné automaty** ↪ [[#Konečné automaty]]
- *Formální definice KA?* → Pětice (Q, Σ, R, s, F) — stavy, abeceda, pravidla, počáteční a koncové stavy.
- *DFA vs. NFA?* → NFA: ε-přechody a více přechodů na stejný symbol; DFA: nejvýše jeden přechod.
- *Determinizace NFA→DFA?* → Podmnožinová (powerset) konstrukce, max. 2ⁿ stavů; každý NFA má ekvivalentní DFA.
- *Minimalizace?* → Sloučení nerozlišitelných stavů → jednoznačný minimální DFA.

**Regulární výrazy** ↪ [[#Regulární výrazy a gramatiky]]
- *Operace RV?* → konkatenace, sjednocení (+), iterace (*); příklad a(a+b)*b.
- *Převod RV ↔ KA?* → Vzájemně převoditelné (RV → NFA → DFA).

**Regulární jazyky** ↪ [[#Jazyky a regulární jazyk]]
- *Jazyk, slovo, abeceda?* → Abeceda Σ; slovo ∈ Σ*; jazyk L ⊆ Σ*.
- *Důkaz neregulárnosti?* → Pumping lemma (sporem).

**Gramatiky** ↪ [[#Regulární výrazy a gramatiky]]
- *Regulární gramatika vs. RV?* → RG generuje, RV značí týž regulární jazyk; Chomského hierarchie (RJ ⊂ BKJ ⊂ …).

## Plné znění (ke studiu)

### Abeceda

Konečná, neprázdná množina prvků, které nazýváme symboly. Značíme **Σ**.

### Řetězec

Jakákoliv posloupnost terminálních a neterminálních symbolů (znaků). Nechť Σ je abeceda.

- **ε** je řetězec nad abecedou **Σ.**
  - ε: Prázdný řetězec (prázdné slovo), který ale vyhovuje jazyku (je možné jej vygenerovat a přijmout).
- Pokud **x** je řetězec nad abecedou Σ a **s ∈ Σ**, pak **xs** je **řetězec** nad abecedou **Σ**.

### Jazyk

Nechť **Σ\*** značí **množinu** všech **řetězců** (**slov**) nad **Σ**. Každá **podmnožina L ⊆ Σ\*** je **jazyk** nad **Σ**. Jazyk tedy značí podmnožinu řetězců abecedy. **Počet** všech **slov** jazyka je jeho **kardinalita**.

- **Konečný a nekonečný** - Jazyk **L** je **konečný**, pokud L obsahuje **konečný počet řetězců**, **jinak** je **nekonečný**.
- **Operace nad jazyky**
  - **Sjednocení** - Stejně jako u množin.
  - **Průnik** - Stejně jako u množin.
  - **Rozdíl** - Stejně jako u množin.
  - **Doplněk** - Stejně jako u množin.
  - **Konkatenace** - Nechť **L1** a **L2** jsou dva **jazyky** nad **Σ**. Konkatenace jazyků L1 a L2 je definována jako

> L = L1•L2 = {xy: x ∈ L1 a y ∈ L2 }. Například **L = L1•L2 = {0, 1}•{2, 3} = {02, 03, 12, 13}.**

- **Pozor:** Stejně jako při násobení můžeme konkatenační operátor (**•**) někdy vynechat: $L_1 \cdot L_2 = L_1 L_2$.
- **Pozor:** L{ **ε** } = { **ε** }L = **L**, ale **Ø**L = L**Ø** = **Ø**.

<!-- -->

- **Reverzace** - Nechť **L** je jazyk nad abecedou **Σ**. Reverzace jazyka **L**, **reverse(L)**, je definována: **reverse(L) = {reverse(x): x L}**. Jedná se o převrácení slov abecedy. **reverse({02, 03, 12, 13}) = {20, 30, 21, 31}**.

## Regulární jazyk

Regulární jazyky jsou **nejjednodušší formální jazyky** v rámci **Chomského hierarchie**. Nad abecedou **Σ** je lze zavést následovně:

- Prázdný jazyk **Ø** je regulární.
- Pro každé **a**, **a ∈ Σ**, jazyk **{ a }** je regulární.
- Pokud **A** a **B** **jsou regulární** jazyky, **A ∪ B** (sjednocení), **A • B** (konkatenace), a **A\*** (iterace, umožňuje jazyk prázdného řetězce **{ ε }**) také **regulární**.
- Žádné **další** regulární jazyky **nejsou**.

Dále platí, že jazyk je regulární, pokud:

- existuje **konečný automat** (deterministický i nedeterministický), který **akceptuje** právě všechna slova z tohoto jazyka (**akceptuje/přijímá** tento jazyk),
- existuje **regulární výraz**, který tento jazyk **značí**,
- existuje **regulární gramatika,** která jej **generuje**.

## Konečný automat (KA)

Konečný automat (KA) je **pětice** **M = (Q, Σ, R, s, F)**, kde:

- **Q** je **konečná množina stavů**,
- **Σ** je **vstupní abeceda**,
- **R** je **konečná množina pravidel** tvaru: **pa → q**, kde **p, q ∈ Q, a ∈ Σ ∪ {ε}**,
- **s ∈ Q** je **počáteční stav**,
- **F ⊆ Q** je **množina koncových stavů**.

Graficky KA značíme následovně:
![[media/szz-21/media/image4.png]]

### Přijímaný jazyk KA

Pokud se s nějakou **vstupní posloupností znaků** dostaneme z **počátečního stavu** automatu až do **koncového** **stavu** automatu, automat tento **jazyk přijímá**.

### Ekvivalentní KA

Dva modely pro popis formálních jazyků (např. konečné automaty) jsou ekvivalentní, pokud specifikují **tentýž jazyk**. (Jsou ekvivalentní, pokud oba dokáží zpracovat všechny řetězce z určitého jazyka a odmítnou všechny řetězce, které z daného jazyka nevychází).

### Typy konečných automatů

- **Nedeterministický**: Může obsahovat **ε** přechody a existují stavy, ze kterých lze s načtením **stejného symbolu** přejít do **více stavů**.
- **Bez epsilon přechodů** - Neobsahuje **ε** přechody.
- **Deterministický** - Neobsahuje **ε** přechody a z každého **stavu** může přejít **maximálně** do **jednoho** dalšího s načtením **stejného znaku**.
- **Úplný deterministický** - Pro **každý znak** abecedy existuje **právě jeden** přechod v **každém stavu** (nepotřebné směřují do **false stavu**). **Nemůže se zaseknout**.
- **Dobře specifikovaný** - **Nemá nedostupné** stavy a má maximálně **jeden** **neukončující** stav (false stav). Pro každý konečný automat existuje ekvivalentní dobře specifikovaný konečný automat.
- **Minimální** - Pokud obsahuje pouze rozlišitelné stavy. Pro dobře specifikovaný KA existuje právě jeden minimální KA.
![[media/szz-21/media/image13.png]]

![[media/szz-21/media/image15.png]]

Shrnutí:
![[media/szz-21/media/image2.png]]

### Determinizace KA

Převod nedeterministického KA na deterministický. Pokud má nedeterministický KA **n stavů**, má jeho deterministická varianta nejvíce **$2^n$ stavů**. Každý nedeterministický automat má svoji deterministickou variantu. Postup:

1. Odstranění **ε** přechodů pomocí **ε** uzávěru - množina stavů, do kterých se můžeme dostat přečtením libovolného symbolu z abecedy.
2. Z počátečního stavu vytváříme nové stavy tak, že tyto stavy jsou množinou stavů, do kterých se můžeme dostat přečtením libovolného symbolu (prázdné stavy neuvažujeme). Z takto vzniklých nových stavů postupujeme dále obdobně (je nutné dávat pozor, aby byly brány v potaz všechny výstupy vzniklé množiny stavů). Za nové koncové stavy označíme ty, které obsahují alespoň jeden původní koncový stav.
![[media/szz-21/media/image7.png]]

Shrnutí:
![[media/szz-21/media/image3.png]]

![[media/szz-21/media/image12.png]]

## Regulární výraz (RV)

Jedná se o výrazy s operátory **“.”**, **“+”**, **“\*”**, které značí v tomto pořadí **konkatenaci**, **sjednocení** a **iteraci**. Nechť **Σ** je **abeceda**. Regulární výrazy nad abecedou **Σ** a **jazyky**, které **značí**, jsou definovány následovně:

- **∅** je **RV** značící prázdnou množinu (**prázdný jazyk**),
- **ε** je **RV** značící jazyk **{ ε },**
- **a**, kde **a ∈ Σ**, je **RV** značící jazyk **{ a }**,
- Nechť **r** a **s** jsou regulární výrazy značící po řadě jazyky **Lr** a **Ls**, potom:
  - **(r.s)** je RV značící jazyk **L = LrLs**,
  - **(r+s)** je RV značící jazyk **L = Lr ∪ Ls**,
  - **(r\*)** je RV značící jazyk **L = Lr\***.

Závorky lze redukovat zavedením priority operátorů:
![[media/szz-21/media/image16.png]]

Příklady RV:
![[media/szz-21/media/image17.png]]

-------------------------------------------------------------------------------------

Převod regulárního výrazu na konečný automat

![[media/szz-21/media/image14.png]]

-------------------------------------------------------------------------------------

## Regulární gramatika

Každá **regulární gramatika generuje regulární jazyk.** Je to čtveřice: **(N, T, P, S)**

- N - Konečná množina neterminálních symbolů,
- T - Konečná množina terminálních symbolů,
- P - Konečná množina pravidel, ve tvaru:
  -
![[media/szz-21/media/image10.png]]
(w je řetězec)

  -
![[media/szz-21/media/image5.png]]

  -
![[media/szz-21/media/image1.png]]
, poté se však nesmí S vyskytovat na pravé straně pravidla.

- S - Počáteční symbol (S náleží do N).

Existují **pravé** (
![[media/szz-21/media/image11.png]]
) a **levé** (
![[media/szz-21/media/image9.png]]
) **regulární gramatiky**, které jsou si **ekvivalentní**.

Příklady:

Oproti zápisu výše (N,T,P,S) jsou v zápisu příkladu prohozeny množiny terminálních a neterminálních symbolů ve formě (T,N,P,S).
![[media/szz-21/media/image8.png]]

![[media/szz-21/media/image6.png]]

### Pumping lemma

Používá se k dokázání, že jazyk **NENÍ REGULÁRNÍ** (důkaz se provádí sporem). **Nemůže** tedy dokázat, že jazyk je regulární. Nechť jazyk **L** je **RJ**. Pak existuje **k ≥ 1** takové, že: pokud **z ∈ L** a **\|z\| ≥ k**, pak existuje **u, v, w: z = uvw**,

- **v ≠ ε**
- **\|uv\| ≤ k**
- pro každé $m \geq 0$, $u v^m w \in L$

[<u>Pumping Lemma (For Regular Languages) \| Example 1</u>](https://youtu.be/Ty9tpikilAo)

**Odkazy**

- Definice z IFJ: [<u>IFJ Teorie</u>](https://docs.google.com/document/d/1nzEwq6uh9h_uMPvk_CWUCTdrLufUaEcmnO9mBPwzzyE/edit?usp=sharing)
- [<u>Minimalizace a kanonizace, nedeterministické konecné automaty a determinizace</u>](https://is.muni.cz/el/1433/podzim2017/IB102/um/slajdy4.pdf)

## Zdroje

- SZZ okruh 21 — studijní materiály FIT BUT (`szz-21.docx`). Obrázky: `media/szz-21/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[topics/20-boolovy-algebry|20. Boolovy algebry]] · další: [[topics/22-bezkontextove-jazyky|22. Bezkontextové jazyky]] ▶
