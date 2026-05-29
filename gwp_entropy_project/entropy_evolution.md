# Entropy evolution from the continuity equation

At this stage, We wanted to step back from only calculating entropy after already knowing the full wavefunction. For the free Gaussian wave packet and the translated harmonic oscillator ground state, we had explicit densities, so the entropy calculation was direct. But if we want to move toward other potentials, especially something like the Morse potential, then it is useful to ask whether there is a more general way to understand how entropy changes in time.

The starting point is the differential Shannon entropy of a quantum probability density:

```math
S(t)
=
-\int \rho(\mathbf r,t)\ln\rho(\mathbf r,t)\,d^dr.
```

Here $d$ is the number of spatial dimensions. For example, $d=1$ for a 1D problem and $d=3$ for a 3D problem. The probability density is

```math
\rho(\mathbf r,t)=|\psi(\mathbf r,t)|^2.
```

I am using $\mathbf r$ here so the same expression works in one, two, or three dimensions.

---

## 1. Taking the time derivative of the entropy

I start by differentiating the entropy with respect to time:

```math
\frac{dS}{dt}
=
-\frac{d}{dt}
\int \rho(\mathbf r,t)\ln\rho(\mathbf r,t)\,d^dr.
```

Assuming I can move the time derivative inside the integral,

```math
\frac{dS}{dt}
=
-\int
\frac{\partial}{\partial t}
\left[
\rho(\mathbf r,t)\ln\rho(\mathbf r,t)
\right]
d^dr.
```

Now I use the product rule. Since

```math
\frac{\partial}{\partial t}
\left[
\rho\ln\rho
\right]
=
\frac{\partial\rho}{\partial t}\ln\rho
+
\rho\frac{\partial}{\partial t}(\ln\rho),
```

and

```math
\frac{\partial}{\partial t}(\ln\rho)
=
\frac{1}{\rho}\frac{\partial\rho}{\partial t},
```

we get

```math
\frac{\partial}{\partial t}
\left[
\rho\ln\rho
\right]
=
\frac{\partial\rho}{\partial t}\ln\rho
+
\frac{\partial\rho}{\partial t}.
```

Therefore,

```math
\frac{dS}{dt}
=
-\int
\frac{\partial\rho}{\partial t}\ln\rho\,d^dr
-
\int
\frac{\partial\rho}{\partial t}\,d^dr.
```

The second term is zero because the total probability stays normalized:

```math
\int \rho(\mathbf r,t)\,d^dr=1.
```

So

```math
\frac{d}{dt}
\int \rho(\mathbf r,t)\,d^dr
=
\int \frac{\partial\rho}{\partial t}\,d^dr
=
0.
```

This leaves

```math
\boxed{
\frac{dS}{dt}
=
-\int
\frac{\partial\rho}{\partial t}\ln\rho\,d^dr.
}
```

This is already a general expression, but it still contains $\partial\rho/\partial t$, so it is not yet very practical.

---

## 2. Bringing in the continuity equation

This is where the connection to the continuity equation comes in. I remember the continuity equation from electrodynamics, where charge conservation is written as

```math
\frac{\partial \rho}{\partial t}
+
\nabla\cdot\mathbf J
=
0.
```

In quantum mechanics, a very similar equation holds for probability density:

```math
\frac{\partial \rho}{\partial t}
+
\nabla\cdot\mathbf J
=
0.
```

Here $\rho$ is the probability density and $\mathbf J$ is the probability current. For the Schrödinger equation with a real potential,

```math
\mathbf J
=
\frac{\hbar}{2mi}
\left(
\psi^*\nabla\psi
-
\psi\nabla\psi^*
\right).
```

Equivalently,

```math
\mathbf J
=
\frac{\hbar}{m}
\operatorname{Im}
\left(
\psi^*\nabla\psi
\right).
```

The continuity equation says that probability is not being created or destroyed. It is only flowing from one region to another.

From the continuity equation,

```math
\frac{\partial\rho}{\partial t}
=
-\nabla\cdot\mathbf J.
```

Substituting this into the entropy derivative gives

```math
\frac{dS}{dt}
=
-\int
\left(
-\nabla\cdot\mathbf J
\right)
\ln\rho\,d^dr.
```

So

```math
\frac{dS}{dt}
=
\int
(\nabla\cdot\mathbf J)\ln\rho\,d^dr.
```

