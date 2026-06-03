---
title: Tag Taxonomy
---

# Tag Taxonomy — szz (FIT BUT státnice)

Controlled vocabulary for wiki tags. Rules: **max 5 tags per page**, lowercase, hyphenated, prefer broad over narrow. `visibility/` tags are system tags and don't count toward the limit.

## Canonical tags

### Hardware & architecture
- `hardware` — physical electronics, circuits, devices
- `electronics` — semiconductors, analog circuitry
- `digital-logic` — gates, combinational/sequential circuits, minimization
- `computer-architecture` — CPU, memory, IO organization
- `cpu` — processor internals, pipelining, instruction sets
- `memory` — memory types, cache, hierarchy
- `io` — peripherals, buses, interrupts, DMA
- `embedded` — embedded systems, microcontrollers
- `fpga` — programmable logic arrays
- `hdl` — hardware description languages (VHDL, Verilog)
- `number-representation` — integer/float encodings, IEEE 754

### Math & theory
- `math` — general mathematics
- `boolean-algebra` — Boolean algebra, logic functions

### Signals & graphics
- `dsp` — digital signal processing
- `signals` — signal theory, sampling
- `fourier` — Fourier analysis, transforms
- `computer-graphics` — 2D/3D graphics, rendering

### Software
- `software-engineering` — SW lifecycle, design, modeling
- `gui` — user interfaces

## Aliases (map → canonical)
- `electronics-devices`, `polovodice` → `electronics`
- `architecture` → `computer-architecture`
- `cache`, `pamet` → `memory`
- `grafika` → `computer-graphics`
- `signal-processing` → `dsp`

## Notes
- New domains will be added as topics 16–44 are ingested (expect: `formal-languages`, `compilers`, `algorithms`, `databases`, `networking`, `operating-systems`, `ai`, `machine-learning`, `statistics`, `probability`, `numerical-methods`, `graph-theory`).
