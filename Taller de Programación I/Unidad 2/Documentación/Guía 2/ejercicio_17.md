### Ejercicio 17: Caja registradora variable con n compras

#### Enunciado del Problema
Desarrolla un script que pida al usuario un número n, que representará la cantidad de compras a procesar. Para cada compra, debe pedir el monto total y aplicar estas reglas:
• Si la compra es mayor a $40.000 y hasta $100.000, se aplica un 10% de descuento
• Si la compra es superior a $100.000, se aplica un 20% de descuento
• Si la compra es de $40.000 o menos, no se aplica descuento
Al final, debe mostrar: Total vendido sin descuento, total descontado, total final recaudado.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `n` | `int` | Variable de control ingresada por el usuario que parametriza dinámicamente el número de transacciones. |
| `total_sin_descuento` | `float` | Acumulador decimal del costo original total de todos los productos cobrados sin rebaja. |
| `total_descontado` | `float` | Acumulador decimal del total de dinero descontado a lo largo de todas las transacciones. |
| `i` | `int` | Variable contadora del ciclo `for` que identifica a la compra actual (0 a n-1). |
| `monto` | `float` | Guarda el costo base decimal de la transacción en curso, validada no negativa. |
| `descuento` | `float` | Variable intermedia que almacena el descuento calculado exclusivamente para la transacción en curso. |
| `precio_final` | `float` | Variable temporal para almacenar el precio neta a pagar de la transacción actual. |
| `total_final` | `float` | Almacena la facturación neta neta final (total sin descuento menos el total descontado). |


## Lógica de la Solución
El programa procesa un flujo dinámico parametrizable de `n` transacciones comerciales. 1. **Validación de n:** Se solicita y valida que la cantidad de transacciones sea un entero estrictamente mayor a cero.2. **Ciclo parametrizado:** Corre un bucle `for i in range(n)` solicitando en cada paso el costo de venta base. El monto ingresado es validado para asegurar que no posea signo negativo (`monto >= 0`).3. **Cálculo de Descuento (DRY):** Se define la variable intermedia `descuento` evaluando con condicionales en cascada: - **Más de $100.000:** 20% de rebaja (`monto * 0.20`).- **Más de $40.000 y hasta $100.000:** 10% de rebaja (`monto * 0.10`).- **$40.000 o menos:** Sin descuento ($0).Se calculan los totales y se informan de forma inmediata en la consola. Al finalizar las `n` iteraciones, el script entrega un balance consolidado.

