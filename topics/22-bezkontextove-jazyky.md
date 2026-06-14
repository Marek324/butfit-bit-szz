---
title: "22. Bezkontextové jazyky a jejich modely (zásobníkové automaty, bezkontextové gramatiky)"
category: okruh
okruh: 22
tags: [theory, formal-languages, automata]
aliases: [bezkontextový jazyk, bezkontextová gramatika, BKG, zásobníkový automat, derivační strom, derivace]
relationships:
  - target: "[[topics/21-regularni-jazyky]]"
    type: extends
  - target: "[[topics/23-struktura-prekladace]]"
    type: related_to
sources: ["_sources/docx/szz-22.docx"]
summary: Bezkontextové jazyky generované bezkontextovou gramatikou (G=N,T,P,S) a přijímané zásobníkovým automatem (sedmice); derivace, srovnání s regulárními jazyky, modely pro syntaktickou analýzu.
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

# 22. Bezkontextové jazyky a jejich modely

> SZZ okruh 22 (FIT BUT). Silnější třída než [[topics/21-regularni-jazyky|regulární jazyky]] — gramatika + zásobníkový automat.

## Shrnutí

### Bezkontextová gramatika
- **G = (N, T, P, S)** — neterminály, terminály (N∩T=∅), pravidla **A → x** (A∈N, x∈(N∪T)*), počáteční symbol.
- Typický BKJ: **L = {aⁿbⁿ | n ≥ 0}** (neregulární).
- **Derivace** (nejlevější/nejpravější), **derivační strom**.

### Zásobníkový automat
- **M = (Q, Σ, Γ, R, s, S, F)** — konečný automat + **zásobník**; pravidlo Apa → wq.
- Přijetí: **koncovým stavem**, **vyprázdněním zásobníku**, nebo obojím — všechny **ekvivalentní**.
- **DZA** (deterministický) je **slabší** než nedeterministický ZA. **RZA** (čte celý řetězec z vrcholu) je ZA ekvivalentní.

### Srovnání jazyků
- RJ ⊂ BKJ. Příklady: a* (oba), aⁿbⁿ (jen BKJ), aⁿbⁿcⁿ (ani jeden).
- ZA/RZA **simulují konstrukci derivačního stromu** pro [[topics/23-struktura-prekladace|syntaktickou analýzu]] (shora dolů = expanze, zdola nahoru = shift/redukce).

## Související syntéza

