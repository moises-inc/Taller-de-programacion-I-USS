### Ejercicio 12: Cálculo de Descuentos por Volumen de Compras

#### Enunciado del Problema
Desarrolla un script para una tienda que aplica descuentos según el monto de compra. Debes pedir al usuario el monto total de la compra y calcular el valor final a pagar considerando las siguientes reglas:
* Si la compra es mayor a $\$40.000$ y hasta $\$100.000$, se aplica un $10\%$ de descuento.
* Si la compra es superior a $\$100.000$, se aplica un $20\%$ de descuento.
* Si la compra es de $\$40.000$ o menos, no se aplica descuento.

El script debe mostrar el monto original, el descuento aplicado y el total a pagar.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `monto_compra` | `float` | Almacena el subtotal acumulado bruto de la compra (debe ser no negativo $\ge 0$). |
| `pct_dcto` | `int` | Representa la tasa condicional de descuento asignada ($0$, $10$ o $20$). |
| `descuento` | `float` | Valor numérico monetario del descuento (`monto_compra * (pct_dcto / 100)`). |
| `total_final` | `float` | Monto neto definitivo que el cliente debe pagar en caja (`monto_compra - descuento`). |

#### Lógica de la Solución
El algoritmo calcula deducciones porcentuales dinámicas según la escala de compra.
Para garantizar la robustez del script frente a excepciones:
1. Se implementa un ciclo interactivo que atrapa caracteres inválidos (`try-except` de `ValueError`).
2. Se añade un filtro condicional de validación comercial que descarta montos de compra negativos.

La clasificación y asignación de la tasa de descuento se realiza en orden jerárquico descendente para optimizar las evaluaciones lógicas:
* Si `monto_compra` es $> 100000 \implies$ se aplica el $20\%$.
* Si no, pero es $> 40000 \implies$ se aplica el $10\%$.
* De lo contrario $\implies$ se aplica $0\%$.

Finalmente, se calculan las diferencias matemáticas correspondientes y se delega la salida a un bloque único final bajo el principio DRY, formateando todos los decimales con precisión de dos dígitos y separadores de miles (`:,.2f`).

#### Explicación Línea por Línea
* **Línea 5 (`while True:`):** Inicia la estructura iterativa de control de ingresos.
* **Línea 6 (`try:`):** Apertura de la zona protegida para conversiones numéricas decimales.
* **Línea 7 (`monto_compra = float(input(...))`):** Captura el monto bruto por consola e intenta castearlo a flotante (`float`).
* **Línea 8 (`if monto_compra >= 0:`):** Valida que el monto bruto sea una cantidad no negativa comercialmente viable.
* **Línea 9 (`break`):** Rompe la iteración si el número es coherente y posee el formato correcto.
* **Línea 10 (`else:`):** Rama en caso de montos negativos.
* **Línea 11 (`print(...)`):** Muestra el mensaje explicativo sobre montos negativos.
* **Línea 12 (`except ValueError:`):** Atrapa las excepciones si la entrada contiene caracteres alfabéticos o no válidos.
* **Línea 13 (`print(...)`):** Informa al usuario acerca del tipo de dato requerido.
* **Líneas 16-21 (`if-elif-else`):** Evalúa progresivamente de mayor a menor el volumen de compra para asignar la tasa de descuento en la variable `pct_dcto`.
* **Línea 23 (`descuento = monto_compra * (pct_dcto / 100)`):** Calcula numéricamente el descuento.
* **Línea 24 (`total_final = monto_compra - descuento`):** Resta el descuento para liquidar el monto neto de la boleta.
* **Líneas 27-30 (`print(...)`):** Bloque único final de salida. Imprime los resultados formateados pedagógicamente con separadores de miles y dos decimales de precisión (`:,.2f`).

#### Código Completo
```python
# Cálculo de descuentos por volumen de compras (DRY)

print("--- Cálculo de Descuentos por Compra ---")

# Bucle interactivo con validación de entradas numéricas reales no negativas
while True:
    try:
        monto_compra = float(input("Ingrese el monto total de la compra: "))
        if monto_compra >= 0:
            break
        else:
            print("El monto de compra no puede ser negativo.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

# Asignación de tasa porcentual de descuento según escala comercial
if monto_compra > 100000:
    pct_dcto = 20
elif monto_compra > 40000:
    pct_dcto = 10
else:
    pct_dcto = 0

# Operaciones matemáticas
descuento = monto_compra * (pct_dcto / 100)
total_final = monto_compra - descuento

# Impresión detallada y unificada de la boleta de venta
print(f"\n--- Resumen de Caja ---")
print(f"Monto Original: ${monto_compra:,.2f}")
print(f"Descuento Aplicado ({pct_dcto}%): -${descuento:,.2f}")
print(f"Total Final a Pagar: ${total_final:,.2f} CLP")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Hasta 40.000 - Sin descuento):
* **Entrada esperada:** `35000`
* **Salida del programa:**
  ```text
  --- Resumen de Caja ---
  Monto Original: $35,000.00
  Descuento Aplicado (0%): -$0.00
  Total Final a Pagar: $35,000.00 CLP
  ```

##### Caso de Uso 2 (Entre 40.000 y 100.000 - 10% Descuento):
* **Entrada esperada:** `75000`
* **Salida del programa:**
  ```text
  --- Resumen de Caja ---
  Monto Original: $75,000.00
  Descuento Aplicado (10%): -$7,500.00
  Total Final a Pagar: $67,500.00 CLP
  ```

##### Caso de Uso 3 (Superior a 100.000 - 20% Descuento):
* **Entrada esperada:** `150000.50`
* **Salida del programa:**
  ```text
  --- Resumen de Caja ---
  Monto Original: $150,000.50
  Descuento Aplicado (20%): -$30,000.10
  Total Final a Pagar: $120,000.40 CLP
  ```

##### Caso de Uso 4 (Error de entrada y recuperación):
* **Entrada esperada:** `cien mil` (luego) `-5000` (luego) `120000`
* **Salida del programa:**
  ```text
  Ingrese el monto total de la compra: cien mil
  Entrada no válida. Por favor, ingrese un número.
  Ingrese el monto total de la compra: -5000
  El monto de compra no puede ser negativo.
  Ingrese el monto total de la compra: 120000
  
  --- Resumen de Caja ---
  Monto Original: $120,000.00
  Descuento Aplicado (20%): -$24,000.00
  Total Final a Pagar: $96,000.00 CLP
  ```
