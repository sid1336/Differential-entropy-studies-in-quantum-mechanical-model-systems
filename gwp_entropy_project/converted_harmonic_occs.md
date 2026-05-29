# Entropy of a Time-Dependent Translated Harmonic-Oscillator Ground State

These are my detailed notes for the harmonic oscillator problem from lecture. I first work through the one-dimensional translated ground state, and then I add the three-dimensional version because that is the natural next step before starting numerical methods. The goal is to connect the Quantum mechanics lecture-note state


$$

\vert \psi_0\rangle
=
\exp\left(-\frac{i\xi \hat p}{\hbar}\right)\vert \phi_0\rangle
=
\hat T(\xi)\vert \phi_0\rangle

$$


to the actual time-dependent probability density and then calculate the differential Shannon entropy,


$$

S_x(t)
=
-\int_{-\infty}^{\infty}\rho(x,t)\ln\rho(x,t)\,dx.

$$


The main result is simple, but the reason behind it is important:


$$

\boxed{
\text{The translated ground state is time-dependent, but its entropy is constant.}
}

$$


This happens because the state oscillates back and forth in the harmonic oscillator potential without spreading. The center of the Gaussian changes with time, but its width does not.

---

# 1. Problem setup from the lecture notes

The one-dimensional harmonic oscillator Hamiltonian is


$$

\hat H
=
\frac{\hat p^2}{2m}
+
\frac12m\omega^2\hat x^2.

$$


The initial state is not just the ground state. It is the ground state shifted by a distance $\xi$:


$$

\vert \psi_0\rangle
=
\exp\left(-\frac{i\xi \hat p}{\hbar}\right)\vert \phi_0\rangle.

$$


The operator


$$

\hat T(\xi)
=
\exp\left(-\frac{i\xi \hat p}{\hbar}\right)

$$


is called the translation operator.

So the lecture-note state is


$$

\vert \psi_0\rangle=\hat T(\xi)\vert \phi_0\rangle.

$$


Physically, this means:


$$

\boxed{
\text{take the harmonic oscillator ground state and shift it from }x=0\text{ to }x=\xi.
}

$$


The time evolution is governed by the harmonic oscillator Hamiltonian:


$$

\vert \psi(t)\rangle
=
e^{-i\hat Ht/\hbar}\vert \psi_0\rangle.

$$


So the question I am studying is the entropy of this time-dependent state.

---

# 2. Creation and annihilation operators

To understand where the ground-state wavefunction comes from, I start from the creation and annihilation operators.

For the harmonic oscillator,


$$

\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\,\hat x
+
\frac{i}{\sqrt{2m\hbar\omega}}\,\hat p,

$$


and


$$

\hat a^\dagger
=
\sqrt{\frac{m\omega}{2\hbar}}\,\hat x
-
\frac{i}{\sqrt{2m\hbar\omega}}\,\hat p.

$$


They satisfy


$$

[\hat a,\hat a^\dagger]=1.

$$


We can also solve these equations for $\hat x$ and $\hat p$:


$$

\hat x
=
\sqrt{\frac{\hbar}{2m\omega}}
(\hat a+\hat a^\dagger),

$$


and


$$

\hat p
=
i\sqrt{\frac{m\hbar\omega}{2}}
(\hat a^\dagger-\hat a).

$$


The Hamiltonian becomes


$$

\hat H
=
\hbar\omega
\left(
\hat a^\dagger\hat a+\frac12
\right).

$$


The ground state is $\vert \phi_0 \rangle$ defined by


$$

\boxed{
\hat a\vert \phi_0\rangle=0.
}

$$


This means the ground state has no oscillator quanta.

---

# 3. Deriving the ground-state wavefunction in position space

Now I derive the formula for $\vert \phi_0(x) \rangle$ , because this is a missing step that can easily feel like it came out of nowhere.

In the position representation,


$$

\hat x \rightarrow x,

$$


and


$$

\hat p \rightarrow -i\hbar\frac{d}{dx}.

$$


The annihilation operator is


$$

\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\,\hat x
+
\frac{i}{\sqrt{2m\hbar\omega}}\,\hat p.

$$


Substitute the position-space form of $ \hat p $ :


$$

\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\,x
+
\frac{i}{\sqrt{2m\hbar\omega}}
\left(
-i\hbar\frac{d}{dx}
\right).

$$


Since $i(-i)=1$,


$$

\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\,x
+
\frac{\hbar}{\sqrt{2m\hbar\omega}}
\frac{d}{dx}.

$$


The second coefficient simplifies as


$$

\frac{\hbar}{\sqrt{2m\hbar\omega}}
=
\sqrt{\frac{\hbar}{2m\omega}}.

$$


So


$$

\hat a
=
\sqrt{\frac{m\omega}{2\hbar}}\,x
+
\sqrt{\frac{\hbar}{2m\omega}}
\frac{d}{dx}.

$$


The ground-state condition is


$$

\hat a\phi_0(x)=0.

$$


Therefore,


$$

\left[
\sqrt{\frac{m\omega}{2\hbar}}\,x
+
\sqrt{\frac{\hbar}{2m\omega}}
\frac{d}{dx}
\right]
\phi_0(x)
=
0.

$$


Move the derivative term to the other side:


$$

\sqrt{\frac{\hbar}{2m\omega}}
\frac{d\phi_0}{dx}
=
-
\sqrt{\frac{m\omega}{2\hbar}}\,x\phi_0(x).

$$


Divide both sides by


$$

\sqrt{\frac{\hbar}{2m\omega}}.

$$


Then


$$

\frac{d\phi_0}{dx}
=
-
\frac{
\sqrt{\frac{m\omega}{2\hbar}}
}{
\sqrt{\frac{\hbar}{2m\omega}}
}
x\phi_0(x).

$$


The ratio is


$$

\frac{
\sqrt{\frac{m\omega}{2\hbar}}
}{
\sqrt{\frac{\hbar}{2m\omega}}
}
=
\sqrt{
\frac{m\omega}{2\hbar}
\cdot
\frac{2m\omega}{\hbar}
}
=
\frac{m\omega}{\hbar}.

$$


So the differential equation is


$$

\frac{d\phi_0}{dx}
=
-\frac{m\omega}{\hbar}x\phi_0(x).

$$


Divide by  $\phi_0(x)$:


$$

\frac{1}{\phi_0(x)}
\frac{d\phi_0}{dx}
=
-\frac{m\omega}{\hbar}x.

$$


This is


$$

\frac{d}{dx}\ln\phi_0(x)
=
-\frac{m\omega}{\hbar}x.

$$


Integrate both sides:


