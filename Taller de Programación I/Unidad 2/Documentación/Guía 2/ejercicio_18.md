### Ejercicio 18: Evaluación grupal de IMC para n personas

#### Enunciado del Problema
Desarrolla un script que pida al usuario un número n, correspondiente a la cantidad de personas a evaluar. Para cada persona, debe pedir: Nombre, Peso en kilogramos, Estatura en metros. Luego debe calcular el IMC = peso / (estatura²) y clasificar según la OMS: Bajo peso (<18.5), Normal (18.5-24.9), Sobrepeso (>=25). Al final, mostrar: Cantidad de personas en cada categoría y promedio de IMC del grupo.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `n` | `int` | Variable de control ingresada por el usuario que parametriza el total de evaluaciones grupales. |
| `bajo_peso` | `int` | Contador de personas catalogadas con Bajo Peso según los límites de la OMS (< 18.5). |
| `normal` | `int` | Contador de personas catalogadas con peso Normal según los límites de la OMS (18.5 a 24.9). |
| `sobrepeso` | `int` | Contador de personas con Sobrepeso según los límites de la OMS (>= 25.0). |
| `suma_imc` | `float` | Acumulador de los valores decimales de IMC calculados para promediarlos al final. |
| `i` | `int` | Variable de iteración del bucle `for` (0 a n-1). |
| `nombre` | `str` | Identificación textual de la persona evaluada, limpia de espacios residuales. |
| `peso` | `float` | Masa corporal en kilogramos de la persona actual, validada en el rango `[2.0, 300.0]`. |
| `estatura` | `float` | Estatura en metros de la persona actual, validada en el rango `[0.50, 2.50]`. |
| `imc` | `float` | Valor decimal calculado del Índice de Masa Corporal de la persona actual. |
| `clasif` | `str` | Glosa textual de la categoría de peso OMS asignada en la iteración. |
| `promedio_imc` | `float` | Media del IMC grupal obtenida al dividir la suma de los IMC por `n`. |


## Lógica de la Solución
El programa evalúa la composición corporal de un grupo variable de `n` personas de forma iterativa y parametrizada. 1. **Validación de n:** Se solicita el tamaño del grupo `n`, asegurando un entero estrictamente positivo con control de excepciones.2. **Bucle Parametrizado:** Se ejecuta un ciclo `for` que solicita la información biométrica de cada individuo:- **Nombre:** Limpia espacios con `.strip()` y se rechaza si se envía vacío.- **Peso:** Se valida con `try-except` que sea flotante y pertenezca al rango real `[2.0, 300.0] kg`.- **Estatura:** Se valida con `try-except` que sea flotante y pertenezca al rango real `[0.50, 2.50] metros`.3. **Cálculo y Clasificación:** Se aplica la fórmula oficial del IMC: $IMC = \frac{peso}{estatura^2}$. Luego, se clasifica según los estándares de la OMS: - **Bajo peso:** IMC menor a 18.5.- **Normal:** IMC mayor o igual a 18.5 y menor a 25.0.- **Sobrepeso:** IMC mayor o igual a 25.0.Se incrementa el contador respectivo, se acumula en `suma_imc` y se muestra el veredicto en pantalla. Al finalizar las `n` evaluaciones, se calcula el promedio de IMC del grupo y se genera una boleta estadística de salud.

## Explicación Línea por Línea
- **`while True: (primero)`**: Bucle interactivo de control de entrada para asegurar que la cantidad `n` de personas sea válida.
- **`n = int(input(...))`**: Solicita la cantidad de personas, las fuerza a tipo entero y las guarda en `n`.
- **`if n > 0:`**: Verifica que el número de personas a evaluar sea mayor que cero.
- **`break`**: Sale del bucle de validación de `n` e inicia las evaluaciones biométricas.
- **`except ValueError: (primero)`**: Atrapa excepciones de tipo si se ingresa texto en `n`.
- **`bajo_peso = 0`**: Inicializa en cero el contador de personas de bajo peso.
- **`normal = 0`**: Inicializa en cero el contador de personas de peso normal.
- **`sobrepeso = 0`**: Inicializa en cero el contador de personas con sobrepeso.
- **`suma_imc = 0.0`**: Inicializa en 0.0 la variable acumuladora de valores de IMC grupal.
- **`for i in range(n):`**: Inicia el ciclo principal que procesará exactamente a las `n` personas de la secuencia.
- **`nombre = input(...).strip()`**: Captura el nombre, limpia espacios marginales y lo guarda en `nombre`.
- **`while not nombre:`**: Bucle de validación para impedir el registro de personas sin identificación.
- **`nombre = input(...).strip()`**: Vuelve a requerir el nombre si se omitió.
- **`while True: (segundo)`**: Bucle de validación interna infinita para la variable de peso.
- **`peso = float(input(...))`**: Captura el peso convirtiéndolo a decimal y guardándolo en `peso`.
- **`if 2.0 <= peso <= 300.0:`**: Verifica lógicamente que el peso corporal esté en un rango biológicamente posible.
- **`break`**: Sale de la validación del peso actual al ser correcto.
- **`while True: (tercero)`**: Bucle de validación interna infinita para la variable de estatura.
- **`estatura = float(input(...))`**: Captura la estatura en metros convirtiéndola a decimal flotante y la guarda.
- **`if 0.50 <= estatura <= 2.50:`**: Verifica lógicamente que la estatura sea realista y posible.
- **`break`**: Sale de la validación de estatura e inicia las operaciones biométricas.
- **`imc = peso / (estatura ** 2)`**: Calcula aritméticamente el Índice de Masa Corporal aplicando la potencia de la estatura con el operador `**`.
- **`suma_imc += imc`**: Acumula el IMC calculado de la persona actual en la variable de sumas del grupo.
- **`if imc < 18.5:`**: Clasifica el IMC individual bajo el rango OMS de Bajo Peso.
- **`bajo_peso += 1`**: Suma 1 al contador de bajo peso.
- **`clasif = "Bajo peso"`**: Glosa descriptiva asignada.
- **`elif imc < 25.0:`**: Filtro en cascada. Clasifica el IMC bajo el rango de peso Normal.
- **`normal += 1`**: Suma 1 al contador de peso normal.
- **`clasif = "Normal"`**: Glosa descriptiva asignada.
- **`else:`**: Ejecutado al superarse los límites del peso normal (IMC de 25.0 o superior).
- **`sobrepeso += 1`**: Suma 1 al acumulador de sobrepeso.
- **`clasif = "Sobrepeso"`**: Glosa descriptiva asignada.
- **`print(f"Persona: {nombre} | IMC...")`**: Informa de forma inmediata en la terminal el estado de salud y el IMC de la persona en curso.
- **`promedio_imc = suma_imc / n`**: Calcula el promedio de IMC del grupo dividiendo la suma total acumulada por el número total de evaluados `n`.
- **`print("\n--- Informe Grupal de Salud ---")`**: Encabezado impreso en consola tras finalizar todas las iteraciones.
- **`print(...)`**: Imprime los reportes demográficos y el promedio de IMC de todo el grupo.


