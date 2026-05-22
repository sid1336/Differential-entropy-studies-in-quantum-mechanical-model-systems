# Differential Entropy Studies in Quantum Mechanical Model Systems

This project studies how differential Shannon entropy can be used to understand the time evolution of simple quantum mechanical wave packets.

The main idea is to start with systems where the wavefunction and probability density can be written down clearly, then calculate how the entropy changes over time. Right now, the project focuses on Gaussian wave packets, including the free-particle Gaussian wave packet and the translated harmonic-oscillator ground state.

For the free Gaussian wave packet, the position-space density spreads with time, so the position entropy increases. For the translated harmonic-oscillator ground state, the center of the packet moves, but the width stays fixed, so the entropy remains constant.

The goal of these early calculations is to build intuition before moving into more complicated systems, especially wave packets in a Morse potential. The Morse potential will be used later as a model for vibrational motion in diatomic molecules. At that stage, the time-dependent Schrödinger equation will be solved numerically, and the entropy will be analyzed from the resulting wave packets.

## Current focus

- Differential Shannon entropy in quantum mechanics
- Free Gaussian wave packet entropy
- Momentum-space and position-space entropy
- Translated harmonic-oscillator ground state
- 3D generalization of the harmonic oscillator case
- Preparing for numerical time evolution in a Morse potential

## Repository structure

```text
docs/
  detailed notes and derivations

scripts/
  Python scripts for entropy calculations and plots

figures/
  generated plots

notebooks/
  future numerical notebooks

data/
  future numerical outputs
```

## Status

This repository is still a work in progress. At this stage, I am mainly using it to organize my notes, derivations, and early Python calculations. The README will be expanded once the project is closer to completion.
