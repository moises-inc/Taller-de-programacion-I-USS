### Ejercicio 13: Control de cobros para 20 vehículos

#### Enunciado del Problema
Desarrolla un script que permita registrar la entrada de 20 vehículos a un estacionamiento. Para cada vehículo, debe pedir Patente y Horas enteras estacionado. Aplica las tarifas:
• Hasta 2 horas: $2.000
• Más de 2 horas y hasta 5 horas: $3.500
• Más de 5 horas: $5.000
Al final, debe mostrar: Total recaudado, cantidad de vehículos en cada tramo de cobro.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `total_recaudado` | `int` | Acumulador del monto monetario global obtenido por todos los arriendos de espacio. |
| `tramo_1_cnt` | `int` | Contador de vehículos cuya permanencia fue menor o igual a 2 horas. |
| `tramo_2_cnt` | `int` | Contador de vehículos cuya permanencia estuvo en el intervalo de más de 2 y hasta 5 horas. |
| `tramo_3_cnt` | `int` | Contador de vehículos cuya permanencia excedió las 5 horas. |
| `i` | `int` | Variable contadora del ciclo `for` que identifica secuencialmente los vehículos (0 a 19). |
| `patente` | `str` | Identificador del auto formateado en mayúsculas y limpio de espacios. |
| `horas` | `int` | Guarda el número entero de horas estacionado del vehículo actual. |
| `costo` | `int` | Variable de salida intermedia que almacena la tarifa del vehículo evaluado. |


## Lógica de la Solución
El programa efectúa un registro de entrada y cálculo de costo consecutivo para un grupo cerrado de 20 vehículos mediante un ciclo determinista `for i in range(20)`. En cada iteración: - Se solicita y valida la patente asegurando que no se guarde en blanco con un bucle `while not patente` y limpiando con `.strip().upper()`.- Se solicitan las horas enteras validando con un ciclo interactivo `while True` y `try-except` que sea un entero mayor o igual a cero.- Se clasifica la tarifa de forma condicionada incrementando el contador del tramo respectivo.- Se añade el valor al acumulador `total_recaudado`.Al finalizar las 20 iteraciones del bucle, el script emite un balance de operaciones con la recaudación final y el desglose de tramos.

## Explicación Línea por Línea
- **`total_recaudado = 0`**: Inicializa en cero la caja acumuladora de dinero total recaudado por el estacionamiento.
- **`tramo_1_cnt = 0`**: Inicializa el contador del primer tramo tarifario (hasta 2 horas).
- **`tramo_2_cnt = 0`**: Inicializa el contador del segundo tramo tarifario (2 a 5 horas).
- **`tramo_3_cnt = 0`**: Inicializa el contador del tercer tramo tarifario (más de 5 horas).
- **`for i in range(20):`**: Inicia el ciclo principal determinista que iterará exactamente 20 veces (con índices de 0 a 19).
- **`patente = input(...).strip().upper()`**: Solicita la patente, remueve espacios y la pasa a mayúsculas.
- **`while not patente:`**: Controlador de validación de patente vacía para impedir saltarse campos.
- **`patente = input(...).strip().upper()`**: Vuelve a requerir la patente en la terminal.
- **`while True:`**: Ciclo interactivo interno infinito para validar de forma robusta las horas.
- **`try:`**: Sección de control que vigila ingresos de caracteres extraños.
- **`horas = int(input(...))`**: Solicita las horas enteras convirtiendo la entrada con `int()` y las guarda.
- **`if horas >= 0:`**: Verifica lógicamente que las horas no posean signo negativo.
- **`break`**: Sale del bucle de validación al obtenerse un entero correcto.
- **`print("Error: Las horas no...")`**: Mensaje del `else` que notifica que no se admiten horas negativas.
- **`except ValueError:`**: Atrapa excepciones causadas al ingresar datos no enteros.
- **`print("Error: Ingrese un entero...")`**: Informa que se requiere ingresar un número entero.
- **`if horas <= 2:`**: Evalúa si las horas pertenecen al tramo inicial.
- **`costo = 2000`**: Asigna la tarifa de $2.000 pesos al vehículo.
- **`tramo_1_cnt += 1`**: Suma 1 al acumulador del tramo 1.
- **`elif horas <= 5:`**: Evaluación en cascada para el tramo secundario de 2 a 5 horas.
- **`costo = 3500`**: Asigna la tarifa de $3.500 pesos.
- **`tramo_2_cnt += 1`**: Suma 1 al acumulador del tramo 2.
- **`else:`**: Ejecutado al superarse las 5 horas de estadía.
- **`costo = 5000`**: Asigna la tarifa máxima de $5.000 pesos.
- **`tramo_3_cnt += 1`**: Suma 1 al acumulador del tramo 3.
- **`total_recaudado += costo`**: Suma el cobro del vehículo actual a la recaudación total consolidada.
- **`print(f"Vehículo {patente} | Cobro...")`**: Informa el cobro individual del vehículo procesado actual formateando miles.
- **`print("\n--- Balance del Estacionamiento ---")`**: Encabezado del balance general final emitido tras finalizar los 20 ciclos.
- **`print(...)`**: Imprime las estadísticas consolidadas finales de recaudación y tramos.


