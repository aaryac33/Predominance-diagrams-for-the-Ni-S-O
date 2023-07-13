import numpy as np
import matplotlib.pyplot as plt


# Topic : Predominance diagram of Zn-S-O

R = 8.314  # Universal Gas Constant
T = float(input("Enter the value of Temperature"))  # Temperature in the reaction


# Pressure of O2 = antilog(p)
# Pressure of SO2 = antilog(q)


def line1(p):
    G_naught_1 = -49011.15  # - R x T x ln(K)
    k = np.exp(G_naught_1 / (R * T))
    q = 1.5 * p + np.log(k) + np.log(np.exp(22))
    return q


def line2(p):
    G_naught_2 = -3267.402  # - R x T x ln(K)
    k = np.exp(G_naught_2 / (R * T))  # Equilibrium Constant
    q = -0.5 * p - np.log(k)
    return q


x1 = np.linspace(-22, -7)
x2 = np.linspace(-7, 0)
x = [-7]
y = [(3.95, 10)]

plt.plot(x1, line1(x1), label='ZnO-ZnS line')
plt.plot(x2, line2(x2), label='ZnS-ZnSO4 line')
plt.text(-10, -8, 'ZnS')
plt.text(-6, 4, 'ZnSO4')
plt.text(-17.5, 0, 'ZnO')
plt.plot((x, x), ([i for (i, j) in y], [j for (i, j) in y]), color='blue', label='ZnS-ZnSO4 line')
plt.xlim(xmin=-20, xmax=0)
plt.ylim(ymin=-12, ymax=5)

plt.legend((['ZnO-ZnS line', 'ZnS-ZnSO4 line', 'ZnS-ZnSO4 line']))


def get_sub(l):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = l.maketrans(''.join(normal), ''.join(sub_s))
    return l.translate(res)


plt.xlabel('log(P O{})'.format(get_sub('2')))
plt.ylabel('log(P SO{})'.format(get_sub('2')))
plt.show()
