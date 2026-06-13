---
title: "20. Boolovy algebry"
category: okruh
okruh: 20
tags: [math, boolean-algebra, discrete-math]
aliases: [Booleova algebra, svaz, distributivní komplementární svaz, De Morgan, Shefferova funkce, Peirceova funkce]
relationships:
  - target: "[[okruhy/16-mnoziny-relace-zobrazeni]]"
    type: related_to
  - target: "[[okruhy/08-minimalizace-logickych-vyrazu]]"
    type: related_to
  - target: "[[okruhy/01-polovodicove-prvky-cmos]]"
    type: related_to
sources: ["_sources/docx/szz-20.docx"]
summary: Booleova algebra jako distributivní komplementární svaz (šestice B,∧,∨,¬,0,1), její axiomy a zákony (De Morgan), modely (výroky, množiny, obvody) a úplné systémy spojek (NAND, NOR).
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

# 20. Boolovy algebry

> SZZ okruh 20 (FIT BUT). Algebraická struktura zobecňující množinové a logické operace.

## Shrnutí

### Booleova algebra
- **Šestice (B, ∧, ∨, ¬, 0, 1)** — **distributivní komplementární svaz**; ∧ vrací **infimum**, ∨ **supremum**.
- **Axiomy**: uzavřenost, komutativita, distributivita, neutralita 0/1, komplementárnost, nedegenerovanost (0 ≠ 1).
- **Zákony**: asociativita, absorpce, idempotence, agresivita 0/1, dvojitá negace, **De Morgan** (¬(x∨y)=¬x∧¬y, ¬(x∧y)=¬x∨¬y).
- Souvisí s [[okruhy/16-mnoziny-relace-zobrazeni|uspořádáním a svazy]] (Hasseův diagram, reflexivita/antisymetrie/tranzitivita).

> [!note] Ke kontrole
> Zdroj nejprve píše, že infimum/supremum vrací „menší/větší z operandů" — to je **nepřesné** (a sám zdroj to o pár řádků níže opravuje): infimum = **největší dolní závora**, supremum = **nejmenší horní závora** obou prvků, ne nutně jeden z nich. Drž se opravené definice.

### Funkce a úplné systémy
- Nad 2 proměnnými lze realizovat **(2²)² = 16** funkcí (AND, OR, NOT, XOR, NAND, NOR, XNOR, …).
- **Shefferova (NAND, ↑)** i **Peirceova (NOR, ↓)** funkce jsou samostatně **funkčně úplné** — vyjádří všechny ostatní (využití v [[okruhy/01-polovodicove-prvky-cmos|CMOS]]).
- Modely BA: algebra výroků, množinová algebra, spínací (switching) algebra obvodů.

## Časté otázky u zkoušky

*Na co se u tohoto okruhu typicky ptají. Plné odpovědi níže.*