Now integrate by parts. If the wavefunction is localized enough that the boundary term vanishes at infinity, then

```math
\int
(\nabla\cdot\mathbf J)\ln\rho\,d^dr
=
-\int
\mathbf J\cdot\nabla\ln\rho\,d^dr.
```

Therefore,

```math
\boxed{
\frac{dS}{dt}
=
-\int
\mathbf J\cdot\nabla\ln\rho\,d^dr.
}
```

This is a nicer expression because it connects entropy change to probability current.

---

## 3. Writing it using a probability-flow velocity

If I write the probability current as

```math
\mathbf J=\rho\mathbf v,
```

then $\mathbf v$ acts like a probability-flow velocity field. Substituting this into the previous expression,

```math
\frac{dS}{dt}
=
-\int
\rho\mathbf v\cdot\nabla\ln\rho\,d^dr.
```

Using

```math
\rho\nabla\ln\rho=\nabla\rho,
```

this becomes

```math
\frac{dS}{dt}
=
-\int
\mathbf v\cdot\nabla\rho\,d^dr.
```

Integrating by parts again, and assuming the boundary term vanishes,

```math
\frac{dS}{dt}
=
\int
\rho(\nabla\cdot\mathbf v)\,d^dr.
```

So the entropy rate can be written as

```math
\boxed{
\frac{dS}{dt}
=
\left\langle
\nabla\cdot\mathbf v
\right\rangle.
}
```

This form helped me understand the meaning better. If the probability flow is expanding on average, the entropy increases. If the flow is compressing on average, the entropy decreases. If the packet only translates without changing shape, then the entropy does not have to change.

---

## 4. What this says about the examples already studied

For the free Gaussian wave packet, the packet spreads. Its position-space width increases with time, so the entropy increases. In that case,

```math
\frac{dS_x}{dt}>0
```

for $t>0$.

For the translated harmonic oscillator ground state, the center moves, but the width stays fixed. So the probability cloud is moving back and forth, but it is not expanding. That is why

```math
\frac{dS_x}{dt}=0.
```

This helped me separate two ideas that I was initially mixing together:

```math
\text{time-dependent state}
\neq
\text{changing entropy}.
```

The translated harmonic oscillator state is time-dependent, but its entropy is constant because its width is constant.

---

## 5. Can this give a general expression for $S(t)$?

This is the part where I think we have to be careful.

The expression

```math
\frac{dS}{dt}
=
-\int
\mathbf J\cdot\nabla\ln\rho\,d^dr
```

is general and useful conceptually. But it is not automatically a closed formula for $S(t)$, because $\rho$ and $\mathbf J$ still depend on the wavefunction $\psi(\mathbf r,t)$. To know them, we usually still need to solve the time-dependent Schrödinger equation.

So I would say this gives a general evolution equation for entropy, but not usually a simple closed-form solution.

It becomes more useful in special cases.



---

## 6. Why this matters for other potentials

For free motion and harmonic oscillator motion, the Hamiltonian is quadratic. In these cases, Gaussian wave packets often remain Gaussian or at least stay analytically manageable. That is why we can get clean entropy formulas.

For a more general potential, such as a Morse potential, I should not assume the wave packet will remain Gaussian. The packet may stretch, skew, reflect, or develop non-Gaussian structure. In that case, the covariance alone will not contain all the information needed for the entropy.

So for a general potential, the formal expression

```math
\frac{dS}{dt}
=
-\int
\mathbf J\cdot\nabla\ln\rho\,d^dr
```

is still true, but the practical route is probably numerical:

1. solve the time-dependent Schrödinger equation for $\psi(x,t)$,
2. compute $\rho(x,t)=|\psi(x,t)|^2$,
3. compute the entropy from

```math
S(t)
=
-\int \rho(x,t)\ln\rho(x,t)\,dx,
```

4. compare the behavior with the current-based expression or moment-based quantities.

---

## 7. What I take from this

The continuity-equation approach gives a useful bridge between the entropy calculation and the dynamics of the wavefunction.

The key result is

```math
\boxed{
\frac{dS}{dt}
=
-\int
\mathbf J\cdot\nabla\ln\rho\,d^dr
=
\int
\rho(\nabla\cdot\mathbf v)\,d^dr.
}
```

This tells me that entropy change is connected to how the probability flow expands or contracts.


This seems like the point where the project naturally moves from analytic examples into numerical methods.