$$

\ln\phi_0(x)
=
-\frac{m\omega}{2\hbar}x^2+C.

$$


Exponentiate:


$$

\phi_0(x)
=
A
\exp\left[
-\frac{m\omega x^2}{2\hbar}
\right].

$$


Now normalize it:


$$

\int_{-\infty}^{\infty}\vert \phi_0(x)\vert^2dx=1.

$$


Since


$$

\vert \phi_0(x)\vert^2
=
\vert A\vert^2
\exp\left[
-\frac{m\omega x^2}{\hbar}
\right],

$$


we need


$$

\vert A\vert^2
\int_{-\infty}^{\infty}
\exp\left[
-\frac{m\omega}{\hbar}x^2
\right]dx
=
1.

$$


Using


$$

\int_{-\infty}^{\infty}e^{-ax^2}dx
=
\sqrt{\frac{\pi}{a}},

$$


with


$$

a=\frac{m\omega}{\hbar},

$$


we get


$$

\int_{-\infty}^{\infty}
\exp\left[
-\frac{m\omega}{\hbar}x^2
\right]dx
=
\sqrt{\frac{\pi\hbar}{m\omega}}.

$$


Therefore,


$$

\vert A\vert^2
\sqrt{\frac{\pi\hbar}{m\omega}}
=
1.

$$


So


$$

\vert A\vert^2
=
\sqrt{\frac{m\omega}{\pi\hbar}}.

$$


Taking $A$ real and positive,


$$

A
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/4}.

$$


Therefore,


$$

\boxed{
\phi_0(x)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m\omega x^2}{2\hbar}
\right].
}

$$


This is the formula for the harmonic oscillator ground-state wavefunction.

---

# 4. Ground-state density and entropy

The ground-state density is


$$

\rho_0(x)
=
\vert \phi_0(x)\vert^2.

$$


So


$$

\rho_0(x)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega x^2}{\hbar}
\right].

$$


Define


$$

\beta=\frac{m\omega}{\hbar}.

$$


Then


$$

\rho_0(x)
=
\sqrt{\frac{\beta}{\pi}}
e^{-\beta x^2}.

$$


This is a Gaussian centered at $x=0$.

Its entropy is


$$

S_x
=
-\int_{-\infty}^{\infty}
\rho_0(x)\ln\rho_0(x)\,dx.

$$


For a Gaussian of the form


$$

\rho(x)=\sqrt{\frac{\beta}{\pi}}e^{-\beta x^2},

$$


the entropy is


$$

S_x
=
\frac12\ln\left(\frac{\pi e}{\beta}\right).

$$


Substituting $\beta=m\omega/\hbar$,


$$

\boxed{
S_x
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right).
}

$$


This will also be the answer for the translated and time-dependent state, because translation and harmonic-oscillator motion do not change the width.

---

# 5. What the translation operator does

The lecture notes write


$$

\vert \psi_0\rangle
=
\exp\left(-\frac{i\xi\hat p}{\hbar}\right)\vert \phi_0\rangle.

$$


This operator translates the state by $\xi$. I want to check the sign carefully.

In position space,


$$

\hat p=-i\hbar\frac{d}{dx}.

$$


Therefore,


$$

\hat T(\xi)
=
\exp\left(-\frac{i\xi\hat p}{\hbar}\right)
=
\exp\left(
-\xi\frac{d}{dx}
\right).

$$


The operator


$$

\exp\left(-\xi\frac{d}{dx}\right)

$$


acts on a function by shifting its argument:


$$

e^{-\xi d/dx}f(x)=f(x-\xi).

$$


Therefore,


$$

\psi_0(x)
=
\langle x\vert \psi_0\rangle
=
\phi_0(x-\xi).

$$


So


$$

\boxed{
\psi_0(x)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m\omega (x-\xi)^2}{2\hbar}
\right].
}

$$


The density is


$$

\rho(x,0)
=
\vert \psi_0(x)\vert^2
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega (x-\xi)^2}{\hbar}
\right].

$$


This is the same Gaussian as the ground state, but centered at $x=\xi$.

---

# 6. Translation operator using commutators

The same result can be checked using commutators.

We know


$$

[\hat x,\hat p]=i\hbar.

$$


For


$$

\hat T(\xi)=e^{-i\xi\hat p/\hbar},

$$


one can show


$$

\hat T^\dagger(\xi)\hat x\hat T(\xi)
=
\hat x+\xi.

$$


Then the initial expectation value is


$$

\langle x\rangle_0
=
\langle\psi_0\vert \hat x\vert \psi_0\rangle.

$$


Substitute


$$

\vert \psi_0\rangle=\hat T(\xi)\vert \phi_0\rangle:

$$


$$

\langle x\rangle_0
=
\langle\phi_0\vert 
\hat T^\dagger(\xi)\hat x\hat T(\xi)
\vert \phi_0\rangle.

$$


Using the translation identity,


$$

\langle x\rangle_0
=
\langle\phi_0\vert 
(\hat x+\xi)
\vert \phi_0\rangle.

$$


The ground state is centered at zero, so


$$

\langle\phi_0\vert \hat x\vert \phi_0\rangle=0.

$$


Therefore,


$$

\boxed{
\langle x\rangle_0=\xi.
}

$$


Similarly,


$$

\hat T^\dagger(\xi)\hat p\hat T(\xi)=\hat p,

$$


because $\hat p$ commutes with itself. Therefore,


$$

\boxed{
\langle p\rangle_0=0.
}

$$


So the translated ground state starts at position $\xi$ with zero average momentum.

---

# 7. Small-displacement expansion in the oscillator basis

The lecture notes expand the translated state for small $\xi$:


$$

\vert \psi_0\rangle
=
e^{-i\xi\hat p/\hbar}\vert \phi_0\rangle.

$$


Using the exponential expansion,


$$

e^{-i\xi\hat p/\hbar}
=
1
-
\frac{i\xi}{\hbar}\hat p
-
\frac{\xi^2}{2\hbar^2}\hat p^2
+
O(\xi^3).

$$


So


$$

\vert \psi_0\rangle
=
\left[
1
-
\frac{i\xi}{\hbar}\hat p
-
\frac{\xi^2}{2\hbar^2}\hat p^2
+
O(\xi^3)
\right]
\vert \phi_0\rangle.

$$


The expansion coefficient in the energy basis is


$$

c_n
=
\langle\phi_n\vert \psi_0\rangle.

$$


Therefore,


$$

