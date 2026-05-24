### Ejercicio 3: Identificador de Números Mayores, Menores o Iguales

#### Enunciado del Problema
Desarrolla un script que pida dos números al usuario y determine cuál de ellos es mayor, o bien indique si ambos son iguales.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `numero1` | `float` | Almacena el primer valor numérico real ingresado por el usuario para la comparación. |
| `numero2` | `float` | Almacena el segundo valor numérico real ingresado por el usuario para la comparación. |

#### Lógica de la Solución
El algoritmo soluciona el problema de la comparación binaria mediante una estructura selectiva anidada (`if-elif-else`).
Previamente, se unifican las validaciones numéricas en un único ciclo `try-except` interactivo para asegurar que ambos valores sean compatibles con la aritmética de números de punto flotante (`float`). 
La lógica de comparación evalúa las tres posibilidades mutuamente excluyentes en la relación de orden de los números reales:
1. Si el primer número es estrictamente mayor que el segundo.
2. Si el primer número es estrictamente menor que el segundo.
3. Si los valores de ambos números son equivalentes (iguales).

#### Explicación Línea por Línea
* **Línea 3 (`while True:`):** Declara el bucle de control iterativo para blindar la entrada de datos.
* **Línea 4 (`try:`):** Establece el inicio del bloque de comprobación de tipos de datos.
* **Línea 5 (`numero1 = float(input(...))`):** Captura el primer dato entrante y lo convierte a punto flotante.
* **Línea 6 (`numero2 = float(input(...))`):** Captura el segundo dato entrante y lo convierte a punto flotante. Si alguna de las dos conversiones falla, el control salta inmediatamente a la línea 8.
* **Línea 7 (`break`):** Interrumpe de manera definitiva el ciclo de validación al confirmarse que ambos ingresos de datos son numéricos válidos.
* **Línea 8 (`except ValueError:`):** Atrapa el error en caso de que alguna entrada no sea interpretable numéricamente.
* **Línea 9 (`print(...)`):** Muestra un error explicativo solicitando el reingreso de ambos parámetros.
* **Línea 11 (`if numero1 > numero2:`):** Compara mediante el operador mayor qué (`>`) si el valor de `numero1` supera al de `numero2`.
* **Línea 12 (`print(...)`):** Imprime en pantalla que el primer número es mayor que el segundo.
* **Línea 13 (`elif numero1 < numero2:`):** Evalúa mediante el operador menor qué (`<`) si el primer número es menor que el segundo.
* **Línea 14 (`print(...)`):** Despliega el mensaje indicando que el primer número es menor.
* **Línea 15 (`else:`):** Flujo de escape lógico que se activa cuando no se cumplen las condiciones de mayor o menor (lo que garantiza la estricta igualdad matemática).
* **Línea 16 (`print(...)`):** Muestra un mensaje detallado señalando la igualdad y el valor compartido por ambas variables.

#### Código Completo
```python
# Identificador de números mayores, menores o iguales

while True:
    try:
        # Validación unificada de entradas numéricas de punto flotante
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        break  # Se interrumpe el ciclo si ambos valores son válidos
    except ValueError:
        # Se activa si cualquiera de las dos conversiones lanza excepción
        print("Entrada no válida. Por favor, ingrese valores numéricos.")

# Estructura selectiva anidada para resolver la tricotomía de números reales
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"El número {numero1} es menor que {numero2}.")
else:
    print(f"Ambos números son iguales ({numero1}).")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Primer número mayor):
* **Entrada esperada:** `12.4` (primer número), `5.1` (segundo número)
* **Salida del programa:** `El número 12.4 es mayor que 5.1.`

##### Caso de Uso 2 (Segundo número mayor):
* **Entrada esperada:** `-3` (primer número), `7.2` (segundo número)
* **Salida del programa:** `El número -3.0 es menor que 7.2.`

##### Caso de Uso 3 (Números iguales):
* **Entrada esperada:** `42` (primer número), `42.0` (segundo número)
* **Salida del programa:** `Ambos números son iguales (42.0).`

##### Caso de Uso 4 (Error inicial y reintento):
* **Entrada esperada:** `diez` (primer número), `5` (segundo número) -> *Error* -> `10` y `5`
* **Salida del programa:**
  ```text
  Ingrese el primer número: diez
  Entrada no válida. Por favor, ingrese valores numéricos.
  Ingrese el primer número: 10
  Ingrese el segundo número: 5
  El número 10.0 es mayor que 5.0.
  ```
