import numpy as np
import matplotlib.pyplot as plt
import sys

def analizar_elipse():
    """
    Función interactiva para analizar y graficar una elipse
    a partir de su ecuación general o canónica.
    """
    print("=" * 50)
    print("📐 ANALIZADOR DE ELIPSES")
    print("=" * 50)
    print("Seleccione el formato de entrada:")
    print("1. Forma Canónica: (x-h)^2 / A_den + (y-k)^2 / B_den = 1")
    print("2. Forma General : Ax^2 + By^2 + Cx + Dy + E = 0")
    
    opcion = input("Ingrese 1 o 2: ").strip()

    # ---------------------------------------------------------
    # 1. INGRESO Y PROCESAMIENTO DE LA ECUACIÓN
    # ---------------------------------------------------------
    if opcion == '1':
        print("\n--- Ha seleccionado la Forma Canónica ---")
        h = float(input("Ingrese el valor de h (coordenada x del centro): "))
        k = float(input("Ingrese el valor de k (coordenada y del centro): "))
        A_den = float(input("Ingrese el denominador debajo de las 'x' (A_den): "))
        B_den = float(input("Ingrese el denominador debajo de las 'y' (B_den): "))
        
        if A_den <= 0 or B_den <= 0:
            print("Error: Los denominadores deben ser estrictamente positivos.")
            return
    elif opcion == '2':
        print("\n--- Ha seleccionado la Forma General ---")
        A = float(input("Ingrese A (coeficiente de x^2): "))
        B = float(input("Ingrese B (coeficiente de y^2): "))
        C = float(input("Ingrese C (coeficiente de x): "))
        D = float(input("Ingrese D (coeficiente de y): "))
        E = float(input("Ingrese E (término independiente): "))
        # Validación matemática para elipses reales: A y B deben tener el mismo signo
        if A * B <= 0:
            print("Error: Los coeficientes A y B deben tener el mismo signo para ser una elipse.")
            return
        # Completación de cuadrados algebraicamente:
        # A(x^2 + (C/A)x) + B(y^2 + (D/B)y) = -E
        # Se suma (C/2A)^2 y (D/2B)^2 compensando al otro lado
        h = -C / (2 * A)
        k = -D / (2 * B)
        # Término constante al lado derecho de la ecuación tras completar cuadrados
        F = (C**2) / (4 * A) + (D**2) / (4 * B) - E
        if F <= 0:
            print("Error: Los coeficientes dados forman una elipse imaginaria o un solo punto.")
            return
        # Al dividir todo entre F, obtenemos los denominadores de la forma canónica
        A_den = F / A
        B_den = F / B       
        print(f"\n✅ Ecuación canónica obtenida:")
        print(f"(x - {h:.2f})^2 / {A_den:.2f} + (y - {k:.2f})^2 / {B_den:.2f} = 1")
    else:
        print("Opción no válida. Ejecute el script nuevamente.")
        return
    # ---------------------------------------------------------
    # 2. ANÁLISIS GEOMÉTRICO
    # ---------------------------------------------------------
    # Determinamos la orientación evaluando cuál denominador es mayor
    if A_den > B_den:
        orientacion = "Horizontal"
        a = np.sqrt(A_den) # Semieje mayor en X
        b = np.sqrt(B_den) # Semieje menor en Y
        c = np.sqrt(a**2 - b**2) # Distancia del centro al foco
        
        vertices = [(h - a, k), (h + a, k)]
        co_vertices = [(h, k - b), (h, k + b)]
        focos = [(h - c, k), (h + c, k)]
    else:
        orientacion = "Vertical"
        a = np.sqrt(B_den) # Semieje mayor en Y
        b = np.sqrt(A_den) # Semieje menor en X
        c = np.sqrt(a**2 - b**2) # Distancia del centro al foco
        
        # Las coordenadas cambian de eje respecto al caso horizontal
        vertices = [(h, k - a), (h, k + a)]
        co_vertices = [(h - b, k), (h + b, k)]
        focos = [(h, k - c), (h, k + c)]

    # ---------------------------------------------------------
    # 3. IMPRESIÓN DE RESULTADOS
    # ---------------------------------------------------------
    print("\n" + "-" * 50)
    print("📊 RESULTADOS DEL ANÁLISIS")
    print("-" * 50)
    print(f"Orientación  : {orientacion}")
    print(f"Centro (h,k) : ({h:.2f}, {k:.2f})")
    print(f"Eje Mayor    : {2*a:.2f} unidades")
    print(f"Eje Menor    : {2*b:.2f} unidades")
    print(f"Dist. Focal  : {2*c:.2f} unidades (Distancia entre los dos focos)")
    print(f"Vértices     : V1({vertices[0][0]:.2f}, {vertices[0][1]:.2f}) y V2({vertices[1][0]:.2f}, {vertices[1][1]:.2f})")
    print(f"Co-vértices  : C1({co_vertices[0][0]:.2f}, {co_vertices[0][1]:.2f}) y C2({co_vertices[1][0]:.2f}, {co_vertices[1][1]:.2f})")
    print(f"Focos        : F1({focos[0][0]:.2f}, {focos[0][1]:.2f}) y F2({focos[1][0]:.2f}, {focos[1][1]:.2f})")
    print("-" * 50)

    # ---------------------------------------------------------
    # 4. GRÁFICO 2D
    # ---------------------------------------------------------
    # Usamos ecuaciones paramétricas para dibujar la elipse: 
    # x(t) = h + a*cos(t), y(t) = k + b*sin(t)
    t = np.linspace(0, 2 * np.pi, 1000)
    x_plot = h + np.sqrt(A_den) * np.cos(t)
    y_plot = k + np.sqrt(B_den) * np.sin(t)

    plt.figure(figsize=(8, 8))
    
    # Dibujar la elipse
    plt.plot(x_plot, y_plot, label='Elipse', color='#1f77b4', linewidth=2)
    
    # Dibujar los puntos clave extrayendo las coordenadas X e Y de las listas
    plt.plot(h, k, 'ko', label='Centro', markersize=6)
    
    # Extraemos las 'x' y las 'y' de la lista de tuplas para los Vértices
    v_x = [v[0] for v in vertices]
    v_y = [v[1] for v in vertices]
    plt.plot(v_x, v_y, 'ro', label='Vértices', markersize=6)
    
    # Extraemos las 'x' y las 'y' de la lista de tuplas para los Focos
    f_x = [f[0] for f in focos]
    f_y = [f[1] for f in focos]
    plt.plot(f_x, f_y, 'gx', label='Focos', markersize=7, marker='X')

    # Dibujar los ejes mayor y menor de forma visual con líneas punteadas
    plt.plot([v_x[0], v_x[1]], [v_y[0], v_y[1]], 'r--', alpha=0.5, label='Eje Mayor')
    plt.plot([co_vertices[0][0], co_vertices[1][0]], [co_vertices[0][1], co_vertices[1][1]], 'b--', alpha=0.5, label='Eje Menor')

    # Formato del plano cartesiano
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(color='gray', linestyle=':', alpha=0.7)
    
    # IMPORTANTE: Forzamos la relación de aspecto 1:1 para que la elipse no se deforme
    plt.axis('equal') 
    
    plt.legend(loc='upper right')
    plt.title('Representación Gráfica de la Elipse', fontsize=14, fontweight='bold')
    plt.xlabel('Eje X', fontsize=12)
    plt.ylabel('Eje Y', fontsize=12)
    
    # Mostrar gráfico
    plt.show()

analizar_elipse()