c_n
=
\langle\phi_n\vert \phi_0\rangle
-
\frac{i\xi}{\hbar}
\langle\phi_n\vert \hat p\vert \phi_0\rangle
-
\frac{\xi^2}{2\hbar^2}
\langle\phi_n\vert \hat p^2\vert \phi_0\rangle
+
O(\xi^3).

$$


The first term is


$$

\langle\phi_n\vert \phi_0\rangle=\delta_{n0}.

$$


Now use


$$

\hat p
=
i\sqrt{\frac{m\hbar\omega}{2}}
(\hat a^\dagger-\hat a).

$$


Since


$$

\hat a\vert \phi_0\rangle=0,

$$


and


$$

\hat a^\dagger\vert \phi_0\rangle=\vert \phi_1\rangle,

$$


we get


$$

\hat p\vert \phi_0\rangle
=
i\sqrt{\frac{m\hbar\omega}{2}}\vert \phi_1\rangle.

$$


Therefore,


$$

\langle\phi_n\vert \hat p\vert \phi_0\rangle
=
i\sqrt{\frac{m\hbar\omega}{2}}\delta_{n1}.

$$


For $\hat p^2\vert \phi_0\rangle$,


$$

\hat p^2
=
-\frac{m\hbar\omega}{2}
(\hat a^\dagger-\hat a)^2.

$$


Acting on the ground state,


$$

(\hat a^\dagger-\hat a)^2\vert \phi_0\rangle
=
(\hat a^\dagger)^2\vert \phi_0\rangle
-
\hat a\hat a^\dagger\vert \phi_0\rangle.

$$


Now,


$$

(\hat a^\dagger)^2\vert \phi_0\rangle
=
\sqrt{2}\vert \phi_2\rangle,

$$


and


$$

\hat a\hat a^\dagger\vert \phi_0\rangle
=
\vert \phi_0\rangle.

$$


So


$$

(\hat a^\dagger-\hat a)^2\vert \phi_0\rangle
=
\sqrt2\vert \phi_2\rangle-\vert \phi_0\rangle.

$$


Therefore,


$$

\hat p^2\vert \phi_0\rangle
=
-\frac{m\hbar\omega}{2}
\left(
\sqrt2\vert \phi_2\rangle-\vert \phi_0\rangle
\right).

$$


So


$$

\langle\phi_n\vert \hat p^2\vert \phi_0\rangle
=
-\frac{m\hbar\omega}{2}
\left(
\sqrt2\delta_{n2}-\delta_{n0}
\right).

$$


Substitute everything into $c_n$:


$$

c_n
=
\delta_{n0}
-
\frac{i\xi}{\hbar}
\left[
i\sqrt{\frac{m\hbar\omega}{2}}\delta_{n1}
\right]
-
\frac{\xi^2}{2\hbar^2}
\left[
-\frac{m\hbar\omega}{2}
\left(
\sqrt2\delta_{n2}-\delta_{n0}
\right)
\right]
+
O(\xi^3).

$$


The first-order term becomes


$$

-\frac{i\xi}{\hbar}
i\sqrt{\frac{m\hbar\omega}{2}}\delta_{n1}
=
\sqrt{\frac{m\omega}{2\hbar}}\xi\,\delta_{n1}.

$$


The second-order term becomes


$$

\frac{m\omega}{4\hbar}\xi^2
\left(
\sqrt2\delta_{n2}-\delta_{n0}
\right).

$$


Therefore,


$$

\boxed{
c_n
=
\delta_{n0}
+
\sqrt{\frac{m\omega}{2\hbar}}\xi\,\delta_{n1}
+
\frac{m\omega}{4\hbar}\xi^2
\left(
\sqrt2\delta_{n2}-\delta_{n0}
\right)
+
O(\xi^3).
}

$$


So the first few coefficients are


$$

\boxed{
c_0
=
1-\frac{m\omega}{4\hbar}\xi^2
+
O(\xi^4),
}

$$


$$

\boxed{
c_1
=
\sqrt{\frac{m\omega}{2\hbar}}\xi
+
O(\xi^3),
}

$$


$$

\boxed{
c_2
=
\frac{m\omega}{\sqrt8\,\hbar}\xi^2
+
O(\xi^4),
}

$$


and


$$

\boxed{
c_{n>2}=0
\quad
\text{up to order }\xi^2.
}

$$


This matches the lecture-note expansion.

---

# 8. Time dependence from the Heisenberg equations

The lecture notes give the Heisenberg-picture solutions:


$$

\hat x_H(t)
=
\hat x_S\cos\omega t
+
\frac{\hat p_S}{m\omega}\sin\omega t,

$$


and


$$

\hat p_H(t)
=
\hat p_S\cos\omega t
-
m\omega\hat x_S\sin\omega t.

$$


Because the Schrödinger and Heisenberg pictures agree at $t=0$, we can calculate expectation values using the initial state.

For the translated ground state,


$$

\langle x\rangle_0=\xi,

$$


and


$$

\langle p\rangle_0=0.

$$


Therefore,


$$

\langle x\rangle(t)
=
\langle \hat x_H(t)\rangle
=
\langle x\rangle_0\cos\omega t
+
\frac{\langle p\rangle_0}{m\omega}\sin\omega t.

$$


So


$$

\boxed{
\langle x\rangle(t)=\xi\cos\omega t.
}

$$


Similarly,


$$

\langle p\rangle(t)
=
\langle \hat p_H(t)\rangle
=
\langle p\rangle_0\cos\omega t
-
m\omega\langle x\rangle_0\sin\omega t.

$$


Thus,


$$

\boxed{
\langle p\rangle(t)=-m\omega\xi\sin\omega t.
}

$$


This is exactly the classical harmonic oscillator motion, which is a useful check on the result.

---

# 9. Why the wave packet does not spread

To calculate entropy, knowing only the center is not enough. Entropy depends on the width of the density. So I need to check whether the width changes with time.

The ground-state uncertainties are


$$

\Delta x_0^2=\frac{\hbar}{2m\omega},

$$


and


$$

\Delta p_0^2=\frac{m\hbar\omega}{2}.

$$


A translation changes the center but does not change the width. Therefore, for the translated ground state,


$$

\Delta x_0^2=\frac{\hbar}{2m\omega},

$$


and


$$

\Delta p_0^2=\frac{m\hbar\omega}{2}.

$$


The covariance is zero:


$$

\frac12\langle \Delta x\Delta p+\Delta p\Delta x\rangle_0=0.

$$


Now use


$$

\hat x_H(t)
=
\hat x_S\cos\omega t
+
\frac{\hat p_S}{m\omega}\sin\omega t.

$$


The fluctuation operator is


$$

\Delta \hat x_H(t)
=
\Delta \hat x_S\cos\omega t
+
\frac{\Delta \hat p_S}{m\omega}\sin\omega t.

