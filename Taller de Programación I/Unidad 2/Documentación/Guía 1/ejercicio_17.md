### Ejercicio 17: Calculadora Aritmética Interactiva

#### Enunciado del Problema
Desarrolla un script que pida dos números al usuario y luego solicite una operación matemática entre las siguientes opciones: `+`, `-`, `*`, `/`.
El programa debe mostrar el resultado de aplicar la operación seleccionada a ambos números. En caso de división, debe evitar dividir por cero.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `n1` | `float` | Almacena el primer operando real (decimal o entero) de la operación. |
| `n2` | `float` | Almacena el segundo operando real (decimal o entero) de la operación. |
| `operaciones_validas` | `list` | Colección indexada que contiene los caracteres admisibles como operadores matemáticos. |
| `operacion` | `str` | Almacena la operación matemática elegida por el usuario (sanitizada). |
| `resultado` | `float` o `str` | Almacena el valor numérico obtenido o, en su defecto, la cadena de advertencia ante división por cero. |

#### Lógica de la Solución
El algoritmo soluciona de forma interactiva y segura la ejecución de las cuatro operaciones básicas de la aritmética. En el diseño de sistemas de cálculo digital, **el control preventivo de errores aritméticos** es de máxima prioridad. Si el usuario ingresa un divisor igual a $0$ para la operación de cociente (`/`), el sistema colapsará con un error del sistema de tipo `ZeroDivisionError`. 

Para evitar este comportamiento indeseado:
1. Se capturan y validan los operandos (`n1` y `n2`) como números reales (`float`).
2. Se pide y valida el operador matemático comprobando su existencia en la lista `["+", "-", "*", "/"]`.
3. Al procesar la división, se evalúa preventivamente si el segundo operando (`n2`) es exactamente igual a $0.0$. Si la condición es verdadera, se asigna a `resultado` un mensaje descriptivo controlado. En caso contrario, se efectúa la división de forma regular.

#### Explicación Línea por Línea
* **Línea 5 (`while True:`):** Bucle infinito de control para asegurar que los operandos sean numéricos.
* **Línea 6 (`try:`):** Apertura de la zona protegida de conversión decimal.
* **Línea 7 (`n1 = float(input(...))`):** Captura el primer número como flotante.
* **Línea 8 (`n2 = float(input(...))`):** Captura el segundo número como flotante. Si ocurre una excepción en cualquiera de los dos ingresos, salta a la línea 10.
* **Línea 9 (`break`):** Rompe la iteración al obtener ambos operandos válidos.
* **Línea 10 (`except ValueError:`):** Atrapa ingresos no numéricos.
* **Línea 11 (`print(...)`):** Muestra mensaje aclaratorio.
* **Línea 13 (`operaciones_validas = [...]`):** Lista con los caracteres autorizados para efectuar operaciones.
* **Línea 14 (`while True:`):** Bucle para la validación estricta del operador.
* **Línea 15 (`operacion = input(...).strip()`):** Lee el operador matemático removiendo espacios vacíos.
* **Línea 16 (`if operacion in operaciones_validas:`):** Evalúa si el carácter forma parte de la lista autorizada.
* **Línea 17 (`break`):** Rompe el bucle de validación de operador.
* **Línea 18 (`else:`):** Rama si ingresa un operador ajeno a las opciones.
* **Línea 19 (`print(...)`):** Informa acerca de los caracteres aceptados.
* **Líneas 22-29 (`if-elif-else`):** Ejecuta la bifurcación lógica según el operador seleccionado:
  * Si es `"+"`, `resultado = n1 + n2`.
  * Si es `"-"`, `resultado = n1 - n2`.
  * Si es `"*"`, `resultado = n1 * n2`.
  * Si es `"/"`, evalúa de forma preventiva si `n2 == 0`. En caso afirmativo, le asigna a `resultado` la cadena descriptiva de la indefinición matemática. En caso negativo, efectúa la división regular.
* **Línea 31 (`print(...)`):** Despliega el resultado formateado de la operación por pantalla.

#### Código Completo
```python
# Calculadora Interactiva con control de errores

print("--- Calculadora Aritmética Interactiva ---")

# Bucle interactivo para la captura y validación de operandos
while True:
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, ingrese valores numéricos.")

# Bucle interactivo para la validación estricta de operadores
operaciones_validas = ["+", "-", "*", "/"]
while True:
    operacion = input("Seleccione la operación (+, -, *, /): ").strip()
    if operacion in operaciones_validas:
        break
    else:
        print("Operador no válido. Ingrese exclusivamente uno de estos caracteres: +, -, *, /")

# Ejecución aritmética condicional y control preventivo de división por cero
if operacion == "+":
    resultado = n1 + n2
elif operacion == "-":
    resultado = n1 - n2
elif operacion == "*":
    resultado = n1 * n2
else:  # operacion == "/"
    if n2 == 0:
        resultado = "Error: Indefinición matemática (No se puede dividir por cero)"
    else:
        resultado = n1 / n2

# Salida del resultado
print(f"\nResultado de la operación ({n1} {operacion} {n2}): {resultado}")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Multiplicación decimal):
* **Entrada esperada:** `4.5` (n1), `2` (n2), `*` (operador)
* **Salida del programa:** `Resultado de la operación (4.5 * 2.0): 9.0`

##### Caso de Uso 2 (División regular):
* **Entrada esperada:** `15` (n1), `3` (n2), `/` (operador)
* **Salida del programa:** `Resultado de la operación (15.0 / 3.0): 5.0`

##### Caso de Uso 3 (Prevención de división por cero):
* **Entrada esperada:** `20` (n1), `0` (n2), `/` (operador)
* **Salida del programa:** `Resultado de la operación (20.0 / 0.0): Error: Indefinición matemática (No se puede dividir por cero)`

##### Caso de Uso 4 (Errores de entrada y resolución):
* **Entrada esperada:** `hola` (n1) -> *Error* -> `10` y `2`, `&` (operador) -> *Error* -> `+` (operador)
* **Salida del programa:**
  ```text
  Ingrese el primer número: hola
  Entrada no válida. Por favor, ingrese valores numéricos.
  Ingrese el primer número: 10
  Ingrese el segundo número: 2
  Seleccione la operación (+, -, *, /): &
  Operador no válido. Ingrese exclusivamente uno de estos caracteres: +, -, *, /
  Seleccione la operación (+, -, *, /): +
  
  Resultado de la operación (10.0 + 2.0): 12.0
  ```
