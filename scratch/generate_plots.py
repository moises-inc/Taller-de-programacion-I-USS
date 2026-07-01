import os
import numpy as np
import matplotlib.pyplot as plt

# Usar estilo limpio y profesional
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# Definir colores institucionales USS
USS_BLUE = (0/255, 32/255, 91/255)
USS_GOLD = (212/255, 175/255, 55/255)
ACCENT_BLUE = (30/255, 144/255, 255/255)
DARK_GRAY = (50/255, 50/255, 50/255)

# Crear directorio docs si no existe (por seguridad)
os.makedirs("docs", exist_ok=True)
os.makedirs("USS SPIDERBOT (solemne 3)/docs", exist_ok=True)

# =============================================================================
# GRAFICO 1: Simulación de Ángulos del Ciclo de Marcha (Crawl Gait)
# =============================================================================
t = np.linspace(0, 1, 500)
# Ángulo Coxa: oscila adelante y atrás
coxa = 90 + 20 * np.sin(2 * np.pi * t)
# Ángulo Fémur: sube en fase de swing y apoya en stance
femur = 60 + 30 * np.maximum(0, np.sin(2 * np.pi * t))

plt.figure(figsize=(8, 4.5), dpi=300)
plt.plot(t * 100, coxa, label="Servo Coxa (Cadera)", color=USS_BLUE, linewidth=2.5)
plt.plot(t * 100, femur, label="Servo Fémur (Muslo)", color=USS_GOLD, linewidth=2.5, linestyle="--")

# Decoración del gráfico
plt.title("Perfiles Angulares del Ciclo de Marcha (Crawl Gait)", fontsize=13, fontweight='bold', color=USS_BLUE, pad=15)
plt.xlabel("Progreso del Ciclo (%)", fontsize=11, color=DARK_GRAY)
plt.ylabel("Ángulo de Servo (Grados)", fontsize=11, color=DARK_GRAY)
plt.axvspan(0, 50, alpha=0.15, color='gray', label="Fase de Apoyo (Stance)")
plt.axvspan(50, 100, alpha=0.15, color=USS_GOLD, label="Fase de Vuelo (Swing)")
plt.legend(loc="upper right", frameon=True, facecolor='white', edgecolor='lightgray')
plt.ylim(30, 130)
plt.tight_layout()

plt.savefig("docs/gait_simulation.png", dpi=300)
plt.savefig("USS SPIDERBOT (solemne 3)/docs/gait_simulation.png", dpi=300)
plt.close()

# =============================================================================
# GRAFICO 2: Lazo de Compensación Inercial Activa (MPU6050)
# =============================================================================
time = np.linspace(0, 5, 500)
# Perturbación: oscilación atenuada que simula el movimiento del terreno
perturbacion = 10 * np.sin(1.5 * np.pi * time) * np.exp(-0.4 * time)
# Respuesta del lazo cerrado: estabilización rápida gracias a la corrección inercial
tolerancia = 3.0
tolerancia_line = np.ones_like(time) * tolerancia

# Simular respuesta activa con amortiguación más rápida
respuesta_estabilizada = perturbacion * np.exp(-1.5 * time)

plt.figure(figsize=(8, 4.5), dpi=300)
plt.plot(time, perturbacion, label="Ángulo sin Compensación (Lazo Abierto)", color='red', linewidth=1.8, linestyle=":")
plt.plot(time, respuesta_estabilizada, label="Ángulo Estabilizado (Compensación Activa)", color=USS_BLUE, linewidth=2.5)
plt.axhline(0, color='gray', linewidth=0.8)
plt.axhline(tolerancia, color='green', linestyle="--", linewidth=1.2, label=f"Banda de Tolerancia (±{tolerancia}°)")
plt.axhline(-tolerancia, color='green', linestyle="--", linewidth=1.2)

# Decoración del gráfico
plt.title("Respuesta Inercial Transitoria ante Perturbación Externa (Pitch/Roll)", fontsize=13, fontweight='bold', color=USS_BLUE, pad=15)
plt.xlabel("Tiempo (Segundos)", fontsize=11, color=DARK_GRAY)
plt.ylabel("Desviación Angular (Grados)", fontsize=11, color=DARK_GRAY)
plt.legend(loc="upper right", frameon=True, facecolor='white', edgecolor='lightgray')
plt.ylim(-12, 12)
plt.tight_layout()

plt.savefig("docs/stabilization_response.png", dpi=300)
plt.savefig("USS SPIDERBOT (solemne 3)/docs/stabilization_response.png", dpi=300)
plt.close()

print("Gráficos generados y guardados exitosamente en docs/ y USS SPIDERBOT (solemne 3)/docs/")
