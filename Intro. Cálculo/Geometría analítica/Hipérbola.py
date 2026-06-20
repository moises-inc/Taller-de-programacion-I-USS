import numpy as np
import matplotlib.pyplot as plt

def analizar_hiperbola():
    """
    Analiza y grafica una hipérbola transformando ecuaciones algebraicamente.
    """
    print("=" * 50)
    print("⏳ ANALIZADOR DE HIPÉRBOLAS")
    print("=" * 50)
    print("Seleccione el formato de entrada:")
    print("1. Forma Canónica")
    print("2. Forma General : Ax^2 + By^2 + Cx + Dy + E = 0")
    
    opcion = input("Ingrese 1 o 2: ").strip()

    if opcion == '1':
        print("\nOrientación: 1. Horizontal (x positivo) | 2. Vertical (y positivo)")
        ori = input("Ingrese 1 o 2: ").strip()
        h = float(input("Ingrese h (x del centro): "))
        k = float(input("Ingrese k (y del centro): "))
        a_cuadrado = float(input("Ingrese a^2 (denominador del término positivo): "))
        b_cuadrado = float(input("Ingrese b^2 (denominador del término negativo): "))
        
        a = np.sqrt(a_cuadrado)
        b = np.sqrt(b_cuadrado)
        orientacion = "Horizontal" if ori == '1' else "Vertical"

    elif opcion == '2':
        A = float(input("Ingrese A (coeficiente de x^2): "))
        B = float(input("Ingrese B (coeficiente de y^2): "))
        C = float(input("Ingrese C (coeficiente de x): "))
        D = float(input("Ingrese D (coeficiente de y): "))
        E = float(input("Ingrese E (término independiente): "))

        if A * B >= 0:
            print("Error: En una hipérbola, A y B deben tener signos opuestos.")
            return

        # Completación de cuadrados
        h = -C / (2 * A)
        k = -D / (2 * B)
        F = (C**2) / (4 * A) + (D**2) / (4 * B) - E
        
        if F == 0:
            print("Error: Hipérbola degenerada (son dos líneas rectas secantes).")
            return

        # Denominadores: F/A y F/B. Uno será positivo y el otro negativo.
        den_X = F / A
        den_Y = F / B
        
        if den_X > 0:
            orientacion = "Horizontal"
            a = np.sqrt(den_X)
            b = np.sqrt(abs(den_Y))
        else:
            orientacion = "Vertical"
            a = np.sqrt(den_Y)
            b = np.sqrt(abs(den_X))
            
        print(f"\n✅ Ecuación canónica procesada (Centro en {h:.2f}, {k:.2f})")

    else:
        return

    # --- ANÁLISIS GEOMÉTRICO ---
    c = np.sqrt(a**2 + b**2) # Pitágoras para la hipérbola (se suman los cuadrados)
    
    if orientacion == "Horizontal":
        vertices = [(h - a, k), (h + a, k)]
        focos = [(h - c, k), (h + c, k)]
        asintota1 = fr"y - {k:.2f} = {b/a:.2f}(x - {h:.2f})"
        asintota2 = fr"y - {k:.2f} = {-b/a:.2f}(x - {h:.2f})"
        m_asintota = b/a
    else:
        vertices = [(h, k - a), (h, k + a)]
        focos = [(h, k - c), (h, k + c)]
        asintota1 = fr"y - {k:.2f} = {a/b:.2f}(x - {h:.2f})"
        asintota2 = fr"y - {k:.2f} = {-a/b:.2f}(x - {h:.2f})"
        m_asintota = a/b

    print("\n" + "-" * 50)
    print("📊 RESULTADOS DEL ANÁLISIS")
    print("-" * 50)
    print(f"Orientación      : {orientacion}")
    print(f"Centro (h,k)     : ({h:.2f}, {k:.2f})")
    print(f"Eje Transverso 2a: {2*a:.2f} (Distancia entre vértices)")
    print(f"Eje Conjugado 2b : {2*b:.2f}")
    print(f"Dist. Focal 2c   : {2*c:.2f} (Distancia entre focos)")
    print(f"Vértices         : V1({vertices[0][0]:.2f}, {vertices[0][1]:.2f}) y V2({vertices[1][0]:.2f}, {vertices[1][1]:.2f})")
    print(f"Focos            : F1({focos[0][0]:.2f}, {focos[0][1]:.2f}) y F2({focos[1][0]:.2f}, {focos[1][1]:.2f})")
    print(f"Asíntota 1       : {asintota1}")
    print(f"Asíntota 2       : {asintota2}")
    print("-" * 50)

    # --- GRÁFICO ---
    plt.figure(figsize=(8, 8))
    
    # Parámetro t para la curva paramétrica usando funciones hiperbólicas (cosh, sinh)
    t = np.linspace(-2.5, 2.5, 500)
    
    if orientacion == "Horizontal":
        # Rama derecha e izquierda
        x_rama1 = h + a * np.cosh(t)
        x_rama2 = h - a * np.cosh(t)
        y_ramas = k + b * np.sinh(t)
        plt.plot(x_rama1, y_ramas, color='#d62728', linewidth=2, label='Hipérbola')
        plt.plot(x_rama2, y_ramas, color='#d62728', linewidth=2)
        
        # Asíntotas
        x_asintota = np.linspace(h - a*4, h + a*4, 100)
        y_asintota1 = k + m_asintota * (x_asintota - h)
        y_asintota2 = k - m_asintota * (x_asintota - h)
        
    else:
        # Rama superior e inferior
        x_ramas = h + b * np.sinh(t)
        y_rama1 = k + a * np.cosh(t)
        y_rama2 = k - a * np.cosh(t)
        plt.plot(x_ramas, y_rama1, color='#d62728', linewidth=2, label='Hipérbola')
        plt.plot(x_ramas, y_rama2, color='#d62728', linewidth=2)
        
        # Asíntotas
        x_asintota = np.linspace(h - b*4, h + b*4, 100)
        y_asintota1 = k + m_asintota * (x_asintota - h)
        y_asintota2 = k - m_asintota * (x_asintota - h)

    # Dibujo de Asíntotas
    plt.plot(x_asintota, y_asintota1, 'b--', alpha=0.5, label='Asíntotas')
    plt.plot(x_asintota, y_asintota2, 'b--', alpha=0.5)

    # Puntos clave
    plt.plot(h, k, 'ko', label='Centro')
    plt.plot([v[0] for v in vertices], [v[1] for v in vertices], 'ro', label='Vértices')
    plt.plot([f[0] for f in focos], [f[1] for f in focos], 'gx', markersize=8, label='Focos')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle=':', alpha=0.7)
    plt.axis('equal')
    plt.legend()
    plt.title('Representación Gráfica de la Hipérbola', fontweight='bold')
    plt.show()


analizar_hiperbola()