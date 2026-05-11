import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon

A = (0, 0)
D = (10, 5)

def bezier_cubica(P0, P1, P2, P3, ts):
    return np.array([
        (1-t)**3 * P0 + 3*(1-t)**2*t * P1 + 3*(1-t)*t**2 * P2 + t**3 * P3
        for t in ts
    ])

def longitud_curva(curva):
    diffs = np.diff(curva, axis=0)
    return np.sum(np.sqrt((diffs**2).sum(axis=1)))

def configurar_mapa(ax):
    ax.set_aspect('equal')
    ax.set_xlim(-1, 12)
    ax.set_ylim(-2, 8)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.set_xlabel('Coordenada X', fontsize=11, fontweight='bold')
    ax.set_ylabel('Coordenada Y', fontsize=11, fontweight='bold')
    ax.set_xticks(np.arange(-1, 12, 1))
    ax.set_yticks(np.arange(-2, 8, 1))
    ax.plot(*A, 'go', markersize=12, label='A (0,0)', zorder=5)
    ax.plot(*D, 'ro', markersize=12, label='D (10,5)', zorder=5)
    ax.text(A[0]+0.1, A[1]-0.3, 'A (0,0)', fontsize=10, fontweight='bold', color='green')
    ax.text(D[0]+0.1, D[1]+0.2, 'D (10,5)', fontsize=10, fontweight='bold', color='red')

def configurar_obstaculos(ax):
    commons = dict(edgecolor='black', alpha=0.7, linewidth=2)
    pozo     = Polygon([(1.5,5.5),(2.2,5.8),(2.8,5.5),(2.5,4.8),(1.8,4.8)], facecolor='darkblue', **commons)
    roca     = Circle((4, 3), 1.2, facecolor='gray', **commons)
    casa     = Rectangle((6, 1), 2, 3, facecolor='brown', **commons)
    arbustos = Polygon([(8.5,6.2),(9.5,6.0),(9.2,5.3),(8.2,5.5)], facecolor='green',
                       edgecolor='darkgreen', alpha=0.5, linestyle='--', linewidth=2)
    for patch in [pozo, roca, casa, arbustos]:
        ax.add_patch(patch)
    text = dict(ha='center', va='center', fontsize=10, fontweight='bold')
    ax.text(4, 3, 'Roca', **text)
    ax.text(7, 2.5, 'Casa\nAbandonada', **text)
    ax.text(2.15, 5.3, 'Pozo', **text)
    ax.text(8.85, 5.75, 'Arbustos', **text)

def graficar_curva(ax, P1, P2, color, label):
    P0 = np.array(A)
    P3 = np.array(D)
    P1 = np.array(P1)
    P2 = np.array(P2)
    ts = np.linspace(0, 1, 100)
    curva = bezier_cubica(P0, P1, P2, P3, ts)
    longitud = longitud_curva(curva)
    ax.plot(curva[:,0], curva[:,1], color=color, linewidth=2, label=f'{label} (long≈{longitud:.2f})')
    pts = np.array([P0, P1, P2, P3])
    ax.plot(pts[:,0], pts[:,1], '--', color=color, alpha=0.3, linewidth=1)
    for p in [P1, P2]:
        ax.scatter(*p, color=color, s=50, zorder=5)

fig, ax = plt.subplots(figsize=(15, 9))
configurar_mapa(ax)
configurar_obstaculos(ax)




# mejor_longitud = np.inf
# mejor_P1 = None
# mejor_P2 = None
#
# def choca(curva):
#     # podriamos hacer una matrzi con todos los puntos de los obstaculos y vemos si la curva tiene esos puntos
#     pass
#
# for p1x in np.arange(0, 10, 1):        
#     for p1y in np.arange(4, 8, 1):     
#         for p2x in np.arange(0, 10, 1):
#             for p2y in np.arange(4, 8, 1): 
#                 P1 = np.array([p1x, p1y])
#                 P2 = np.array([p2x, p2y])
#                 curva = bezier_cubica(A, P1, P2, D, np.linspace(0, 1, 100))
#                 if not choca(curva):          # si no choca con nada ??????????????????????????
#                     long = longitud_curva(curva)
#                     if long < mejor_longitud:
#                         mejor_longitud = long
#                         mejor_P1 = P1.copy()
#                         mejor_P2 = P2.copy()



graficar_curva(ax, P1=(0, 0), P2=(10, 5), color='gray',   label='camino ideal')
# graficar_curva(ax, P1=(5.4, 6.451), P2=(1.0, 3.051), color='red',   label='camino dudoso')
graficar_curva(ax, P1=(5.4, 6.4), P2=(1.0, 3.0), color='blue',   label='camino cool')
# graficar_curva(ax, P1=mejor_P1, P2=mejor_P2, color='green',   label='camino cool')


ax.legend(loc='upper left', fontsize=9)
plt.tight_layout()
plt.show()