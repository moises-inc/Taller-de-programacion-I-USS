### Ejercicio 19: Calculadora aritmética controlada de n operaciones

#### Enunciado del Problema
Desarrolla un script que pida al usuario un número n, correspondiente a la cantidad de operaciones que desea realizar. Para cada operación, debe pedir: Primer número, Segundo número, Operación (+, -, *, /). El programa debe mostrar el resultado de cada operación. En caso de división, debe evitar dividir por cero. Al final, debe indicar cuántas operaciones de cada tipo se realizaron.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `n` | `int` | Variable de control ingresada por el usuario que parametriza dinámicamente el número de operaciones matemáticas. |
| `sumas` | `int` | Contador incremental de adiciones ejecutadas de forma satisfactoria. |
| `restas` | `int` | Contador incremental de sustracciones ejecutadas de forma satisfactoria. |
| `mults` | `int` | Contador incremental de multiplicaciones ejecutadas. |
| `divs` | `int` | Contador incremental de divisiones válidas realizadas (sin divisor nulo). |
| `i` | `int` | Variable de control de ciclo `for` (0 a n-1). |
| `num1` | `float` | Primer operando decimal flotante ingresado. |
| `num2` | `float` | Segundo operando decimal flotante ingresado. |
| `op` | `str` | Carácter que representa al operador matemático seleccionado, validado estrictamente en `['+', '-', '*', '/']`. |
| `result` | `float` | Almacena temporalmente el resultado aritmético calculado en el ciclo. |


## Lógica de la Solución
El programa implementa una calculadora multipropósito repetitiva para `n` operaciones parametrizadas por el usuario. 1. **Validación de n:** Se solicita el total de operaciones asegurando un entero positivo (`n > 0`).2. **Bucle de Operaciones:** Se ejecuta un ciclo `for` que solicita los operandos y el operador en cada iteración: - **Operandos:** Se capturan y validan dos flotantes (`num1`, `num2`) con `try-except`.- **Operador:** Se captura una cadena limpia de espacios y se valida que pertenezca al conjunto de operaciones elementales: `+`, `-`, `*` o `/`.3. **Ejecución y Control de Cero:** Se aplican bifurcaciones para resolver la operación matemática. En el caso de la división, se evalúa con un condicional secundario si el divisor es igual a cero (`num2 == 0`) para bloquear activamente la operación y emitir un error crítico, previniendo caídas del programa y divisiones indefinidas. Al cerrarse el ciclo general, se entregan estadísticas de los operadores procesados.

## Explicación Línea por Línea
- **`while True: (primero)`**: Inicia el bucle de validación interactiva para capturar de forma robusta la variable de control `n`.
- **`n = int(input(...))`**: Solicita la cantidad de operaciones, las fuerza a tipo entero con `int()` y las guarda en `n`.
- **`if n > 0:`**: Verifica que el número de operaciones matemáticas sea mayor que cero.
- **`break`**: Sale del bucle de validación de `n` e inicia el procesamiento de cálculos.
- **`except ValueError: (primero)`**: Atrapa excepciones de tipo si el usuario ingresa textos en `n`.
- **`sumas = 0`**: Inicializa en cero el contador acumulador de adiciones.
- **`restas = 0`**: Inicializa en cero el contador acumulador de sustracciones.
- **`mults = 0`**: Inicializa en cero el contador acumulador de multiplicaciones.
- **`divs = 0`**: Inicializa en cero el contador acumulador de divisiones válidas.
- **`for i in range(n):`**: Inicia el ciclo principal determinado que repetirá el cálculo aritmético `n` veces consecutivas.
- **`while True: (segundo)`**: Bucle interactivo interno de validación para capturar los operandos numéricos flotantes.
- **`num1 = float(input(...))`**: Solicita y convierte a decimal el primer número de la operación asignándolo a `num1`.
- **`num2 = float(input(...))`**: Solicita y convierte a decimal el segundo número de la operación asignándolo a `num2`.
- **`break`**: Sale de la validación de operandos al confirmarse de tipo flotante exitosos.
- **`except ValueError: (segundo)`**: Atrapa excepciones si los números de entrada contienen caracteres extraños.
- **`while True: (tercero)`**: Bucle de validación interno para forzar la elección de un operador aritmético reglamentario.
- **`op = input(...).strip()`**: Captura el operador matemático en formato string eliminando espacios y lo guarda.
- **`if op in ["+", "-", "*", "/"]:`**: Verifica lógica de membresía en la lista de operadores elementales permitidos.
- **`break`**: Sale de la validación del operador actual al confirmarse reglamentario.
- **`if op == "+":`**: Evalúa si la operación solicitada es una suma.
- **`result = num1 + num2`**: Realiza aritméticamente la adición de los operandos.
- **`sumas += 1`**: Suma 1 al contador acumulador de adiciones.
- **`print(f"Resultado...")`**: Muestra en pantalla el desglose del resultado calculado de la suma.
- **`elif op == "-":`**: Evalúa si la operación solicitada es una resta.
- **`result = num1 - num2`**: Realiza aritméticamente la sustracción.
- **`restas += 1`**: Suma 1 al acumulador de restas.
- **`print(f"Resultado...")`**: Informa del resultado calculado de la sustracción.
- **`elif op == "*":`**: Evalúa si la operación solicitada es una multiplicación.
- **`result = num1 * num2`**: Realiza aritméticamente la multiplicación.
- **`mults += 1`**: Suma 1 al acumulador de multiplicaciones.
- **`print(f"Resultado...")`**: Informa del resultado calculado de la multiplicación.
- **`else:`**: Bloque ejecutado al seleccionarse división por descarte de condiciones.
- **`if num2 == 0:`**: Control secundario: verifica lógicamente si el divisor actual de la operación es igual a cero.
- **`print("Error crítico...")`**: Informa al usuario que la división por cero no posee definición matemática real.
- **`else:`**: Ejecutado al ser el divisor un número válido diferente de cero.
- **`result = num1 / num2`**: Realiza aritméticamente la división de los operandos flotantes.
- **`divs += 1`**: Suma 1 al acumulador de divisiones válidas.
- **`print(f"Resultado...")`**: Muestra en consola el resultado de la división realizada.
- **`print("\n--- Estadísticas de Operaciones ---")`**: Encabezado final impreso tras cerrarse las `n` operaciones del ciclo.
- **`print(...)`**: Imprime los reportes de frecuencias de los operadores procesados de forma consolidada.


