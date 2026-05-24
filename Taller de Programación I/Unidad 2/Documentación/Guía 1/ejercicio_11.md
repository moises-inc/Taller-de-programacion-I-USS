### Ejercicio 11: Sistema de Facturación de Arriendo de Autos

#### Enunciado del Problema
Desarrolla un script para una compañía de arriendo de autos que cobra una tarifa fija de $\$50.000$ por día.
Debes pedir al usuario la cantidad de días de arriendo y calcular el valor final según estas reglas:
* Si arrienda más de $7$ días, obtiene un $25\%$ de descuento sobre el total.
* Si arrienda más de $3$ días y hasta $7$ días, obtiene un $10\%$ de descuento sobre el total.
* Si arrienda $3$ días o menos, no recibe descuento.

El script debe mostrar el total a pagar.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `tarifa_diaria` | `int` | Constante entera inicializada en $50000$ que representa la tarifa base diaria de arriendo. |
| `dias` | `int` | Cantidad de días de alquiler solicitada por el usuario (validada estrictamente $> 0$). |
| `costo_bruto` | `int` | Monto bruto calculado antes de aplicar cualquier rebaja comercial (`tarifa_diaria * dias`). |
| `porcentaje_dcto` | `int` | Tasa porcentual de descuento asignada condicionalmente ($0$, $10$ o $25$). |
| `descuento` | `int` | Valor numérico monetario descontado del total bruto, truncado a entero. |
| `total_pagar` | `int` | Monto neto final facturado y exigible al usuario (`costo_bruto - descuento`). |

#### Lógica de la Solución
El algoritmo soluciona de forma precisa el modelo comercial de arriendo. El script original presentaba imprecisiones de cálculo aritmético al calcular el descuento por separado sobre la tarifa unitaria diaria y multiplicar de forma anómala.
La lógica correcta y optimizada implementa los siguientes pasos:
1. **Captura y validación robusta:** Asegura que los días ingresados correspondan a un valor de tipo entero (`int`) y que este sea mayor que cero ($0$).
2. **Cálculo del costo acumulado:** Determina el subtotal inicial mediante la multiplicación de la tarifa por los días rentados: $\text{costo\_bruto} = \text{tarifa\_diaria} \times \text{dias}$.
3. **Clasificación condicional de descuentos:** Determina el porcentaje de rebaja analizando los rangos de días mediante una estructura selectiva anidada:
   * $\text{dias} > 7 \implies 25\%$
   * $3 < \text{dias} \le 7 \implies 10\%$
   * $\text{dias} \le 3 \implies 0\%$
4. **Cálculo del Neto Facturado:** Aplica la tasa de descuento al costo bruto total, convirtiendo el resultado a entero (debido a que el peso chileno no utiliza fracciones), y lo sustrae para obtener el total a pagar.
5. **Salida DRY:** Emplea un solo bloque final para el recibo.

#### Explicación Línea por Línea
* **Línea 5 (`tarifa_diaria = 50000`):** Establece el valor por defecto del arriendo diario del automóvil.
* **Línea 7 (`while True:`):** Inicia el bucle de validación de entrada de datos.
* **Línea 8 (`try:`):** Establece la zona de resguardo para la captura de enteros.
* **Línea 9 (`dias = int(input(...))`):** Pide la cantidad de días y la convierte a entero (`int`).
* **Línea 10 (`if dias > 0:`):** Valida que la cantidad de días sea un período de tiempo real estrictamente positivo.
* **Línea 11 (`break`):** Sale del ciclo interactivo si la condición se cumple.
* **Línea 12 (`else:`):** Flujo para valores menores o iguales a 0.
* **Línea 13 (`print(...)`):** Despliega el error explicativo sobre días no válidos.
* **Línea 14 (`except ValueError:`):** Intercepta texto libre o números flotantes ingresados de forma errónea.
* **Línea 15 (`print(...)`):** Informa al usuario acerca del tipo de dato requerido.
* **Línea 17 (`costo_bruto = tarifa_diaria * dias`):** Calcula aritméticamente el subtotal bruto acumulado por los días de arriendo.
* **Líneas 20-25 (`if-elif-else`):** Evalúa los límites en cascada de mayor a menor para definir el porcentaje de descuento a aplicar:
  * Si `dias > 7`, el porcentaje es `25`.
  * Si no, pero `dias > 3`, el porcentaje es `10`.
  * En cualquier otro caso, el porcentaje es `0`.
