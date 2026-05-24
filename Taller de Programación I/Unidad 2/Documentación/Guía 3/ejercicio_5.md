### Ejercicio 5: Monitoreo de niveles de oxígeno en centros de cultivo

#### Enunciado del Problema
En los centros de cultivo de salmones, el nivel de oxígeno disuelto en el agua es crítico para la supervivencia de los peces. Durante el día, un sensor registra mediciones periódicas.
Desarrolla un script en Python que permita analizar estas mediciones. El programa debe:
- Generar una lista con valores de oxígeno disuelto (puedes usar `random` en un rango entre 4.0 y 10.0 mg/L o ingresarlos manualmente).
- La cantidad de mediciones no es fija: el usuario debe indicar cuántas mediciones se registrarán.
- Mostrar:
    + El promedio de oxígeno (promedio = suma de mediciones / cantidad de mediciones).
    + Cuántas mediciones están bajo 5.0 mg/L (nivel crítico).
    + Cuántas están entre 5.0 y 7.0 mg/L (nivel aceptable).
    + Cuántas están sobre 7.0 mg/L (nivel óptimo).

Consideraciones:
- Debes usar un ciclo para generar o ingresar las mediciones (por ejemplo, un `while` o `for` según corresponda).
- Luego, debes recorrer la lista para realizar el análisis.
- Piensa cómo clasificar cada medición en su categoría correspondiente.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `mediciones_objetivo`| `int` | Cantidad total de mediciones que se registrarán en la jornada (indicado por el usuario). |
| `modo` | `int` | Modo de ingreso de datos del menú principal (1 para manual, 2 para automático). |
| `mediciones` | `list (float)` | Lista que almacena de forma ordenada las lecturas de oxígeno disuelto en mg/L. |
| `ox` | `float` | Representa de forma temporal la lectura de oxígeno disuelto evaluada. |
| `suma_ox` | `float` | Acumulador manual para almacenar la suma total de las lecturas registradas. |
| `critico` | `int` | Contador de mediciones ubicadas en el rango crítico (menores a 5.0 mg/L). |
| `aceptable` | `int` | Contador de mediciones ubicadas en el rango aceptable ($5.0 \le \text{ox} \le 7.0$ mg/L). |
| `optimo` | `int` | Contador de mediciones ubicadas en el rango óptimo (mayores a 7.0 mg/L). |
| `promedio` | `float` | Media aritmética calculada del total de mediciones de oxígeno disuelto. |

---

#### Lógica de la Solución
1. **Configuración de Muestra Dinámica:** El programa no limita el volumen de datos de la simulación. En primer lugar, se solicita el tamaño de muestra deseado `mediciones_objetivo` mediante una estructura iterativa de validación.
2. **Carga Estructurada de Datos (Modularidad):** El script expone un menú dual que llena la lista de forma robusta. Si es manual, restringe los valores a límites físicos posibles del sensor en piscifactorías (rango de 4.0 a 10.0 mg/L). Si es automático, utiliza `random.uniform()` limitado a dos decimales con `round()`.
3. **Clasificación por Intervalos Aritméticos:** Se procesan las lecturas recorriendo la colección mediante un ciclo `for`. En cada paso, se evalúan las condiciones excluyentes:
   - Menores a 5.0 mg/L: Rango Crítico.
   - Entre 5.0 y 7.0 mg/L (inclusive): Rango Aceptable.
   - Mayores a 7.0 mg/L: Rango Óptimo.
4. **Alerta Condicional en el Reporte:** Se genera una salida inteligente en consola que añade un mensaje de alerta dinámica `(¡Requiere aireación urgente!)` si se detecta al menos un registro en el nivel crítico.

---

#### Explicación Línea por Línea
- **Línea 3:** `import random`: Importa el generador pseudoaleatorio de Python.
- **Línea 7:** `while True:`: Garantiza la lectura correcta de la cantidad de mediciones.
- **Líneas 8 a 13:** `try-except ValueError`: Captura entradas que no sean enteros y valida que `mediciones_objetivo > 0`.
- **Líneas 16 y 17:** `print(...)`: Imprime en la consola el menú de carga.
- **Línea 19:** `while True:`: Garantiza la elección correcta de la opción del menú dual.
- **Líneas 20 a 26:** `try-except ValueError`: Captura excepciones y limita la opción a `1` o `2`.
- **Línea 28:** `mediciones = []`: Inicializa la lista vacía de lecturas del día.
- **Línea 30:** `if modo == 1:`: Ejecuta la captura manual.
- **Línea 31:** `for i in range(mediciones_objetivo):`: Itera tantas veces como cantidad de lecturas solicitó el usuario.
- **Línea 32:** `while True:`: Validador de rangos para la medición en curso.
- **Líneas 33 a 40:** `try-except ValueError`: Captura entradas no numéricas decimales e impone el rango industrial de oxígeno ($4.0 \le \text{ox} \le 10.0$ mg/L). Si es correcto, anexa la muestra con `append()` y rompe el ciclo interno.
- **Línea 41:** `else:`: Ejecuta la generación automática aleatoria.
- **Línea 42:** `for _ in range(mediciones_objetivo):`: Bucle finito iterativo automático.
- **Línea 43:** `mediciones.append(...)`: Genera valores flotantes entre 4.0 y 10.0 mediante `random.uniform()`, limita a 2 decimales y los agrega a la lista de muestras.
- **Línea 47:** `suma_ox = 0.0`: Inicializa a cero el acumulador del volumen de oxígeno.
- **Líneas 48 a 50:** `critico = 0`, `aceptable = 0` y `optimo = 0`: Inicializa los contadores de categorías.
- **Línea 52:** `for ox in mediciones:`: Recorre secuencialmente cada lectura decimal de la lista.
- **Línea 53:** `suma_ox += ox`: Acumula el valor de la muestra de forma iterativa.
- **Líneas 54 a 59:** `if-elif-else`: Evalúa por rangos excluyentes e incrementa la categoría correspondiente de forma manual.
- **Línea 61:** `promedio = suma_ox / len(mediciones)`: Calcula la media general del oxígeno.
- **Líneas 64 a 69:** `print(...)`: Formatea e imprime las estadísticas consolidadas. Utiliza un operador ternario para concatenar el mensaje `(¡Requiere aireación urgente!)` en caso de que `critico > 0`.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Monitoreo y Análisis de Oxigenación Ambiental (Piscifactorías)
# ==============================================================================
import random

