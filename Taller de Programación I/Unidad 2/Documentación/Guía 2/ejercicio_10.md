### Ejercicio 10: Cálculo de forma de pago y recargos/descuentos

#### Enunciado del Problema
Desarrolla un script que considere un producto con precio base de $80.000. Luego, debe pedir al usuario la forma de pago: efectivo, débito o crédito. Aplica las siguientes reglas:
- Si paga con efectivo, se realiza un descuento de $5.000.
- Si paga con crédito, se aplica un recargo de $3.000.
- Si paga con débito, el precio no cambia.
El script debe mostrar el precio final a pagar.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `precio_base` | `int` | Constante entera fija en $80.000 que representa el valor original de venta del artículo. |
| `forma_pago` | `str` | Almacena y normaliza el método de pago elegido (efectivo, débito, crédito). |
| `variacion` | `int` | Almacena algebraicamente el descuento (número negativo) o recargo (número positivo). |
| `detalle` | `str` | Mensaje de texto descriptivo del cambio monetario para imprimir en el resumen final. |
| `precio_final` | `int` | Precio neto final calculado que debe cancelar el comprador. |


## Lógica de la Solución
El programa simula un terminal de Punto de Venta (POS) con variaciones de tarifa dependientes del medio de pago seleccionado. Para lograr un procesamiento robusto y evitar rechazos por tildes o mayúsculas, el script aplica una normalización activa de la entrada: pasa todo a minúsculas con `.lower()`, elimina espacios extra con `.strip()` y reemplaza explícitamente palabras acentuadas (`débito` a `debito` y `crédito` a `credito`). Posteriormente, implementa el principio DRY utilizando una variable intermedia `variacion` que guarda el valor del recargo o descuento. Al finalizar el condicional, se aplica la fórmula aritmética `precio_final = precio_base + variacion` y se despliega una boleta de venta estructurada.

## Explicación Línea por Línea
- **`precio_base = 80000`**: Define el precio original fijo del producto como una constante entera.
- **`while True:`**: Bucle interactivo de captura del medio de pago para forzar una selección admitida por el POS.
- **`forma_pago = input(...).strip().lower()`**: Solicita la forma de pago, remueve espacios vacíos con `.strip()` y pasa el texto a minúsculas mediante `.lower()`.
- **`if forma_pago == "crédito":`**: Verifica si el cliente escribió la palabra crédito conteniendo tilde ortográfica.
- **`forma_pago = "credito"`**: Reescribe el valor en minúscula y sin tilde para simplificar las evaluaciones lógicas posteriores.
- **`elif forma_pago == "débito":`**: Verifica el ingreso de débito con tilde.
- **`forma_pago = "debito"`**: Normaliza débito a su equivalente plano sin acentos ortográficos.
- **`if forma_pago in ["efectivo", "credito", "debito"]:`**: Comprueba si la cadena normalizada se encuentra en el conjunto de formas de pago aceptadas.
- **`break`**: Sale del bucle de validación al confirmarse un medio de pago admitido por el sistema.
- **`else:`**: Se ejecuta si la palabra escrita no coincide con las opciones.
- **`print("Método de pago inválido...")`**: Muestra advertencia e invita a escribir la opción correcta.
- **`if forma_pago == "efectivo":`**: Evalúa si el cliente cancelará su compra empleando dinero en efectivo.
- **`variacion = -5000`**: Determina una variación de -$5.000 pesos en la variable intermedia (número negativo para restar en la suma).
- **`detalle = "Descuento por Efectivo..."`**: Asigna la glosa descriptiva de la rebaja.
- **`elif forma_pago == "credito":`**: Evalúa si el cliente utilizará tarjeta de crédito bancaria.
- **`variacion = 3000`**: Aplica un incremento positivo de +$3.000 pesos a la variable `variacion`.
- **`detalle = "Recargo por Tarjeta..."`**: Asigna la glosa explicativa del recargo de crédito.
- **`else:`**: Bloque ejecutado al seleccionarse débito por descarte de condiciones.
- **`variacion = 0`**: La variación de precio es nula en pagos con débito.
- **`detalle = "Sin descuentos..."`**: Establece la glosa neutra del cobro de débito.
- **`precio_final = precio_base + variacion`**: Aplica la suma algebraica de la variación para calcular el valor neto a cancelar.
- **`print(...)`**: Imprime una boleta de venta estructurada con separador de miles mediante la directiva `{precio_base:,}`.


#### Código Completo
```python
# Inicialización de precio base
precio_base = 80000

# Bucle de captura con normalización de caracteres ortográficos
while True:
    forma_pago = input("Ingrese forma de pago (efectivo / débito / crédito): ").strip().lower()
    if forma_pago == "crédito":
        forma_pago = "credito"
    elif forma_pago == "débito":
        forma_pago = "debito"
        
    # Validación lógica de membresía en lista
    if forma_pago in ["efectivo", "credito", "debito"]:
        break
    else:
        print("Método de pago inválido. Intente nuevamente.")

# Cálculo DRY del recargo o descuento en variable intermedia
if forma_pago == "efectivo":
    variacion = -5000
    detalle = "Descuento por Efectivo: -$5.000"
elif forma_pago == "credito":
    variacion = 3000
    detalle = "Recargo por Tarjeta de Crédito: +$3.000"
else:
    variacion = 0
    detalle = "Sin descuentos ni recargos en Débito"

# Determinación y desglose de boleta de venta final
precio_final = precio_base + variacion

print(f"\n--- Resumen de Venta ---")
print(f"Precio Base: ${precio_base:,}")
print(f"Detalle: {detalle}")
print(f"Total Neto a Pagar: ${precio_final:,} CLP")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese forma de pago (efectivo / débito / crédito): cheque
Método de pago inválido. Intente nuevamente.
Ingrese forma de pago (efectivo / débito / crédito): Crédito
```
**Salida:**
```text
--- Resumen de Venta ---
Precio Base: $80,000
Detalle: Recargo por Tarjeta de Crédito: +$3.000
Total Neto a Pagar: $83,000 CLP
```