#### Código Completo
```python
print("--- Control de Estacionamiento (20 Vehículos) ---")
total_recaudado = 0
tramo_1_cnt = 0  # Hasta 2 horas
tramo_2_cnt = 0  # 2 a 5 horas
tramo_3_cnt = 0  # Más de 5 horas

# Ciclo determinado para procesar 20 vehículos
for i in range(20):
    print(f"\n--- Vehículo {i+1} ---")
    # Solicitud y saneamiento de patente obligatoria
    patente = input("Ingrese patente del vehículo: ").strip().upper()
    while not patente:
        patente = input("Error: La patente es requerida: ").strip().upper()

    # Validación interactiva de horas estacionado
    while True:
        try:
            horas = int(input(f"Cantidad de horas enteras para {patente}: "))
            if horas >= 0:
                break
            print("Error: Las horas no pueden ser negativas.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

    # Clasificación por tramos tarifarios
    if horas <= 2:
        costo = 2000
        tramo_1_cnt += 1
    elif horas <= 5:
        costo = 3500
        tramo_2_cnt += 1
    else:
        costo = 5000
        tramo_3_cnt += 1

    # Acumulación de tarifas en caja
    total_recaudado += costo
    print(f"Vehículo {patente} | Cobro: ${costo:,} CLP")

# Balance general final del estacionamiento
print("\n--- Balance del Estacionamiento ---")
print(f"Total recaudado: ${total_recaudado:,} CLP")
print(f"Vehículos en Tramo 1 (hasta 2h): {tramo_1_cnt}")
print(f"Vehículos en Tramo 2 (2h a 5h): {tramo_2_cnt}")
print(f"Vehículos en Tramo 3 (más de 5h): {tramo_3_cnt}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Control de Estacionamiento (20 Vehículos) ---

--- Vehículo 1 ---
Ingrese patente del vehículo: aa-bb-12
Cantidad de horas enteras para AA-BB-12: 1
Vehículo AA-BB-12 | Cobro: $2,000 CLP

--- Vehículo 2 ---
Ingrese patente del vehículo: cc-dd-34
Cantidad de horas enteras para CC-DD-34: 4
Vehículo CC-DD-34 | Cobro: $3,500 CLP
[... Se procesan vehículos del 3 al 19 ...]

--- Vehículo 20 ---
Ingrese patente del vehículo: ee-ff-56
Cantidad de horas enteras para EE-FF-56: 7
Vehículo EE-FF-56 | Cobro: $5,000 CLP
```
**Salida:**
```text
--- Balance del Estacionamiento ---
Total recaudado: $68,500 CLP
Vehículos en Tramo 1 (hasta 2h): 8
Vehículos en Tramo 2 (2h a 5h): 7
Vehículos en Tramo 3 (más de 5h): 5
```
