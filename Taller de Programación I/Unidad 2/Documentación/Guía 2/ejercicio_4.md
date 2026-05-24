### Ejercicio 4: Identificador de múltiplos

#### Enunciado del Problema
Desarrolla un script que pida dos números enteros al usuario e indique si el primer número es múltiplo del segundo, utilizando el operador módulo (%).

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `numero` | `int` | El número entero base que será evaluado como posible múltiplo. |
| `multiplo` | `int` | El número entero divisor contra el cual se evaluará la relación de divisibilidad. |


## Lógica de la Solución
Para que un número $A$ sea múltiplo de $B$, la división entera de $A / B$ debe ser exacta, es decir, el residuo de la operación debe ser cero. Esto se evalúa empleando la expresión lógica `numero % multiplo == 0`. Sin embargo, existe un peligro matemático latente: si el usuario ingresa un divisor igual a cero ($B=0$), el intérprete de Python lanzará un error fatal de ejecución llamado `ZeroDivisionError`. Por lo tanto, el script incorpora una doble validación: 1. Captura de números enteros válidos con `try-except`.2. Un ciclo anidado de validación lógica `while True` exclusivo para la variable `multiplo` que rechaza activamente el valor 0.

## Explicación Línea por Línea
- **`while True:`**: Ciclo externo que controla la captura y validación sintáctica de los datos de entrada de todo el bloque.
- **`try:`**: Prepara la captura de excepciones para las conversiones a enteros.
- **`numero = int(input("Ingrese el primer número..."))`**: Solicita y convierte a entero el dividendo, guardándolo en la variable `numero`.
- **`while True:`**: Inicia un ciclo de validación interno dedicado en exclusiva a garantizar un divisor seguro.
- **`multiplo = int(input("Ingrese el segundo..."))`**: Solicita y convierte a entero el divisor (multiplo) dentro del bucle de seguridad.
- **`if multiplo == 0:`**: Evalúa si el divisor es matemáticamente inválido por ser igual a cero.
- **`print("El divisor no puede ser cero...")`**: Muestra un mensaje de advertencia y exige un nuevo ingreso al no interrumpir el ciclo interno.
- **`else:`**: Bloque que se ejecuta si el divisor es distinto de cero y por ende seguro.
- **`break`**: Rompe el ciclo interno de validación al comprobar que el divisor no es cero.
- **`break`**: Rompe el ciclo de validación externo al haberse capturado ambas entradas de forma robusta.
- **`except ValueError:`**: Captura errores de sintaxis si el usuario escribe texto o decimales.
- **`print("Entrada no válida...")`**: Muestra advertencia por ingresos no enteros.
- **`if numero % multiplo == 0:`**: Verifica mediante operador módulo si el residuo de la división es exactamente cero (divisibilidad exacta).
- **`print(...) (en if)`**: Imprime que el primer número es efectivamente múltiplo del segundo.
- **`else:`**: Bloque alternativo si el residuo es mayor que cero.
- **`print(...) (en else)`**: Imprime que el primer número no posee relación de divisibilidad exacta con el divisor.


#### Código Completo
```python
while True:
    try:
        # Captura y validación del primer número entero
        numero = int(input("Ingrese el primer número entero: "))
        
        # Bucle de validación exclusivo para evitar la división por cero
        while True:
            multiplo = int(input("Ingrese el segundo número entero (distinto de 0): "))
            if multiplo == 0:
                print("El divisor no puede ser cero ya que causará un error matemático. Intente de nuevo.")
            else:
                break  # Sale del ciclo interno si el divisor es válido
        break  # Sale del ciclo externo al capturar ambos valores de forma correcta
    except ValueError:
        print("Entrada no válida. Por favor, ingrese números enteros válidos.")

# Evaluación de la divisibilidad usando el residuo modular
if numero % multiplo == 0:
    print(f"El número {numero} es múltiplo de {multiplo}.")
else:
    print(f"El número {numero} no es múltiplo de {multiplo}.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese el primer número entero: 15
Ingrese el segundo número entero (distinto de 0): 0
El divisor no puede ser cero ya que causará un error matemático. Intente de nuevo.
Ingrese el segundo número entero (distinto de 0): 5
```
**Salida:**
```text
El número 15 es múltiplo de 5.
```
