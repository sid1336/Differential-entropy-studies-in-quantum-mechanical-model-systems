# Analysis Notes on Differential Entropy and Information Measures in Quantum Systems

These notes are my cleaned-up version of the three-paper summary. I wanted this to read less like a generic summary and more like a set of notes from someone who actually worked through the ideas, checked the formulas, and tried to understand why the papers matter for studying wave packets, entropy, and quantum dynamics.

The main thread I see across all three papers is this:

$$
\text{wave function} \rightarrow \text{probability density} \rightarrow \text{single information number}.
$$

The wave function itself can be complicated, especially when it depends on time, position, momentum, electronic coordinates, or nuclear coordinates. But once we construct a density such as

$$
\rho(x,t)=|\psi(x,t)|^2,
$$

we can calculate information measures such as Shannon entropy, Fisher information, and Onicescu information energy. These measures turn the shape of a distribution into a number that tells us something physical, such as whether the quantum state is localized, spread out, correlated, or dynamically changing.

The three papers I analyzed are:

1. P. Schürger and V. Engel, **"Information Theoretical Approach to Coupled Electron-Nuclear Wave Packet Dynamics: Time-Dependent Differential Shannon Entropies"**, *Journal of Physical Chemistry Letters* **14**, 334-339 (2023).

2. S. Hazra, **"A comparative study on information theoretic approach for atomic and molecular systems"**, *Computational and Theoretical Chemistry* **1179**, 112801 (2020).

3. P. Sarkar, R. Chattopadhyay, and J. K. Bhattacharjee, **"Quantum dynamics of wave packets in a Morse potential: A dynamical system approach"**, *Physical Review E* **110**, 034207 (2024).

What I found useful is that the papers are not doing exactly the same thing, but they are connected by the same conceptual structure. Paper A focuses on time-dependent Shannon entropy and mutual information in coupled electron-nuclear motion. Paper B compares different information measures for atoms and molecules. Paper C studies wave-packet motion in a Morse potential using both the Schrödinger equation and moment dynamics. Together, they give a useful path for thinking about differential entropy in quantum mechanical model systems.

---

# 0. Background ideas I needed before reading the papers

Before going into the papers, I first had to make sure the basic objects were clear. The most important object is the probability density.

For a continuous coordinate \(x\), the probability density \(\rho(x)\) is not itself a probability. Instead,

$$
\rho(x)\,dx
$$

is the probability of finding the particle in the small interval between \(x\) and \(x+dx\). Because the particle must be somewhere, the density must satisfy

$$
\int \rho(x)\,dx=1.
$$

In quantum mechanics, the probability density is obtained from the wave function by

$$
\rho(x,t)=|\psi(x,t)|^2.
$$

This matters because information theory is applied to the density, not directly to the complex wave function. The phase of the wave function can affect later dynamics, but the density itself is what enters the entropy integral.

---

## 0.1 Position space and momentum space

A wave function can be described in position space,

$$
\psi(x),
$$

or in momentum space,

$$
\tilde{\psi}(p).
$$

The two are connected by a Fourier transform. In one common convention,

$$
\tilde{\psi}(p)=\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}e^{-ipx/\hbar}\psi(x)\,dx.
$$

The momentum density is then

$$
\gamma(p)=|\tilde{\psi}(p)|^2.
$$

This is important because localization in position space and localization in momentum space are linked by uncertainty. A narrow distribution in \(x\) usually corresponds to a broad distribution in \(p\), and a broad distribution in \(x\) usually corresponds to a narrow distribution in \(p\).

This is why the entropy in position space and the entropy in momentum space should not be thought of independently. Their relationship gives another version of the uncertainty principle, but written in terms of entropy.

---

## 0.2 Shannon entropy

For a continuous density, the Shannon entropy is

$$
S[\rho]=-\int \rho(x)\ln\rho(x)\,dx.
$$

This is also called **differential entropy**. The important thing I had to keep in mind is that differential entropy is not exactly the same as discrete entropy. For a continuous density, \(S\) can even be negative depending on the units and width of the distribution. So the most meaningful quantity is often a difference in entropy or a comparison between similar systems.

The rough interpretation is:

$$
\text{spread-out density} \Rightarrow \text{larger } S,
$$

and

$$
\text{localized density} \Rightarrow \text{smaller } S.
$$

For a Gaussian, this is very direct because the entropy is controlled by the width.

---

## 0.3 Fisher information

Fisher information measures how sharply a density changes. In one dimension,

$$
I[\rho]=\int \frac{|\nabla \rho(x)|^2}{\rho(x)}\,dx.
$$

If a density has steep gradients or sharp features, Fisher information is large. If the density is smooth and spread out, Fisher information is smaller.

So Fisher information behaves in almost the opposite way from Shannon entropy:

$$
\text{localized density} \Rightarrow \text{larger Fisher information}.
$$

---

## 0.4 Onicescu information energy

The Onicescu information energy is

$$
E[\rho]=\int \rho(x)^2\,dx.
$$

This quantity is also large when the distribution is concentrated and small when it is spread out. It is called an information energy because it measures how concentrated or disequilibrated the density is.

For a Gaussian,

$$
\rho(x)=\frac{1}{\sqrt{2\pi}\sigma}
\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],
$$

the Onicescu information energy is

$$
E[\rho]=\int \rho(x)^2\,dx=\frac{1}{2\sigma\sqrt{\pi}}.
$$

This confirms the interpretation: as \(\sigma\) gets smaller, the density gets narrower, and \(E\) gets larger.