$$


So


$$

\Delta x^2(t)
=
\langle [\Delta \hat x_H(t)]^2\rangle.

$$


Expanding,


$$

\Delta x^2(t)
=
\Delta x_0^2\cos^2\omega t
+
\frac{\Delta p_0^2}{m^2\omega^2}\sin^2\omega t
+
\frac{1}{m\omega}
\langle
\frac12(\Delta x\Delta p+\Delta p\Delta x)
\rangle_0
2\sin\omega t\cos\omega t.

$$


The covariance term is zero, so


$$

\Delta x^2(t)
=
\Delta x_0^2\cos^2\omega t
+
\frac{\Delta p_0^2}{m^2\omega^2}\sin^2\omega t.

$$


Substitute


$$

\Delta x_0^2=\frac{\hbar}{2m\omega},

$$


and


$$

\Delta p_0^2=\frac{m\hbar\omega}{2}.

$$


Then


$$

\frac{\Delta p_0^2}{m^2\omega^2}
=
\frac{m\hbar\omega/2}{m^2\omega^2}
=
\frac{\hbar}{2m\omega}.

$$


So


$$

\Delta x^2(t)
=
\frac{\hbar}{2m\omega}\cos^2\omega t
+
\frac{\hbar}{2m\omega}\sin^2\omega t.

$$


Therefore,


$$

\Delta x^2(t)
=
\frac{\hbar}{2m\omega}
(\cos^2\omega t+\sin^2\omega t).

$$


Since


$$

\cos^2\omega t+\sin^2\omega t=1,

$$


we get


$$

\boxed{
\Delta x^2(t)=\frac{\hbar}{2m\omega}.
}

$$


So the width is constant.

This is the key physical reason the entropy is constant.

---

# 10. Time-dependent position density


Before writing the full density, I think there is one assumption I should make clear.

From the lecture notes, I know the center moves like

$$

x_c(t)=\xi\cos(\omega t).

$$

But knowing the center is not enough to know the whole probability density. To write

$$

\rho(x,t)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega}{\hbar}
\left(
x-\xi\cos(\omega t)
\right)^2
\right],

$$

I am also assuming that the width of the Gaussian stays the same as the ground-state width.

So the assumption is

$$

\Delta x^2(t)=\Delta x^2(0)=\frac{\hbar}{2m\omega}.

$$

This is not obvious just from the center moving. A wave packet could move and also spread. That is what happened for the free Gaussian wave packet. Here, I am using the fact that this is a harmonic oscillator and the initial state is only a shifted ground state. Earlier, I checked the width using the Heisenberg equation for 

$$

\hat x_H(t)

$$
, and it gave

$$

\Delta x^2(t)=\frac{\hbar}{2m\omega}.

$$

So my logic is:

$$

\text{center changes, but width stays fixed.}

$$

That is why I write the density as the same Gaussian shape, just with the center replaced by

$$

x_c(t)=\xi\cos(\omega t).

$$

This is the step I should be careful about. The formula is not true for every wave packet. It works here because the translated harmonic-oscillator ground state keeps the same Gaussian width while it oscillates.
With that assumption, the density becomes

$$

\rho(x,t)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega}{\hbar}
\left(
x-\xi\cos(\omega t)
\right)^2
\right].

$$

This is something I should mention because the formula assumes no spreading and no change in shape. It is valid for a translated harmonic-oscillator ground state, but it would not automatically be true for a general wave packet, a squeezed state, a free particle, or an anharmonic potential.

The important point is that I am not assuming the state is stationary. The state is time-dependent because the center moves.  That is why the entropy stays constant.
Since the center is


$$

x_c(t)=\xi\cos\omega t,

$$


and the width is constant, the position-space density is


$$

\boxed{
\rho(x,t)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega}{\hbar}
\left(
x-\xi\cos\omega t
\right)^2
\right].
}

$$


This density is time-dependent because the center moves. But it is not spreading.

Using


$$

\beta=\frac{m\omega}{\hbar},

$$


we can write


$$

\rho(x,t)
=
\sqrt{\frac{\beta}{\pi}}
e^{-\beta(x-x_c(t))^2}.

$$


---

# 11. Position-space entropy calculation

Now calculate


$$

S_x(t)
=
-\int_{-\infty}^{\infty}
\rho(x,t)\ln\rho(x,t)\,dx.

$$


Start with


$$

\rho(x,t)
=
\sqrt{\frac{\beta}{\pi}}
e^{-\beta(x-x_c)^2}.

$$


Take the logarithm:


$$

\ln\rho(x,t)
=
\ln\left[
\sqrt{\frac{\beta}{\pi}}
e^{-\beta(x-x_c)^2}
\right].

$$


Using log rules,


$$

\ln\rho(x,t)
=
\frac12\ln\left(\frac{\beta}{\pi}\right)
-
\beta(x-x_c)^2.

$$


Substitute into the entropy:


$$

S_x(t)
=
-\int
\rho(x,t)
\left[
\frac12\ln\left(\frac{\beta}{\pi}\right)
-
\beta(x-x_c)^2
\right]dx.

$$


Separate the terms:


$$

S_x(t)
=
-\frac12\ln\left(\frac{\beta}{\pi}\right)
\int \rho(x,t)\,dx
+
\beta
\int (x-x_c)^2\rho(x,t)\,dx.

$$


The first integral is normalization:


$$

\int \rho(x,t)\,dx=1.

$$


The second integral is the variance of this Gaussian:


$$

\int (x-x_c)^2\rho(x,t)\,dx
=
\frac{1}{2\beta}.

$$


Therefore,


$$

S_x(t)
=
-\frac12\ln\left(\frac{\beta}{\pi}\right)
+
\beta\left(\frac{1}{2\beta}\right).

$$


So


$$

S_x(t)
=
-\frac12\ln\left(\frac{\beta}{\pi}\right)+\frac12.

$$


Equivalently,


$$

S_x(t)
=
\frac12\ln\left(\frac{\pi}{\beta}\right)+\frac12.

$$


Now substitute


$$

\beta=\frac{m\omega}{\hbar}.

$$


Then


$$

\frac{\pi}{\beta}
=
\frac{\pi\hbar}{m\omega}.

$$


So


$$

S_x(t)
=
\frac12
\ln\left(
\frac{\pi\hbar}{m\omega}
\right)
+
\frac12.

$$


Use


$$

\frac12=\frac12\ln e.

$$


Then


$$

S_x(t)
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right).

$$


Therefore,


$$

\boxed{
S_x(t)
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right).
}

