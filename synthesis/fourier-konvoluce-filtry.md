---
title: Spektrální analýza × konvoluce × číslicové filtry
category: synthesis
tags: [dsp, signals, fourier]
sources: ["topics/14-spektralni-analyza.md", "topics/15-cislicove-filtry.md"]
summary: Spektrální analýza a číslicové filtry jsou dvě poloviny jednoho příběhu spojené konvolučním teorémem; FFT je to, co celý vztah dělá prakticky použitelným.
provenance:
  extracted: 0.2
  inferred: 0.7
  ambiguous: 0.1
base_confidence: 0.37
lifecycle: draft
lifecycle_changed: 2026-06-03
created: 2026-06-03T19:30:00Z
updated: 2026-06-03T19:30:00Z
---

# Spektrální analýza × konvoluce × číslicové filtry

## Spojení

[[topics/14-spektralni-analyza|Okruh 14]] (spektrální analýza) a [[topics/15-cislicove-filtry|okruh 15]] (číslicové filtry) se na první pohled učí zvlášť, ale jsou to **dvě poloviny téhož**, slepené **konvolučním teorémem**:

- **Impulsní odezva h[n]** plně definuje LTI filtr v **časové** doméně (okruh 15).
- Její **Fourierova/Z-transformace** je **frekvenční charakteristika / přenosová funkce** — týž filtr ve **frekvenční** doméně.
- Spektrální analýza (okruh 14) je nástroj, kterým se mezi těmito doménami pohybujeme.

## Kde se potkávají

- **Konvoluce** je definovaná v obou okruzích: v 15 jako operace filtru (výstup = vstup ∗ h[n]), ve 14 jako aplikace FFT.
- **Jednotkový impuls** má ve frekvenci hodnotu 1 pro všechny frekvence (okruh 15) — proto impulsní odezva „obsahuje vše" a definuje systém.

## Průřezový poznatek

**„Navrhnout filtr" a „analyzovat spektrum" jsou tatáž operace ve dvou doménách; konvoluční teorém je most a FFT ho dělá levným.** ^[inferred]

- **Filtrace v čase = konvoluce** s h[n]; **filtrace ve frekvenci = násobení** přenosovou funkcí H(ω). Je to jeden děj, jen jednou jako konvoluce (drahá, O(n²)) a jednou jako násobení (levné).
- **FFT** (okruh 14) je důvod, proč je to v praxi proveditelné: převede konvoluci na O(n·log n) (FFT → vynásob → IFFT). Bez FFT by byl celý vztah jen teorie.
- Proto komprese (JPEG/MP3) i reálná DSP filtrace stojí na témže: převod do frekvence → zahození/úprava složek → zpět. ^[inferred]

## Napětí a kompromisy

- **Časová vs. frekvenční doména**: krátká h[n] (FIR) se snadno konvoluuje přímo; dlouhá konvoluce se vyplatí dělat přes FFT. Hranice „kdy se vyplatí přejít do frekvence" je praktický kompromis.
- **FIR vs. IIR** (okruh 15): IIR má nekonečnou h[n] (rekurze) → nelze ji přímo konvoluovat konečně; nutno přes přenosovou funkci / diferenční rovnici. Frekvenční pohled je tu nutnost, ne volba.

## Otevřené otázky

- Vztah DCT (reálně použité v JPEG) vs. DFT/FFT — okruh 14 uvádí FFT, ale JPEG používá DCT; kdy se který hodí?

## Související

- [[topics/14-spektralni-analyza]]
- [[topics/15-cislicove-filtry]]
