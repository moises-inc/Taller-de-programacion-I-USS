### Ejercicio 12: Caja registradora fija de 25 clientes

#### Enunciado del Problema
Desarrolla un script que procese la compra de 25 clientes en una tienda. Cada cliente compra un producto con precio base de $80.000. El programa debe pedir la forma de pago: efectivo, débito o crédito. Aplica las siguientes reglas:
• Si paga con efectivo, se realiza un descuento de $5.000.
• Si paga con crédito, se aplica un recargo de $3.000.
• Si paga con débito, el precio no cambia.
Al final, debe mostrar: Total recaudado, cantidad de pagos en efectivo, débito y crédito.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `precio_base` | `int` | Constante fija de precio de compra base del artículo ($80.000). |
| `total_recaudado` | `int` | Acumulador del total facturado y cobrado en dinero a lo largo del día por los 25 clientes. |
| `efectivo_cnt` | `int` | Contador incremental de clientes que pagaron mediante efectivo. |
| `debito_cnt` | `int` | Contador incremental de clientes que pagaron mediante débito. |
| `credito_cnt` | `int` | Contador incremental de clientes que pagaron mediante crédito. |
| `i` | `int` | Variable de control del ciclo `for` que identifica al cliente actual (0 a 24). |
| `forma_pago` | `str` | Almacena temporalmente la opción ingresada por el cliente y normalizada. |
| `descuento` | `int` | Variable intermedia que almacena el descuento aplicable en el ciclo. |
| `recargo` | `int` | Variable intermedia que almacena el recargo aplicable en el ciclo. |
| `precio_final` | `int` | Precio de venta neto calculado de manera condicionada para el cliente actual. |


## Lógica de la Solución
El script simula de forma iterativa y controlada una caja de ventas para exactamente 25 transacciones consecutivas. Para ello, emplea un ciclo `for i in range(25)`. En cada iteración: - Se solicita el medio de pago del cliente actual. Se limpian espacios con `.strip()` y se transforma a minúsculas con `.lower()` para evitar fallos por capitalización.- Se evalúa mediante condicionales `if-elif-else` para definir las variables intermedias `descuento` y `recargo`, además de incrementar el contador respectivo.- Se calcula el `precio_final` de la transacción actual, se imprime en pantalla y se añade al acumulador `total_recaudado`.Al completarse el ciclo para los 25 clientes, se emite un reporte global consolidado con el balance final y estadísticas de medios de pago.