$$


There is no $t$ left in the answer. The $t$-dependence only shifts the center $x_c(t)$, and differential entropy is unchanged by translation.

---

# 12. Momentum-space density and entropy

The center in momentum space is


$$

p_c(t)
=
-m\omega\xi\sin\omega t.

$$


The momentum distribution remains Gaussian with fixed width:


$$

\boxed{
\gamma(p,t)
=
\frac{1}{\sqrt{\pi m\hbar\omega}}
\exp\left[
-\frac{(p-p_c(t))^2}{m\hbar\omega}
\right].
}

$$


Define


$$

\eta=\frac{1}{m\hbar\omega}.

$$


Then


$$

\gamma(p,t)
=
\sqrt{\frac{\eta}{\pi}}
e^{-\eta(p-p_c(t))^2}.

$$


Using the same entropy calculation,


$$

S_p(t)
=
\frac12\ln\left(\frac{\pi}{\eta}\right)+\frac12.

$$


Substitute


$$

\eta=\frac{1}{m\hbar\omega}.

$$


Then


$$

\frac{\pi}{\eta}
=
\pi m\hbar\omega.

$$


Therefore,


$$

S_p(t)
=
\frac12\ln(\pi m\hbar\omega)+\frac12.

$$


Using


$$

\frac12=\frac12\ln e,

$$


we get


$$

\boxed{
S_p(t)
=
\frac12\ln(\pi e m\hbar\omega).
}

$$


Again, there is no time dependence because the momentum density only shifts its center.

---

# 13. Total entropy

The total entropy is


$$

S_{\text{tot}}(t)
=
S_x(t)+S_p(t).

$$


Using


$$

S_x(t)
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right),

$$


and


$$

S_p(t)
=
\frac12
\ln(\pi e m\hbar\omega),

$$


we get


$$

S_{\text{tot}}(t)
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right)
+
\frac12
\ln(\pi e m\hbar\omega).

$$


Combine the logarithms:


$$

S_{\text{tot}}(t)
=
\frac12
\ln\left[
\left(
\frac{\pi e\hbar}{m\omega}
\right)
(\pi e m\hbar\omega)
\right].

$$


Simplify inside the logarithm:


$$

\left(
\frac{\pi e\hbar}{m\omega}
\right)
(\pi e m\hbar\omega)
=
\pi^2e^2\hbar^2.

$$


Therefore,


$$

S_{\text{tot}}(t)
=
\frac12\ln(\pi^2e^2\hbar^2).

$$


So


$$

\boxed{
S_{\text{tot}}(t)=\ln(\pi e\hbar).
}

$$


This is the minimum-uncertainty Gaussian value.

---

# 14. Final physical interpretation

The translated harmonic oscillator ground state has


$$

\langle x\rangle(t)=\xi\cos\omega t,

$$


and


$$

\langle p\rangle(t)=-m\omega\xi\sin\omega t.

$$


So the center moves exactly like a classical harmonic oscillator.

But the width stays fixed:


$$

\Delta x^2(t)=\frac{\hbar}{2m\omega}.

$$


Therefore the position density is always a Gaussian of the same width:


$$

\rho(x,t)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{1/2}
\exp\left[
-\frac{m\omega}{\hbar}
(x-\xi\cos\omega t)^2
\right].

$$


Since entropy depends on the spread of the density and not on the center location,


$$

\boxed{
S_x(t)=S_x(0).
}

$$


The final answers are


$$

\boxed{
S_x(t)
=
\frac12
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right),
}

$$


$$

\boxed{
S_p(t)
=
\frac12
\ln(\pi e m\hbar\omega),
}

$$


and


$$

\boxed{
S_{\text{tot}}(t)=\ln(\pi e\hbar).
}

$$


So the translated harmonic oscillator ground state is time-dependent, but its entropy is not. It is a coherent-state-like packet: it oscillates without spreading.

This is different from the free Gaussian wave packet, where the width increases with time and the entropy increases like


$$

S_x(t)=S_x(0)+\frac12\ln(1+\alpha^2t^2).

$$


For the harmonic oscillator translated ground state, the corresponding statement is instead


$$

\boxed{
\text{center changes, width does not change, entropy stays constant.}
}

$$


---

# 15. Three-dimensional generalization

After finishing the one-dimensional case, I wanted to write the same idea in three dimensions. This is the version I need before moving into numerical methods, because most realistic wave packets will not only live on one line. The good news is that the logic does not change too much. The 3D problem is basically three one-dimensional oscillator problems placed side by side.

The important thing I noticed is this: the wave packet can move in the $x$, $y$, and $z$ directions, but if it is still a translated harmonic-oscillator ground state, the Gaussian shape does not spread. So the entropy stays constant for the same reason as before. The center changes, but the widths do not.

## 15.1 Starting from the 3D harmonic oscillator Hamiltonian

In one dimension, the harmonic oscillator Hamiltonian was


$$

\hat H
=
\frac{\hat p^2}{2m}
+
\frac12m\omega^2\hat x^2.

$$


In three dimensions, the position vector is


$$

\mathbf r=(x,y,z),

$$


and the momentum operator is


$$

\hat{\mathbf p}=(\hat p_x,\hat p_y,\hat p_z).

$$


For the most general separable oscillator, I can allow the oscillator frequency to be different in each direction. Then


$$

\hat H
=
\frac{\hat p_x^2+\hat p_y^2+\hat p_z^2}{2m}
+
\frac12m\omega_x^2\hat x^2
+
\frac12m\omega_y^2\hat y^2
+
\frac12m\omega_z^2\hat z^2.

$$


I can also write this as


$$

\hat H=\hat H_x+\hat H_y+\hat H_z,

$$


where


$$

\hat H_x
=
\frac{\hat p_x^2}{2m}
+
\frac12m\omega_x^2\hat x^2,

$$


$$

\hat H_y
=
\frac{\hat p_y^2}{2m}
+
\frac12m\omega_y^2\hat y^2,

$$


and


$$

\hat H_z
=
\frac{\hat p_z^2}{2m}
+
\frac12m\omega_z^2\hat z^2.

$$


This is why the 3D calculation is not really a brand-new problem. It is three independent copies of the 1D oscillator.

## 15.2 The 3D ground state

From the 1D result, the ground-state wavefunction in the $x$ direction is


$$

\phi_{0x}(x)
=
\left(
\frac{m\omega_x}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m\omega_xx^2}{2\hbar}
\right].

$$


Similarly,


$$

\phi_{0y}(y)
=
\left(
\frac{m\omega_y}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m\omega_yy^2}{2\hbar}
\right],

$$


