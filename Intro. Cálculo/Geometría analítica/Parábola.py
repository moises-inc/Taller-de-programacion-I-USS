import numpy as np
import matplotlib.pyplot as plt

def analizar_parabola():
    """
    Analiza y grafica una parábola vertical u horizontal.
    """
    print("=" * 50)
    print("📈 ANALIZADOR DE PARÁBOLAS")
    print("=" * 50)
    print("Seleccione la orientación (basado en el término cuadrático):")
    print("1. Vertical   (x-h)^2 = 4p(y-k)  [o Ax^2 + Cx + Dy + E = 0]")
    print("2. Horizontal (y-k)^2 = 4p(x-h)  [o By^2 + Cx + Dy + E = 0]")
    
    orientacion = input("Ingrese 1 o 2: ").strip()
    
    if orientacion not in ['1', '2']:
        print("Opción no válida.")
        return

    print("\nSeleccione el formato de entrada:")
    print("1. Forma Canónica")
    print("2. Forma General")
    formato = input("Ingrese 1 o 2: ").strip()

    if formato == '1':
        h = float(input("Ingrese h (coordenada x del vértice): "))
        k = float(input("Ingrese k (coordenada y del vértice): "))
        p = float(input("Ingrese el parámetro p (distancia vértice-foco): "))
        if p == 0:
            print("Error: El parámetro p no puede ser 0.")
            return

    elif formato == '2':
        if orientacion == '1': # Vertical (Ax^2 + Cx + Dy + E = 0)
            A = float(input("Ingrese A (coeficiente de x^2): "))
            C = float(input("Ingrese C (coeficiente de x): "))
            D = float(input("Ingrese D (coeficiente de y): "))
            E = float(input("Ingrese E (término independiente): "))
            
            if A == 0 or D == 0:
                print("Error: No es una parábola vertical válida (A y D no pueden ser 0).")
                return
                
            # Completación: A(x^2 + (C/A)x) = -Dy - E -> (x + C/2A)^2 = (-D/A)y + ...
            h = -C / (2 * A)
            k = (C**2 / (4 * A) - E) / D
            p = -D / (4 * A)
            
        else: # Horizontal (By^2 + Cx + Dy + E = 0)
            B = float(input("Ingrese B (coeficiente de y^2): "))
            C = float(input("Ingrese C (coeficiente de x): "))
            D = float(input("Ingrese D (coeficiente de y): "))
            E = float(input("Ingrese E (término independiente): "))
            
            if B == 0 or C == 0:
                print("Error: No es una parábola horizontal válida (B y C no pueden ser 0).")
                return
                
            k = -D / (2 * B)
            h = (D**2 / (4 * B) - E) / C
            p = -C / (4 * B)
            
        print(f"\n✅ Parámetros obtenidos: Vértice({h:.2f}, {k:.2f}), p={p:.2f}")

    else:
        print("Formato no válido.")
        return

    # --- ANÁLISIS ---
    print("\n" + "-" * 50)
    print("📊 RESULTADOS DEL ANÁLISIS")
    print("-" * 50)
    print(f"Vértice (h,k)  : ({h:.2f}, {k:.2f})")
    print(f"Parámetro (p)  : {p:.2f}")
    print(f"Lado Recto |4p|: {abs(4*p):.2f} unidades")
    
    if orientacion == '1':
        print(f"Foco           : ({h:.2f}, {k+p:.2f})")
        print(f"Directriz      : Línea y = {k-p:.2f}")
        print(f"Eje de simetría: Línea x = {h:.2f}")
        apertura = "Arriba" if p > 0 else "Abajo"
    else:
        print(f"Foco           : ({h+p:.2f}, {k:.2f})")
        print(f"Directriz      : Línea x = {h-p:.2f}")
        print(f"Eje de simetría: Línea y = {k:.2f}")
        apertura = "Derecha" if p > 0 else "Izquierda"
        
    print(f"Apertura       : Hacia la {apertura}")
    print("-" * 50)

    # --- GRÁFICO ---
    plt.figure(figsize=(8, 8))
    
    if orientacion == '1': # Vertical
        # Rango de x para graficar (vértice +- 4 veces p para buena visibilidad)
        x_plot = np.linspace(h - abs(4*p), h + abs(4*p), 500)
        y_plot = (x_plot - h)**2 / (4 * p) + k
        plt.plot(x_plot, y_plot, label='Parábola', color='#ff7f0e', linewidth=2)
        plt.plot(h, k+p, 'gx', label='Foco', markersize=8) # Foco
        plt.axhline(k-p, color='r', linestyle='--', label='Directriz') # Directriz
        
    else: # Horizontal
        y_plot = np.linspace(k - abs(4*p), k + abs(4*p), 500)
        x_plot = (y_plot - k)**2 / (4 * p) + h
        plt.plot(x_plot, y_plot, label='Parábola', color='#ff7f0e', linewidth=2)
        plt.plot(h+p, k, 'gx', label='Foco', markersize=8) # Foco
        plt.axvline(h-p, color='r', linestyle='--', label='Directriz') # Directriz

    plt.plot(h, k, 'ko', label='Vértice') # Vértice general
    
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle=':', alpha=0.7)
    plt.axis('equal')
    plt.legend()
    plt.title('Representación Gráfica de la Parábola', fontweight='bold')
    plt.show()

analizar_parabola()