## Explicación Línea por Línea
- **`precio_base = 80000`**: Establece el valor inicial estándar del producto a adquirir por todos los clientes.
- **`total_recaudado = 0`**: Inicializa en cero la variable acumuladora de dinero total ingresado a caja.
- **`efectivo_cnt = 0`**: Inicializa en cero el contador de transacciones en efectivo.
- **`debito_cnt = 0`**: Inicializa en cero el contador de transacciones con tarjeta de débito.
- **`credito_cnt = 0`**: Inicializa en cero el contador de transacciones con tarjeta de crédito.
- **`for i in range(25):`**: Inicia el ciclo principal determinista que iterará exactamente 25 veces.
- **`while True:`**: Bucle infinito de validación de medio de pago para forzar una selección correcta.
- **`forma_pago = input(...).strip().lower()`**: Captura el medio de pago, elimina espacios iniciales/finales y lo convierte a minúsculas.
- **`if forma_pago == "efectivo":`**: Verifica si el usuario seleccionó la opción de pago en efectivo.
- **`descuento = 5000`**: Asigna a la variable intermedia `descuento` el valor de $5.000 pesos.
- **`recargo = 0`**: Asigna un recargo de $0 pesos al pagar en efectivo.
- **`efectivo_cnt += 1`**: Suma 1 al contador de transacciones en efectivo.
- **`break`**: Rompe el bucle de validación de forma de pago y continúa con el cálculo del precio.
- **`elif forma_pago in ["credito", "crédito"]:`**: Evalúa si seleccionó crédito (incluyendo variantes ortográficas con tilde).
- **`descuento = 0`**: Establece el descuento de crédito en $0 pesos.
- **`recargo = 3000`**: Establece el recargo comercial de tarjeta de crédito en $3.000 pesos.
- **`credito_cnt += 1`**: Suma 1 al contador de transacciones con tarjeta de crédito.
- **`break`**: Sale de la validación al confirmarse el medio de pago.
- **`elif forma_pago in ["debito", "débito"]:`**: Evalúa si seleccionó débito (incluyendo variante con tilde).
- **`descuento = 0`**: Establece descuento nulo de débito.
- **`recargo = 0`**: Establece recargo nulo de débito.
- **`debito_cnt += 1`**: Suma 1 al contador de transacciones con débito.
- **`break`**: Sale de la validación al confirmarse la forma de pago.
- **`else:`**: Rama por defecto ejecutada si se ingresó un texto inválido.
- **`print("Método de pago no válido...")`**: Muestra advertencia e invita a corregir la opción.
- **`precio_final = precio_base - descuento + recargo`**: Calcula la transacción neta aplicando la rebaja y el recargo respectivos.
- **`total_recaudado += precio_final`**: Añade el precio neto del cliente actual al total acumulado en caja.
- **`print(f"Precio final Cliente {i+1}...")`**: Muestra el desglose de pago del cliente en curso en pesos chilenos formateados.
- **`print("\n--- Reporte de Cierre de Caja ---")`**: Encabezado del desglose final al completarse las 25 iteraciones.
- **`print(...)`**: Imprime el resumen general de recaudación y frecuencias de medios de pago.


#### Código Completo
```python
print("--- Punto de Venta (25 Clientes) ---")
precio_base = 80000
total_recaudado = 0
efectivo_cnt = 0
debito_cnt = 0
credito_cnt = 0

# Ciclo determinado para procesar 25 transacciones
for i in range(25):
    print(f"\n--- Cliente {i+1} ---")
    # Validación interactiva del medio de pago
    while True:
        forma_pago = input("Ingrese forma de pago (efectivo / debito / credito): ").strip().lower()
        if forma_pago == "efectivo":
            descuento = 5000
            recargo = 0
            efectivo_cnt += 1
            break
        elif forma_pago in ["credito", "crédito"]:
            descuento = 0
            recargo = 3000
            credito_cnt += 1
            break
        elif forma_pago in ["debito", "débito"]:
            descuento = 0
            recargo = 0
            debito_cnt += 1
            break
        else:
            print("Método de pago no válido. Reintente.")

    # Cálculo e incremento del total facturado
    precio_final = precio_base - descuento + recargo
    total_recaudado += precio_final
    print(f"Precio final Cliente {i+1}: ${precio_final:,} CLP")

# Informe consolidated al cierre de operaciones de caja
print("\n--- Reporte de Cierre de Caja ---")
print(f"Total recaudado en el día: ${total_recaudado:,} CLP")
print(f"Pagos en efectivo: {efectivo_cnt}")
print(f"Pagos con débito: {debito_cnt}")
print(f"Pagos con crédito: {credito_cnt}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Punto de Venta (25 Clientes) ---

--- Cliente 1 ---
Ingrese forma de pago (efectivo / debito / credito): efectivo
Precio final Cliente 1: $75,000 CLP

--- Cliente 2 ---
Ingrese forma de pago (efectivo / debito / credito): débito
Precio final Cliente 2: $80,000 CLP
[... Se procesan clientes del 3 al 24 ...]

--- Cliente 25 ---
Ingrese forma de pago (efectivo / debito / credito): crédito
Precio final Cliente 25: $83,000 CLP
```
**Salida:**
```text
--- Reporte de Cierre de Caja ---
Total recaudado en el día: $1,972,000 CLP
Pagos en efectivo: 10
Pagos con débito: 8
Pagos con crédito: 7
```