---

## 0.5 My working rule of thumb

The three information measures behave like this:

| Density behavior | Shannon \(S\) | Fisher \(I\) | Onicescu \(E\) |
|---|---:|---:|---:|
| More spread out | larger | smaller | smaller |
| More localized | smaller | larger | larger |

This rule helped me read all three papers. Paper A mainly uses Shannon entropy. Paper B compares Shannon, Fisher, and Onicescu measures. Paper C does not focus directly on entropy, but it tracks the width and moments of a wave packet, which are closely related to entropy for Gaussian-like states.

---

# 1. Paper A: Schürger and Engel, time-dependent differential Shannon entropies

## 1.1 What I think the paper is trying to do

Schürger and Engel study a coupled electron-nuclear quantum system and ask what time-dependent Shannon entropy can tell us about the motion. The system has both an electron coordinate and a proton coordinate, so the total wave function depends on two variables.

The main thing I understood from the paper is that entropy is being used in two different ways:

1. To measure how spread out the electron and proton densities are.
2. To measure how correlated the electron and proton are through mutual information.

This is important because "coupled motion" does not automatically mean strong correlation in the density. One of the paper's most interesting results is that strong non-adiabatic population transfer can happen even when the electron-proton mutual information is close to zero.

That was one of the main conceptual points I took away from the paper.

---

## 1.2 The model system

The model is a one-dimensional toy molecular system. There are two fixed protons located at

$$
R_1=-5\ \text{\AA},
\qquad
R_2=+5\ \text{\AA}.
$$

There is also one moving proton with coordinate \(R\), and one moving electron with coordinate \(r\). The potential energy is written as

$$
V(r,R)
=
\frac{1}{|R_1-R_2|}
+
\frac{1}{|R-R_1|}
+
\frac{1}{|R-R_2|}
-
\frac{\operatorname{erf}(|R_1-r|/R_f)}{|R_1-r|}
-
\frac{\operatorname{erf}(|R-r|/R_c)}{|R-r|}
-
\frac{\operatorname{erf}(|R_2-r|/R_f)}{|R_2-r|}
-
\Delta E.
$$

My interpretation of the terms is:

- The positive terms are proton-proton repulsions.
- The negative terms are electron-proton attractions.
- The error function softens the Coulomb singularity.
- \(R_f=1.5\ \text{\AA}\) is fixed.
- \(R_c\) is varied and controls the electron-moving-proton interaction.
- \(\Delta E\) shifts the energy minimum to zero.

The Hamiltonian is

$$
\hat H
=
\frac{\hat p^2}{2}
+
\frac{\hat P^2}{2M}
+
V(r,R),
$$

where \(\hat p\) is the electron momentum operator, \(\hat P\) is the proton momentum operator, and \(M\) is the proton mass. The electron mass is taken as 1 in atomic units.

They solve the time-dependent Schrödinger equation,

$$
i\frac{\partial \Psi}{\partial t}
=
\hat H\Psi,
$$

numerically using a split-operator method on a \(512\times512\) grid with time step

$$
0.0024\ \text{fs}.
$$

This matters because the paper is not only formal. They actually propagate the full two-coordinate wave function and calculate entropies from it as functions of time.

---

## 1.3 Densities and entropies

The full probability density is

$$
\rho(r,R,t)=|\Psi(r,R,t)|^2.
$$

From this, the nuclear and electronic marginal densities are obtained by integrating out the other coordinate:

$$
\rho_{\text{nuc}}(R,t)
=
\int \rho(r,R,t)\,dr,
$$

and

$$
\rho_{\text{el}}(r,t)
=
\int \rho(r,R,t)\,dR.
$$

The corresponding Shannon entropies are

$$
S_{\text{tot}}(t)
=
-\int\!\!\int
\rho(r,R,t)\ln\rho(r,R,t)\,dr\,dR,
$$

$$
S_{\text{nuc}}(t)
=
-\int
\rho_{\text{nuc}}(R,t)\ln\rho_{\text{nuc}}(R,t)\,dR,
$$

and

$$
S_{\text{el}}(t)
=
-\int
\rho_{\text{el}}(r,t)\ln\rho_{\text{el}}(r,t)\,dr.
$$

The mutual information is then

$$
\boxed{
I(t)=S_{\text{el}}(t)+S_{\text{nuc}}(t)-S_{\text{tot}}(t).
}
$$

I found this definition especially useful because it separates simple spreading from actual electron-nuclear correlation.

If the density factorizes,

$$
\rho(r,R,t)=\rho_{\text{el}}(r,t)\rho_{\text{nuc}}(R,t),
$$

then the electron and nucleus are statistically independent. In that case,

$$
\ln\rho(r,R,t)
=
\ln\rho_{\text{el}}(r,t)+\ln\rho_{\text{nuc}}(R,t).
$$

So

$$
S_{\text{tot}}
=
-\int\!\!\int
\rho_{\text{el}}\rho_{\text{nuc}}
\left[
\ln\rho_{\text{el}}+\ln\rho_{\text{nuc}}
\right]dr\,dR.
$$

Using normalization,

$$
\int \rho_{\text{el}}(r,t)\,dr=1,
\qquad
\int \rho_{\text{nuc}}(R,t)\,dR=1,
$$

we get

$$
S_{\text{tot}}=S_{\text{el}}+S_{\text{nuc}}.
$$

Therefore,

$$
I(t)=0.
$$

So my understanding is:

$$
\boxed{
I(t)=0 \text{ means no statistical electron-nuclear correlation in the density.}
}
$$

