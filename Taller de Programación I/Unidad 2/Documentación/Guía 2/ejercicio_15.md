### Ejercicio 15: Evaluación consecutiva de 15 años bisiestos

#### Enunciado del Problema
Desarrolla un script que pida 15 años e indique para cada uno si corresponde a un año bisiesto o no bisiesto. Al final, debe mostrar: Cantidad de años bisiestos y cantidad de años no bisiestos.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `bisiestos` | `int` | Contador incremental de los años evaluados como bisiestos. |
| `no_bisiestos` | `int` | Contador incremental de los años evaluados como ordinarios o no bisiestos. |
| `i` | `int` | Variable contadora del ciclo `for` que identifica al año actual evaluado (0 a 14). |
| `ano` | `int` | Almacena temporalmente el año entero en evaluación ingresado por el usuario. |
| `es_bisiesto` | `bool` | Variable lógica intermedia que almacena el veredicto del cálculo astronómico (True/False). |


## Lógica de la Solución
El programa evalúa secuencialmente la condición astronómica de bisiesto para un conjunto cerrado de 15 años usando un ciclo determinista `for i in range(15)`. En cada iteración: - Se solicita el año validando con `while True` y `try-except` que sea un número entero estrictamente positivo (`ano > 0`).- Se aplica la fórmula matemática de bisiesto en el calendario gregoriano: Un año es bisiesto si es divisible exactamente por 4 y no por 100 (`ano % 4 == 0 and ano % 100 != 0`), a menos que sea divisible por 400 (`ano % 400 == 0`). Esta regla lógica compleja se expresa como: `es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`.Posteriormente, se informa la condición individual de bisiesto del año analizado y se incrementa el contador estadístico correspondiente, emitiéndose un balance total final.

## Explicación Línea por Línea
- **`bisiestos = 0`**: Inicializa el contador acumulador de años bisiestos en cero.
- **`no_bisiestos = 0`**: Inicializa el contador acumulador de años ordinarios o no bisiestos en cero.
- **`for i in range(15):`**: Declara el ciclo determinado principal que se ejecutará exactamente 15 veces consecutivas.
- **`while True:`**: Bucle infinito interno para asegurar la obtención de un año correcto mayor a cero.
- **`try:`**: Región encargada de capturar excepciones en la entrada de datos del usuario.
- **`ano = int(input(...))`**: Solicita el año, lo fuerza a formato entero con `int()` y lo almacena.
- **`if ano > 0:`**: Verifica lógicamente que el año sea posterior a la era cero.
- **`break`**: Sale del bucle de validación al obtenerse un año entero correcto.
- **`print("Error: El año debe...")`**: Mensaje del `else` que indica que los años deben ser valores positivos.
- **`except ValueError:`**: Atrapa excepciones si el usuario escribe textos o decimales.
- **`print("Error: Ingrese un entero.")`**: Notifica que se requiere exclusivamente un año en formato de entero.
- **`es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`**: Evalúa mediante lógica booleana la divisibilidad del año bajo la regla formal del calendario gregoriano.
- **`if es_bisiesto:`**: Evalúa si la variable intermedia booleana contiene el estado `True`.
- **`bisiestos += 1`**: Añade 1 unidad al contador acumulador de años bisiestos.
- **`print(f"El año {ano} es BISIESTO.")`**: Muestra en consola la condición bisiesta del año actual.
- **`else:`**: Bloque ejecutado si la evaluación booleana de bisiesto resultó ser `False`.
- **`no_bisiestos += 1`**: Suma 1 unidad al contador de años no bisiestos.
- **`print(f"El año {ano} es NO BISIESTO.")`**: Informa que el año actual corresponde a un año ordinario.
- **`print("\n--- Resumen de Registros ---")`**: Despliega el encabezado final del balance general tras cerrarse las 15 iteraciones.
- **`print(...)`**: Imprime los contadores estadísticos de años bisiestos y ordinarios totales.


#### Código Completo
```python
print("--- Verificación de Años Bisiestos (15 registros) ---")
bisiestos = 0
no_bisiestos = 0

# Ciclo determinado para procesar exactamente 15 registros
for i in range(15):
    # Validación interactiva interna de integridad
    while True:
        try:
            ano = int(input(f"Ingrese el año {i+1} a evaluar (mayor a 0): "))
            if ano > 0:
                break  # Año correcto, sale del bucle de validación
            print("Error: El año debe ser mayor a cero.")
        except ValueError:
            print("Error: Ingrese un número entero.")

    # Algoritmo de lógica booleana para bisiestos en el calendario gregoriano
    es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    # Asignación y acumulación estadística de estados
    if es_bisiesto:
        bisiestos += 1
        print(f"El año {ano} es BISIESTO.")
    else:
        no_bisiestos += 1
        print(f"El año {ano} es NO BISIESTO.")

# Despliegue consolidado de registros estadísticos finales
print("\n--- Resumen de Registros ---")
print(f"Total años bisiestos: {bisiestos}")
print(f"Total años no bisiestos: {no_bisiestos}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Verificación de Años Bisiestos (15 registros) ---
Ingrese el año 1 a evaluar (mayor a 0): 2024
El año 2024 es BISIESTO.
Ingrese el año 2 a evaluar (mayor a 0): 1900
El año 1900 es NO BISIESTO.
[... Se evalúan los años 3 al 14 ...]
Ingrese el año 15 a evaluar (mayor a 0): 2000
El año 2000 es BISIESTO.
```
**Salida:**
```text
--- Resumen de Registros ---
Total años bisiestos: 6
Total años no bisiestos: 9
```
