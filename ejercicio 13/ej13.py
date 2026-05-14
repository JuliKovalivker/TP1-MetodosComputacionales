import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

### a) ###
def bezier_cubica(P0, P1, P2, P3, ts):
    return np.array([
        (1-t)**3 * P0 + 3*(1-t)**2*t * P1 + 3*(1-t)*t**2 * P2 + t**3 * P3
        for t in ts
    ])

# Elegimos por default rango=10 para obtener resultados más prolijos
def generar_puntos(rango=10):
    return [np.random.uniform(-rango, rango, 2) for _ in range(4)]

puntos_B1 = generar_puntos()
puntos_B2 = generar_puntos()

P0, P1, P2, P3 = puntos_B1
Q0, Q1, Q2, Q3 = puntos_B2

ts = np.linspace(0, 1, 100)
B1 = bezier_cubica(P0, P1, P2, P3, ts)
B2 = bezier_cubica(Q0, Q1, Q2, Q3, ts)

print("\n")
print("Las curvas de Bézier alteatorias poseen los siguienten puntos de control:")
print(f"B₁(t) -> P₀ = {P0}   P₁ = {P1}   P₂ = {P2}   P₃ = {P3}")
print(f"B₂(t) -> Q₀ = {Q0}   Q₁ = {Q1}   Q₂ = {Q2}   Q₃ = {Q3}\n")

### c) ###
# T @ P0 = Q3  y  T @ P3 = Q0
# planteamos T @ [P0 | P3] = [Q3 | Q0]
# => T = [Q3 | Q0] @ inv([P0 | P3])
A = np.column_stack([P0, P3])
B = np.column_stack([Q3, Q0])
 
while abs(np.linalg.det(A)) <= 1e-10: # Por si hay algun error de redondeo
    print("P0 y P3 son LD, regenerando puntos...")
    puntos_B1 = generar_puntos()
    P0, P1, P2, P3 = puntos_B1
    A = np.column_stack([P0, P3])
 
T = B @ np.linalg.inv(A)

print("\n")
print("Es posible definir T -> ")
print(T)
print("\n")
print(f"T(P0) = {T @ P0}  debería ser Q3 = {Q3}")
print(f"T(P3) = {T @ P3}  debería ser Q0 = {Q0}")
print("\n")
 
# Aplicar T a los puntos de control de B1
TP0 = T @ P0
TP1 = T @ P1
TP2 = T @ P2
TP3 = T @ P3
TB1 = bezier_cubica(TP0, TP1, TP2, TP3, ts)

### d) ###
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

def graficar_bezier(ax, curva, puntos, titulo, color_curva, color_ctrl):
    pts = np.array(puntos)
    ax.plot(pts[:,0], pts[:,1], 'o--', color='gray', alpha=0.4, linewidth=1.2)
    ax.plot(curva[:,0], curva[:,1], color=color_curva, linewidth=2.5, label='Curva')
    nombres = ['P₀','P₁','P₂','P₃'] if 'B1' in titulo else ['Q₀','Q₁','Q₂','Q₃']
    for i, (p, nombre) in enumerate(zip(puntos, nombres)):
        c = color_curva if i in [0,3] else color_ctrl
        ax.scatter(*p, color=c, s=80, zorder=5)
        ax.annotate(nombre, p, textcoords="offset points", xytext=(6,6), fontsize=10)
    ax.set_title(titulo, fontsize=12)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

# Gráfico B1
graficar_bezier(axes[0], B1, [P0,P1,P2,P3], 'Curva B1(t)', '#3B8BD4', '#E85D24')

# Gráfico B2
graficar_bezier(axes[1], B2, [Q0,Q1,Q2,Q3], 'Curva B2(t)', '#2CA470', '#E85D24')

# Gráfico T(B1) y B2 juntas
ax = axes[2]
pts_TB1 = np.array([TP0, TP1, TP2, TP3])
pts_B2  = np.array([Q0, Q1, Q2, Q3])

ax.plot(pts_TB1[:,0], pts_TB1[:,1], 'o--', color='gray', alpha=0.3, linewidth=1)
ax.plot(pts_B2[:,0],  pts_B2[:,1],  'o--', color='gray', alpha=0.3, linewidth=1)

ax.plot(TB1[:,0], TB1[:,1], color='#3B8BD4', linewidth=2.5, label='T(B1(t))')
ax.plot(B2[:,0],  B2[:,1],  color='#2CA470', linewidth=2.5, label='B2(t)')

ax.scatter(*TP0, color='red', s=100, zorder=6)
ax.scatter(*TP3, color='red', s=100, zorder=6, label='Puntos de encuentro')
ax.annotate('T(P₀)=Q₃', TP0, textcoords="offset points", xytext=(6,6), fontsize=9, color='red')
ax.annotate('T(P₃)=Q₀', TP3, textcoords="offset points", xytext=(6,6), fontsize=9, color='red')

ax.set_title('T(B1(t)) y B2(t): figura cerrada', fontsize=12)
ax.legend(fontsize=9)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('ej13', dpi=150, bbox_inches='tight')
print("\nGráfico guardado.")