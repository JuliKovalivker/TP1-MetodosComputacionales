import numpy as np
import matplotlib.pyplot as plt

P0 = np.array([-5, 0])
P1 = np.array([2, -2])
P2 = np.array([9, 6])
P3 = np.array([16, 3])

### b) ###
def h(puntos, t):
    P0 = puntos[0]
    P1 = puntos[1]
    P2 = puntos[2]
    P3 = puntos[3]
    b0 = (1 - t)**3
    b1 = 3 * (1 - t)**2 * t
    b2 = 3 * (1 - t) * t**2
    b3 = t**3
    return b0*P0 + b1*P1 + b2*P2 + b3*P3


### c) ###
puntos = [P0, P1, P2, P3]
ts_curva = np.linspace(0, 1, 100)
curva = np.array([h(puntos, t) for t in ts_curva])  

fig, ax = plt.subplots(figsize=(7, 5))
pts = np.array([P0, P1, P2, P3])

ax.plot(pts[:,0], pts[:,1], 'o--', color='gray', alpha=0.5, linewidth=1.5, label='Polígono de control')
ax.plot(curva[:,0], curva[:,1], color='#3B8BD4', linewidth=2.5, label='Curva de Bézier')

nombres = ['P₀', 'P₁', 'P₂', 'P₃']
offsets = [(-20, -18), (6, 6), (6, 6), (6, -18)]
for p, nombre, off in zip(pts, nombres, offsets):
    ax.scatter(*p, color='#3B8BD4', s=80, zorder=5)
    ax.annotate(nombre, p, textcoords="offset points", xytext=off, fontsize=10)

ax.set_title('Curva de Bézier cúbica', fontsize=13)
ax.legend(fontsize=10)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ej12_curva', dpi=150, bbox_inches='tight')

b0 = (1 - ts_curva)**3
b1 = 3 * (1 - ts_curva)**2 * ts_curva
b2 = 3 * (1 - ts_curva) * ts_curva**2
b3 = ts_curva**3

fig2, ax2 = plt.subplots(figsize=(7, 5))

ax2.plot(ts_curva, b0, label='$b_0(t) = (1-t)^3$', linewidth=2)
ax2.plot(ts_curva, b1, label='$b_1(t) = 3(1-t)^2t$', linewidth=2)
ax2.plot(ts_curva, b2, label='$b_2(t) = 3(1-t)t^2$', linewidth=2)
ax2.plot(ts_curva, b3, label='$b_3(t) = t^3$', linewidth=2)

ax2.set_title('Coeficientes de Bernstein', fontsize=13)
ax2.set_xlabel('t')
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ej12', dpi=150, bbox_inches='tight')