#### Código Completo
```python
print("--- Calculadora Repetitiva Variable ---")
# Captura y validación de la cantidad de operaciones n
while True:
    try:
        n = int(input("¿Cuántas operaciones matemáticas desea realizar?: "))
        if n > 0:
            break
        print("Error: El número de operaciones debe ser mayor a cero.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

sumas = 0
restas = 0
mults = 0
divs = 0

# Ciclo dinámico controlado por la variable n
for i in range(n):
    print(f"\n--- Operación {i+1} de {n} ---")
    # Validación interactiva interna de operandos
    while True:
        try:
            num1 = float(input("Ingrese primer número: "))
            num2 = float(input("Ingrese segundo número: "))
            break
        except ValueError:
            print("Error: Ingrese valores numéricos.")

    # Validación interactiva interna de operador
    while True:
        op = input("Seleccione operación (+, -, *, /): ").strip()
        if op in ["+", "-", "*", "/"]:
            break
        print("Error: Operador matemático inválido.")

    # Bifurcación condicional de operaciones con protección de división por cero
    if op == "+":
        result = num1 + num2
        sumas += 1
        print(f"Resultado: {num1} + {num2} = {result}")
    elif op == "-":
        result = num1 - num2
        restas += 1
        print(f"Resultado: {num1} - {num2} = {result}")
    elif op == "*":
        result = num1 * num2
        mults += 1
        print(f"Resultado: {num1} * {num2} = {result}")
    else:
        if num2 == 0:
            print("Error crítico: División por cero no permitida en matemáticas reales.")
        else:
            result = num1 / num2
            divs += 1
            print(f"Resultado: {num1} / {num2} = {result}")

# Informe consolidated estadístico de operaciones exitosas
print("\n--- Estadísticas de Operaciones ---")
print(f"Sumas realizadas         : {sumas}")
print(f"Restas realizadas        : {restas}")
print(f"Multiplicaciones realizadas: {mults}")
print(f"Divisiones válidas realizadas: {divs}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Calculadora Repetitiva Variable ---
¿Cuántas operaciones matemáticas desea realizar?: 2

--- Operación 1 de 2 ---
Ingrese primer número: 8
Ingrese segundo número: 0
Seleccione operación (+, -, *, /): /
Error crítico: División por cero no permitida en matemáticas reales.

--- Operación 2 de 2 ---
Ingrese primer número: 12.5
Ingrese segundo número: 4
Seleccione operación (+, -, *, /): *
Resultado: 12.5 * 4.0 = 50.0
```
**Salida:**
```text
--- Estadísticas de Operaciones ---
Sumas realizadas         : 0
Restas realizadas        : 0
Multiplicaciones realizadas: 1
Divisiones válidas realizadas: 0
```