and


$$

\phi_{0z}(z)
=
\left(
\frac{m\omega_z}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m\omega_zz^2}{2\hbar}
\right].

$$


Since the Hamiltonian separates, the full 3D ground state is a product:


$$

\phi_0(x,y,z)
=
\phi_{0x}(x)\phi_{0y}(y)\phi_{0z}(z).

$$


Substituting each factor gives


$$

\phi_0(x,y,z)
=
\left(
\frac{m\omega_x}{\pi\hbar}
\right)^{1/4}
\left(
\frac{m\omega_y}{\pi\hbar}
\right)^{1/4}
\left(
\frac{m\omega_z}{\pi\hbar}
\right)^{1/4}
\exp\left[
-\frac{m}{2\hbar}
\left(
\omega_xx^2+\omega_yy^2+\omega_zz^2
\right)
\right].

$$


The normalization constants multiply together:


$$

\left(
\frac{m\omega_x}{\pi\hbar}
\right)^{1/4}
\left(
\frac{m\omega_y}{\pi\hbar}
\right)^{1/4}
\left(
\frac{m\omega_z}{\pi\hbar}
\right)^{1/4}
=
\left(
\frac{m^3\omega_x\omega_y\omega_z}{\pi^3\hbar^3}
\right)^{1/4}.

$$


Therefore,


$$

\boxed{
\phi_0(\mathbf r)
=
\left(
\frac{m^3\omega_x\omega_y\omega_z}{\pi^3\hbar^3}
\right)^{1/4}
\exp\left[
-\frac{m}{2\hbar}
\left(
\omega_xx^2+\omega_yy^2+\omega_zz^2
\right)
\right].
}

$$


If the oscillator has the same frequency in all directions, then


$$

\omega_x=\omega_y=\omega_z=\omega.

$$


This is the isotropic oscillator. In that case,


$$

\phi_0(\mathbf r)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{3/4}
\exp\left[
-\frac{m\omega}{2\hbar}
(x^2+y^2+z^2)
\right].

$$


Since


$$

r^2=x^2+y^2+z^2,

$$


I can write the isotropic ground state as


$$

\boxed{
\phi_0(\mathbf r)
=
\left(
\frac{m\omega}{\pi\hbar}
\right)^{3/4}
\exp\left[
-\frac{m\omega r^2}{2\hbar}
\right].
}

$$


## 15.3 Translating the 3D ground state

In one dimension, the translation was controlled by one displacement, $\xi$. In three dimensions, I need a displacement vector:


$$

\boldsymbol{\xi}
=
(\xi_x,\xi_y,\xi_z).

$$


The 3D translation operator is


$$

\hat T(\boldsymbol{\xi})
=
\exp\left[
-\frac{i}{\hbar}
\boldsymbol{\xi}\cdot\hat{\mathbf p}
\right].

$$


The dot product means


$$

\boldsymbol{\xi}\cdot\hat{\mathbf p}
=
\xi_x\hat p_x+\xi_y\hat p_y+\xi_z\hat p_z.

$$


So the translated initial state is


$$

\boxed{
\vert \psi_0\rangle
=
\hat T(\boldsymbol{\xi})\vert \phi_0\rangle
=
\exp\left[
-\frac{i}{\hbar}
\boldsymbol{\xi}\cdot\hat{\mathbf p}
\right]
\vert \phi_0\rangle.
}

$$


In position space, the translation shifts the argument of the wavefunction:


$$

\psi_0(\mathbf r)
=
\phi_0(\mathbf r-\boldsymbol{\xi}).

$$


Since


$$

\mathbf r-\boldsymbol{\xi}
=
(x-\xi_x,\ y-\xi_y,\ z-\xi_z),

$$


this means


$$

\boxed{
\psi_0(x,y,z)
=
\phi_0(x-\xi_x,\ y-\xi_y,\ z-\xi_z).
}

$$


Using the anisotropic ground state, the translated wavefunction is


$$

\psi_0(x,y,z)
=
\left(
\frac{m^3\omega_x\omega_y\omega_z}{\pi^3\hbar^3}
\right)^{1/4}
\exp\left[
-\frac{m}{2\hbar}
\left(
\omega_x(x-\xi_x)^2
+
\omega_y(y-\xi_y)^2
+
\omega_z(z-\xi_z)^2
\right)
\right].

$$


This is where I can already see the important point. The center has moved from the origin to $(\xi_x,\xi_y,\xi_z)$, but the Gaussian widths have not changed.

## 15.4 Time-dependent center in 3D

From the one-dimensional Heisenberg result, the center in the $x$ direction moves as


$$

x_c(t)=\xi_x\cos(\omega_xt).

$$


The same thing happens in the other directions:


$$

y_c(t)=\xi_y\cos(\omega_yt),

$$


and


$$

z_c(t)=\xi_z\cos(\omega_zt).

$$


So the full center vector is


$$

\boxed{
\mathbf r_c(t)
=
\left(
\xi_x\cos(\omega_xt),
\xi_y\cos(\omega_yt),
\xi_z\cos(\omega_zt)
\right).
}

$$


The momentum center is


$$

\boxed{
\mathbf p_c(t)
=
\left(
-m\omega_x\xi_x\sin(\omega_xt),
-m\omega_y\xi_y\sin(\omega_yt),
-m\omega_z\xi_z\sin(\omega_zt)
\right).
}

$$


This is just the classical harmonic oscillator motion happening separately in each coordinate.

## 15.5 The 3D probability density

The time-dependent 3D probability density is the same Gaussian shape centered at $\mathbf r_c(t)$:


$$

\rho(\mathbf r,t)
=
\left(
\frac{m^3\omega_x\omega_y\omega_z}{\pi^3\hbar^3}
\right)^{1/2}
\exp\left[
-\frac{m}{\hbar}
\left(
\omega_x(x-x_c(t))^2
+
\omega_y(y-y_c(t))^2
+
\omega_z(z-z_c(t))^2
\right)
\right].

$$


To make the entropy calculation cleaner, I define


$$

\beta_x=\frac{m\omega_x}{\hbar},
\qquad
\beta_y=\frac{m\omega_y}{\hbar},
\qquad
\beta_z=\frac{m\omega_z}{\hbar}.

$$


Then


$$

\rho(x,y,z,t)
=
\sqrt{\frac{\beta_x}{\pi}}
\sqrt{\frac{\beta_y}{\pi}}
\sqrt{\frac{\beta_z}{\pi}}
\exp\left[
-\beta_x(x-x_c)^2
-\beta_y(y-y_c)^2
-\beta_z(z-z_c)^2
\right].

$$


