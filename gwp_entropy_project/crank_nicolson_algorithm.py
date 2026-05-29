import numpy as np
from scipy.sparse import diags, identity
from scipy.sparse.linalg import splu
import matplotlib.pyplot as plt


# Constants
hbar = 1.0
m = 1.0

# Grid
N = 1000
x_min = -50
x_max = 50
x = np.linspace(x_min, x_max, N)
dx = x[1] - x[0]

# Time step
dt = 0.01

# Potential
V = np.zeros(N)

# Hamiltonian coefficients
main_diag = hbar**2 / (m * dx**2) + V
off_diag = -hbar**2 / (2 * m * dx**2) * np.ones(N - 1)

H = diags(
    [off_diag, main_diag, off_diag],
    offsets=[-1, 0, 1],
    format="csc"
)

I = identity(N, format="csc")

A = I + 1j * dt / (2 * hbar) * H
B = I - 1j * dt / (2 * hbar) * H

# Factorize A once for efficiency
A_lu = splu(A)

# Initial Gaussian wavepacket
x0 = -10
sigma = 2
k0 = 2

psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)

# Normalize
norm = np.sqrt(np.sum(np.abs(psi)**2) * dx)
psi = psi / norm

# Time evolution
num_steps = 1000

for n in range(num_steps):
    b = B @ psi
    psi = A_lu.solve(b)

    # Optional: renormalize tiny numerical drift
    psi = psi / np.sqrt(np.sum(np.abs(psi)**2) * dx)



plt.figure(figsize=(8, 5))
plt.plot(x, np.abs(psi)**2)
plt.xlabel("x")
plt.ylabel(r"$|\psi(x,t)|^2$")
plt.title("Final probability density after Crank-Nicolson evolution")
plt.grid(True)
plt.show()