and

$$
\boxed{
I(t)>0 \text{ means the electron and proton positions are correlated.}
}
$$

---

## 1.4 Expansion in adiabatic electronic states

The paper also writes the full wave function as an expansion over electronic adiabatic states:

$$
\Psi(R,r,t)
=
\sum_{n=0}^{\infty}
\psi_n(R,t)\phi_n(r;R).
$$

Here:

- \(\phi_n(r;R)\) is the electronic wave function for electronic state \(n\), with \(R\) treated as a parameter.
- \(\psi_n(R,t)\) is the nuclear wave packet moving on electronic state \(n\).
- The population of electronic state \(n\) is

$$
P_n(t)=\int |\psi_n(R,t)|^2\,dR.
$$

The populations satisfy

$$
\sum_n P_n(t)=1.
$$

This decomposition is important because the paper compares entropy behavior with electronic population transfer. One might expect that large changes in populations automatically mean large electron-nuclear correlation, but the paper shows that this is not always true.

---

## 1.5 Case 1: Born-Oppenheimer-like dynamics

In the weak-coupling case,

$$
R_c=1.5\ \text{\AA},
$$

the ground electronic state is well separated from the excited states. The system starts in the electronic ground state with a nuclear Gaussian wave packet centered at

$$
R_0=-3.5\ \text{\AA}.
$$

The population remains almost entirely in the ground state:

$$
P_0(t)\geq 99.9\%.
$$

So this is essentially Born-Oppenheimer dynamics.

The electron and proton densities oscillate in phase with a period of about

$$
80\ \text{fs}.
$$

The paper finds that

$$
S_{\text{nuc}}(t)
$$

tracks the width of the nuclear density. This makes sense because Shannon entropy increases when the distribution spreads out and decreases when it becomes localized.

At the classical turning points, the wave packet slows down and refocuses. The density becomes narrower, so

$$
S_{\text{nuc}}(t)
$$

has minima there.

The electronic entropy,

$$
S_{\text{el}}(t),
$$

behaves similarly, although its absolute value is larger because the electron is more spatially delocalized than the proton.

The total entropy,

$$
S_{\text{tot}}(t),
$$

also follows the same general trend.

The most interesting part is what happens to the mutual information. The mutual information has minima at the classical turning points. The reason is that when the nuclear wave packet is sharply peaked near its mean value,

$$
\langle R\rangle_t,
$$

the electronic state can be approximated as

$$
\phi_0(r;R)\approx \phi_0(r;\langle R\rangle_t).
$$

Then the total wave function approximately factorizes:

$$
\Psi(r,R,t)
\approx
\psi_0(R,t)\phi_0(r;\langle R\rangle_t).
$$

If the wave function factorizes, then the density approximately factorizes, and the mutual information becomes small:

$$
I(t)\approx 0.
$$

So the physical picture is:

$$
\boxed{
\text{At turning points, the nuclear packet is focused, so electron-nuclear density correlation decreases.}
}
$$

This helped me understand that entropy is not just measuring "motion." It is measuring the spread and correlation structure of the quantum density.

---

## 1.6 Case 2: Strongly non-adiabatic or diabatic dynamics

In the strongly coupled case,

$$
R_c=5.0\ \text{\AA}.
$$

The gap between the ground and first excited adiabatic potentials near \(R=0\) becomes very small:

$$
0.0076\ \text{eV}.
$$

The system starts in \(\phi_1\) at

$$
R_0=-1.5\ \text{\AA}.
$$

The nuclear motion remains almost harmonic, but the electron density stays close to the right fixed proton at

$$
R_2=+5\ \text{\AA}.
$$

In other words, the electron density is almost independent of the moving proton coordinate \(R\). This is why the paper calls the motion diabatic.

The surprising result is:

$$
S_{\text{el}}(t)\approx \text{constant},
$$

and

$$
S_{\text{tot}}(t)\approx S_{\text{el}}(t)+S_{\text{nuc}}(t).
$$

Therefore,

$$
I(t)\approx 0.
$$

This happens even though the electronic populations \(P_0(t)\) and \(P_1(t)\) oscillate strongly. Around

$$
t=18.7\ \text{fs},
$$

there is nearly complete population transfer.

This is the part I think is conceptually important:

$$
\boxed{
\text{Strong non-adiabatic population transfer does not necessarily mean strong electron-nuclear mutual information.}
}
$$

The population basis can change dramatically, but if the actual density \(\rho(r,R,t)\) is approximately factorized, then the mutual information remains small.

So Schürger and Engel are careful to distinguish between:

$$
\text{electronic population transfer}
$$

and

$$
\text{electron-nuclear density correlation}.
$$

They are related concepts, but they are not the same.

---

## 1.7 State-resolved entropy

The paper also analyzes the density in terms of state contributions. Starting from

$$
\Psi(R,r,t)=\sum_n\psi_n(R,t)\phi_n(r;R),
$$

the full density becomes

$$
\rho(r,R,t)
=
\sum_{n,m}
\rho_{nm}(r,R,t),
$$

where

$$
\rho_{nm}
=
\psi_n^*(R,t)\psi_m(R,t)
\phi_n^*(r;R)\phi_m(r;R).
$$

The diagonal terms are

$$
\rho_{nn}.
$$

These are positive and can be interpreted as the contribution of state \(n\) to the density. They are not normalized to 1. Instead, they integrate to the population \(P_n(t)\).