This factors into three one-dimensional Gaussian densities:


$$

\rho(x,y,z,t)
=
\rho_x(x,t)\rho_y(y,t)\rho_z(z,t),

$$


where


$$

\rho_x(x,t)=\sqrt{\frac{\beta_x}{\pi}}e^{-\beta_x(x-x_c)^2},

$$


$$

\rho_y(y,t)=\sqrt{\frac{\beta_y}{\pi}}e^{-\beta_y(y-y_c)^2},

$$


and


$$

\rho_z(z,t)=\sqrt{\frac{\beta_z}{\pi}}e^{-\beta_z(z-z_c)^2}.

$$


This factorization is the main reason the 3D entropy calculation stays manageable.

## 15.6 Position-space entropy in 3D

The 3D position-space entropy is


$$

S_{\mathbf r}(t)
=
-\int_{\mathbb R^3}
\rho(\mathbf r,t)\ln\rho(\mathbf r,t)\,d^3r.

$$


Since


$$

d^3r=dx\,dy\,dz,

$$


this means


$$

S_{\mathbf r}(t)
=
-\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
\int_{-\infty}^{\infty}
\rho(x,y,z,t)
\ln\rho(x,y,z,t)
\,dx\,dy\,dz.

$$


Now take the logarithm of the density:


$$

\ln\rho
=
\frac12\ln\left(\frac{\beta_x}{\pi}\right)
+
\frac12\ln\left(\frac{\beta_y}{\pi}\right)
+
\frac12\ln\left(\frac{\beta_z}{\pi}\right)
-\beta_x(x-x_c)^2
-\beta_y(y-y_c)^2
-\beta_z(z-z_c)^2.

$$


Substitute this into the entropy:


$$

S_{\mathbf r}(t)
=
-\int\rho
\left[
\frac12\ln\left(\frac{\beta_x}{\pi}\right)
+
\frac12\ln\left(\frac{\beta_y}{\pi}\right)
+
\frac12\ln\left(\frac{\beta_z}{\pi}\right)
-\beta_x(x-x_c)^2
-\beta_y(y-y_c)^2
-\beta_z(z-z_c)^2
\right]d^3r.

$$


The normalization is


$$

\int\rho\,d^3r=1.

$$


The variance in each direction is


$$

\int (x-x_c)^2\rho\,d^3r
=
\frac{1}{2\beta_x},

$$


$$

\int (y-y_c)^2\rho\,d^3r
=
\frac{1}{2\beta_y},

$$


and


$$

\int (z-z_c)^2\rho\,d^3r
=
\frac{1}{2\beta_z}.

$$


So the entropy becomes


$$

S_{\mathbf r}(t)
=
-\frac12\ln\left(\frac{\beta_x}{\pi}\right)
-\frac12\ln\left(\frac{\beta_y}{\pi}\right)
-\frac12\ln\left(\frac{\beta_z}{\pi}\right)
+
\frac12+
\frac12+
\frac12.

$$


Therefore,


$$

S_{\mathbf r}(t)
=
\frac12\ln\left(\frac{\pi}{\beta_x}\right)
+
\frac12\ln\left(\frac{\pi}{\beta_y}\right)
+
\frac12\ln\left(\frac{\pi}{\beta_z}\right)
+
\frac32.

$$


Now I split the $3/2$ into three copies of $1/2$, and use


$$

\frac12=\frac12\ln e.

$$


This gives


$$

S_{\mathbf r}(t)
=
\frac12\ln\left(\frac{\pi e}{\beta_x}\right)
+
\frac12\ln\left(\frac{\pi e}{\beta_y}\right)
+
\frac12\ln\left(\frac{\pi e}{\beta_z}\right).

$$


Now substitute $\beta_x=m\omega_x/\hbar$, $\beta_y=m\omega_y/\hbar$, and $\beta_z=m\omega_z/\hbar$:


$$

\boxed{
S_{\mathbf r}(t)
=
\frac12\ln\left(\frac{\pi e\hbar}{m\omega_x}\right)
+
\frac12\ln\left(\frac{\pi e\hbar}{m\omega_y}\right)
+
\frac12\ln\left(\frac{\pi e\hbar}{m\omega_z}\right).
}

$$


Combining the logarithms,


$$

\boxed{
S_{\mathbf r}(t)
=
\frac12
\ln\left[
\frac{(\pi e\hbar)^3}{m^3\omega_x\omega_y\omega_z}
\right].
}

$$


There is no time left in the answer. This matches what I expected: the packet moves, but the shape does not spread, so the entropy is constant.

## 15.7 Isotropic 3D result

If the oscillator has the same frequency in all directions,


$$

\omega_x=\omega_y=\omega_z=\omega,

$$


then


$$

S_{\mathbf r}(t)
=
\frac12
\ln\left[
\frac{(\pi e\hbar)^3}{m^3\omega^3}
\right].

$$


This is


$$

S_{\mathbf r}(t)
=
\frac12
\ln\left[
\left(
\frac{\pi e\hbar}{m\omega}
\right)^3
\right].

$$


Using $\ln(A^3)=3\ln A$,


$$

\boxed{
S_{\mathbf r}(t)
=
\frac32
\ln\left(
\frac{\pi e\hbar}{m\omega}
\right).
}

$$


So for the isotropic oscillator,


$$

\boxed{
S_{\mathbf r,\mathrm{3D}}(t)=3S_{x,\mathrm{1D}}(t).
}

$$


This is a good check because the isotropic 3D oscillator is three identical 1D oscillators.

## 15.8 Momentum-space entropy in 3D

The momentum-space density is also a product of three Gaussians. Define


$$

\eta_x=\frac{1}{m\hbar\omega_x},
\qquad
\eta_y=\frac{1}{m\hbar\omega_y},
\qquad
\eta_z=\frac{1}{m\hbar\omega_z}.

$$


Then


$$

\gamma(\mathbf p,t)
=
\sqrt{\frac{\eta_x}{\pi}}
\sqrt{\frac{\eta_y}{\pi}}
\sqrt{\frac{\eta_z}{\pi}}
\exp\left[
-\eta_x(p_x-p_{x,c})^2
-\eta_y(p_y-p_{y,c})^2
-\eta_z(p_z-p_{z,c})^2
\right].

$$


The entropy calculation is the same as position space, just with $\eta$ instead of $\beta$:


$$

S_{\mathbf p}(t)
=
\frac12\ln\left(\frac{\pi e}{\eta_x}\right)
+
\frac12\ln\left(\frac{\pi e}{\eta_y}\right)
+
\frac12\ln\left(\frac{\pi e}{\eta_z}\right).

