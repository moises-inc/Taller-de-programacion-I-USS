### Ejercicio 6: Clasificador de Temperatura Celsius

#### Enunciado del Problema
Desarrolla un script que pida una temperatura en grados Celsius y la clasifique como bajo cero, fría, templada o caliente. El estudiante debe definir explícitamente los rangos para cada categoría antes de programar la solución.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `temperatura` | `float` | Almacena el valor numérico real (entero o decimal) de la temperatura medida en grados Celsius (°C). |

#### Lógica de la Solución
El algoritmo está diseñado para procesar variables continuas en el dominio de los números reales. Dado que las temperaturas pueden tener valores decimales y signos negativos, la entrada se valida y formatea como `float` utilizando una estructura interactiva con captura de excepciones.
Los rangos lógicos definidos para las categorías climáticas son:
1. **Bajo cero:** $\text{Temperatura} < 0\text{ °C}$
2. **Fría:** $0\text{ °C} \le \text{Temperatura} < 15\text{ °C}$
3. **Templada:** $15\text{ °C} \le \text{Temperatura} < 30\text{ °C}$
4. **Caliente:** $\text{Temperatura} \ge 30\text{ °C}$

La clasificación se ejecuta mediante una estructura lógica selectiva encadenada (`if-elif-else`), donde las condiciones se evalúan en orden progresivo y excluyente.

#### Explicación Línea por Línea
* **Línea 5 (`print(...)`):** Despliega el encabezado informando el propósito del programa.
* **Línea 7 (`while True:`):** Declara el bucle de control para asegurar la validez del dato de entrada.
* **Línea 8 (`try:`):** Apertura de la zona segura de captura de errores aritméticos o de casteo.
* **Línea 9 (`temperatura = float(input(...))`):** Solicita y lee la temperatura, permitiendo números decimales y negativos gracias a la conversión a flotante (`float`).
* **Línea 10 (`break`):** Interrumpe la repetición del ciclo de captura cuando se comprueba el formato de entrada numérico.
* **Línea 11 (`except ValueError:`):** Captura el error de formato si la entrada es no numérica (ej: texto arbitrario).
* **Línea 12 (`print(...)`):** Muestra un mensaje correctivo de error por pantalla.
* **Línea 21 (`if temperatura < 0:`):** Evalúa si el valor es estrictamente inferior a $0$ para definirlo como "bajo cero".
* **Línea 22 (`print(...)`):** Imprime en consola la clasificación "bajo cero".
* **Línea 23 (`elif 0 <= temperatura < 15:`):** Si no es bajo cero, evalúa si se encuentra en el intervalo semiabierto $[0, 15)$ para catalogarla como "fría".
* **Línea 24 (`print(...)`):** Imprime que la temperatura es "fría".
* **Línea 25 (`elif 15 <= temperatura < 30:`):** Si falla lo anterior, evalúa si pertenece al intervalo $[15, 30)$ para categorizarla como "templada".
* **Línea 26 (`print(...)`):** Despliega la etiqueta "templada".
* **Línea 27 (`else:`):** Condición residual que abarca cualquier temperatura igual o superior a $30\text{ °C}$.
* **Línea 28 (`print(...)`):** Muestra por consola la etiqueta de temperatura "caliente".

#### Código Completo
```python
# Clasificador de temperatura Celsius

print("--- Clasificación de Temperatura ---")

while True:
    try:
        # Se lee y valida la temperatura como número decimal (float)
        temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
        break  # Se interrumpe el ciclo si la conversión a float fue exitosa
    except ValueError:
        # Control del error en caso de que ingresen strings o símbolos inválidos
        print("Entrada no válida. Por favor, ingrese un número.")

# Clasificación condicional secuencial según los rangos lógicos establecidos:
# - Bajo cero: Menos de 0°C
# - Frío: 0°C a 14.9°C
# - Templado: 15°C a 29.9°C
# - Caliente: 30°C o más
if temperatura < 0:
    print(f"La temperatura de {temperatura}°C es bajo cero.")
elif 0 <= temperatura < 15:
    print(f"La temperatura de {temperatura}°C es fría.")
elif 15 <= temperatura < 30:
    print(f"La temperatura de {temperatura}°C es templada.")
else:
    print(f"La temperatura de {temperatura}°C es caliente.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Bajo cero):
* **Entrada esperada:** `-4.2`
* **Salida del programa:** `La temperatura de -4.2°C es bajo cero.`

##### Caso de Uso 2 (Fría):
* **Entrada esperada:** `12`
* **Salida del programa:** `La temperatura de 12.0°C es fría.`

##### Caso de Uso 3 (Templada):
* **Entrada esperada:** `22.5`
* **Salida del programa:** `La temperatura de 22.5°C es templada.`

##### Caso de Uso 4 (Caliente):
* **Entrada esperada:** `35`
* **Salida del programa:** `La temperatura de 35.0°C es caliente.`

##### Caso de Uso 5 (Entrada no válida y recuperación):
* **Entrada esperada:** `templado` (luego) `18`
* **Salida del programa:**
  ```text
  Ingrese la temperatura en grados Celsius: templado
  Entrada no válida. Por favor, ingrese un número.
  Ingrese la temperatura en grados Celsius: 18
  La temperatura de 18.0°C es templada.
  ```