The paper defines state-specific entropies \(S_n(t)\), \(S_n^{\text{nuc}}(t)\), and \(S_n^{\text{el}}(t)\) using these diagonal densities.

One of the main observations is that

$$
S_{\text{tot}}(t)\approx \sum_n S_n(t),
$$

and

$$
S_{\text{nuc}}(t)\approx \sum_n S_n^{\text{nuc}}(t),
$$

because the nuclear wave packets on different electronic surfaces do not overlap much. Therefore, off-diagonal terms are negligible for the total and nuclear entropies.

However, the electronic entropy behaves differently. Even when off-diagonal terms are negligible, the diagonal sum does not simply equal \(S_{\text{el}}(t)\).

At a transition time \(t_{\text{tr}}\), where

$$
P_0(t_{\text{tr}})=P_1(t_{\text{tr}})=\frac12,
$$

the paper gives approximately

$$
\boxed{
S_{\text{el}}(t_{\text{tr}})
\approx
\ln 2
+
S_0^{\text{el}}(t_{\text{tr}})
+
S_1^{\text{el}}(t_{\text{tr}}).
}
$$

The \(\ln 2\) comes from mixing two equal components. This is the same mathematical idea as a two-outcome probability distribution with equal weights, where the entropy contains a mixing contribution of \(\ln 2\).

My understanding is that the electronic marginal density keeps more direct information about the electronic populations, while the nuclear and total densities are more sensitive to spatial separation of wave packets.

---

## 1.8 What I took from Paper A

My main takeaways from Paper A are:

1. Shannon entropy follows the width of the probability density.

2. For wave packets, a narrower density gives smaller entropy, while a broader density gives larger entropy.

3. Mutual information,

$$
I(t)=S_{\text{el}}(t)+S_{\text{nuc}}(t)-S_{\text{tot}}(t),
$$

measures density correlation, not simply non-adiabaticity.

4. Born-Oppenheimer motion can still have time-dependent mutual information because the electron adapts to the nuclear coordinate.

5. Strong non-adiabatic population transfer can happen while mutual information remains close to zero.

6. State-resolved entropy mixes two ideas: state occupation and spatial localization.

For my own project, this paper gives the direct motivation for calculating differential Shannon entropy for model wave packets. It shows that entropy can track spreading, focusing, and correlations in a time-dependent quantum system.

---

# 2. Paper B: Hazra, information measures for atoms and molecules

## 2.1 What I think this paper contributes

Hazra's paper compares three information measures:

$$
S,\qquad I,\qquad E,
$$

where \(S\) is Shannon entropy, \(I\) is Fisher information, and \(E\) is Onicescu information energy.

The paper applies these measures to atoms from H to Ar and to several diatomic molecules:

$$
\mathrm{H_2},\ \mathrm{N_2},\ \mathrm{CO},\ \mathrm{O_2},\ \mathrm{HCl},\ \mathrm{F_2},\ \mathrm{Cl_2}.
$$

The main value of the paper for me is that it compares information measures in both position and momentum space. This is useful because a density may be localized in position space while delocalized in momentum space.

The technical contribution is that the paper computes Fisher information in momentum space using analytical Fourier transforms of Gaussian basis functions. This avoids noisy numerical Fourier transforms.

---

## 2.2 Position and momentum densities

For an \(N\)-electron system, the many-body wave function is

$$
\psi(\vec r_1,\vec r_2,\ldots,\vec r_N).
$$

The one-electron position density is

$$
\rho(\vec r)
=
N
\int
|\psi(\vec r,\vec r_2,\ldots,\vec r_N)|^2
\,d^3r_2\cdots d^3r_N.
$$

The momentum-space wave function is obtained by Fourier transforming the many-body wave function. The one-electron momentum density is

$$
\gamma(\vec p)
=
N
\int
|\tilde{\phi}(\vec p,\vec p_2,\ldots,\vec p_N)|^2
\,d^3p_2\cdots d^3p_N.
$$

Both densities are normalized to the number of electrons:

$$
\int \rho(\vec r)\,d^3r=N,
$$

and

$$
\int \gamma(\vec p)\,d^3p=N.
$$

This is different from the one-particle wave packet calculations, where the density is normalized to 1. The normalization matters because it changes the numerical form of the entropy.

---

## 2.3 Shannon entropy

In position space,

$$
S_{\vec r}
=
-\int \rho(\vec r)\ln\rho(\vec r)\,d^3r.
$$

In momentum space,

$$
S_{\vec p}
=
-\int \gamma(\vec p)\ln\gamma(\vec p)\,d^3p.
$$

The total Shannon entropy is defined as

$$
S_{\text{Total}}
=
S_{\vec r}+S_{\vec p}.
$$

So for Shannon entropy, the position and momentum contributions are added.

---

## 2.4 Fisher information

The Fisher information in position space is

$$
I_{\vec r}
=
\int
\frac{|\nabla\rho(\vec r)|^2}{\rho(\vec r)}
\,d^3r.
$$

In momentum space,

$$
I_{\vec p}
=
\int
\frac{|\nabla\gamma(\vec p)|^2}{\gamma(\vec p)}
\,d^3p.
$$

The total Fisher information is written as

$$
I_{\text{Total}}
=
I_{\vec r}I_{\vec p}.
$$

This is a product rather than a sum. I had to be careful here because in Paper A, \(I\) means mutual information, while in Paper B, \(I\) means Fisher information. They are completely different quantities.

---

## 2.5 Onicescu information energy

The Onicescu information energy in position space is

