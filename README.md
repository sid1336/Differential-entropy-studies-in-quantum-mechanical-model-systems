# Differential Shannon Entropy of Gaussian Wave Packets

This write-up collects the calculations I worked through for Gaussian wave packets and differential Shannon entropy. The goal is to make the derivation professor-review ready and GitHub-ready, with every important algebraic step shown clearly.

The entropy definition used here is the one used by Schürger and Engel for a continuous probability density:

$$
S(t)=-\int \rho(x,t)\ln \rho(x,t)\,dx.
$$

For a wavefunction,

$$
\rho(x,t)=|\psi(x,t)|^2.
$$

All logarithms are natural logarithms. Throughout the calculations, I use the standard physics convention where the variables are treated in a fixed unit system. Strictly, differential entropy for dimensional variables depends on the unit scale. In practice, this is usually handled by working in atomic units, natural units, or by comparing entropy differences rather than absolute values.

---

## Contents

1. [Stationary 1D Gaussian wave packet](#1-stationary-1d-gaussian-wave-packet)
2. [Free spreading Gaussian wave packet in position space](#2-free-spreading-gaussian-wave-packet-in-position-space)
3. [Free Gaussian wave packet in momentum space](#3-free-gaussian-wave-packet-in-momentum-space)
4. [Total position plus momentum entropy](#4-total-position-plus-momentum-entropy)
5. [Shape of the entropy curves](#5-shape-of-the-entropy-curves)
6. [Python visualization code](#6-python-visualization-code)
7. [How to run this project](#7-how-to-run-this-project)

---

# 1. Stationary 1D Gaussian wave packet

I first consider a stationary one-dimensional Gaussian wave packet of the form

$$
\psi(x)=\frac{1}{\pi^{1/4}\sigma^{1/2}}
\exp\left[-\frac{(x-x_0)^2}{2\sigma^2}\right]e^{ikx}.
$$

Here:

- \(x_0\) is the center of the packet.
- \(\sigma\) controls the spatial width.
- \(k\) is the average wave number.
- The phase factor \(e^{ikx}\) does not affect the probability density.

The probability density is

$$
\rho(x)=|\psi(x)|^2.
$$

Since

$$
|e^{ikx}|^2=1,
$$

we get

$$
\rho(x)
=
\frac{1}{\sigma\sqrt{\pi}}
\exp\left[-\frac{(x-x_0)^2}{\sigma^2}\right].
$$

The entropy is

$$
S_x=-\int_{-\infty}^{\infty}\rho(x)\ln\rho(x)\,dx.
$$

First compute the logarithm:

$$
\ln\rho(x)
=
\ln\left[
\frac{1}{\sigma\sqrt{\pi}}
\exp\left(-\frac{(x-x_0)^2}{\sigma^2}\right)
\right].
$$

Using

$$
\ln(AB)=\ln A+\ln B,
$$

this becomes

$$
\ln\rho(x)
=
\ln\left(\frac{1}{\sigma\sqrt{\pi}}\right)
+
\ln\left[
\exp\left(-\frac{(x-x_0)^2}{\sigma^2}\right)
\right].
$$

Since

$$
\ln(e^A)=A,
$$

we have

$$
\ln\rho(x)
=
-\ln(\sigma\sqrt{\pi})
-
\frac{(x-x_0)^2}{\sigma^2}.
$$

Now substitute into the entropy:

$$
S_x
=
-\int_{-\infty}^{\infty}
\rho(x)
\left[
-\ln(\sigma\sqrt{\pi})
-
\frac{(x-x_0)^2}{\sigma^2}
\right]dx.
$$

Distribute the minus sign:

$$
S_x
=
\int_{-\infty}^{\infty}
\rho(x)\ln(\sigma\sqrt{\pi})\,dx
+
\int_{-\infty}^{\infty}
\rho(x)\frac{(x-x_0)^2}{\sigma^2}\,dx.
$$

The first term is

$$
\ln(\sigma\sqrt{\pi})
\int_{-\infty}^{\infty}\rho(x)\,dx.
$$

Because the probability density is normalized,

$$
\int_{-\infty}^{\infty}\rho(x)\,dx=1.
$$

Therefore,

$$
\text{first term}=\ln(\sigma\sqrt{\pi}).
$$

For the second term,

$$
\int_{-\infty}^{\infty}
\rho(x)\frac{(x-x_0)^2}{\sigma^2}\,dx
=
\frac{1}{\sigma^2}
\int_{-\infty}^{\infty}
(x-x_0)^2\rho(x)\,dx.
$$

For this Gaussian density,

$$
\int_{-\infty}^{\infty}
(x-x_0)^2\rho(x)\,dx
=
\frac{\sigma^2}{2}.
$$

So

$$
\text{second term}
=
\frac{1}{\sigma^2}\frac{\sigma^2}{2}
=
\frac12.
$$

Therefore,

$$
S_x
=
\ln(\sigma\sqrt{\pi})+\frac12.
$$

This is already a complete answer. It can also be written in a compact form. Since

$$
\frac12=\ln(e^{1/2}),
$$

we can write

$$
S_x
=
\ln(\sigma\sqrt{\pi})+\ln(e^{1/2}).
$$

Using

$$
\ln A+\ln B=\ln(AB),
$$

we get

$$
S_x
=
\ln(\sigma\sqrt{\pi}\sqrt e).
$$

Therefore,

$$
S_x
=
\ln(\sigma\sqrt{\pi e}).
$$

Equivalently,

$$
\boxed{
S_x=\frac12\ln(\pi e\sigma^2).
}
$$

The important point is that the \(e\) appears only because the extra \(+\frac12\) term can be written as a logarithm:

$$
\frac12=\ln(e^{1/2}).
$$

For a stationary wave packet, \(\sigma\) is constant, so

$$
\boxed{
S_x(t)=S_x(0)=\frac12\ln(\pi e\sigma^2).
}
$$

---

# 2. Free spreading Gaussian wave packet in position space

Now I consider the free-particle Gaussian wave packet from the PHYS 4010 problem:

$$
\psi_0(x)
=
\left(\frac{2\lambda}{\pi}\right)^{1/4}e^{-\lambda x^2},
\qquad \lambda>0.
$$

At later time \(t>0\), the free-particle solution is

$$
\psi(x,t)
=
\left(\frac{2\lambda}{\pi}\right)^{1/4}
\frac{1}{\sqrt{1+i\alpha t}}
\exp\left[
-\frac{\lambda x^2}{1+i\alpha t}
\right],
$$

where

$$
\alpha=\frac{2\hbar\lambda}{m}.
$$

This result comes from applying the free-particle propagator to the initial Gaussian:

$$
\psi(x,t)=\int_{-\infty}^{\infty}K(x,t;x',0)\psi_0(x')\,dx',
$$

with

$$
K(x,t;x',0)
=
\sqrt{\frac{m}{2\pi i\hbar t}}
\exp\left[
\frac{im(x-x')^2}{2\hbar t}
\right].
$$

The propagator integral is a Gaussian integral. After completing the square and simplifying, the final result is the spreading Gaussian above.

---

## 2.1 Position-space density

We now calculate

$$
\rho(x,t)=|\psi(x,t)|^2.
$$

Write

$$
\psi(x,t)
=
A
\frac{1}{\sqrt{1+i\alpha t}}
\exp\left[
-\frac{\lambda x^2}{1+i\alpha t}
\right],
$$

where

$$
A=\left(\frac{2\lambda}{\pi}\right)^{1/4}.
$$

Then

$$
|\psi(x,t)|^2
=
|A|^2
\left|
\frac{1}{\sqrt{1+i\alpha t}}
\right|^2
\left|
\exp\left[
-\frac{\lambda x^2}{1+i\alpha t}
\right]
\right|^2.
$$

The first factor is

$$
|A|^2
=
\left(\frac{2\lambda}{\pi}\right)^{1/2}.
$$

For the second factor,

$$
\left|
\frac{1}{\sqrt{1+i\alpha t}}
\right|^2
=
\frac{1}{|1+i\alpha t|}.
$$

Since

$$
|1+i\alpha t|=\sqrt{1+\alpha^2t^2},
$$

we get

$$
\left|
\frac{1}{\sqrt{1+i\alpha t}}
\right|^2
=
\frac{1}{\sqrt{1+\alpha^2t^2}}.
$$

For the exponential factor, use

$$
|e^z|^2=e^{z+z^*}=e^{2\operatorname{Re}(z)}.
$$

Here,

$$
z=-\frac{\lambda x^2}{1+i\alpha t}.
$$

Rewrite the reciprocal:

$$
\frac{1}{1+i\alpha t}
=
\frac{1-i\alpha t}{1+\alpha^2t^2}.
$$

Therefore,

$$
z
=
-\lambda x^2\frac{1-i\alpha t}{1+\alpha^2t^2}.
$$

The real part is

$$
\operatorname{Re}(z)
=
-\frac{\lambda x^2}{1+\alpha^2t^2}.
$$

Hence,

$$
\left|
\exp\left[
-\frac{\lambda x^2}{1+i\alpha t}
\right]
\right|^2
=
\exp\left[
-\frac{2\lambda x^2}{1+\alpha^2t^2}
\right].
$$

Putting the factors together,

$$
\rho(x,t)
=
\left(\frac{2\lambda}{\pi}\right)^{1/2}
\frac{1}{\sqrt{1+\alpha^2t^2}}
\exp\left[
-\frac{2\lambda x^2}{1+\alpha^2t^2}
\right].
$$

So

$$
\boxed{
\rho(x,t)
=
\sqrt{\frac{2\lambda}{\pi(1+\alpha^2t^2)}}
\exp\left[
-\frac{2\lambda x^2}{1+\alpha^2t^2}
\right].
}
$$

This is still a Gaussian in \(x\), but its width increases with time.

---

## 2.2 Rewriting the density using \(\beta(t)\)

To make the entropy integral cleaner, define

$$
\beta(t)=\frac{2\lambda}{1+\alpha^2t^2}.
$$

Then the density becomes

$$
\rho(x,t)=\sqrt{\frac{\beta(t)}{\pi}}e^{-\beta(t)x^2}.
$$

This is not a new physical assumption. It is only a shorthand for the time-dependent Gaussian width.

---

## 2.3 Calculating the entropy directly

The entropy is

$$
S_x(t)
=
-\int_{-\infty}^{\infty}
\rho(x,t)\ln\rho(x,t)\,dx.
$$

Start with

$$
\rho(x,t)=\sqrt{\frac{\beta}{\pi}}e^{-\beta x^2}.
$$

The logarithm is

$$
\ln\rho(x,t)
=
\ln\left[
\sqrt{\frac{\beta}{\pi}}e^{-\beta x^2}
\right].
$$

Using logarithm rules,

$$
\ln\rho(x,t)
=
\ln\left(\sqrt{\frac{\beta}{\pi}}\right)
+
\ln(e^{-\beta x^2}).
$$

So

$$
\ln\rho(x,t)
=
\frac12\ln\left(\frac{\beta}{\pi}\right)
-
\beta x^2.
$$

Substitute this into the entropy:

$$
S_x(t)
=
-\int_{-\infty}^{\infty}
\rho(x,t)
\left[
\frac12\ln\left(\frac{\beta}{\pi}\right)
-
\beta x^2
\right]dx.
$$

Separate the two terms:

$$
S_x(t)
=
-\frac12\ln\left(\frac{\beta}{\pi}\right)
\int_{-\infty}^{\infty}\rho(x,t)\,dx
+
\beta
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx.
$$

Because the density is normalized,

$$
\int_{-\infty}^{\infty}\rho(x,t)\,dx=1.
$$

Therefore,

$$
S_x(t)
=
-\frac12\ln\left(\frac{\beta}{\pi}\right)
+
\beta
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx.
$$

Now compute the remaining integral:

$$
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx
=
\sqrt{\frac{\beta}{\pi}}
\int_{-\infty}^{\infty}x^2e^{-\beta x^2}\,dx.
$$

To evaluate the Gaussian integral, start from

$$
I(\beta)=\int_{-\infty}^{\infty}e^{-\beta x^2}\,dx.
$$

The standard result is

$$
I(\beta)=\sqrt{\frac{\pi}{\beta}}=\sqrt{\pi}\beta^{-1/2}.
$$

Differentiate with respect to \(\beta\):

$$
\frac{dI}{d\beta}
=
\frac{d}{d\beta}
\int_{-\infty}^{\infty}e^{-\beta x^2}\,dx.
$$

Move the derivative inside the integral:

$$
\frac{dI}{d\beta}
=
\int_{-\infty}^{\infty}
\frac{\partial}{\partial\beta}
e^{-\beta x^2}\,dx.
$$

Since

$$
\frac{\partial}{\partial\beta}e^{-\beta x^2}
=
-x^2e^{-\beta x^2},
$$

we get

$$
\frac{dI}{d\beta}
=
-\int_{-\infty}^{\infty}x^2e^{-\beta x^2}\,dx.
$$

Differentiate the right-hand side:

$$
\frac{d}{d\beta}\left(\sqrt{\pi}\beta^{-1/2}\right)
=
-\frac12\sqrt{\pi}\beta^{-3/2}.
$$

Therefore,

$$
-\int_{-\infty}^{\infty}x^2e^{-\beta x^2}\,dx
=
-\frac12\sqrt{\pi}\beta^{-3/2}.
$$

So

$$
\int_{-\infty}^{\infty}x^2e^{-\beta x^2}\,dx
=
\frac{\sqrt{\pi}}{2\beta^{3/2}}.
$$

Now substitute this result:

$$
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx
=
\sqrt{\frac{\beta}{\pi}}
\frac{\sqrt{\pi}}{2\beta^{3/2}}.
$$

Simplify:

$$
\sqrt{\frac{\beta}{\pi}}\sqrt{\pi}
=
\sqrt{\beta}.
$$

So

$$
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx
=
\frac{\sqrt{\beta}}{2\beta^{3/2}}.
$$

Since

$$
\beta^{3/2}=\beta\sqrt{\beta},
$$

we get

$$
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx
=
\frac{1}{2\beta}.
$$

Therefore,

$$
\beta
\int_{-\infty}^{\infty}x^2\rho(x,t)\,dx
=
\frac12.
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
\beta(t)=\frac{2\lambda}{1+\alpha^2t^2}.
$$

Then

$$
\frac{\pi}{\beta(t)}
=
\frac{\pi(1+\alpha^2t^2)}{2\lambda}.
$$

Therefore,

$$
S_x(t)
=
\frac12
\ln\left[
\frac{\pi(1+\alpha^2t^2)}{2\lambda}
\right]
+\frac12.
$$

This is the clean non-compressed result:

$$
\boxed{
S_x(t)
=
\frac12
\ln\left[
\frac{\pi(1+\alpha^2t^2)}{2\lambda}
\right]
+\frac12.
}
$$

If we want to combine the \(+\frac12\) into the logarithm, use

$$
\frac12=\frac12\ln e.
$$

Then

$$
S_x(t)
=
\frac12
\ln\left[
\frac{\pi e(1+\alpha^2t^2)}{2\lambda}
\right].
$$

So the final compact form is

$$
\boxed{
S_x(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
\left(1+\alpha^2t^2\right)
\right].
}
$$

Using

$$
\alpha=\frac{2\hbar\lambda}{m},
$$

this can also be written as

$$
\boxed{
S_x(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
\left(
1+\frac{4\hbar^2\lambda^2t^2}{m^2}
\right)
\right].
}
$$

At \(t=0\),

$$
\boxed{
S_x(0)=\frac12\ln\left(\frac{\pi e}{2\lambda}\right).
}
$$

A useful form is therefore

$$
\boxed{
S_x(t)=S_x(0)+\frac12\ln(1+\alpha^2t^2).
}
$$

This shows directly that the entropy increases because the free wave packet spreads in position space.

---

# 3. Free Gaussian wave packet in momentum space

Now I calculate the momentum-space entropy for the same free Gaussian.

The momentum-space wavefunction is defined using the Fourier transform

$$
\phi(p,t)=
\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}
e^{-ipx/\hbar}\psi(x,t)\,dx.
$$

At \(t=0\),

$$
\phi_0(p)=
\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}
e^{-ipx/\hbar}\psi_0(x)\,dx.
$$

Substitute

$$
\psi_0(x)=\left(\frac{2\lambda}{\pi}\right)^{1/4}e^{-\lambda x^2}.
$$

Then

$$
\phi_0(p)
=
\left(\frac{2\lambda}{\pi}\right)^{1/4}
\frac{1}{\sqrt{2\pi\hbar}}
\int_{-\infty}^{\infty}
\exp\left(
-\lambda x^2-\frac{ipx}{\hbar}
\right)dx.
$$

The key integral is

$$
I(p)=
\int_{-\infty}^{\infty}
\exp\left(
-\lambda x^2-\frac{ipx}{\hbar}
\right)dx.
$$

---

## 3.1 Evaluating the Fourier Gaussian integral

Start with the exponent:

$$
-\lambda x^2-\frac{ipx}{\hbar}.
$$

Factor out \(-\lambda\):

$$
-\lambda x^2-\frac{ipx}{\hbar}
=
-\lambda
\left[
x^2+\frac{ip}{\lambda\hbar}x
\right].
$$

Complete the square:

$$
x^2+\frac{ip}{\lambda\hbar}x
=
\left(
x+\frac{ip}{2\lambda\hbar}
\right)^2
-
\left(
\frac{ip}{2\lambda\hbar}
\right)^2.
$$

Now,

$$
\left(
\frac{ip}{2\lambda\hbar}
\right)^2
=
-\frac{p^2}{4\lambda^2\hbar^2}.
$$

Therefore,

$$
x^2+\frac{ip}{\lambda\hbar}x
=
\left(
x+\frac{ip}{2\lambda\hbar}
\right)^2
+
\frac{p^2}{4\lambda^2\hbar^2}.
$$

So

$$
-\lambda x^2-\frac{ipx}{\hbar}
=
-\lambda
\left(
x+\frac{ip}{2\lambda\hbar}
\right)^2
-
\frac{p^2}{4\lambda\hbar^2}.
$$

Thus,

$$
I(p)
=
e^{-p^2/(4\lambda\hbar^2)}
\int_{-\infty}^{\infty}
\exp\left[
-\lambda
\left(
x+\frac{ip}{2\lambda\hbar}
\right)^2
\right]dx.
$$

The remaining shifted Gaussian integral equals the ordinary Gaussian integral:

$$
\int_{-\infty}^{\infty}
\exp\left[
-\lambda
\left(
x+\frac{ip}{2\lambda\hbar}
\right)^2
\right]dx
=
\sqrt{\frac{\pi}{\lambda}}.
$$

Therefore,

$$
\boxed{
I(p)
=
\sqrt{\frac{\pi}{\lambda}}
\exp\left[
-\frac{p^2}{4\lambda\hbar^2}
\right].
}
$$

So

$$
\phi_0(p)
=
\left(\frac{2\lambda}{\pi}\right)^{1/4}
\frac{1}{\sqrt{2\pi\hbar}}
\sqrt{\frac{\pi}{\lambda}}
\exp\left[
-\frac{p^2}{4\lambda\hbar^2}
\right].
$$

---

## 3.2 Complex-analysis interpretation of the shifted Gaussian

The shifted Gaussian step can be justified using Cauchy's theorem.

Let

$$
a=\frac{p}{2\lambda\hbar}.
$$

Then

$$
x+\frac{ip}{2\lambda\hbar}=x+ia.
$$

The integral becomes an integral along the horizontal line \(\operatorname{Im}(z)=a\):

$$
\int_{-\infty}^{\infty}e^{-\lambda(x+ia)^2}\,dx
=
\int_{-\infty+ia}^{\infty+ia}e^{-\lambda z^2}\,dz.
$$

The function

$$
f(z)=e^{-\lambda z^2}
$$

is entire. It has no poles. Therefore, the residue theorem is not the useful tool here because there are no residues to compute.

Instead, Cauchy's theorem says the contour integral around a rectangle with horizontal sides on \(\operatorname{Im}(z)=0\) and \(\operatorname{Im}(z)=a\) is zero. In the limit where the rectangle width goes to infinity, the vertical side integrals vanish, so

$$
\int_{-\infty+ia}^{\infty+ia}e^{-\lambda z^2}\,dz
=
\int_{-\infty}^{\infty}e^{-\lambda x^2}\,dx.
$$

Thus,

$$
\int_{-\infty}^{\infty}e^{-\lambda(x+ia)^2}\,dx
=
\sqrt{\frac{\pi}{\lambda}}.
$$

So the complex-analysis statement is:

$$
\boxed{
\text{complete the square, then use Cauchy's theorem to shift the contour.}
}
$$

---

## 3.3 Time evolution in momentum space

For a free particle,

$$
\hat H=\frac{\hat p^2}{2m}.
$$

A momentum eigenstate has energy

$$
E_p=\frac{p^2}{2m}.
$$

Therefore, the momentum-space wavefunction only gains a phase in time:

$$
\phi(p,t)
=
\phi_0(p)
\exp\left(-\frac{iE_pt}{\hbar}\right).
$$

Since

$$
E_p=\frac{p^2}{2m},
$$

we get

$$
\phi(p,t)
=
\phi_0(p)
\exp\left(
-\frac{ip^2t}{2m\hbar}
\right).
$$

The phase has magnitude one:

$$
\left|
\exp\left(
-\frac{ip^2t}{2m\hbar}
\right)
\right|^2=1.
$$

So the momentum density is time-independent:

$$
\gamma(p,t)=|\phi(p,t)|^2=|\phi_0(p)|^2.
$$

---

## 3.4 Momentum-space probability density

From

$$
\phi_0(p)
=
\left(\frac{2\lambda}{\pi}\right)^{1/4}
\frac{1}{\sqrt{2\pi\hbar}}
\sqrt{\frac{\pi}{\lambda}}
\exp\left[
-\frac{p^2}{4\lambda\hbar^2}
\right],
$$

we get

$$
\gamma(p,t)=|\phi_0(p)|^2.
$$

Square the prefactor:

$$
\left[
\left(\frac{2\lambda}{\pi}\right)^{1/4}
\right]^2
=
\left(\frac{2\lambda}{\pi}\right)^{1/2},
$$

$$
\left[
\frac{1}{\sqrt{2\pi\hbar}}
\right]^2
=
\frac{1}{2\pi\hbar},
$$

and

$$
\left[
\sqrt{\frac{\pi}{\lambda}}
\right]^2
=
\frac{\pi}{\lambda}.
$$

The exponential becomes

$$
\left[
\exp\left(
-\frac{p^2}{4\lambda\hbar^2}
\right)
\right]^2
=
\exp\left(
-\frac{p^2}{2\lambda\hbar^2}
\right).
$$

Therefore,

$$
\gamma(p,t)
=
\left(\frac{2\lambda}{\pi}\right)^{1/2}
\frac{1}{2\pi\hbar}
\frac{\pi}{\lambda}
\exp\left(
-\frac{p^2}{2\lambda\hbar^2}
\right).
$$

Simplify the prefactor:

$$
\frac{1}{2\pi\hbar}\frac{\pi}{\lambda}
=
\frac{1}{2\lambda\hbar}.
$$

So

$$
\gamma(p,t)
=
\frac{1}{2\lambda\hbar}
\sqrt{\frac{2\lambda}{\pi}}
\exp\left(
-\frac{p^2}{2\lambda\hbar^2}
\right).
$$

This is

$$
\boxed{
\gamma(p,t)
=
\frac{1}{\hbar\sqrt{2\pi\lambda}}
\exp\left[
-\frac{p^2}{2\lambda\hbar^2}
\right].
}
$$

This density does not depend on time.

---

## 3.5 Calculating the momentum-space entropy

The momentum-space entropy is

$$
S_p(t)
=
-\int_{-\infty}^{\infty}
\gamma(p,t)\ln\gamma(p,t)\,dp.
$$

Write the momentum density as

$$
\gamma(p,t)=\sqrt{\frac{\eta}{\pi}}e^{-\eta p^2},
$$

where

$$
\eta=\frac{1}{2\lambda\hbar^2}.
$$

This works because

$$
\sqrt{\frac{\eta}{\pi}}
=
\sqrt{\frac{1}{2\lambda\hbar^2\pi}}
=
\frac{1}{\hbar\sqrt{2\pi\lambda}}.
$$

Now compute the logarithm:

$$
\ln\gamma(p,t)
=
\ln\left[
\sqrt{\frac{\eta}{\pi}}e^{-\eta p^2}
\right].
$$

So

$$
\ln\gamma(p,t)
=
\frac12\ln\left(\frac{\eta}{\pi}\right)-\eta p^2.
$$

Substitute into the entropy:

$$
S_p(t)
=
-\int_{-\infty}^{\infty}
\gamma(p,t)
\left[
\frac12\ln\left(\frac{\eta}{\pi}\right)-\eta p^2
\right]dp.
$$

Separate the two terms:

$$
S_p(t)
=
-\frac12\ln\left(\frac{\eta}{\pi}\right)
\int_{-\infty}^{\infty}\gamma(p,t)\,dp
+
\eta
\int_{-\infty}^{\infty}p^2\gamma(p,t)\,dp.
$$

Since the density is normalized,

$$
\int_{-\infty}^{\infty}\gamma(p,t)\,dp=1.
$$

The first term is therefore

$$
-\frac12\ln\left(\frac{\eta}{\pi}\right).
$$

The remaining integral is

$$
\int_{-\infty}^{\infty}p^2\gamma(p,t)\,dp
=
\sqrt{\frac{\eta}{\pi}}
\int_{-\infty}^{\infty}p^2e^{-\eta p^2}\,dp.
$$

Using the same Gaussian integral logic,

$$
\int_{-\infty}^{\infty}p^2e^{-\eta p^2}\,dp
=
\frac{\sqrt{\pi}}{2\eta^{3/2}}.
$$

Therefore,

$$
\int_{-\infty}^{\infty}p^2\gamma(p,t)\,dp
=
\sqrt{\frac{\eta}{\pi}}
\frac{\sqrt{\pi}}{2\eta^{3/2}}.
$$

This simplifies to

$$
\int_{-\infty}^{\infty}p^2\gamma(p,t)\,dp
=
\frac{1}{2\eta}.
$$

Therefore,

$$
\eta
\int_{-\infty}^{\infty}p^2\gamma(p,t)\,dp
=
\frac12.
$$

So

$$
S_p(t)
=
-\frac12\ln\left(\frac{\eta}{\pi}\right)+\frac12.
$$

Equivalently,

$$
S_p(t)
=
\frac12\ln\left(\frac{\pi}{\eta}\right)+\frac12.
$$

Now substitute

$$
\eta=\frac{1}{2\lambda\hbar^2}.
$$

Then

$$
\frac{\pi}{\eta}
=
2\pi\lambda\hbar^2.
$$

Therefore,

$$
S_p(t)
=
\frac12\ln(2\pi\lambda\hbar^2)+\frac12.
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
\frac12\ln(2\pi e\lambda\hbar^2).
}
$$

Since \(\gamma(p,t)\) is time-independent,

$$
\boxed{
S_p(t)=S_p(0).
}
$$

---

# 4. Total position plus momentum entropy

The total position plus momentum entropy is

$$
S_{\text{tot}}(t)=S_x(t)+S_p(t).
$$

Using

$$
S_x(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
(1+\alpha^2t^2)
\right],
$$

and

$$
S_p(t)
=
\frac12\ln(2\pi e\lambda\hbar^2),
$$

we get

$$
S_{\text{tot}}(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
(1+\alpha^2t^2)
\right]
+
\frac12
\ln(2\pi e\lambda\hbar^2).
$$

Combine the logarithms:

$$
S_{\text{tot}}(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
(1+\alpha^2t^2)
(2\pi e\lambda\hbar^2)
\right].
$$

Simplify the constants:

$$
\frac{1}{2\lambda}(2\lambda)=1.
$$

So

$$
S_{\text{tot}}(t)
=
\frac12
\ln\left[
\pi^2e^2\hbar^2
(1+\alpha^2t^2)
\right].
$$

Therefore,

$$
\boxed{
S_{\text{tot}}(t)
=
\ln(\pi e\hbar)
+
\frac12\ln(1+\alpha^2t^2).
}
$$

At \(t=0\),

$$
\boxed{
S_{\text{tot}}(0)=\ln(\pi e\hbar).
}
$$

This is the minimum value for the initial Gaussian. As time increases, \(S_p\) stays constant but \(S_x(t)\) increases, so \(S_{\text{tot}}(t)\) increases.

---

# 5. Shape of the entropy curves

A point that confused me at first is whether the entropy curve should look Gaussian. The answer is no.

The probability density remains Gaussian in position:

$$
\rho(x,t)
=
\sqrt{\frac{2\lambda}{\pi(1+\alpha^2t^2)}}
\exp\left[
-\frac{2\lambda x^2}{1+\alpha^2t^2}
\right].
$$

So as a function of \(x\), the density is Gaussian.

But the entropy is a single number as a function of time:

$$
S_x(t)
=
S_x(0)+\frac12\ln(1+\alpha^2t^2).
$$

This is not Gaussian in time. It is a logarithmic-type growth curve.

For small \(t\), use

$$
\ln(1+\alpha^2t^2)\approx \alpha^2t^2.
$$

So near \(t=0\),

$$
S_x(t)\approx S_x(0)+\frac12\alpha^2t^2.
$$

That means it starts almost flat and curves upward.

For large \(t\),

$$
1+\alpha^2t^2\approx \alpha^2t^2.
$$

Therefore,

$$
S_x(t)
\approx
S_x(0)+\frac12\ln(\alpha^2t^2).
$$

Since

$$
\frac12\ln(\alpha^2t^2)=\ln(\alpha t),
$$

we get

$$
\boxed{
S_x(t)\approx S_x(0)+\ln(\alpha t)
\qquad \text{for large }t.
}
$$

So at large time, if time doubles,

$$
S_x(2t)-S_x(t)\approx \ln 2.
$$

If time triples,

$$
S_x(3t)-S_x(t)\approx \ln 3.
$$

The entropy keeps increasing, but it increases more slowly at late times.

---

# 6. Python visualization code

The following plots use the parameters

$$
\hbar=1,\qquad m=1,\qquad \lambda=1.
$$

Then

$$
\alpha=\frac{2\hbar\lambda}{m}=2.
$$

These are natural units chosen only for visualization. Different parameter values will change the scale but not the main qualitative behavior.

## 6.1 Entropy curves

![Entropy curves for the spreading Gaussian wave packet](figures/gwp_entropy_plot.png)

This plot shows:

- \(S_x(t)\) increases because the free wave packet spreads in position space.
- \(S_p(t)\) stays constant because the momentum-space density does not change with time.
- \(S_{\rm tot}(t)\) increases because it is \(S_x(t)\) shifted upward by the constant \(S_p\).

## 6.2 Large-time behavior

![Large-time entropy behavior](figures/gwp_entropy_large_time.png)

This plot confirms the large-time approximation

$$
S_x(t)\approx S_x(0)+\ln(\alpha t).
$$

The entropy does not grow like a Gaussian. It grows logarithmically at large time.

---

## 6.3 Full Python script

```python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# Entropy of a free spreading Gaussian wave packet
#
# Initial state:
#   psi_0(x) = (2 lambda / pi)^(1/4) exp(-lambda x^2)
#
# Free-particle spreading parameter:
#   alpha = 2 hbar lambda / m
#
# Position-space entropy:
#   Sx(t) = 1/2 ln[ (pi e / (2 lambda)) (1 + alpha^2 t^2) ]
#
# Momentum-space entropy:
#   Sp(t) = 1/2 ln[ 2 pi e lambda hbar^2 ]
#
# Total entropy:
#   Stot(t) = Sx(t) + Sp(t)
# ============================================================

output_dir = Path("figures")
output_dir.mkdir(exist_ok=True)

# Parameters.
# For visualization, I use natural units: hbar = 1, m = 1.
hbar = 1.0
m = 1.0
lam = 1.0
alpha = 2.0 * hbar * lam / m

# ------------------------------------------------------------
# Plot 1: moderate time range
# ------------------------------------------------------------
t = np.linspace(0, 5, 500)

Sx = 0.5 * np.log((np.pi * np.e / (2.0 * lam)) * (1.0 + alpha**2 * t**2))
Sp = 0.5 * np.log(2.0 * np.pi * np.e * lam * hbar**2) * np.ones_like(t)
Stot = Sx + Sp

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    Sx,
    linewidth=2.5,
    label=r"$S_x(t)=\frac{1}{2}\ln\!\left[\frac{\pi e}{2\lambda}(1+\alpha^2t^2)\right]$",
)

plt.plot(
    t,
    Sp,
    linewidth=2.5,
    linestyle="--",
    label=r"$S_p(t)=\frac{1}{2}\ln\!\left(2\pi e\lambda\hbar^2\right)$",
)

plt.plot(
    t,
    Stot,
    linewidth=2.5,
    linestyle=":",
    label=r"$S_{\rm tot}(t)=S_x(t)+S_p(t)$",
)

plt.xlabel(r"Time $t$", fontsize=13)
plt.ylabel(r"Differential Shannon entropy", fontsize=13)
plt.title(
    rf"Entropy of a Spreading Free Gaussian Wave Packet "
    rf"$(\lambda={lam},\ \hbar={hbar},\ m={m},\ \alpha={alpha})$",
    fontsize=14,
)
plt.legend(fontsize=10, loc="best")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "gwp_entropy_plot.png", dpi=300, bbox_inches="tight")
plt.show()

# ------------------------------------------------------------
# Plot 2: large-time logarithmic behavior
# ------------------------------------------------------------
t = np.linspace(0, 50, 2000)

Sx0 = 0.5 * np.log(np.pi * np.e / (2.0 * lam))
Sx = Sx0 + 0.5 * np.log(1.0 + alpha**2 * t**2)
Sp = 0.5 * np.log(2.0 * np.pi * np.e * lam * hbar**2) * np.ones_like(t)
Stot = Sx + Sp

# Large-time approximation:
#   Sx(t) ~ Sx(0) + ln(alpha t)
# Avoid t=0 because ln(0) is undefined.
t_asym = t[t > 1 / alpha]
Sx_asym = Sx0 + np.log(alpha * t_asym)

plt.figure(figsize=(10, 6))

plt.plot(
    t,
    Sx,
    linewidth=2.5,
    label=r"Exact $S_x(t)=S_x(0)+\frac{1}{2}\ln(1+\alpha^2t^2)$",
)

plt.plot(
    t,
    Sp,
    linewidth=2.5,
    linestyle="--",
    label=r"$S_p(t)=\mathrm{constant}$",
)

plt.plot(
    t,
    Stot,
    linewidth=2.5,
    linestyle=":",
    label=r"$S_{\rm tot}(t)=S_x(t)+S_p$",
)

plt.plot(
    t_asym,
    Sx_asym,
    linewidth=2,
    linestyle="-.",
    label=r"Large-time $S_x(t)\approx S_x(0)+\ln(\alpha t)$",
)

plt.xlabel(r"Time $t$", fontsize=13)
plt.ylabel(r"Differential Shannon entropy", fontsize=13)
plt.title(r"Large-Time Entropy Shape for a Free Spreading Gaussian Wave Packet", fontsize=14)
plt.legend(fontsize=10, loc="best")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(output_dir / "gwp_entropy_large_time.png", dpi=300, bbox_inches="tight")
plt.show()
```

---

# 7. How to run this project

Recommended file structure:

```text
gwp_entropy_project/
├── README.md
├── gwp_entropy_plots.py
└── figures/
    ├── gwp_entropy_plot.png
    └── gwp_entropy_large_time.png
```

To run the script from the terminal:

```bash
python gwp_entropy_plots.py
```

The script will create the `figures/` folder if it does not exist and save the plots automatically.

Required Python packages:

```bash
pip install numpy matplotlib
```

---

# Final results summary

For the stationary Gaussian wave packet,

$$
\boxed{
S_x=\frac12\ln(\pi e\sigma^2).
}
$$

For the free spreading Gaussian wave packet in position space,

$$
\boxed{
S_x(t)
=
\frac12
\ln\left[
\frac{\pi e}{2\lambda}
\left(
1+\frac{4\hbar^2\lambda^2t^2}{m^2}
\right)
\right].
}
$$

For the same free Gaussian wave packet in momentum space,

$$
\boxed{
S_p(t)=\frac12\ln(2\pi e\lambda\hbar^2).
}
$$

For the total position plus momentum entropy,

$$
\boxed{
S_{\text{tot}}(t)
=
\ln(\pi e\hbar)
+
\frac12\ln(1+\alpha^2t^2),
\qquad
\alpha=\frac{2\hbar\lambda}{m}.
}
$$

The final interpretation is:

$$
\boxed{
\rho(x,t)\text{ remains Gaussian in }x,\quad
S_x(t)\text{ grows logarithmically in time at large }t,\quad
S_p(t)\text{ remains constant.}
}
```