print("--- Sensor de Oxígeno Disuelto ---")

# Solicitar de forma dinámica el número de muestras del día
while True:
    try:
        mediciones_objetivo = int(input("¿Cuántas mediciones de oxígeno desea registrar hoy?: "))
        if mediciones_objetivo > 0:
            break
        print("Debe registrar al menos una medición.")
    except ValueError:
        print("Ingrese un número entero válido.")

print("\n1. Ingresar mediciones manualmente")
print("2. Generar mediciones automáticamente (Aleatorio entre 4.0 y 10.0 mg/L)")

# Validar opción del menú operativo
while True:
    try:
        modo = int(input("Seleccione su opción (1 o 2): "))
        if modo in [1, 2]:
            break
        print("Opción inválida. Seleccione 1 o 2.")
    except ValueError:
        print("Por favor, ingrese un número entero.")

mediciones = []

# Carga de datos
if modo == 1:
    for i in range(mediciones_objetivo):
        while True:
            try:
                ox = float(input(f"Nivel de oxígeno medición {i+1} (4.0 a 10.0 mg/L): "))
                if 4.0 <= ox <= 10.0:
                    mediciones.append(ox)
                    break
                print("Lectura fuera de la escala del barómetro de oxígeno (4.0 a 10.0 mg/L).")
            except ValueError:
                print("Ingrese un valor numérico decimal.")
else:
    for _ in range(mediciones_objetivo):
        mediciones.append(round(random.uniform(4.0, 10.0), 2))
    print(f"\n{mediciones_objetivo} mediciones generadas de forma automática.")

# Algoritmo de clasificación por rangos biológicos (Evitando sum())
suma_ox = 0.0
critico = 0
aceptable = 0
optimo = 0

for ox in mediciones:
    suma_ox += ox
    if ox < 5.0:
        critico += 1
    elif ox <= 7.0:
        aceptable += 1
    else:
        optimo += 1

promedio = suma_ox / len(mediciones)

# Impresión del Reporte Consolidado
print("\n--- Análisis de Estado de Oxigenación ---")
print(f"Mediciones obtenidas: {mediciones}")
print(f"Oxígeno Promedio de la jornada: {promedio:.2f} mg/L")
# Alerta de emergencia dinámica mediante evaluación lógica en línea
alerta_critica = " (¡Requiere aireación urgente!)" if critico > 0 else ""
print(f"Mediciones en Nivel Crítico (<5.0 mg/L)    : {critico}{alerta_critica}")
print(f"Mediciones en Nivel Aceptable (5.0 a 7.0 mg/L): {aceptable}")
print(f"Mediciones en Nivel Óptimo (>7.0 mg/L)      : {optimo}")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Lecturas en Niveles Óptimos (Carga Aleatoria)
```text
--- Sensor de Oxígeno Disuelto ---
¿Cuántas mediciones de oxígeno desea registrar hoy?: 5

1. Ingresar mediciones manualmente
2. Generar mediciones automáticamente (Aleatorio entre 4.0 y 10.0 mg/L)
Seleccione su opción (1 o 2): 2

5 mediciones generadas de forma automática.

--- Análisis de Estado de Oxigenación ---
Mediciones obtenidas: [7.85, 8.12, 6.9, 7.22, 9.01]
Oxígeno Promedio de la jornada: 7.82 mg/L
Mediciones en Nivel Crítico (<5.0 mg/L)    : 0
Mediciones en Nivel Aceptable (5.0 a 7.0 mg/L): 1
Mediciones en Nivel Óptimo (>7.0 mg/L)      : 4
```

##### Caso 2: Alerta por Nivel Crítico (Carga Manual)
```text
--- Sensor de Oxígeno Disuelto ---
¿Cuántas mediciones de oxígeno desea registrar hoy?: 3

1. Ingresar mediciones manualmente
2. Generar mediciones automáticamente (Aleatorio entre 4.0 y 10.0 mg/L)
Seleccione su opción (1 o 2): 1
Nivel de oxígeno medición 1 (4.0 a 10.0 mg/L): 4.2
Nivel de oxígeno medición 2 (4.0 a 10.0 mg/L): 6.8
Nivel de oxígeno medición 3 (4.0 a 10.0 mg/L): 3.5
Lectura fuera de la escala del barómetro de oxígeno (4.0 a 10.0 mg/L).
Nivel de oxígeno medición 3 (4.0 a 10.0 mg/L): 5.1

--- Análisis de Estado de Oxigenación ---
Mediciones obtenidas: [4.2, 6.8, 5.1]
Oxígeno Promedio de la jornada: 5.37 mg/L
Mediciones en Nivel Crítico (<5.0 mg/L)    : 1 (¡Requiere aireación urgente!)
Mediciones en Nivel Aceptable (5.0 a 7.0 mg/L): 2
Mediciones en Nivel Óptimo (>7.0 mg/L)      : 0
```
