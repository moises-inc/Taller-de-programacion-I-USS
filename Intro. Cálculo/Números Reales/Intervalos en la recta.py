import matplotlib.pyplot as plt
import numpy as np

def graficar_intervalos(intervalos, x_min=-10, x_max=10):
    """
    Grafica una lista de intervalos en una recta real, soportando infinitos.
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Dibujar la recta real base
    ax.axhline(0, color='black', linewidth=1.5)
    
    # Configurar los ticks (números) de la recta real
    ax.set_xticks(range(x_min, x_max + 1))
    ax.set_yticks([]) 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    
    desplazamiento_y = 0.2 
    
    for nombre, inicio, fin, incl_inicio, incl_fin, color in intervalos:
        # Determinar las coordenadas de dibujo limitadas por la gráfica
        coord_inicio = x_min if inicio == -np.inf else inicio
        coord_fin = x_max if fin == np.inf else fin
        
        # Dibujar la línea principal
        ax.plot([coord_inicio, coord_fin], [desplazamiento_y, desplazamiento_y], color=color, linewidth=3)
        
        # Extremo izquierdo
        if inicio == -np.inf:
            # Si tiende a -infinito, ponemos una flecha hacia la izquierda
            ax.plot(coord_inicio, desplazamiento_y, marker='<', markersize=8, color=color)
        else:
            # Si es un número, dibujamos el círculo correspondiente
            color_fondo = color if incl_inicio else 'white'
            ax.plot(inicio, desplazamiento_y, marker='o', markersize=8, color=color, markerfacecolor=color_fondo, zorder=5)
            
        # Extremo derecho
        if fin == np.inf:
            # Si tiende a infinito, ponemos una flecha hacia la derecha
            ax.plot(coord_fin, desplazamiento_y, marker='>', markersize=8, color=color)
        else:
            # Si es un número, dibujamos el círculo correspondiente
            color_fondo = color if incl_fin else 'white'
            ax.plot(fin, desplazamiento_y, marker='o', markersize=8, color=color, markerfacecolor=color_fondo, zorder=5)
            
        # Etiqueta del intervalo (centrada dinámicamente)
        if inicio == -np.inf and fin == np.inf:
            centro_x = 0
        elif inicio == -np.inf:
            centro_x = coord_fin - 2
        elif fin == np.inf:
            centro_x = coord_inicio + 2
        else:
            centro_x = (inicio + fin) / 2
            
        ax.text(centro_x, desplazamiento_y + 0.01, nombre, color=color, fontsize=12, fontweight='bold', ha='center')
        
        # Sombrear el área
        ax.fill_between([coord_inicio, coord_fin], 0, desplazamiento_y, color=color, alpha=0.1, hatch='//')
        
        desplazamiento_y += 0.2

    # Configurar los límites de la gráfica para añadir un pequeño margen a las flechas
    plt.xlim(x_min - 0.5, x_max + 0.5)
    plt.title("Representación de Intervalos", pad=20)
    plt.show()

# ==========================================
# PARÁMETROS CONFIGURABLES
# ==========================================
# Formato: (Nombre, Inicio, Fin, Incluye_Inicio, Incluye_Fin, Color)
# Usa np.inf para infinito positivo y -np.inf para infinito negativo
# (Para los infinitos, da igual si pones True o False en la inclusión,
# el código dibujará una flecha automáticamente)

mis_intervalos = [
    (r"$\{x \in \mathbb{R} : x \geq -1 \}$", -1, np.inf, False, False, 'blue'),  
]

# Modifica los límites x_min y x_max según los valores que necesites observar
graficar_intervalos(mis_intervalos, x_min=-6, x_max=10)