$$
E_{\vec r}
=
\int \rho(\vec r)^2\,d^3r.
$$

In momentum space,

$$
E_{\vec p}
=
\int \gamma(\vec p)^2\,d^3p.
$$

The total Onicescu measure is

$$
E_{\text{Total}}
=
E_{\vec r}E_{\vec p}.
$$

Like Fisher information, Onicescu information energy is large when a distribution is concentrated.

For a discrete distribution,

$$
E=\sum_i p_i^2.
$$

If all probability is in one state, \(E=1\). If the probability is spread equally across \(k\) states, then

$$
E=\frac1k.
$$

So it is a concentration measure.

For a continuous Gaussian,

$$
\rho(x)
=
\frac{1}{\sqrt{2\pi}\sigma}
\exp\left[
-\frac{(x-\mu)^2}{2\sigma^2}
\right],
$$

we calculate

$$
E[\rho]=\int \rho(x)^2\,dx.
$$

Squaring the density gives

$$
\rho(x)^2=
\frac{1}{2\pi\sigma^2}
\exp\left[
-\frac{(x-\mu)^2}{\sigma^2}
\right].
$$

Then

$$
E[\rho]
=
\frac{1}{2\pi\sigma^2}
\int_{-\infty}^{\infty}
\exp\left[
-\frac{(x-\mu)^2}{\sigma^2}
\right]dx.
$$

The Gaussian integral gives

$$
\int_{-\infty}^{\infty}
\exp\left[
-\frac{(x-\mu)^2}{\sigma^2}
\right]dx
=
\sigma\sqrt{\pi}.
$$

Therefore,

$$
E[\rho]
=
\frac{1}{2\pi\sigma^2}
\sigma\sqrt{\pi}
=
\frac{1}{2\sigma\sqrt{\pi}}.
$$

So

$$
\boxed{
E[\rho]=\frac{1}{2\sigma\sqrt{\pi}}.
}
$$

This confirms that narrower Gaussians have larger Onicescu information energy.

---

## 2.6 Entropic uncertainty relation

Hazra uses the Bialynicki-Birula-Mycielski entropic uncertainty relation. For \(N\)-normalized densities in three dimensions, the paper gives

$$
\boxed{
S_{\text{Total}}
=
S_{\vec r}+S_{\vec p}
\geq
3N(1+\ln\pi)-2N\ln N.
}
$$

For one electron, \(N=1\), this becomes

$$
S_{\vec r}+S_{\vec p}
\geq
3(1+\ln\pi).
$$

Numerically,

$$
3(1+\ln\pi)\approx 6.434.
$$

This is the three-dimensional entropy uncertainty lower bound.

I found this useful because it gives a direct entropy version of the uncertainty principle. Instead of saying

$$
\Delta x\Delta p\geq \frac{\hbar}{2},
$$

it says that the sum of position and momentum entropies cannot become arbitrarily small.

---

## 2.7 Shape functions and normalization

The paper also discusses the shape function,

$$
\sigma_{\vec r}=\frac{\rho}{N},
$$

which is normalized to 1 rather than \(N\). If we change from \(\rho\) to \(\sigma_{\vec r}\), the information measures transform as

$$
I_{\sigma_{\vec r}}=\frac{I_{\vec r}}{N},
$$

$$
S_{\sigma_{\vec r}}=\frac{S_{\vec r}}{N}+\ln N,
$$

and

$$
E_{\sigma_{\vec r}}=\frac{E_{\vec r}}{N^2}.
$$

The Shannon transformation can be checked directly. Since

$$
\rho=N\sigma_{\vec r},
$$

we have

$$
S_{\vec r}
=
-\int N\sigma_{\vec r}\ln(N\sigma_{\vec r})\,d^3r.
$$

Using

$$
\ln(N\sigma_{\vec r})=\ln N+\ln\sigma_{\vec r},
$$

we get

$$
S_{\vec r}
=
-N\ln N
\int\sigma_{\vec r}\,d^3r
-
N\int\sigma_{\vec r}\ln\sigma_{\vec r}\,d^3r.
$$

Because

$$
\int\sigma_{\vec r}\,d^3r=1,
$$

this becomes

$$
S_{\vec r}
=
-N\ln N+N S_{\sigma_{\vec r}}.
$$

Solving for \(S_{\sigma_{\vec r}}\),

$$
\boxed{
S_{\sigma_{\vec r}}
=
\frac{S_{\vec r}}{N}+\ln N.
}
$$

This is a useful warning that entropy values depend on normalization conventions.

---

## 2.8 Computational method

The paper uses Gaussian-type orbitals to build the electronic wave functions. The calculations use:

- B3LYP density functional theory.
- 6-311++G** basis set.
- GAMESS quantum chemistry package.

The main computational point is that Gaussian-type orbitals have analytical Fourier transforms. Therefore, the momentum-space density can be computed without relying on numerical FFTs.

This is especially important for Fisher information, because Fisher information depends on gradients:

$$
I[\rho]=\int \frac{|\nabla\rho|^2}{\rho}\,d^3r.
$$

Gradients can become noisy if the density is obtained numerically. Hazra avoids this by using analytical expressions and Gauss-Legendre quadrature in spherical polar coordinates.

---

## 2.9 Main results for atoms

For atoms from H to Ar, Hazra reports several important patterns.

First,

$$
S_{\vec r}
$$

has local minima at closed-shell noble gases:

$$
\mathrm{He},\quad \mathrm{Ne},\quad \mathrm{Ar}.
$$

This means the position-space electron density is more localized for closed-shell atoms.

