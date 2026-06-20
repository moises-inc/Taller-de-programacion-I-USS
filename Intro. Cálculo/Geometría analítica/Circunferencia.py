import numpy as np
import matplotlib.pyplot as plt

def analizar_circunferencia():
    """
    Analiza y grafica una circunferencia desde su forma canónica o general.
    """
    print("=" * 50)
    print("🔵 ANALIZADOR DE CIRCUNFERENCIAS")
    print("=" * 50)
    print("Seleccione el formato de entrada:")
    print("1. Forma Canónica: (x-h)^2 + (y-k)^2 = r^2")
    print("2. Forma General : x^2 + y^2 + Cx + Dy + E = 0")
    
    opcion = input("Ingrese 1 o 2: ").strip()

    if opcion == '1':
        print("\n--- Forma Canónica ---")
        h = float(input("Ingrese h (coordenada x del centro): "))
        k = float(input("Ingrese k (coordenada y del centro): "))
        r_cuadrado = float(input("Ingrese el radio al cuadrado (r^2): "))
        
        if r_cuadrado <= 0:
            print("Error: El radio al cuadrado debe ser mayor a 0.")
            return
        r = np.sqrt(r_cuadrado)

    elif opcion == '2':
        print("\n--- Forma General ---")
        print("Nota: Se asume que los coeficientes de x^2 e y^2 son 1.")
        C = float(input("Ingrese C (coeficiente de x): "))
        D = float(input("Ingrese D (coeficiente de y): "))
        E = float(input("Ingrese E (término independiente): "))

        # Completación de cuadrados: (x + C/2)^2 + (y + D/2)^2 = (C/2)^2 + (D/2)^2 - E
        h = -C / 2
        k = -D / 2
        r_cuadrado = h**2 + k**2 - E
        
        if r_cuadrado <= 0:
            print("Error: Los coeficientes forman un punto o un radio imaginario.")
            return
        r = np.sqrt(r_cuadrado)
        print(f"\n✅ Ecuación canónica: (x - {h:.2f})^2 + (y - {k:.2f})^2 = {r:.2f}^2")

    else:
        print("Opción no válida.")
        return

    # --- ANÁLISIS ---
    print("\n" + "-" * 50)
    print("📊 RESULTADOS DEL ANÁLISIS")
    print("-" * 50)
    print(f"Centro (h,k) : ({h:.2f}, {k:.2f})")
    print(f"Radio (r)    : {r:.2f} unidades")
    print(f"Diámetro     : {2*r:.2f} unidades")
    print("-" * 50)

    # --- GRÁFICO ---
    t = np.linspace(0, 2 * np.pi, 1000)
    x_plot = h + r * np.cos(t)
    y_plot = k + r * np.sin(t)

    plt.figure(figsize=(8, 8))
    plt.plot(x_plot, y_plot, label='Circunferencia', color='#2ca02c', linewidth=2)
    plt.plot(h, k, 'ko', label=f'Centro ({h:.2f}, {k:.2f})')
    
    # Línea del radio
    plt.plot([h, h+r], [k, k], 'r--', label=f'Radio = {r:.2f}')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle=':', alpha=0.7)
    plt.axis('equal') # Vital para que sea redonda y no elíptica
    
    plt.legend(loc='upper right')
    plt.title('Representación Gráfica de la Circunferencia', fontweight='bold')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()

analizar_circunferencia()