$$


Substituting the $\eta$ values gives


$$

\boxed{
S_{\mathbf p}(t)
=
\frac12\ln(\pi e m\hbar\omega_x)
+
\frac12\ln(\pi e m\hbar\omega_y)
+
\frac12\ln(\pi e m\hbar\omega_z).
}

$$


Combining the logarithms,


$$

\boxed{
S_{\mathbf p}(t)
=
\frac12
\ln\left[
(\pi e)^3m^3\hbar^3\omega_x\omega_y\omega_z
\right].
}

$$


For the isotropic case,


$$

\boxed{
S_{\mathbf p}(t)
=
\frac32\ln(\pi e m\hbar\omega).
}

$$


## 15.9 Total 3D entropy

The total 3D entropy is


$$

S_{\mathrm{tot}}(t)
=
S_{\mathbf r}(t)+S_{\mathbf p}(t).

$$


Using the two results,


$$

S_{\mathbf r}(t)
=
\frac12
\ln\left[
\frac{(\pi e\hbar)^3}{m^3\omega_x\omega_y\omega_z}
\right],

$$


and


$$

S_{\mathbf p}(t)
=
\frac12
\ln\left[
(\pi e)^3m^3\hbar^3\omega_x\omega_y\omega_z
\right],

$$


I get


$$

S_{\mathrm{tot}}(t)
=
\frac12
\ln\left[
\frac{(\pi e\hbar)^3}{m^3\omega_x\omega_y\omega_z}
(\pi e)^3m^3\hbar^3\omega_x\omega_y\omega_z
\right].

$$


The $m^3$ cancels, and the product $\omega_x\omega_y\omega_z$ also cancels:


$$

S_{\mathrm{tot}}(t)
=
\frac12
\ln\left[
(\pi e)^6\hbar^6
\right].

$$


Therefore,


$$

\boxed{
S_{\mathrm{tot}}(t)=3\ln(\pi e\hbar).
}

$$


This is exactly three times the 1D total entropy:


$$

\boxed{
S_{\mathrm{tot,3D}}(t)=3S_{\mathrm{tot,1D}}(t).
}

$$


## 15.10 What I take away from the 3D version

The 3D version helped me see the structure more clearly. The result is not constant because the state is stationary. It is not stationary. The center moves in time. The entropy is constant because the probability cloud keeps the same widths in all directions.

In 1D, the width was


$$

\Delta x^2=\frac{\hbar}{2m\omega}.

$$


In 3D, the widths are


$$

\Delta x^2=\frac{\hbar}{2m\omega_x},
\qquad
\Delta y^2=\frac{\hbar}{2m\omega_y},
\qquad
\Delta z^2=\frac{\hbar}{2m\omega_z}.

$$


These widths do not change with time for a translated harmonic-oscillator ground state. The center moves, but the Gaussian volume does not expand. That is why


$$

\boxed{
S_{\mathbf r}(t)=S_{\mathbf r}(0),
\qquad
S_{\mathbf p}(t)=S_{\mathbf p}(0).
}

$$


This is also the clean contrast with the free Gaussian wave packet. The free Gaussian spreads, so its position entropy grows. The translated harmonic oscillator Gaussian does not spread, so its entropy stays fixed.

---


# 16. Python code can be used for the visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# Entropy of a translated harmonic-oscillator ground state
#
# Initial state:
#   |psi_0> = exp(-i xi p_hat / hbar) |phi_0>
#
# This is the harmonic oscillator ground state translated by xi.
#
# Position density:
#   rho(x,t) = sqrt(m omega/(pi hbar))
#              exp[-(m omega/hbar)(x - xi cos(omega t))^2]
#
# Momentum density:
#   gamma(p,t) = 1/sqrt(pi m hbar omega)
#                exp[-(p + m omega xi sin(omega t))^2/(m hbar omega)]
#
# Entropies:
#   Sx(t) = 1/2 ln(pi e hbar/(m omega))
#   Sp(t) = 1/2 ln(pi e m hbar omega)
#   Stot(t) = ln(pi e hbar)
# ============================================================

output_dir = Path("figures")
output_dir.mkdir(exist_ok=True)

# Natural-unit parameters for visualization.
hbar = 1.0
m = 1.0
omega = 1.0
xi = 2.0

beta = m * omega / hbar
eta = 1.0 / (m * hbar * omega)

# ------------------------------------------------------------
# Plot 1: entropy versus time
# ------------------------------------------------------------
t = np.linspace(0, 4*np.pi, 600)

Sx = 0.5 * np.log(np.pi * np.e * hbar / (m * omega)) * np.ones_like(t)
Sp = 0.5 * np.log(np.pi * np.e * m * hbar * omega) * np.ones_like(t)
Stot = Sx + Sp

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    Sx,
    linewidth=2.5,
    label=r"$S_x(t)=\frac{1}{2}\ln\!\left(\frac{\pi e\hbar}{m\omega}\right)$",
)

plt.plot(
    t,
    Sp,
    linewidth=2.5,
    linestyle="--",
    label=r"$S_p(t)=\frac{1}{2}\ln\!\left(\pi e m\hbar\omega\right)$",
)

plt.plot(
    t,
    Stot,
    linewidth=2.5,
    linestyle=":",
    label=r"$S_{\rm tot}(t)=\ln(\pi e\hbar)$",
)

plt.xlabel(r"Time $t$", fontsize=13)
plt.ylabel(r"Differential Shannon entropy", fontsize=13)
plt.title(r"Entropy of a Translated Harmonic-Oscillator Ground State", fontsize=14)
plt.legend(fontsize=10, loc="best")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "ho_entropy_constant.png", dpi=300, bbox_inches="tight")
plt.show()

# ------------------------------------------------------------
# Plot 2: moving Gaussian position density
# ------------------------------------------------------------
x = np.linspace(-4.5, 4.5, 1000)

times = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]

plt.figure(figsize=(10, 6))

for tt in times:
    xc = xi * np.cos(omega * tt)
    rho = np.sqrt(beta/np.pi) * np.exp(-beta * (x - xc)**2)
    plt.plot(x, rho, linewidth=2.2, label=rf"$t={tt:.2f},\ x_c(t)={xc:.2f}$")

plt.xlabel(r"Position $x$", fontsize=13)
plt.ylabel(r"Probability density $\rho(x,t)$", fontsize=13)
plt.title(r"Translated Ground-State Density: Same Width, Oscillating Center", fontsize=14)
plt.legend(fontsize=10, loc="best")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "ho_density_moving_gaussian.png", dpi=300, bbox_inches="tight")
plt.show()

$$


