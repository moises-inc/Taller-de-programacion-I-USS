### Ejercicio 3: Comparador de dos números

#### Enunciado del Problema
Desarrolla un script que pida dos números al usuario y determine cuál de ellos es mayor, o bien indique si ambos son iguales.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `numero1` | `float` | Almacena el primer número decimal ingresado para la comparación. |
| `numero2` | `float` | Almacena el segundo número decimal ingresado para la comparación. |


## Lógica de la Solución
El script implementa un comparador numérico real bilateral. Solicita dos números decimales, asegurando su validez matemática mediante un bucle interactivo que encapsula la conversión a `float`. Una vez obtenidos de forma segura ambos operandos, el algoritmo ejecuta una comparación en cascada: primero verifica si el primero es mayor al segundo (`numero1 > numero2`), luego si el primero es menor al segundo (`numero1 < numero2`), y finalmente, si ninguna de las condiciones anteriores se cumple, infiere lógicamente que ambos valores son exactamente iguales.

## Explicación Línea por Línea
- **`while True:`**: Establece el ciclo infinito para repetir la captura de datos en caso de errores de ingreso.
- **`try:`**: Inicia la zona protegida de manejo de excepciones.
- **`numero1 = float(input("Ingrese el primer número: "))`**: Captura y convierte a tipo de dato decimal flotante el primer número ingresado por el usuario.
- **`numero2 = float(input("Ingrese el segundo número: "))`**: Captura y convierte a tipo flotante el segundo número del usuario en la misma iteración.
- **`break`**: Sale de la captura de datos si ambas conversiones se realizan de forma exitosa.
- **`except ValueError:`**: Captura los fallos de conversión que ocurren cuando el usuario proporciona datos no numéricos.
- **`print("Entrada no válida...")`**: Advierte sobre el error de tipeo y reanuda el ciclo interactivo de entrada.
- **`if numero1 > numero2:`**: Compara si el primer número es algebraicamente mayor que el segundo.
- **`print(f"El número {numero1} es mayor que {numero2}.")`**: Muestra el resultado si la primera variable supera a la segunda.
- **`elif numero1 < numero2:`**: Condicional alternativo que determina si el primer número es menor que el segundo.
- **`print(f"El número {numero1} es menor que {numero2}.")`**: Muestra el resultado si el segundo operando es mayor.
- **`else:`**: Sección final del condicional en cascada que se ejecuta al cumplirse la igualdad de ambos operandos.
- **`print(f"Ambos números son iguales ({numero1}).")`**: Muestra un mensaje de equivalencia de valores en consola.


#### Código Completo
```python
while True:
    try:
        # Captura de ambos números con conversión a flotantes
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        break  # Rompe el bucle si las entradas son válidas
    except ValueError:
        print("Entrada no válida. Por favor, ingrese valores numéricos.")

# Comparación lógica de los dos valores obtenidos
if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}.")
elif numero1 < numero2:
    print(f"El número {numero1} es menor que {numero2}.")
else:
    print(f"Ambos números son iguales ({numero1}).")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese el primer número: 12.4
Ingrese el segundo número: 12.4
```
**Salida:**
```text
Ambos números son iguales (12.4).
```