## Explicación Línea por Línea
- **`while True: (primero)`**: Bucle interactivo infinito de control para capturar de forma robusta la variable de control `n`.
- **`n = int(input(...))`**: Solicita la cantidad de compras, convirtiéndola a entero con `int()`, y la guarda en `n`.
- **`if n > 0:`**: Verifica lógicamente que la cantidad de compras sea un entero positivo.
- **`break`**: Sale del bucle de validación de `n` e inicia el procesamiento comercial.
- **`except ValueError: (primero)`**: Atrapa excepciones sintácticas si se digita texto en `n`.
- **`total_sin_descuento = 0.0`**: Inicializa en 0.0 el acumulador de montos de compra originales.
- **`total_descontado = 0.0`**: Inicializa en 0.0 el acumulador de dinero descontado.
- **`for i in range(n):`**: Inicia el ciclo principal parametrizado que iterará exactamente `n` veces consecutives.
- **`while True: (segundo)`**: Bucle interactivo interno de validación para capturar con seguridad el costo de la compra actual.
- **`monto = float(input(...))`**: Solicita el monto bruto de la compra actual, convirtiéndolo a decimal y guardándolo en `monto`.
- **`if monto >= 0:`**: Verifica lógicamente que el monto no sea un valor negativo.
- **`break`**: Sale del bucle de validación interna al confirmarse un monto decimal válido.
- **`except ValueError: (segundo)`**: Atrapa excepciones si el costo de la compra es alfanumérico.
- **`if monto > 100000:`**: Evalúa si el costo de la compra actual es estrictamente superior a $100.000 pesos.
- **`descuento = monto * 0.20`**: Calcula la rebaja correspondiente al 20% del valor base y la asigna a la variable intermedia.
- **`elif monto > 40000:`**: Filtro en cascada. Evalúa si el costo de la compra es estrictamente mayor a $40.000 pesos.
- **`descuento = monto * 0.10`**: Calcula la rebaja correspondiente al 10% del valor base y la asigna a la variable intermedia.
- **`else:`**: Se ejecuta por descarte si el costo de la compra es menor o igual a $40.000 pesos.
- **`descuento = 0.0`**: Se asigna un descuento nulo a la variable intermedia.
- **`total_sin_descuento += monto`**: Añade el monto de compra original bruto del cliente al acumulador correspondiente.
- **`total_descontado += descuento`**: Añade el descuento calculado del cliente al acumulador correspondiente.
- **`precio_final = monto - descuento`**: Calcula el precio final neto restando el descuento determinado al monto bruto.
- **`print(f"Compra {i+1} | Original...")`**: Informa al instante los detalles de la venta actual con dos decimales.
- **`total_final = total_sin_descuento - total_descontado`**: Calcula la facturación neta final recaudada.
- **`print("\n--- Consolidado de Ventas ---")`**: Encabezado impreso tras concluir las `n` transacciones del ciclo.
- **`print(...)`**: Imprime los reportes financieros consolidados de la caja registradora.


#### Código Completo
```python
print("--- Procesamiento de n Compras ---")
# Captura y validación de la cantidad de compras n
while True:
    try:
        n = int(input("¿Cuántas compras desea procesar hoy?: "))
        if n > 0:
            break
        print("Error: La cantidad de compras debe ser mayor a cero.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

total_sin_descuento = 0.0
total_descontado = 0.0

# Ciclo dinámico controlado por la variable n
for i in range(n):
    # Validación interactiva interna de cada transacción
    while True:
        try:
            monto = float(input(f"Monto de la compra {i+1} de {n}: $"))
            if monto >= 0:
                break
            print("Error: El monto no puede ser negativo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

    # Lógica de cálculo DRY de descuentos escalonados
    if monto > 100000:
        descuento = monto * 0.20
    elif monto > 40000:
        descuento = monto * 0.10
    else:
        descuento = 0.0

    # Acumulación de valores e informes individuales inmediatos
    total_sin_descuento += monto
    total_descontado += descuento
    precio_final = monto - descuento
    print(f"Compra {i+1} | Original: ${monto:,.2f} | Descuento: ${descuento:,.2f} | Pagar: ${precio_final:,.2f}")

# Reporte financiero consolidated final
total_final = total_sin_descuento - total_descontado
print("\n--- Consolidado de Ventas ---")
print(f"Total vendido sin descuento: ${total_sin_descuento:,.2f} CLP")
print(f"Total descontado del día    : ${total_descontado:,.2f} CLP")
print(f"Total neto final recaudado  : ${total_final:,.2f} CLP")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Procesamiento de n Compras ---
¿Cuántas compras desea procesar hoy?: 3
Monto de la compra 1 de 3: 35000
Compra 1 | Original: $35,000.00 | Descuento: $0.00 | Pagar: $35,000.00
Monto de la compra 2 de 3: 50000
Compra 2 | Original: $50,000.00 | Descuento: $5,000.00 | Pagar: $45,000.00
Monto de la compra 3 de 3: 120000
Compra 3 | Original: $120,000.00 | Descuento: $24,000.00 | Pagar: $96,000.00
```
**Salida:**
```text
--- Consolidado de Ventas ---
Total vendido sin descuento: $205,000.00 CLP
Total descontado del día    : $29,000.00 CLP
Total neto final recaudado  : $176,000.00 CLP
```