- [[synthesis/konecne-automaty-napric-obory|Konečné automaty napříč obory]] — syntéza
- [[synthesis/zasobnik-napric-obory|Zásobník napříč obory]] — syntéza

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Bezkontextová gramatika** ↪ [[#Bezkontextová gramatika]]
- *Definice, tvar pravidla?* → Čtveřice (N,T,P,S); pravidlo A → x, kde A je neterminál, x řetězec terminálů/neterminálů.
- *Co generuje, příklad?* → Množinu řetězců derivovatelných z S; klasicky aⁿbⁿ.
- *Derivační strom / krok?* → Postupné přepisování neterminálů (nejlevější/nejpravější derivace).

**Zásobníkový automat** ↪ [[#Zásobníkový automat]]
- *Definice (sedmice)?* → (Q, Σ, Γ, R, s, S, F) — konečný automat se zásobníkem.
- *Jak přijímá jazyk?* → koncovým stavem / vyprázdněním zásobníku / obojím (ekvivalentní).

**Srovnání** ↪ [[#Srovnání jazyků]]
- *RJ vs. BKJ?* → Každý RJ je BKJ, ne naopak (aⁿbⁿ je BKJ, ne RJ); aⁿbⁿcⁿ není ani BKJ.
- *Proč „bezkontextový"?* → Pravidlo přepisuje neterminál bez ohledu na okolní kontext.

## Plné znění (ke studiu)

## Bezkontextový jazyk (BKJ)

Jedná se o formální jazyk, pro který platí:

- **Generuje** jej **bezkontextová gramatika**,
- **Přijímá** (akceptuje) jej **zásobníkový automat**.

## Bezkontextová gramatika

Slouží pro **generování BKJ**. Je to **čtveřice** **G = (N, T, P, S)**, kde:

- **N** - abeceda **neterminálů**,
- **T** - abeceda **terminálů**, přičemž **N ∩ T = ∅**,
- **P** - konečná **množina pravidel** tvaru **A → x**,

> kde **A ∈ N, x ∈ (N ∪ T)\***,

- **S** - počáteční neterminál, **S ∈ N**.

Nejznámějším bezkontextovým jazykem je jazyk $L(G) = \{a^n b^n : n \geq 0\}$
![[media/szz-22/media/image6.png]]

### Derivační krok BKG

Jedná se o změnění řetězce použitím pravidla na neterminál. Pokud **uAv ⇒ uxv** v **G**, můžeme říct, že **G** provádí derivační krok z **uAv** do **uxv**.
![[media/szz-22/media/image19.png]]

![[media/szz-22/media/image10.png]]

![[media/szz-22/media/image1.png]]

- **Nejlevější derivace**: Během nejlevějšího derivačního kroku je přepsán nejlevější neterminál.
- **Nejpravější derivace**: Během nejpravějšího derivačního kroku je přepsán nejpravější neterminál.
![[media/szz-22/media/image12.png]]

![[media/szz-22/media/image17.png]]

![[media/szz-22/media/image7.png]]

## Zásobníkový automat

Konečný automat rozšířený o **zásobník**. Pro každou **BKG** **existuje** zásobníkový **automat,** který **ji přijímá**. Zásobníkový automat (ZA) je **sedmice**:

**M = ( Q, Σ, Γ, R, s, S, F)**, kde:

- **Q** je konečná **množina stavů**,
- **Σ** je **vstupní abeceda**,
- **Γ** je **zásobníková abeceda**,
- **R** je konečná **množina pravidel** tvaru **Apa→wq**, kde **A ∈ Γ**; **p,q ∈ Q;**

> **a ∈ Σ ∪ {ε}**, **w ∈ Γ\***, (R je konečná relace z Γ × Q × (Σ ∪ {ε}) do Γ\* × Q)

- **s** ∈ Q je **počáteční stav**,
- **S** ∈ Γ je **počáteční symbol na zásobníku**,
- **F** ⊆ Q je **množina koncových stavů**.

**Interpretace pravidel**: **Apa → wq** **∈ R** znamená, že pokud je aktuální stav **p**, aktuální symbol na vstupní pásce **a** a symbol na vrcholu zásobníku **A**, potom zásobníkový automat může přečíst **a** a na zásobníku nahradit **A** za **w** a přejít ze stavu **p** do **q**.
![[media/szz-22/media/image9.png]]

![[media/szz-22/media/image8.png]]

### Typy přijímaných jazyků ZA

- **Přechodem do koncového stavu**: **ZA M** přijímá jazyk **L**, pokud se čtením všech řetězců jazyka **L** dostane do koncového stavu.
- **Vyprázdněním zásobníků**: **ZA M** přijímá jazyk **L**, pokud se čtením všech řetězců jazyka **L** vyprázdní jeho zásobník.
- **Přechodem do koncového stavu a vyprázdněním zásobníku**: přijímá jazyk **L**, pokud se čtením všech řetězců jazyka **L** dostane do koncového stavu **a současně** se vyprázdní jeho zásobník.

Tyto tři typy ZA jsou si **ekvivalentní** a **existují** algoritmy pro **převody** mezi nimi.

### Konfigurace ZA

Konfigurace **ZA M** je řetězec **χ ∈ Γ\*QΣ\***. Jedná se o **aktuální stav zásobníku**, **aktuálního stavu** a **vstupní pásky**, jejíž část **nebyla** ještě **přečtena**.

### Deterministický zásobníkový automat (DZA)
![[media/szz-22/media/image15.png]]

Může provést z každé konfigurace **maximálně jeden přechod**. **M** je deterministický **ZA**, pokud pro každé pravidlo tvaru **Apa → wq ∈ R** platí, že množina **R \\ {Apa → wq}** (množinový rozdíl) neobsahuje **žádné pravidlo** s levou stranou **Apa** nebo **Ap**. Jinak řečeno, **levá strana** pravidel je v množině **R** vždy **pouze jednou** – **je unikátní**. **DZA** je **podmnožinou ZA**, DZA nemusí přijímat některé jazyky, která ZA přijímá → **ZA je silnější než DZA**.

### Rozšířený zásobníkový automat (RZA)
![[media/szz-22/media/image13.png]]

Z vrcholu zásobníku v **RZA** lze číst **celý řetězec** (v ZA to byl pouze jeden symbol). Pravidla jsou tak definována takto: **R** je **konečná** množina pravidel tvaru: **vpa → wq**, kde **v, w ∈ Γ\***; **p, q ∈ Q**; **a ∈ Σ ∪ {ε}**. RZA je **ekvivalentní** s ZA (jsou stejně silné).

Mohou existovat **RZA**, které **přijímají jazyky přechodem do koncového stavu**, **vyprázdněním zásobníku** nebo vyprázdněním zásobníku a současně přechodem do koncového stavu. Opět jsou tyto typu RZA ekvivalentní. Následuje příklad RZA.
![[media/szz-22/media/image3.png]]

## RZA a ZA jako modely pro synt. analýzu

**RZA** nebo **ZA** mohou **SIMULOVAT konstrukci derivačního stromu** pro **BKG**. Používají se k tomu dva přístupy:
![[media/szz-22/media/image18.png]]

### Převod z BKG na RZA (pro SA zdola nahoru)

1. obrázek je pro SA zdola nahoru, 2. pro SA shora dolů.

Např. (pořadí obrázků zůstává):
![[media/szz-22/media/image16.png]]

![[media/szz-22/media/image2.png]]

![[media/szz-22/media/image4.png]]

![[media/szz-22/media/image11.png]]

![[media/szz-22/media/image5.png]]

### Modely pro syntaktickou analýzu shora dolů
![[media/szz-22/media/image14.png]]

**ZA M = (Q, Σ, Γ, R, s, S , F)** (F = prázdná množina) a **BKG G = (N, T, P, S)**

1. **M** obsahuje **porovnávací pravidla**, která **porovnají** symbol z vrcholu **zásobníku** a aktuální symbol ze **vstupní pásky**. (tvorba: pro každé a ∈ Σ: přidej asa → s do R)
2. **M** obsahuje **expanzivní pravidla**, která **simulují gramatická pravidla**. (tvorba: pro každé **A → t1…tn ∈ P** v **G**, přidej **As → tn…t1s** do **R**; = **reversal(t1…tn)**)

Jinak řečeno:

Z počátečního neterminálu **S**, který přepisujeme na jiné neterminály a terminály, se snažíme dostat k řetězci, který načítáme. Potřebujeme k tomu dva druhy pravidel:

1. Pravidla, které přepíší neterminál z vrcholu zásobníků na jiný neterminál/neterminály nebo přímo načítané znaky řetězce, tak aby byl **první znak** řetězce **na vrcholu zásobníku** (na zásobník jsou zapisovány od konce - reversal),
2. pravidla, která kontrolují, jestli jsou načítaný znak a znak na zásobníku stejný.

### Modely pro syntaktickou analýzu zdola nahoru

**RZA M = (Q, Σ, Γ, R, s, \#, F)** (# je počáteční symbol na zásobníku, s je počáteční stav) a **BKG G = (N, T, P, S)**.

1. **M** obsahuje **shiftovací pravidla**, která **přesouvají** vstupní symboly **na zásobník**. (tvorba: Pro každé **t ∈ Σ**: přidej **st → ts** do **R**.)
2. **M** obsahuje **redukční pravidla**, která simulují **aplikaci gramatických pravidel** pozpátku. (tvorba: Pro každé **A → x ∈ P v G**: přidej **xs → As** do **R**)
3. **M** také obsahuje **speciální pravidlo \#Ss → f**, pomocí kterého provede **M** přechod do **koncového stavu**.

Jinak řečeno:

Načítáním symbolů se snažíme dostat do takového stavu, že na zásobníku jsou pouze symboly **\#** (dno zásobníku) a **S** (kořenový neterminál derivačního stromu, syntaktickou analýzou se snažíme dokázat, že použitím vhodných pravidel se lze z S dostat ke čtenému řetězci). Potřebujeme k tomu dva druhy pravidel:

1. Pravidla, která si **zapamatují již přečtené znaky** (tj. uloží je na zásobník),
2. pravidla, která **identifikují správné posloupnosti zapamatovaných znaků a neterminálů** (tj. symbolů na zásobníku) a přepíší je na neterminál.

**odkazy:**

- Definice z IFJ: [<u>IFJ Teorie</u>](https://docs.google.com/document/d/1nzEwq6uh9h_uMPvk_CWUCTdrLufUaEcmnO9mBPwzzyE/edit?usp=sharing)

## Zdroje

- SZZ okruh 22 — studijní materiály FIT BUT (`szz-22.docx`). Obrázky: `media/szz-22/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[topics/21-regularni-jazyky|21. Regulární jazyky]] · další: [[topics/23-struktura-prekladace|23. Struktura překladače]] ▶