* **Línea 27 (`descuento = int(costo_bruto * (porcentaje_dcto / 100))`):** Calcula el valor monetario del descuento aplicando el porcentaje al total acumulado y lo fuerza a tipo `int`.
* **Línea 28 (`total_pagar = costo_bruto - descuento`):** Obtiene el total final neto restando el descuento al costo bruto.
* **Líneas 31-35 (`print(...)`):** Despliega detalladamente la boleta de facturación, aplicando formato de miles a todas las cifras en moneda local (`:,`).

#### Código Completo
```python
# Sistema de facturación de arriendo de autos (Corregido y DRY)

print("--- Rent-a-Car: Cálculo de Arriendo ---")
tarifa_diaria = 50000

# Entrada estructurada y validación de cantidad de días
while True:
    try:
        dias = int(input("Ingrese la cantidad de días de arriendo: "))
        if dias > 0:
            break
        else:
            print("La cantidad de días debe ser mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Cálculo bruto de la tarifa
costo_bruto = tarifa_diaria * dias

# Clasificación secuencial de descuentos según rangos
if dias > 7:
    porcentaje_dcto = 25
elif dias > 3:
    porcentaje_dcto = 10
else:
    porcentaje_dcto = 0

# Deducción matemática final
descuento = int(costo_bruto * (porcentaje_dcto / 100))
total_pagar = costo_bruto - descuento

# Impresión del recibo de facturación consolidada
print(f"\n--- Recibo de Facturación ---")
print(f"Días rentados: {dias}")
print(f"Precio base acumulado ({dias} x ${tarifa_diaria:,}): ${costo_bruto:,}")
print(f"Descuento aplicado ({porcentaje_dcto}%): -${descuento:,}")
print(f"Monto total final a pagar: ${total_pagar:,} CLP")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (3 días o menos - Sin Descuento):
* **Entrada esperada:** `3`
* **Salida del programa:**
  ```text
  --- Recibo de Facturación ---
  Días rentados: 3
  Precio base acumulado (3 x $50,000): $150,000
  Descuento aplicado (0%): -$0
  Monto total final a pagar: $150,000 CLP
  ```

##### Caso de Uso 2 (Entre 3 y 7 días - Descuento del 10%):
* **Entrada esperada:** `5`
* **Salida del programa:**
  ```text
  --- Recibo de Facturación ---
  Días rentados: 5
  Precio base acumulado (5 x $50,000): $250,000
  Descuento aplicado (10%): -$25,000
  Monto total final a pagar: $225,000 CLP
  ```

##### Caso de Uso 3 (Más de 7 días - Descuento del 25%):
* **Entrada esperada:** `10`
* **Salida del programa:**
  ```text
  --- Recibo de Facturación ---
  Días rentados: 10
  Precio base acumulado (10 x $50,000): $500,000
  Descuento aplicado (25%): -$125,000
  Monto total final a pagar: $375,000 CLP
  ```

##### Caso de Uso 4 (Entrada no válida y resolución):
* **Entrada esperada:** `-5` (luego) `cero` (luego) `8`
* **Salida del programa:**
  ```text
  Ingrese la cantidad de días de arriendo: -5
  La cantidad de días debe ser mayor a cero.
  Ingrese la cantidad de días de arriendo: cero
  Entrada no válida. Por favor, ingrese un número entero.
  Ingrese la cantidad de días de arriendo: 8
  
  --- Recibo de Facturación ---
  Días rentados: 8
  Precio base acumulado (8 x $50,000): $400,000
  Descuento aplicado (25%): -$100,000
  Monto total final a pagar: $300,000 CLP
  ```
