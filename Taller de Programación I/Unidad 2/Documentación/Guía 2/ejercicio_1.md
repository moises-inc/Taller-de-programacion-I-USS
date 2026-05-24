### Ejercicio 1: Identificador de números positivos, negativos o cero

#### Enunciado del Problema
Desarrolla un script que pida un número al usuario e identifique si el valor ingresado es positivo, negativo o cero.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `numero` | `float` | Almacena el valor numérico decimal ingresado por el usuario para ser analizado. |


## Lógica de la Solución
El algoritmo solicita un número al usuario y lo clasifica comparándolo con cero. Para lograr esto de forma robusta, se implementa una estructura de control de excepciones `try-except` dentro de un ciclo infinito `while True`. De este modo, si el usuario ingresa un dato no numérico (por ejemplo, texto), el programa no se interrumpe abruptamente con un error, sino que captura el fallo y vuelve a solicitar el dato de forma indefinida hasta recibir una entrada numérica válida. Posteriormente, utiliza bifurcaciones condicionales lógicas mediante `if`, `elif` y `else` para evaluar si el número es mayor que cero (positivo), menor que cero (negativo) o igual a cero (cero).

## Explicación Línea por Línea
- **`while True:`**: Inicia un bucle infinito que continuará iterando hasta que se ejecute la instrucción de interrupción `break`. Se utiliza para forzar al usuario a ingresar una entrada válida.
- **`try:`**: Define un bloque de prueba de excepciones. Python intentará ejecutar las instrucciones dentro de este bloque, derivando el flujo al bloque `except` si ocurre un error.
- **`numero = float(input("Ingrese un número: "))`**: Solicita una entrada al usuario mediante `input()`, la convierte a un número de punto flotante (`float`) y la asigna a la variable `numero`. Si la conversión falla, se levanta una excepción `ValueError`.
- **`break`**: Interrumpe y sale del bucle `while True`. Esta línea solo se ejecuta si la línea anterior no genera ninguna excepción (es decir, el dato ingresado es un número válido).
- **`except ValueError:`**: Captura la excepción de tipo `ValueError` que se produce si el usuario ingresa un texto o caracteres no numéricos que la función `float()` no puede procesar.
- **`print("Entrada no válida...")`**: Muestra un mensaje de advertencia indicando al usuario que la entrada no es un número válido, invitándolo a intentarlo nuevamente en la próxima iteración del ciclo.
- **`if numero > 0:`**: Evalúa si el valor de `numero` es estrictamente mayor que cero. Si se cumple, ejecuta la instrucción de impresión correspondiente.
- **`print(f"El número {numero} es positivo.")`**: Muestra en consola un mensaje informando que el número es positivo mediante formato de cadenas (f-strings).
- **`elif numero < 0:`**: Evalúa una condición alternativa que solo se procesa si la anterior resultó falsa. Verifica si el número es estrictamente menor que cero.
- **`print(f"El número {numero} es negativo.")`**: Informa que el número es negativo si se cumple la condición del `elif`.
- **`else:`**: Bloque por defecto que se ejecuta únicamente si todas las condiciones anteriores (`if` y `elif`) resultaron falsas, lo que por exclusión matemática implica que el número es cero.
- **`print("El número es cero.")`**: Muestra en consola que el número ingresado corresponde exactamente al valor cero.


#### Código Completo
```python
while True:
    try:
        # Solicita la entrada del usuario y la convierte a número decimal
        numero = float(input("Ingrese un número: "))
        break  # Sale del bucle si la conversión es exitosa
    except ValueError:
        # Captura el error si el valor ingresado no es numérico
        print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Clasificación del número mediante condiciones lógicas
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print("El número es cero.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese un número: hola
Entrada no válida. Por favor, ingrese un número decimal o entero.
Ingrese un número: -8.5
```
**Salida:**
```text
El número -8.5 es negativo.
```
