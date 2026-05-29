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