**Booleova algebra** ↪ [[#Booleova algebra]]
- *Definice (šestice)?* → (B, ∧, ∨, ¬, 0, 1), distributivní komplementární svaz; ∧ = infimum, ∨ = supremum.
- *Axiomy a zákony?* → uzavřenost, komutativita, distributivita, neutralita 0/1, komplementárnost + odvozené (absorpce, idempotence, De Morgan).
- *De Morgan?* → ¬(x∨y) = ¬x∧¬y; ¬(x∧y) = ¬x∨¬y.

**Použití a modely** ↪ [[#Booleova algebra]]
- *Příklady BA?* → výroky (0/1, ∧∨¬), množiny (∅/U, ∩∪doplněk), elektrické obvody (low/high, AND/OR/NOT).
- *Kolik funkcí 2 proměnných?* → (2²)² = 16.

**Svazy a uspořádání** ↪ [[#Booleova algebra]]
- *Vztah BA a svazu?* → BA = distributivní komplementární svaz; svaz = uspořádaná množina, kde každé dva prvky mají supremum i infimum.
- *Vlastnosti uspořádání?* → reflexivita, antisymetrie, tranzitivita (znázornění Hasseovým diagramem).

**Úplné systémy spojek** ↪ [[#Funkce a úplné systémy]]
- *Shefferova/Peirceova funkce?* → NAND i NOR jsou samostatně funkčně úplné — vyjádří libovolnou logickou funkci.

## Plné znění (ke studiu)

**Booleova algebra** je algebraická struktura se dvěma binárními (**∧**, **∨**) a jedním unárním operátorem (**¬**). Jedná se o **distributivní komplementární svaz**. **Zobecňuje** **vlastnosti** **množinových a** **logických** **operací**. Používá se k reprezentaci pravdivostních hodnot a logických funkcí.

Booleova algebra je **šestice** **(B, ∧, ∨, ¬, 0, 1)**, kde:

- B je neprázdná množina,
- 0 ∈ B a je nejmenší prvek,
- 1 ∈ B a je největší prvek,
- ∧ je **binární** operace **průsek**,
- ∨ je **binární** operace **spojení**,
- ¬ je **unární** operace **doplňku**.

Jelikož Booleova algebra je svaz (a tedy částečně seřazená množina) **průsek** vrací právě ***infimum*** (menší z operandů a∧b) a **spojení** vrací právě ***supremum*** (větší z operandů a∨b).

**Pozor: Boolova algebra v kontexte IDM/IZLO je ešte trochu rozšírená:**

Boolova algebra je totiž aj synonymum pre “Boolov zväz”. [<u>https://en.wikipedia.org/wiki/Boolean_algebra\_(structure)</u>](https://en.wikipedia.org/wiki/Boolean_algebra_(structure))

Je preto potrebné si pozrieť pojmy ako **čiastočne usporiadaná množina**, **zväz**, a pojmy ako **infimum**, **supremum**, **komplementarita**, **distributivita**, a tak ďalej. Práve toto sa pýtali na štátniciach u tejto otázky. Zvyšok tohto dokumentu o niektorých veciach hovorí tiež, no nepriamo. Napríklad text hore hovorí o infime a supremu zle - nie vždy vracia menší/väčší z operandov, ale vracia najbližší menší než oba dva alebo najbližší väčší než oba dva.

### Axiomy

- **Uzavřenost**: Uzavřenost operací na množině B **(a+b) ∈ B**, **(aᐧb)** **∈ B**, **¬a ∈ B** (a, b ∈ B).
- **Komutativita:** Binární operace u níž **nezáleží na pořadí prvků**. $x \lor y = y \lor x, \quad x \land y = y \land x$
- **Distributivita**: Binární operaci je možné distribuovat přes jinou operaci. Operaci **průsek** je možné **distribuovat** **přes** operaci **spojení** a operaci **spojení přes** operaci **průsek**. $x \lor (y \land z) = (x \lor y) \land (x \lor z), \quad x \land (y \lor z) = (x \land y) \lor (x \land z)$
- **Neutralita 0 a 1**: **0** je neutrální prvek pro operaci **spojení** a **1** je neutrální prvek pro operaci **průsek**. $x \lor 0 = x, \quad x \land 1 = x$
- **Komplementárnost:** existence doplňku (komplementu) $x \lor \lnot x = 1, \quad x \land \lnot x = 0$
- **Nedegenerovanost**: množina B obsahuje alespoň dva různé prvky (0 != 1), někdy je připouštěna tzv. **triviální BA** pouze s jedním prvkem, pak platí **0 == 1** a všechny operace na BA vrací stejnou hodnotu.

### Vlastnosti / Teorémy

- **Asociativita**: u operace nezáleží, jak jsou použity závorky u více operandů (někde nebývá jako axiom). $a \lor (b \lor c) = (a \lor b) \lor c, \quad a \land (b \land c) = (a \land b) \land c$
- **Absorpce**: $a \lor (a \land b) = a, \quad a \land (a \lor b) = a$
- **Agresivita nuly** - Při průseku jakéhokoliv prvku s 0, je výsledek 0. $x \land 0 = 0$
- **Agresivita jedničky** - Při spojení jakéhokoliv prvku s 1, je výsledek 1. $x \lor 1 = 1$
- **Idempotence** - Opakovaným použitím na nějaký vstup vznikne stejný výstup. Tedy jakákoliv binární operace prvku se sebou samým má za výsledek ten stejný prvek. $x \lor x = x, \quad x \land x = x$
- **Absorpce** **negace** $x \lor (\lnot x \land y) = x \lor y, \quad x \land (\lnot x \lor y) = x \land y$
- **Dvojitá negace** $\lnot(\lnot x) = x$
- **0 a 1 jsou vzájemně komplementární** $\lnot 0 = 1, \quad \lnot 1 = 0$
- **De Morganovy zákony** $\lnot x \land \lnot y = \lnot(x \lor y), \quad \lnot x \lor \lnot y = \lnot(x \land y)$

### Příklady Booleových algeber

- **triviální algebry:**
  - **0 = 1** (obsahují pouze jeden prvek)
  - všechny operace dávají stejný výsledek
- **algebry výroků**:
  - **0 - false** (nepravda), **1 - true** (pravda),
  - **∧ - konjunkce**, **∨ - disjunkce**, **¬ - negace**
- **množinová algebra**:
  - **0 - prázdná množina** (Ø), **1 - univerzum** (U),
  - **∧ - průnik**, **∨ - sjednocení**, **¬ - doplněk**
- **algebry elektrických obvodů**:
  - **0 - low** (log. 0), **1 - high** (log. 1)
  - **∧ - AND**, **∨ - OR**, **¬ - NOT**

### Funkce

Na Booleově algebrách lze realizovat $(2^2)^2$, tedy **16** funkcí (Dva operandy, každý s dvěma možnými hodnotami: $2^2$ možných kombinací vstupů. Každý výstup těchto kombinací může nabývat dvou možných hodnot. Celkem tedy Booleovy algebry mohou realizovat $(2^2)^2 = 16$ možných operací.).

Přehled všech 16 funkcí dvou proměnných:

| Funkce | Název funkce | Logický člen | Algebraický výraz |
|--------|--------------|--------------|-------------------|
| $f_0$ | konstanta | | $0$ |
| $f_1$ | logický součet | NEBO (OR, ODER) | $a + b$ |
| $f_2$ | implikace | | $\bar a + b$ |
| $f_3$ | implikace | | $a + \bar b$ |
| $f_4$ | Shefferova funkce | NAND | $\bar a + \bar b = \overline{ab}$ |
| $f_5$ | logický součin | A (AND, UND) | $ab$ |
| $f_6$ | inhibice | | $\bar a b$ |
| $f_7$ | inhibice | | $a \bar b$ |
| $f_8$ | Peirceova funkce | NOR | $\bar a \cdot \bar b = \overline{a + b}$ |
| $f_9$ | identita | | $a$ |
| $f_{10}$ | identita | | $b$ |
| $f_{11}$ | ekvivalence | | $ab + \bar a \bar b$ |
| $f_{12}$ | neekvivalence | Exclusive OR | $\bar a b + a \bar b$ |
| $f_{13}$ | negace | NE (NOT, NICHT) | $\bar a$ |
| $f_{14}$ | negace | NE (NOT, NICHT) | $\bar b$ |
| $f_{15}$ | konstanta | | $1$ |

- **NOT** - Negace (doplněk)

![[media/szz-20/media/image10.png]]

- **Opakovač** - Realizuje funkci **identity**. Lze použít jako **buffer**.

![[media/szz-20/media/image8.png]]

- **OR** - Disjunkce (spojení)

![[media/szz-20/media/image15.png]]

- **AND** - Konjunkce (průnik)

![[media/szz-20/media/image17.png]]

- **XOR** - negovaná ekvivalence - **Exkluzivní disjunkce**

![[media/szz-20/media/image2.png]]

- **NOR** - Negovaná disjunkce - **Peirceova funkce**

![[media/szz-20/media/image14.png]]

- **NAND** - Negovaná konjunkce - **Shefferova funkce**

![[media/szz-20/media/image4.png]]

- **XNOR** - negovaná exkluzivní disjunkce - **Ekvivalence**

![[media/szz-20/media/image1.png]]

### Shefferova funkce

Pomocí Shefferovy funkce lze vyjádřit všechny ostatní funkce Booleovy algebry, viz:

**¬p ≡ ¬(p∧p)**

**p∧q ≡ ¬(¬(p∧q)) ≡ ¬(¬(p∧q)∧¬(p∧q)))**

**p∨q ≡ ¬(¬p∧¬q) ≡ ¬(¬(p∧p)∧¬(q∧q)))**

**p→q ≡ ¬p∨q ≡ ¬(p∧¬q) ≡ ¬(p∧¬(q∧q)))**

### Peirceova funkce

Pomocí Piercovy funkce lze lze také vyjádřit všechny ostatní funkce Booleovy algebry, viz:

**¬p ≡ ¬(p∨p)**

**p∧q ≡ ¬(¬p∨¬q) ≡ ¬(¬(p∨p)∨¬(q∨q)))**

**p∨q ≡ ¬(¬(p∨q)) ≡ ¬(¬(p∨q)∨¬(p∨q)))**

**p→q ≡ ¬p∨q ≡ ¬(p∨p)∨q ≡ ¬(¬(¬(p∨p)∨q)∨¬(¬(p∨p)∨q)))**

### Vennovy diagramy

Grafické znázornění příslušnosti prvků do množin.

![[media/szz-20/media/image3.png]]

![[media/szz-20/media/image13.png]]

### Switching algebra

Jiný výraz pro Booleovu algebru a vyjadřuje to, že v tomto systému (dvojkový systém) jsou prováděny všechny operace (**AND**, **OR**, **NOT**). Tedy použitím Booleovy algebry děláme výpočty ve dvojkové soustavě.

## Zdroje

- SZZ okruh 20 — studijní materiály FIT BUT (`szz-20.docx`). Obrázky: `media/szz-20/`.

---
**Navigace:** [[index|📋 Přehled okruhů]] · ◀ [[okruhy/19-vyrokova-predikatova-logika|19. Výroková a predikátová logika]] · další: [[okruhy/21-regularni-jazyky|21. Regulární jazyky]] ▶
