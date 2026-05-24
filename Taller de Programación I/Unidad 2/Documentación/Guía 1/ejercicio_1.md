### Ejercicio 1: Identificador de Números Positivos, Negativos o Cero

#### Enunciado del Problema
Desarrolla un script que pida un número al usuario e identifique si el valor ingresado es positivo, negativo o cero.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `numero` | `float` | Almacena el número decimal o entero ingresado por el usuario para evaluar su signo. |

#### Lógica de la Solución
El algoritmo se basa en una estructura de control selectiva anidada o encadenada (`if-elif-else`). Antes de realizar la evaluación lógica, se implementa un bucle de validación (`while True`) combinado con una estructura de manejo de excepciones (`try-except`). Esto garantiza la robustez del programa, impidiendo interrupciones abruptas si el usuario ingresa texto en lugar de números. Una vez que se asegura un dato de tipo numérico flotante, se clasifica de la siguiente manera:
1. Si el número es estrictamente mayor que $0$, se clasifica como **positivo**.
2. Si el número es estrictamente menor que $0$, se clasifica como **negativo**.
3. Si no cumple ninguna de las anteriores (por descarte lógico), se define como **cero**.

#### Explicación Línea por Línea
* **Línea 3 (`while True:`):** Inicia un bucle de repetición infinito diseñado para insistir en la solicitud hasta que se ingrese un dato válido.
* **Línea 4 (`try:`):** Declara el bloque de prueba donde se intentará realizar una operación propensa a fallas (la conversión de texto a número flotante).
* **Línea 5 (`numero = float(input(...))`):** Captura la entrada del usuario como una cadena de caracteres, intenta convertirla a número real (`float`) y la asigna a la variable `numero`.
* **Línea 6 (`break`):** Si la línea anterior se ejecuta sin errores, se alcanza esta sentencia que rompe el ciclo iterativo inmediatamente.
* **Línea 7 (`except ValueError:`):** Bloque de rescate que se activa únicamente si la conversión a `float` falla (por ejemplo, si el usuario escribe letras).
* **Línea 8 (`print(...)`):** Muestra un mensaje educativo indicando que la entrada debe ser un número entero o decimal, permitiendo que el bucle vuelva a comenzar.
* **Línea 10 (`if numero > 0:`):** Evalúa la primera condición de paridad de orden para comprobar si el número se sitúa a la derecha del cero en la recta numérica.
* **Línea 11 (`print(...)`):** Imprime por consola que el valor es positivo mediante interpolación de cadenas o *f-string*.
* **Línea 12 (`elif numero < 0:`):** Si la condición inicial es falsa, evalúa si el número se sitúa a la izquierda del cero.
* **Línea 13 (`print(...)`):** Imprime un mensaje por consola informando que el número ingresado es negativo.
* **Línea 14 (`else:`):** Rama final por defecto que se ejecuta únicamente si las pruebas lógicas del `if` y `elif` fallaron (es decir, el número es $0$).
* **Línea 15 (`print(...)`):** Muestra por consola que el número es exactamente cero.

#### Código Completo
```python
# Identificador de números positivos, negativos o cero

while True:
    try:
        # Se solicita la entrada del usuario y se intenta convertir a flotante (decimal)
        numero = float(input("Ingrese un número: "))
        break  # Se rompe el bucle de validación si no hay excepciones
    except ValueError:
        # Manejo de error si la conversión a flotante falla
        print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Estructura condicional múltiple para determinar el signo
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Entrada de positivo):
* **Entrada esperada:** `15.5`
* **Salida del programa:** `El número 15.5 es positivo.`

##### Caso de Uso 2 (Entrada de negativo):
* **Entrada esperada:** `-9`
* **Salida del programa:** `El número -9.0 es negativo.`

##### Caso de Uso 3 (Entrada de cero):
* **Entrada esperada:** `0`
* **Salida del programa:** `El número es cero.`

##### Caso de Uso 4 (Entrada errónea y recuperación):
* **Entrada esperada:** `hola` (luego) `4`
* **Salida del programa:**
  ```text
  Entrada no válida. Por favor, ingrese un número decimal o entero.
  Ingrese un número: 4
  El número 4.0 es positivo.
  ```
