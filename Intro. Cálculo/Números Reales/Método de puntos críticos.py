import matplotlib.pyplot as plt
import numpy as np

def graficar_metodo_signos(inecuacion_tex, puntos_criticos, signos, incluye_puntos, buscar_positivos, solucion_tex, x_min=-3, x_max=2):
    """
    Grafica el análisis de signos para inecuaciones mediante el método de puntos críticos.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Dibujar la recta real base
    ax.axhline(0, color='black', linewidth=1.5)
    ax.set_yticks([]) 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    
    # Ordenar los puntos por si acaso
    puntos_criticos = sorted(puntos_criticos)
    
    # Crear la lista de todos los "límites" incluyendo los infinitos para iterar
    limites = [-np.inf] + puntos_criticos + [np.inf]
    
    # Altura para dibujar los arcos y signos
    altura_arco = 0.5
    
    for i in range(len(signos)):
        inicio = limites[i]
        fin = limites[i+1]
        signo_actual = signos[i]
        
        # Determinar el centro del intervalo para colocar el signo
        if inicio == -np.inf:
            centro = puntos_criticos[0] - 1
            x_dibujo_inicio = x_min
            x_dibujo_fin = fin
        elif fin == np.inf:
            centro = puntos_criticos[-1] + 1
            x_dibujo_inicio = inicio
            x_dibujo_fin = x_max
        else:
            centro = (inicio + fin) / 2
            x_dibujo_inicio = inicio
            x_dibujo_fin = fin
            
        # Colocar el texto del signo (+ o -)
        color_signo = 'green' if signo_actual == '+' else 'red'
        ax.text(centro, altura_arco / 2, signo_actual, color=color_signo, fontsize=20, fontweight='bold', ha='center', va='center')
        
        # Sombrear la zona si coincide con lo que buscamos (Paso 6 y 7)
        # Si buscamos positivos (>= 0) y el signo es '+', o negativos (<= 0) y el signo es '-'
        es_solucion = (buscar_positivos and signo_actual == '+') or (not buscar_positivos and signo_actual == '-')
        
        if es_solucion:
            ax.fill_between([x_dibujo_inicio, x_dibujo_fin], 0, altura_arco, color=color_signo, alpha=0.2, hatch='\\\\')
            # Dibujar la línea gruesa de la solución sobre el eje
            ax.plot([x_dibujo_inicio, x_dibujo_fin], [0, 0], color=color_signo, linewidth=4, zorder=4)

            # Flechas para los infinitos en la línea de solución
            if inicio == -np.inf:
                ax.plot(x_dibujo_inicio, 0, marker='<', markersize=8, color=color_signo, zorder=5, clip_on=False)
            if fin == np.inf:
                ax.plot(x_dibujo_fin, 0, marker='>', markersize=8, color=color_signo, zorder=5, clip_on=False)

    # Dibujar los puntos críticos (Paso 2 y 3)
    for pt, incl in zip(puntos_criticos, incluye_puntos):
        color_punto = 'black'
        color_fondo = color_punto if incl else 'white'
        ax.plot(pt, 0, marker='o', markersize=8, color=color_punto, markerfacecolor=color_fondo, zorder=6)
        # Etiqueta numérica del punto crítico
        ax.text(pt, -0.15, f"{pt}", color='black', fontsize=12, ha='center', fontweight='bold')

    # Configuración final visual
    plt.xlim(x_min, x_max)
    plt.title(f"Análisis de Signos: {inecuacion_tex}", pad=20, fontsize=14)
    plt.figtext(0.5, -0.05, f"Solución: {solucion_tex}", ha="center", fontsize=14, bbox={"facecolor":"white", "alpha":0.5, "pad":5})
    
    plt.tight_layout()
    plt.show()

# ==========================================
# PARÁMETROS DEL PROBLEMA (Pasos 1 al 7)
# ==========================================
inecuacion = r"$2x^2 + 3x + 1 \geq 0$"

# Pasos 1, 2 y 3: Identificar ceros y si son cerrados/abiertos
puntos = [-1.0, -0.5]
incluidos = [True, True] # True porque es >= y están en el numerador

# Pasos 4 y 5: Signos evaluados en cada intervalo (de izquierda a derecha)
# Intervalos: ]-inf, -1[, ]-1, -0.5[, ]-0.5, inf[
signos_intervalos = ['+', '-', '+']

# Paso 6: ¿Elegimos los positivos? (True para >= o >, False para <= o <)
elegir_positivos = True 

# Paso 7: Solución final formateada en LaTeX
solucion = r"$S = ]-\infty, -1] \cup [-0.5, +\infty[$"

# Ejecutar gráfica ajustando la ventana visual
graficar_metodo_signos(inecuacion, puntos, signos_intervalos, incluidos, elegir_positivos, solucion, x_min=-3, x_max=1.5)