### Ejercicio 13: Comparación Avanzada de Tres Números

#### Enunciado del Problema
Desarrolla un script que pida tres números al usuario y determine cuál de ellos es el mayor. Si existen números iguales, el programa también debe indicarlo.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `num1` | `float` | Almacena el primer valor numérico de punto flotante ingresado por el usuario. |
| `num2` | `float` | Almacena el segundo valor numérico de punto flotante ingresado por el usuario. |
| `num3` | `float` | Almacena el tercer valor numérico de punto flotante ingresado por el usuario. |
| `mayor` | `float` | Almacena la cifra máxima identificada mediante la función incorporada de Python `max()`. |
| `menor` | `float` | Almacena la cifra mínima identificada mediante la función incorporada de Python `min()`. |
| Parámetro: `posicion` | `str` | Argumento de función que denota el orden en que se pide el número ("primer", "segundo", "tercer"). |

#### Lógica de la Solución
El algoritmo aborda la comparación de múltiples variables aplicando el principio fundamental **DRY**. En lugar de copiar y pegar el bloque de código de entrada interactiva y manejo de excepciones de tipo `ValueError` tres veces seguidas (como ocurría en la solución original rudimentaria), esta implementación define una función modular reutilizable llamada `solicitar_numero(posicion)`.

Una vez capturados con seguridad los tres valores numéricos, la lógica opera de la siguiente manera:
1. **Identificación de Extremos:** Utiliza de forma nativa las funciones optimizadas de Python `max(a, b, c)` y `min(a, b, c)` para extraer de inmediato los números mayor y menor respectivamente, evitando estructuras complejas de condicionales anidados.
2. **Evaluación de Congruencia (Igualdades):** Mediante comparaciones booleanas selectivas, determina el nivel de igualdad:
   * **Tricotomía idéntica:** Si todos son iguales (`num1 == num2 == num3`).
   * **Duplicidad parcial:** Si al menos dos son iguales (`num1 == num2` o `num1 == num3` o `num2 == num3`).
   * **Diversidad total:** Si ninguna igualdad se cumple, significa que todos los valores son distintos.

#### Explicación Línea por Línea
* **Línea 5 (`def solicitar_numero(posicion):`):** Declara una función local parametrizada por el orden de solicitud del número.
* **Línea 6 (`while True:`):** Declara el bucle de repetición de control de entrada para la función modular.
* **Línea 7 (`try:`):** Apertura de la zona de captura segura de la función.
* **Línea 8 (`return float(input(...))`):** Solicita la entrada usando interpolación de la variable `posicion`, la convierte a flotante (`float`) y la retorna inmediatamente, lo que corta la iteración e informa el valor exitosamente.
* **Línea 9 (`except ValueError:`):** Atrapa ingresos no numéricos.
* **Línea 10 (`print(...)`):** Explica didácticamente el error y repite la iteración del número en cuestión.
* **Líneas 12-14 (`num1`, `num2`, `num3`):** Llamadas consecutivas a la función `solicitar_numero()` pasando los textos descriptivos correspondientes.
* **Línea 16 (`mayor = max(...)`):** Determina de forma nativa e integrada el máximo de los tres valores asignados.
* **Línea 17 (`menor = min(...)`):** Determina el mínimo.
* **Líneas 20-25 (`if-elif-else`):** Evalúa el grado de igualdad de los tres números analizados para imprimir un resumen detallado del escenario.
* **Líneas 27-28 (`print(...)`):** Despliega de forma limpia por consola las magnitudes extremas calculadas.

#### Código Completo
```python
# Comparador de tres números (Optimizado con función reutilizable)

print("--- Comparación Avanzada de 3 Números ---")

# Definición de función reutilizable bajo principio DRY
def solicitar_numero(posicion):
    while True:
        try:
            return float(input(f"Ingrese el {posicion} número: "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Capturas modulares de datos
num1 = solicitar_numero("primer")
num2 = solicitar_numero("segundo")
num3 = solicitar_numero("tercer")

# Cálculo eficiente de extremos
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Verificación condicional de redundancia e igualdades
print(f"\n--- Análisis de Resultados ---")
if num1 == num2 == num3:
    print("Información: Los tres números ingresados son exactamente iguales.")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Información: Hay dos números que son iguales entre sí.")
else:
    print("Información: Todos los números ingresados son diferentes.")

# Despliegue de extremos
print(f"Número Mayor: {mayor}")
print(f"Número Menor: {menor}")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Todos distintos):
* **Entrada esperada:** `12.5` (primer), `9.1` (segundo), `45` (tercer)
* **Salida del programa:**
  ```text
  --- Análisis de Resultados ---
  Información: Todos los números ingresados son diferentes.
  Número Mayor: 45.0
  Número Menor: 9.1
  ```

##### Caso de Uso 2 (Dos iguales):
* **Entrada esperada:** `8` (primer), `8` (segundo), `5` (tercer)
* **Salida del programa:**
  ```text
  --- Análisis de Resultados ---
  Información: Hay dos números que son iguales entre sí.
  Número Mayor: 8.0
  Número Menor: 5.0
  ```

##### Caso de Uso 3 (Tres iguales):
* **Entrada esperada:** `7.7` (primer), `7.7` (segundo), `7.7` (tercer)
* **Salida del programa:**
  ```text
  --- Análisis de Resultados ---
  Información: Los tres números ingresados son exactamente iguales.
  Número Mayor: 7.7
  Número Menor: 7.7
  ```

##### Caso de Uso 4 (Error inicial y reintento modular):
* **Entrada esperada:** `hola` (primer) -> *Error* -> `10`, `cinco` (segundo) -> *Error* -> `5`, `3` (tercer)
* **Salida del programa:**
  ```text
  Ingrese el primer número: hola
  Entrada no válida. Por favor, ingrese un número decimal o entero.
  Ingrese el primer número: 10
  Ingrese el segundo número: cinco
  Entrada no válida. Por favor, ingrese un número decimal o entero.
  Ingrese el segundo número: 5
  Ingrese el tercer número: 3
  
  --- Análisis de Resultados ---
  Información: Todos los números ingresados son diferentes.
  Número Mayor: 10.0
  Número Menor: 3.0
  ```