Second,

$$
S_{\vec p}
$$

increases monotonically with atomic number \(Z\). This indicates that momentum-space density becomes more delocalized as \(Z\) increases.

Third,

$$
S_{\text{Total}}
$$

increases with \(Z\).

Fourth,

$$
I_{\vec r}
$$

increases monotonically with \(Z\), meaning the position-space densities become more sharply structured.

Fifth,

$$
I_{\vec p}
$$

has local minima at noble gases.

Sixth,

$$
E_{\vec r}
$$

increases monotonically with \(Z\), while

$$
E_{\vec p}
$$

also has local minima at noble gases.

The main pattern is:

$$
\boxed{
I \text{ and } E \text{ behave similarly, while } S \text{ behaves oppositely.}
}
$$

This agrees with the physical interpretation of the three measures.

---

## 2.10 Main results for diatomic molecules

For the molecules

$$
\mathrm{H_2},\ \mathrm{N_2},\ \mathrm{CO},\ \mathrm{O_2},\ \mathrm{HCl},\ \mathrm{F_2},\ \mathrm{Cl_2},
$$

the paper finds that position-space Shannon entropy fluctuates with bond length.

Momentum-space and total Shannon entropies generally increase smoothly with bond length, except for \(\mathrm{F_2}\).

The paper identifies \(\mathrm{Cl_2}\) as having the largest

$$
I_{\vec r}
$$

and

$$
E_{\vec r},
$$

which means it has the most localized position-space density among the studied molecules according to those measures.

HCl is identified as having the most localized position-space density and the most delocalized momentum-space density in the molecular set.

---

## 2.11 What I took from Paper B

My main takeaways from Paper B are:

1. Shannon entropy is a global measure of delocalization.

2. Fisher information is a local gradient-sensitive measure.

3. Onicescu information energy measures concentration or disequilibrium.

4. Fisher and Onicescu measures tend to behave similarly.

5. Shannon entropy tends to behave oppositely to Fisher and Onicescu.

6. Position-space and momentum-space descriptions must be compared together.

7. Normalization matters, especially when densities are normalized to \(N\) instead of 1.

For my own project, this paper is useful because it gives a broader information-theoretic context. It shows that Shannon entropy is not the only possible measure, but it also helps justify why Shannon entropy is a natural starting point for wave-packet spreading.

---

# 3. Paper C: Sarkar, Chattopadhyay, and Bhattacharjee, wave packets in a Morse potential

## 3.1 What I think this paper is doing

Paper C studies a quantum wave packet moving in a Morse potential. The Morse potential is important because it models molecular vibrations, especially diatomic molecules.

The paper compares two approaches:

1. Direct numerical integration of the time-dependent Schrödinger equation.
2. A moment-based dynamical system based on Ehrenfest's theorem and Gaussian closure.

The reason this paper connects to the entropy project is that if the wave packet remains approximately Gaussian, then its width and variance are directly related to the differential Shannon entropy. So even though this paper is not primarily an entropy paper, it gives a dynamical framework for studying wave-packet width in a realistic molecular potential.

---

## 3.2 The Morse potential

The Morse potential is

$$
\varphi(x)
=
\varphi_0
\left(
e^{-2ax}-2e^{-ax}
\right).
$$

It has a minimum at

$$
x=0,
$$

with value

$$
-\varphi_0.
$$

As

$$
x\to\infty,
$$

the potential approaches zero. Therefore, for a classical particle:

- If \(-\varphi_0<E<0\), the motion is bound.
- If \(E\geq 0\), the particle can escape.

The paper uses

$$
\hbar=1,\qquad m=1,\qquad \varphi_0=1,\qquad a=0.5.
$$

This makes the numerical system simpler.

---

## 3.3 Ehrenfest equations

Ehrenfest's theorem says that expectation values follow Newton-like equations, but with quantum averages of the force.

For position and momentum,

$$
\frac{d\langle x\rangle}{dt}
=
\frac{\langle p\rangle}{m},
$$

and

$$
\frac{d\langle p\rangle}{dt}
=
-\left\langle
\frac{d\varphi}{dx}
\right\rangle.
$$

Therefore,

$$
\frac{d^2\langle x\rangle}{dt^2}
=
-\frac1m
\left\langle
\frac{d\varphi}{dx}
\right\rangle.
$$

This is not exactly the classical equation

$$
m\ddot{x}=-\varphi'(x),
$$

because the force is averaged over the whole wave packet:

$$
-\left\langle \varphi'(x)\right\rangle.
$$

The variance is

$$
V
=
\langle x^2\rangle-\langle x\rangle^2.
$$

The paper derives

$$
\frac{d^2V}{dt^2}
=
\frac{2\langle(\Delta p)^2\rangle}{m^2}
-
\frac2m
\left[
\left\langle
x\frac{d\varphi}{dx}
\right\rangle
-
\langle x\rangle
\left\langle
\frac{d\varphi}{dx}
\right\rangle
\right].
$$

This equation shows that the width of the packet is coupled to both momentum uncertainty and the spatial variation of the force.

The moment hierarchy does not close automatically. Equations for low moments depend on higher moments. So the authors use a Gaussian closure assumption.

---

## 3.4 Gaussian closure

The paper assumes the wave packet has the approximate form

$$
\psi(x,t)
=
\frac{1}{(2\pi V(t))^{1/4}}
\exp\left[
-\frac{(x-\langle x\rangle(t))^2}{4V(t)}
\right]
e^{ik(t)x}.
$$

