### Ejercicio 4: Identificador de Múltiplos con Prevención de División por Cero

#### Enunciado del Problema
Desarrolla un script que pida dos números enteros al usuario e indique si el primer número es múltiplo del segundo, utilizando el operador módulo (`%`).

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `numero` | `int` | Representa el dividendo. Es el primer número entero ingresado para evaluar su divisibilidad. |
| `multiplo` | `int` | Representa el divisor. Es el segundo número entero ingresado y con respecto al cual se determina la multiplicidad (debe ser $\ne 0$). |

#### Lógica de la Solución
Matemáticamente, un número entero $A$ es múltiplo de otro número entero $B$ si el residuo de la división entera $A / B$ es exactamente $0$. En Python, esto se evalúa mediante la expresión booleana `numero % multiplo == 0`.
Sin embargo, esta operación aritmética posee una restricción crítica: **el divisor ($B$) no puede ser cero ($0$)**, debido a que la división por cero está matemáticamente indefinida y causaría un error fatal en tiempo de ejecución (`ZeroDivisionError`).
Por lo tanto, el diseño lógico de este algoritmo implementa:
1. Un bucle de validación externo (`while True`) con estructura `try-except` para garantizar el ingreso estricto de enteros (`int`).
2. Un bucle de validación interno anidado que impide que la variable `multiplo` tome el valor de $0$, forzando al usuario a reingresar un divisor válido antes de avanzar a la comparación condicional final.

#### Explicación Línea por Línea
* **Línea 3 (`while True:`):** Declara el bucle de control externo para asegurar la captura de números válidos.
* **Línea 4 (`try:`):** Apertura de la zona segura para el manejo de excepciones numéricas.
* **Línea 5 (`numero = int(input(...))`):** Captura el dividendo y lo fuerza a ser un entero de Python.
* **Línea 6 (`while True:`):** Inicia un bucle interno dedicado exclusivamente a garantizar que el divisor sea distinto de cero.
* **Línea 7 (`multiplo = int(input(...))`):** Solicita el divisor e intenta guardarlo como entero en `multiplo`.
* **Línea 8 (`if multiplo == 0:`):** Evalúa si el usuario cometió la infracción de ingresar un divisor igual a $0$.
* **Línea 9 (`print(...)`):** Muestra un mensaje detallado explicando por qué el cero no es un divisor matemáticamente válido.
* **Línea 10 (`else:`):** Rama ejecutada si el divisor es distinto de $0$.
* **Línea 11 (`break`):** Rompe únicamente el bucle interno de validación del divisor.
* **Línea 12 (`break`):** Rompe el bucle externo de entrada de datos generales una vez que el dividendo y divisor son válidos.
* **Línea 13 (`except ValueError:`):** Atrapa ingresos no válidos (por ejemplo, textos o números decimales) en cualquiera de las solicitudes.
* **Línea 14 (`print(...)`):** Explica didácticamente el error y reinicia el proceso de ingreso desde el dividendo.
* **Línea 16 (`if numero % multiplo == 0:`):** Calcula el residuo mediante módulo (`%`). Si es $0$, concluye que es múltiplo.
* **Línea 17 (`print(...)`):** Despliega el resultado afirmativo.
* **Línea 18 (`else:`):** Si el residuo de la división es diferente de $0$, concluye que no hay relación de multiplicidad exacta.
* **Línea 19 (`print(...)`):** Muestra por pantalla el resultado negativo.

#### Código Completo
```python
# Identificador de múltiplos con prevención de división por cero

while True:
    try:
        # Captura de datos inicial con validación estricta de enteros
        numero = int(input("Ingrese el primer número entero: "))
        
        # Bucle de seguridad para evitar ZeroDivisionError
        while True:
            multiplo = int(input("Ingrese el segundo número entero (distinto de 0): "))
            if multiplo == 0:
                print("El divisor no puede ser cero ya que causará un error matemático. Intente de nuevo.")
            else:
                break  # Sale del bucle de validación del divisor
        break  # Sale del bucle general de captura
    except ValueError:
        print("Entrada no válida. Por favor, ingrese números enteros válidos.")

# Comprobación de multiplicidad usando el operador módulo (%)
if numero % multiplo == 0:
    print(f"El número {numero} es múltiplo de {multiplo}.")
else:
    print(f"El número {numero} no es múltiplo de {multiplo}.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Es múltiplo):
* **Entrada esperada:** `15` (primer número), `5` (segundo número)
* **Salida del programa:** `El número 15 es múltiplo de 5.`

##### Caso de Uso 2 (No es múltiplo):
* **Entrada esperada:** `10` (primer número), `3` (segundo número)
* **Salida del programa:** `El número 10 no es múltiplo de 3.`

##### Caso de Uso 3 (Prevención de divisor cero):
* **Entrada esperada:** `20` (primer número), `0` (segundo número) -> *Rechazado* -> `4`
* **Salida del programa:**
  ```text
  Ingrese el primer número entero: 20
  Ingrese el segundo número entero (distinto de 0): 0
  El divisor no puede ser cero ya que causará un error matemático. Intente de nuevo.
  Ingrese el segundo número entero (distinto de 0): 4
  El número 20 es múltiplo de 4.
  ```