#### Código Completo
```python
print("--- Sistema de Evaluación de IMC Variable ---")
# Captura y validación de la variable de control de personas n
while True:
    try:
        n = int(input("¿Cuántas personas se evaluarán en el grupo?: "))
        if n > 0:
            break
        print("Error: El número de personas debe ser mayor a cero.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

bajo_peso = 0
normal = 0
sobrepeso = 0
suma_imc = 0.0

# Bucle principal controlado por la variable de entrada n
for i in range(n):
    print(f"\n--- Persona {i+1} de {n} ---")
    # Solicitud y saneamiento de nombre obligatorio
    nombre = input("Ingrese nombre de la persona: ").strip()
    while not nombre:
        nombre = input("El nombre es requerido: ").strip()

    # Validación interactiva interna de peso en kilogramos
    while True:
        try:
            peso = float(input(f"Ingrese peso en kilogramos de {nombre} (2.0 a 300.0 kg): "))
            if 2.0 <= peso <= 300.0:
                break
            print("Error: Ingrese un peso realista.")
        except ValueError:
            print("Error: Ingrese un valor numérico decimal.")

    # Validación interactiva interna de estatura en metros
    while True:
        try:
            estatura = float(input(f"Ingrese estatura en metros de {nombre} (0.50 a 2.50 m): "))
            if 0.50 <= estatura <= 2.50:
                break
            print("Error: Ingrese una estatura realista.")
        except ValueError:
            print("Error: Ingrese un valor numérico decimal.")

    # Cálculo del IMC aplicando la fórmula oficial OMS
    imc = peso / (estatura ** 2)
    suma_imc += imc

    # Clasificación por rangos estándar de la OMS
    if imc < 18.5:
        bajo_peso += 1
        clasif = "Bajo peso"
    elif imc < 25.0:
        normal += 1
        clasif = "Normal"
    else:
        sobrepeso += 1
        clasif = "Sobrepeso"

    print(f"Persona: {nombre} | IMC: {imc:.2f} | Clasificación: {clasif}")

# Informe de salud consolidado final del grupo evaluado
promedio_imc = suma_imc / n
print("\n--- Informe Grupal de Salud ---")
print(f"Cantidad bajo peso  : {bajo_peso}")
print(f"Cantidad peso normal: {normal}")
print(f"Cantidad sobrepeso  : {sobrepeso}")
print(f"Promedio de IMC del grupo: {promedio_imc:.2f}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Sistema de Evaluación de IMC Variable ---
¿Cuántas personas se evaluarán en el grupo?: 2

--- Persona 1 de 2 ---
Ingrese nombre de la persona: Diego
Ingrese peso en kilogramos de Diego (2.0 a 300.0 kg): 78.5
Ingrese estatura en metros de Diego (0.50 a 2.50 m): 1.76
Persona: Diego | IMC: 25.34 | Clasificación: Sobrepeso

--- Persona 2 de 2 ---
Ingrese nombre de la persona: Sofía
Ingrese peso en kilogramos de Sofía (2.0 a 300.0 kg): 54.2
Ingrese estatura en metros de Sofía (0.50 a 2.50 m): 1.62
Persona: Sofía | IMC: 20.65 | Clasificación: Normal
```
**Salida:**
```text
--- Informe Grupal de Salud ---
Cantidad bajo peso  : 0
Cantidad peso normal: 1
Cantidad sobrepeso  : 1
Promedio de IMC del grupo: 23.00
```