Here:

- \(\langle x\rangle(t)\) is the mean position.
- \(V(t)\) is the position variance.
- \(k(t)\) is the mean momentum.
- The packet is assumed to remain approximately Gaussian.

For a Gaussian distribution, higher moments can be expressed in terms of the variance. For example, skewness is zero and kurtosis is proportional to \(V^2\). This lets the authors close the moment equations.

The paper later checks this assumption numerically and finds that skewness stays small, which supports the closure.

---

## 3.5 Low-energy expansion of the Morse potential

Near the minimum, the Morse potential can be expanded as

$$
\varphi(x)
=
-\varphi_0
+
\frac12\omega^2x^2
-
\frac{\mu}{3}x^3
+
\frac{\lambda}{4}x^4
+
\cdots.
$$

The coefficients are

$$
\omega^2=2\varphi_0a^2,
$$

$$
\mu=3\varphi_0a^3,
$$

and

$$
\lambda=\frac{7\varphi_0a^4}{3}.
$$

I checked the expansion by writing

$$
u=ax.
$$

Then

$$
e^{-2u}
=
1-2u+2u^2-\frac43u^3+\frac23u^4+\cdots,
$$

and

$$
-2e^{-u}
=
-2+2u-u^2+\frac13u^3-\frac1{12}u^4+\cdots.
$$

Adding them gives

$$
e^{-2u}-2e^{-u}
=
-1+u^2-u^3+\frac{7}{12}u^4+\cdots.
$$

Multiplying by \(\varphi_0\) and substituting \(u=ax\),

$$
\varphi(x)
=
-\varphi_0
+
\varphi_0a^2x^2
-
\varphi_0a^3x^3
+
\frac{7}{12}\varphi_0a^4x^4
+\cdots.
$$

This matches

$$
\frac12\omega^2x^2
$$

if

$$
\omega^2=2\varphi_0a^2.
$$

It matches

$$
-\frac{\mu}{3}x^3
$$

if

$$
\mu=3\varphi_0a^3.
$$

And it matches

$$
\frac{\lambda}{4}x^4
$$

if

$$
\lambda=\frac{7\varphi_0a^4}{3}.
$$

So the expansion is internally consistent.

---

## 3.6 Dimensionless variables and closed dynamical system

The paper introduces

$$
y=a\langle x\rangle,
$$

$$
u=2a^2V,
$$

and

$$
\tau=ta\sqrt{2\varphi_0}.
$$

Using the Gaussian closure and computing the Gaussian averages of exponentials, the closed system becomes

$$
\boxed{
\frac{d^2y}{d\tau^2}
=
e^{u-2y}
-
e^{u/4-y}.
}
$$

The width variable satisfies

$$
\boxed{
\frac{d^2u}{d\tau^2}
=
\frac{\kappa}{2u}
-
2u
\left[
2e^{u-2y}
-
e^{u/4-y}
\right].
}
$$

Here,

$$
\kappa=\frac{2a^2}{m^2\varphi_0}.
$$

The exponential factors come from Gaussian averages. For example,

$$
\left\langle e^{-2ax}\right\rangle
=
\exp(-2a\langle x\rangle+2a^2V)
=
e^{-2y+u}.
$$

Similarly,

$$
\left\langle e^{-ax}\right\rangle
=
\exp(-a\langle x\rangle+a^2V/2)
=
e^{-y+u/4}.
$$

This showed me why Gaussian wave packets are analytically useful. Exponential potentials and Gaussian distributions work well together because Gaussian averages of exponentials remain simple exponentials.

---

## 3.7 Energy and stability

The paper gives an approximate energy expression for localized packets:

$$
E
\approx
\frac{k^2}{2}
+
\frac{\kappa}{8}u
-
e^{-u/2}.
$$

The fixed point satisfies

$$
y_0=\frac34u_0,
$$

and

$$
u_0e^{-u_0/2}
=
2\left(-\epsilon+e^{-u_0/2}\right).
$$

The stability condition is

$$
\epsilon
<
\left[
\frac{u_0}{4}
\left(
3+\frac72u_0
\right)
+1
\right]
e^{-u_0/2}.
$$

When this condition fails, the fixed point becomes unstable and the dynamical system predicts that the wave packet escapes the Morse well.

This is important because the moment system is not just reproducing small oscillations. It also captures a transition from bounded motion to escape.

---

## 3.8 Comparison with the Schrödinger equation

The paper compares the dynamical system with direct numerical integration of the time-dependent Schrödinger equation.

They start with a Gaussian wave packet at

$$
x=0,
$$

with width

$$
\sigma=1,
$$

and vary the initial momentum \(k\). They measure the time-averaged probability inside a region \(x\leq x_0\), with

$$
x_0=4.
$$

The probability is

$$
P(x_0)
=
\lim_{T\to\infty}
\frac1T
\int_0^Tdt
\int_{-\infty}^{x_0}
|\psi(x,t)|^2\,dx.
$$

The numerical behavior is:

- For \(k\lesssim 0.3\), the probability decreases slowly, so the packet stays mostly inside.
- For \(0.3\lesssim k\lesssim 0.8\), there is a transition region.
- For \(k\gtrsim 0.8\), the packet is mostly outside the classical domain.

The dynamical system predicts an instability at about

$$
k\approx 0.77-0.78.
$$

This agrees well with the Schrödinger simulation.

This is one of the strongest results of the paper: a low-dimensional dynamical system based on moments can predict the same qualitative escape threshold as the full wave equation.

---

