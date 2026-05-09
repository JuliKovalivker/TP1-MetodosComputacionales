import numpy as np
import matplotlib.pyplot as plt

P0 = np.array([0, 0])
P1 = np.array([2, 4])
P2 = np.array([4, 0])

### a) ###
def bezier_explicita(P0, P1, P2, t):
    return (1-t)**2 * P0 + 2*(1-t)*t * P1 + t**2 * P2


### b) ###
ts_curva = np.linspace(0, 1, 100)
curva = np.array([bezier_explicita(P0, P1, P2, t) for t in ts_curva])


### c) ###
fig, ax = plt.subplots(figsize=(7, 5))
puntos = np.array([P0, P1, P2])

ax.plot(puntos[:,0], puntos[:,1], 'o--', color='gray', alpha=0.5, linewidth=1.5, label='Polígono de control')
ax.plot(curva[:,0], curva[:,1], color='#3B8BD4', linewidth=2.5, label='Curva de Bézier')

nombres = ['P₀ (0,0)', 'P₁ (2,4)', 'P₂ (4,0)']
colores = ['#3B8BD4', '#E85D24', '#3B8BD4']
offsets = [(-30, -18), (6, 6), (6, -18)]
for p, nombre, color, off in zip(puntos, nombres, colores, offsets):
    ax.scatter(*p, color=color, s=80, zorder=5)
    ax.annotate(nombre, p, textcoords="offset points", xytext=off, fontsize=10)

ax.set_title('Curva de Bézier cuadrática', fontsize=13)
ax.legend(fontsize=10)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('ej11', dpi=150, bbox_inches='tight')


### d) ###
def bezier_iterada(P0, P1, P2, t):
    Q0 = (1-t)*P0 + t*P1
    Q1 = (1-t)*P1 + t*P2
    B  = (1-t)*Q0 + t*Q1
    return B

ts_comp = np.linspace(0, 1, 10)
print("\n")
print("Comparación de ambos métodos para 10 valores de t:")
for t in ts_comp:
    exp = bezier_explicita(P0, P1, P2, t)
    ite = bezier_iterada(P0, P1, P2, t)
    dif = np.linalg.norm(exp - ite)
    print(f"  t = {t:.2f}  ->  Explícita: ({exp[0]:.5f}, {exp[1]:.5f})   Iterada: ({ite[0]:.5f}, {ite[1]:.5f})   Diferencia: {dif:.2e}")
print("\n")