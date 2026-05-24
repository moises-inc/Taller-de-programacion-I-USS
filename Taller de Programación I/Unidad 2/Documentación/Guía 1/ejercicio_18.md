### Ejercicio 18: Conversor de Unidades Físicas

#### Enunciado del Problema
Desarrolla un script que permita elegir un tipo de conversión de unidades entre las siguientes opciones:
1. Centímetros a pulgadas
2. Kilogramos a libras
3. Litros a galones

Luego, el programa debe pedir el valor a convertir y mostrar el resultado usando las siguientes equivalencias:
* $1\text{ pulgada} = 2.54\text{ cm}$
* $1\text{ libra} = 0.45359237\text{ kg}$
* $1\text{ galón} = 3.785411784\text{ litros}$

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `opcion` | `int` | Almacena la opción de conversión elegida del menú interactivo (validada: $1$, $2$ o $3$). |
| `valor` | `float` | Almacena el valor numérico real de la magnitud a convertir (validada estrictamente $> 0$). |
| `resultado` | `float` | Almacena la magnitud convertida final tras aplicar la constante de equivalencia física. |
| `unidad_orig` | `str` | Etiqueta de la unidad física de origen ("cm", "kg", "litros"). |
| `unidad_dest` | `str` | Etiqueta de la unidad física resultante o de destino ("pulgadas", "libras", "galones"). |

#### Lógica de la Solución
El algoritmo soluciona de forma precisa las conversiones de física clásica mediante un diseño de menú numérico interactivo. Las conversiones físicas exigen rigurosidad en dos dimensiones:
1. **Límites de la Física Real:** No se permite realizar conversiones de valores negativos o iguales a cero, puesto que las magnitudes físicas clásicas (longitud, masa y volumen) son estrictamente positivas en este contexto.
2. **Precisión de Constantes:** Para garantizar la rigurosidad científica exigida en ramos académicos, se aplican los factores de equivalencia con su mantisa completa (hasta $9$ decimales).

El flujo opera solicitando la opción del menú, validando que el valor sea flotante positivo, seleccionando condicionalmente la constante de conversión y aplicando la división correspondiente. Finalmente, la salida redondea a cuatro decimales de precisión (`:.4f`).

#### Explicación Línea por Línea
* **Líneas 5-8 (`print(...)`):** Muestra por consola el menú interactivo con las opciones numéricas de conversión.
* **Línea 10 (`while True:`):** Inicializa el bucle para la captura de la opción seleccionada.
* **Línea 11 (`try:`):** Bloque protegido de conversión de tipo entero.
* **Línea 12 (`opcion = int(input(...))`):** Lee la opción elegida por teclado como entero (`int`).
* **Línea 13 (`if opcion in [1, 2, 3]:`):** Comprueba mediante pertenencia si la opción es $1$, $2$ o $3$.
* **Línea 14 (`break`):** Rompe la iteración si la opción es válida.
* **Línea 15 (`else:`):** Rama si ingresa un entero fuera de rango.
* **Línea 16 (`print(...)`):** Muestra advertencia e inicia nueva iteración del menú.
* **Línea 17 (`except ValueError:`):** Intercepta texto o flotantes en la elección de opción.
* **Línea 18 (`print(...)`):** Notifica del tipo de dato requerido.
* **Línea 20 (`while True:`):** Bucle interactivo para solicitar el valor físico a convertir.
* **Línea 21 (`try:`):** Bloque protegido de conversión decimal.
* **Línea 22 (`valor = float(input(...))`):** Captura el valor a convertir como decimal (`float`).
* **Línea 23 (`if valor > 0:`):** Comprueba que la magnitud física sea estrictamente positiva.
* **Línea 24 (`break`):** Rompe el bucle de validación de valor físico.
* **Línea 25 (`else:`):** Rama para magnitudes inválidas $\le 0$.
* **Línea 26 (`print(...)`):** Muestra el mensaje explicando la imposibilidad de magnitudes no positivas.
* **Líneas 29-38 (`if-elif-else`):** Determina condicionalmente las operaciones en base a la equivalencia exacta:
  * Opción 1: Divide por $2.54$ y asigna etiquetas `"cm"` y `"pulgadas"`.
  * Opción 2: Divide por $0.45359237$ y asigna `"kg"` y `"libras"`.
  * Opción 3: Divide por $3.785411784$ y asigna `"litros"` y `"galones"`.
* **Línea 40 (`print(...)`):** Muestra el resultado de la equivalencia formateando el resultado a cuatro decimales de precisión (`:.4f`).

#### Código Completo
```python
# Conversor de Unidades Físicas

print("--- Conversor de Unidades Físicas ---")
print("1. Centímetros a Pulgadas")
print("2. Kilogramos a Libras")
print("3. Litros a Galones")

# Captura y validación estructurada de opción
while True:
    try:
        opcion = int(input("Seleccione su opción (1, 2 o 3): "))
        if opcion in [1, 2, 3]:
            break
        else:
            print("Opción fuera de rango. Seleccione 1, 2 o 3.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Captura y validación estructurada de la magnitud física a convertir
while True:
    try:
        valor = float(input("Ingrese el valor numérico a convertir (mayor que 0): "))
        if valor > 0:
            break
        else:
            print("El valor a convertir debe ser estrictamente positivo.")
    except ValueError:
        print("Entrada no válida. Ingrese un valor numérico decimal o entero.")

# Ejecución condicional de conversiones físicas con constantes de alta precisión
if opcion == 1:
    # 1 pulgada = 2.54 cm
    resultado = valor / 2.54
    unidad_orig, unidad_dest = "cm", "pulgadas"
elif opcion == 2:
    # 1 libra = 0.45359237 kg
    resultado = valor / 0.45359237
    unidad_orig, unidad_dest = "kg", "libras"
else:
    # 1 galón = 3.785411784 litros
    resultado = valor / 3.785411784
    unidad_orig, unidad_dest = "litros", "galones"

# Salida formateada de alta precisión
print(f"\nResultado: {valor} {unidad_orig} equivalen a: {resultado:.4f} {unidad_dest}.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Centímetros a Pulgadas):
* **Entrada esperada:** `1` (opción), `10` (valor)
* **Salida del programa:** `Resultado: 10.0 cm equivalen a: 3.9370 pulgadas.`

##### Caso de Uso 2 (Kilogramos a Libras):
* **Entrada esperada:** `2` (opción), `5` (valor)
* **Salida del programa:** `Resultado: 5.0 kg equivalen a: 11.0231 libras.`

##### Caso de Uso 3 (Litros a Galones):
* **Entrada esperada:** `3` (opción), `3.785411784` (valor)
* **Salida del programa:** `Resultado: 3.785411784 litros equivalen a: 1.0000 galones.`

##### Caso de Uso 4 (Error inicial y reintento en cascada):
* **Entrada esperada:** `4` (opción) -> *Error* -> `1`, `-5` (valor) -> *Error* -> `15`
* **Salida del programa:**
  ```text
  Seleccione su opción (1, 2 o 3): 4
  Opción fuera de rango. Seleccione 1, 2 o 3.
  Seleccione su opción (1, 2 o 3): 1
  Ingrese el valor numérico a convertir (mayor que 0): -5
  El valor a convertir debe ser estrictamente positivo.
  Ingrese el valor numérico a convertir (mayor que 0): 15
  
  Resultado: 15.0 cm equivalen a: 5.9055 pulgadas.
  ```