## 3.9 Tunneling interpretation

The paper also shows tunneling behavior using the quantity

$$
\langle x\rangle+\sqrt{V}.
$$

For \(k=0.1\) and \(k=0.5\), the energies are still bound, but this quantity can exceed the classical turning point.

For example, at

$$
k=0.1,
$$

with energy approximately

$$
E\approx -0.6,
$$

the value

$$
\langle x\rangle+\sqrt{V}
$$

can reach about

$$
2.25,
$$

while the classical maximum displacement is less than 2.

This means that part of the quantum wave packet extends beyond the classical turning point. That is why the paper interprets this as tunneling.

---

## 3.10 Skewness check

The paper checks the Gaussian closure by studying skewness. The skewness stays small even at long times. It also grows approximately quadratically with \(k\), or linearly with

$$
\Delta E=\frac{E+\varphi_0}{\varphi_0}.
$$

This supports the assumption that ignoring skewness is reasonable for the parameter range studied.

The paper also gives a low-energy prediction,

$$
S_0
=
-\frac{5x_0\Delta E}{3\omega^2}.
$$

The numerical behavior agrees with the idea that skewness remains controlled at low energy.

---

## 3.11 What I took from Paper C

My main takeaways from Paper C are:

1. The Morse potential is a realistic model for molecular vibrational motion.

2. A Gaussian wave packet in a Morse potential can be described approximately by its mean and variance.

3. Ehrenfest's theorem leads naturally to equations for wave-packet moments.

4. Gaussian closure turns the quantum problem into a small nonlinear dynamical system.

5. The moment system predicts stable oscillations at low energy and escape at higher energy.

6. The predicted critical momentum \(k\approx0.77-0.78\) agrees with the Schrödinger equation simulation.

7. The method captures tunneling because the wave-packet width allows part of the density to extend beyond the classical turning point.

For my entropy project, this paper suggests a next step: after free Gaussian wave packets and harmonic oscillator packets, the Morse potential is a natural model because it connects wave-packet spreading to molecular vibrational physics.

---

# 4. How the three papers connect

After reading the three papers together, I think the common structure is:

$$
\text{quantum state}
\rightarrow
\text{probability density}
\rightarrow
\text{measure of spread, localization, or correlation}.
$$

Paper A uses Shannon entropy to study time-dependent electron-nuclear wave packet motion. Paper B compares multiple information measures for atoms and molecules. Paper C studies wave-packet dynamics in a Morse potential using moments, which connect naturally to entropy when the packet is Gaussian-like.

The most useful connection for my project is that a Gaussian wave packet gives a clean starting point. For a Gaussian density,

$$
\rho(x)
=
\frac{1}{\sigma\sqrt{\pi}}
\exp\left[-\frac{(x-\langle x\rangle)^2}{\sigma^2}\right],
$$

the Shannon entropy is

$$
S
=
\ln(\sigma\sqrt{\pi})+\frac12.
$$

Equivalently,

$$
S=\frac12\ln(\pi e\sigma^2).
$$

So for a Gaussian, the entropy is directly tied to the width. This explains why Paper A's entropy tracks wave-packet spreading and why Paper C's variance dynamics are relevant to entropy studies.

---

# 5. Summary table

| Concept | Mathematical form | Physical meaning | Paper connection |
|---|---|---|---|
| Shannon entropy | \(S=-\int \rho\ln\rho\) | spread or uncertainty of density | Papers A and B |
| Fisher information | \(I=\int |\nabla\rho|^2/\rho\) | sharpness and local structure | Paper B |
| Onicescu energy | \(E=\int \rho^2\) | concentration of density | Paper B |
| Mutual information | \(I_{\rm mut}=S_{\rm el}+S_{\rm nuc}-S_{\rm tot}\) | electron-nuclear correlation | Paper A |
| Variance | \(V=\langle x^2\rangle-\langle x\rangle^2\) | wave-packet width | Paper C |
| Gaussian closure | assume packet remains Gaussian | closes moment equations | Paper C |
| Morse potential | \(\varphi(x)=\varphi_0(e^{-2ax}-2e^{-ax})\) | molecular vibration model | Paper C |

---

# 6. Final understanding

My overall understanding is that entropy is useful in quantum dynamics because it gives a compact way to track how a probability density changes. In a simple free Gaussian wave packet, entropy increases because the packet spreads. In a coupled electron-nuclear system, entropy can track both spreading and correlation. In atoms and molecules, entropy and related measures reveal localization patterns across position and momentum space. In a Morse potential, moment dynamics provide a route toward computing how wave-packet width, and therefore entropy, evolves in a molecular model.

The most important conceptual point is that entropy is not just a decorative quantity added after solving the Schrödinger equation. It can diagnose physical behavior:

$$
\text{spreading},
\qquad
\text{localization},
\qquad
\text{turning-point focusing},
\qquad
\text{electron-nuclear correlation},
\qquad
\text{population mixing},
\qquad
\text{escape from a molecular well}.
$$

For the direction of my project, the natural path is:

1. Start with a free Gaussian wave packet, because its entropy can be calculated analytically.
2. Move to harmonic oscillator wave packets, where Gaussian behavior can remain controlled.
3. Move to Morse-potential wave packets, where the dynamics become molecular and nonlinear.
4. Compare the direct entropy calculation with moment-based quantities such as variance.
5. Eventually ask whether entropy provides a useful diagnostic of wave-packet spreading, focusing, tunneling, and escape.

That is how I see the three papers fitting together into a coherent research direction.
