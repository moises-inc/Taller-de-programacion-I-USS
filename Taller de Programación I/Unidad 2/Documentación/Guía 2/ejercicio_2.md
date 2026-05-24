### Ejercicio 2: Identificador de par o impar

#### Enunciado del Problema
Desarrolla un script que pida un número entero al usuario e identifique si es par o impar utilizando el operador módulo (%).

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `numero` | `int` | Almacena el número entero ingresado por el usuario para verificar su paridad. |


## Lógica de la Solución
El algoritmo determina la paridad de un número entero basándose en el operador de residuo aritmético módulo (`%`). En matemáticas, un número es par si es divisible exactamente entre 2 (deja residuo cero) e impar en caso contrario (deja residuo uno). El script solicita al usuario un número entero y valida la entrada con un bloque `try-except` para prevenir caídas ante ingresos alfanuméricos. Luego, aplica la operación `numero % 2` y evalúa mediante una estructura condicional `if-else` si el resultado es igual a cero para reportar el estado.

## Explicación Línea por Línea
- **`while True:`**: Inicia el bucle de validación iterativo para asegurar la obtención de un dato correcto.
- **`try:`**: Abre el bloque de prueba para capturar errores de tipo de datos al realizar la conversión.
- **`numero = int(input("Ingrese un número entero: "))`**: Solicita la entrada por teclado, intenta forzar su conversión a tipo entero (`int`) y la guarda en la variable `numero`.
- **`break`**: Sale del bucle de captura si la conversión a entero fue exitosa sin lanzar excepciones.
- **`except ValueError:`**: Captura la excepción `ValueError` en caso de que la entrada contenga caracteres no válidos para representar un entero (como letras o decimales con punto).
- **`print("Entrada no válida...")`**: Informa al usuario que debe suministrar un número entero de forma exclusiva.
- **`if numero % 2 == 0:`**: Evalúa si el residuo de dividir `numero` entre 2 es exactamente igual a cero utilizando el operador módulo `%`.
- **`print(f"El número {numero} es par.")`**: Se ejecuta si la condición del `if` es verdadera, imprimiendo que el número tiene naturaleza par.
- **`else:`**: Bloque que se ejecuta por defecto si el residuo evaluado es diferente de cero (es decir, el número es impar).
- **`print(f"El número {numero} es impar.")`**: Se ejecuta en el bloque `else`, informando al usuario que el número es impar.


#### Código Completo
```python
while True:
    try:
        # Solicita la entrada del usuario y la convierte a número entero
        numero = int(input("Ingrese un número entero: "))
        break  # Sale del bucle si la conversión es exitosa
    except ValueError:
        # Captura el error si el valor ingresado no es un número entero entero
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Determinación de paridad usando el operador módulo %
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese un número entero: 14.5
Entrada no válida. Por favor, ingrese un número entero.
Ingrese un número entero: 27
```
**Salida:**
```text
El número 27 es impar.
```
