### Ejercicio 10: Cálculo de Forma de Pago y Recargos/Descuentos

#### Enunciado del Problema
Desarrolla un script que considere un producto con precio base de $\$80.000$. Luego, debe pedir al usuario la forma de pago: efectivo, débito o crédito.
Aplica las siguientes reglas:
* Si paga con efectivo, se realiza un descuento de $\$5.000$.
* Si paga con crédito, se aplica un recargo de $\$3.000$.
* Si paga con débito, el precio no cambia.

El script debe mostrar el precio final a pagar.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `precio_base` | `int` | Constante entera inicializada en $80000$ que representa el costo estándar del artículo. |
| `forma_pago` | `str` | Almacena la opción de pago seleccionada por el usuario (sanitizada, sin espacios y en minúsculas). |
| `variacion` | `int` | Representa la alteración del precio: descuento (valor negativo) o recargo (valor positivo). |
| `detalle_movimiento` | `str` | Cadena descriptiva explicativa del descuento o recargo aplicado para el recibo final. |
| `precio_final` | `int` | Almacena el cálculo matemático final de la transacción (`precio_base + variacion`). |

#### Lógica de la Solución
El algoritmo soluciona la transacción comercial optimizando la entrada de texto libre del usuario mediante la técnica de **sanitización y normalización de strings**. Los programas interactivos suelen fallar si el usuario escribe tildes, mayúsculas o espacios accidentales. 
Para resolver esto, el script:
1. Pide la forma de pago en un bucle interactivo.
2. Elimina espacios en los extremos y convierte todo a minúsculas con `.strip().lower()`.
3. Normaliza las variantes ortográficas del español (ej. mapea `"crédito"` $\to$ `"credito"`; `"débito"` $\to$ `"debito"`).
4. Valida la pertenencia de la entrada contra el conjunto de métodos soportados (`["efectivo", "credito", "debito"]`).

Una vez validado el método, se asignan de forma condicional los valores de `variacion` y `detalle_movimiento` empleando `if-elif-else`. Finalmente, se aplica una ecuación unificada de liquidación (`precio_final = precio_base + variacion`) bajo el principio DRY.

#### Explicación Línea por Línea
* **Línea 5 (`precio_base = 80000`):** Define el precio base del producto a comercializar.
* **Línea 7 (`while True:`):** Declara el bucle infinito para la captura robusta del método de pago.
* **Línea 8 (`forma_pago = input(...).strip().lower()`):** Captura el método de pago por teclado, remueve espacios y convierte la cadena a minúsculas.
* **Línea 10 (`if forma_pago == "crédito":`):** Estructura que evalúa si el usuario escribió la palabra "crédito" con acentuación.
* **Línea 11 (`forma_pago = "credito"`):** Reasigna la cadena sin tilde para estandarizar la evaluación posterior.
* **Líneas 12-13 (`elif forma_pago == "débito":`):** Estandariza la palabra "débito" eliminando su tilde.
* **Línea 15 (`if forma_pago in ["efectivo", "credito", "debito"]:`):** Comprueba mediante el operador de pertenencia `in` si la entrada sanitizada forma parte de las opciones permitidas.
* **Línea 16 (`break`):** Rompe la iteración de validación del método de pago al hallar coincidencia exacta.
* **Línea 17 (`else:`):** Rama en caso de un método de pago no reconocido.
* **Línea 18 (`print(...)`):** Muestra el mensaje de advertencia e inicia una nueva petición.
* **Líneas 21-23 (`if forma_pago == "efectivo":`):** Si el pago es en efectivo, define la variación de precio como $-5000$ (descuento) y guarda la descripción en `detalle_movimiento`.
* **Líneas 24-26 (`elif forma_pago == "credito":`):** Si el pago es a crédito, define la variación de precio como $+3000$ (recargo) y guarda la descripción.
* **Líneas 27-29 (`else:`):** Si es débito, define la variación en $0$ y setea el mensaje respectivo.
* **Línea 31 (`precio_final = precio_base + variacion`):** Operación unificada final de liquidación comercial.
* **Líneas 34-37 (`print(...)`):** Imprime de manera estructurada el recibo final, utilizando el formato de coma para separador de miles en los valores numéricos (`:,`).

#### Código Completo
```python
# Cálculo de forma de pago y recargos/descuentos (DRY)

print("--- Punto de Venta - Precio Final ---")
precio_base = 80000

while True:
    forma_pago = input("Ingrese forma de pago (efectivo / débito / crédito): ").strip().lower()
    # Normalización para ignorar tildes en la comparación
    if forma_pago == "crédito":
        forma_pago = "credito"
    elif forma_pago == "débito":
        forma_pago = "debito"
        
    # Comprobación de pertenencia
    if forma_pago in ["efectivo", "credito", "debito"]:
        break
    else:
        print("Método de pago inválido. Por favor, intente nuevamente.")

# Cálculo condicional de variaciones y montos
if forma_pago == "efectivo":
    variacion = -5000
    detalle_movimiento = "Descuento por Efectivo: -$5.000"
elif forma_pago == "credito":
    variacion = 3000
    detalle_movimiento = "Recargo por Tarjeta de Crédito: +$3.000"
else:
    variacion = 0
    detalle_movimiento = "Sin descuentos ni recargos en Débito"

# Fórmula unificada
precio_final = precio_base + variacion

# Impresión unificada limpia con formato de miles
print(f"\n--- Resumen de Venta ---")
print(f"Precio Base: ${precio_base:,}")
print(f"Detalle: {detalle_movimiento}")
print(f"Total Neto a Pagar: ${precio_final:,} CLP")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Pago en Efectivo):
* **Entrada esperada:** `EFECTIVO`
* **Salida del programa:**
  ```text
  --- Resumen de Venta ---
  Precio Base: $80,000
  Detalle: Descuento por Efectivo: -$5.000
  Total Neto a Pagar: $75,000 CLP
  ```

##### Caso de Uso 2 (Pago con Crédito con Tilde):
* **Entrada esperada:** `crédito`
* **Salida del programa:**
  ```text
  --- Resumen de Venta ---
  Precio Base: $80,000
  Detalle: Recargo por Tarjeta de Crédito: +$3.000
  Total Neto a Pagar: $83,000 CLP
  ```

##### Caso de Uso 3 (Pago con Débito):
* **Entrada esperada:** `debito`
* **Salida del programa:**
  ```text
  --- Resumen de Venta ---
  Precio Base: $80,000
  Detalle: Sin descuentos ni recargos en Débito
  Total Neto a Pagar: $80,000 CLP
  ```

##### Caso de Uso 4 (Error de entrada y recuperación):
* **Entrada esperada:** `cheque` (luego) `efectivo`
* **Salida del programa:**
  ```text
  Ingrese forma de pago (efectivo / débito / crédito): cheque
  Método de pago inválido. Por favor, intente nuevamente.
  Ingrese forma de pago (efectivo / débito / crédito): efectivo
  
  --- Resumen de Venta ---
  Precio Base: $80,000
  Detalle: Descuento por Efectivo: -$5.000
  Total Neto a Pagar: $75,000 CLP
  ```
