import numpy as np
import matplotlib.pyplot as plt

class FuncionTrigonometrica:
    def __init__(self, A, B, C, D, tipo='seno'):
        """
        Constructor de la clase. Recibe los parámetros de la forma general:
        y(t) = A * sen(B*t - C) + D   o   y(t) = A * cos(B*t - C) + D
        """
        self.A = float(A)  # Amplitud
        self.B = float(B)  # Frecuencia angular (afecta el período)
        self.C = float(C)  # Desfase horizontal
        self.D = float(D)  # Desplazamiento vertical (nivel medio)
        self.tipo = tipo.lower() # Convertimos a minúsculas para evitar errores ('SENO' -> 'seno')
        
    def analizar(self):
        """
        Calcula y muestra en consola las propiedades matemáticas de la función
        basándose en las definiciones formales, sin usar derivadas ni límites.
        """
        # El valor absoluto de A es la amplitud
        amplitud = abs(self.A)
        
        # El período de seno/coseno es siempre 2*pi dividido por el valor absoluto de B
        periodo = (2 * np.pi) / abs(self.B)
        
        # La frecuencia es la inversa del período (cuántos ciclos por unidad de tiempo)
        frecuencia = 1 / periodo
        
        # El desfase se calcula dividiendo C entre B
        desfase = self.C / self.B
        
        # El recorrido se basa en el nivel medio (D) sumando y restando la amplitud máxima
        recorrido_min = self.D - amplitud
        recorrido_max = self.D + amplitud
        
        # Imprimimos los resultados formateados
        print("-" * 40)
        print(f"📊 ANÁLISIS DE LA FUNCIÓN {self.tipo.upper()}")
        print("-" * 40)
        print(f"Amplitud               : {amplitud}")
        print(f"Período                : {periodo:.5f}")
        print(f"Frecuencia             : {frecuencia:.2f}")
        print(f"Desplazamiento de Fase : {desfase:.2f}")
        print(f"Desplazamiento Vertical: {self.D}")
        print(f"Dominio                : R (Todos los números reales)")
        print(f"Recorrido / Alcance    : [{recorrido_min}, {recorrido_max}]")
        print("-" * 40)
        
        # Retornamos estos valores porque los usaremos para limitar y dibujar el gráfico
        return periodo, recorrido_min, recorrido_max

    def graficar(self):
        """
        Genera una representación visual 2D de la función trigonométrica.
        """
        # Obtenemos los datos calculados en la función analizar()
        periodo, rec_min, rec_max = self.analizar()
        
        # np.linspace genera 1000 puntos espaciados uniformemente.
        # Graficaremos desde t=0 hasta t=3*periodo (para ver exactamente 3 ondas completas)
        t = np.linspace(0, 3 * periodo, 1000)
        
        # Lógica condicional para evaluar si usamos np.sin() o np.cos()
        if self.tipo == 'seno':
            y = self.A * np.sin(self.B * t - self.C) + self.D
            func_str = r'\sin' # Texto para la leyenda (formato LaTeX)
        elif self.tipo == 'coseno':
            y = self.A * np.cos(self.B * t - self.C) + self.D
            func_str = r'\cos' # Texto para la leyenda (formato LaTeX)
        else:
            # Medida de seguridad por si el usuario ingresa un tipo inválido
            raise ValueError("El tipo debe ser 'seno' o 'coseno'")

        # --- CREACIÓN DEL GRÁFICO ---
        plt.figure(figsize=(10, 6))
        
        # Dibujamos la curva principal. 
        # NOTA: Usamos 'fr' (f-string + raw string) para evitar el SyntaxWarning con \cdot y \sin
        etiqueta_leyenda = fr'$p(t) = {self.D} + {self.A} \cdot {func_str}({self.B:.2f}t - {self.C})$'
        plt.plot(t, y, label=etiqueta_leyenda, color='#1f77b4', linewidth=2)
        
        # Añadimos líneas horizontales (axhline) para mostrar el desplazamiento y el recorrido
        plt.axhline(self.D, color='gray', linestyle='--', alpha=0.7, label=f'Nivel Medio (y={self.D})')
        plt.axhline(rec_max, color='red', linestyle=':', alpha=0.8, label=f'Máximo (y={rec_max})')
        plt.axhline(rec_min, color='green', linestyle=':', alpha=0.8, label=f'Mínimo (y={rec_min})')
        
        # Personalización de títulos y etiquetas de los ejes
        plt.title(f'Gráfico de Función {self.tipo.capitalize()}', fontsize=14, fontweight='bold')
        plt.xlabel('Tiempo (t)', fontsize=12)
        plt.ylabel('Amplitud p(t)', fontsize=12)
        
        # Mostramos la leyenda y activamos la grilla de fondo
        plt.legend(loc='upper right')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout() # Ajusta los márgenes automáticamente
        
        # Renderizamos la ventana del gráfico
        plt.show()

# ==========================================
# EJECUCIÓN 1: Función Seno (El ejemplo anterior)
# p(t) = 115 + 25 * sin(160*pi*t)
# ==========================================
print("\n>>> Ejecutando Ejemplo 1 (Seno):")
onda_seno = FuncionTrigonometrica(A=25, B=160*np.pi, C=0, D=115, tipo='seno')
onda_seno.graficar()

# ==========================================
# EJECUCIÓN 2: Función Coseno
# p(t) = 3 - 2 * cos(4*t - pi/2)
# Reordenando: A=-2, B=4, C=pi/2, D=3
# ==========================================
print("\n>>> Ejecutando Ejemplo 2 (Coseno):")
onda_coseno = FuncionTrigonometrica(A=-2, B=4, C=np.pi/2, D=3, tipo='coseno')
onda_coseno.graficar()