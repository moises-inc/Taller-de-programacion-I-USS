### Ejercicio 16: Paridad variable con cantidad n

#### Enunciado del Problema
Desarrolla un script que pida al usuario un número n. Luego, debe solicitar n números enteros e indicar para cada uno si es par o impar. Al final, debe mostrar: Cantidad de números pares e impares.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `n` | `int` | Define la cantidad de números enteros que el usuario desea evaluar. Determina dinámicamente la duración del bucle. |
| `pares` | `int` | Contador incremental de números determinados como pares en la iteración. |
| `impares` | `int` | Contador incremental de números determinados como impares en la iteración. |
| `i` | `int` | Variable de control de ciclo `for` que identifica al elemento actual (0 a n-1). |
| `num` | `int` | Almacena secuencialmente el número entero actual que se evaluará en el ciclo. |


## Lógica de la Solución
El script generaliza la evaluación de paridad numérica permitiendo al usuario definir dinámicamente la cantidad de ciclos a través de una variable controladora `n`. 1. **Validación de n:** Se solicita el número total de operaciones asegurando que sea un entero estrictamente positivo (`n > 0`) mediante `try-except` y un bucle interactivo de seguridad.2. **Ciclo dinámico:** Se ejecuta un ciclo `for i in range(n)` que solicita en cada paso un número entero `num` (también validado contra errores sintácticos).3. **Evaluación de paridad:** Se utiliza la operación de módulo `% 2` para catalogar cada número e incrementar su respectiva estadística.Al finalizar las `n` evaluaciones, se entrega un resumen consolidado de las frecuencias pares e impares.

## Explicación Línea por Línea
- **`while True: (primero)`**: Inicia el bucle infinito interactivo para capturar de forma robusta la variable de control `n`.
- **`n = int(input(...))`**: Solicita la cantidad de números a evaluar y la fuerza a formato entero con `int()`, guardándola en `n`.
- **`if n > 0:`**: Verifica lógicamente que la cantidad ingresada sea estrictamente mayor a cero.
- **`break`**: Sale del bucle de validación de `n` al ser válido e iniciarse el flujo.
- **`print("Error: La cantidad...")`**: Mensaje que se ejecuta si `n` es cero o un valor negativo.
- **`except ValueError: (primero)`**: Atrapa excepciones de conversión si el usuario introduce texto en `n`.
- **`print("Error: Ingrese un entero...")`**: Informa que se requiere digitar un número entero.
- **`pares = 0`**: Inicializa en cero el acumulador estadístico para números pares.
- **`impares = 0`**: Inicializa en cero el acumulador estadístico para números impares.
- **`for i in range(n):`**: Declara el ciclo principal dinámico que repetirá el bloque interno exactamente `n` veces consecutivas.
- **`while True: (segundo)`**: Bucle interactivo anidado de validación para el número entero evaluado en el ciclo actual.
- **`num = int(input(...))`**: Solicita y convierte a entero el número actual de la secuencia asignándolo a `num`.
- **`break`**: Sale de la validación del número al comprobarse su tipo entero.
- **`except ValueError: (segundo)`**: Atrapa excepciones sintácticas si se digita texto o flotantes en la secuencia.
- **`print("Error: Ingrese un entero...")`**: Notifica que el número actual de la iteración debe ser estrictamente entero.
- **`if num % 2 == 0:`**: Evalúa si el número actual de la iteración deja residuo cero al dividirse por 2 (es par).
- **`pares += 1`**: Suma 1 unidad al contador acumulador de números pares.
- **`print(f"El número {num} es PAR.")`**: Informa en pantalla que el número es par.
- **`else:`**: Bloque alternativo que se ejecuta si el residuo de la división no es nulo (impar).
- **`impares += 1`**: Suma 1 unidad al contador acumulador de números impares.
- **`print(f"El número {num} es IMPAR.")`**: Informa en la terminal que el número ingresado posee naturaleza impar.
- **`print("\n--- Resultados ---")`**: Encabezado impreso al finalizar el ciclo dinámico de `n` iteraciones.
- **`print(...)`**: Imprime los contadores estadísticos de números pares e impares consolidados.


#### Código Completo
```python
print("--- Analizador de Paridad Variable ---")
# Captura y validación de la variable controladora de ciclos n
while True:
    try:
        n = int(input("¿Cuántos números enteros desea evaluar?: "))
        if n > 0:
            break  # Entrada de control correcta, continúa el flujo
        print("Error: La cantidad de números debe ser mayor a cero.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

pares = 0
impares = 0

# Ciclo dinámico parametrizado por la variable n
for i in range(n):
    # Validación interactiva interna de cada elemento de la secuencia
    while True:
        try:
            num = int(input(f"Ingrese el número entero {i+1} de {n}: "))
            break  # Elemento correcto, sale del bucle de validación
        except ValueError:
            print("Error: Ingrese un entero válido.")

    # Evaluación e incremento estadístico de paridad
    if num % 2 == 0:
        pares += 1
        print(f"El número {num} es PAR.")
    else:
        impares += 1
        print(f"El número {num} es IMPAR.")

# Informe de resultados consolidados
print("\n--- Resultados ---")
print(f"Número de pares  : {pares}")
print(f"Número de impares: {impares}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Analizador de Paridad Variable ---
¿Cuántos números enteros desea evaluar?: -2
Error: La cantidad de números debe ser mayor a cero.
¿Cuántos números enteros desea evaluar?: 3
Ingrese el número entero 1 de 3: 4
El número 4 es PAR.
Ingrese el número entero 2 de 3: hola
Error: Ingrese un entero válido.
Ingrese el número entero 2 de 3: 15
El número 15 es IMPAR.
Ingrese el número entero 3 de 3: 0
El número 0 es PAR.
```
**Salida:**
```text
--- Resultados ---
Número de pares  : 2
Número de impares: 1
```
