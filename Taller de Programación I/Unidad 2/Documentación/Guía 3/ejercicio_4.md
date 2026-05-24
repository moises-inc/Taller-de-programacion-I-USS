### Ejercicio 4: Registro de ventas en feria agrícola

#### Enunciado del Problema
En una feria agrícola local, distintos productores venden frutas y verduras durante la mañana. El encargado necesita registrar las ventas realizadas para conocer el comportamiento del día.
Desarrolla un script en Python que permita registrar ventas hasta que el usuario decida terminar. El programa debe:
- Usar un diccionario donde la clave sea el nombre del producto y el valor sea la cantidad total vendida.
- Solicitar repetidamente al usuario:
    + Nombre del producto vendido.
    + Cantidad vendida.
- Si el producto ya existe en el diccionario, se debe sumar la nueva cantidad a la cantidad anterior.
- El ingreso de ventas debe continuar hasta que el usuario escriba "fin".
- Al finalizar, mostrar:
    + Todos los productos vendidos con sus cantidades.
    + El producto más vendido.
    + La cantidad total de unidades vendidas entre todos los productos.

Consideraciones:
- Este ejercicio debe usar un ciclo de duración desconocida, por ejemplo `while`.
- Dentro del `while`, se puede recorrer el diccionario con `for` para obtener los resultados finales.
- Se recomienda calcular manualmente el producto más vendido para practicar comparación y recorrido.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `ventas` | `dict` | Diccionario que mapea nombres de productos (claves, `str`) a sus unidades totales vendidas (valores, `int`). |
| `producto` | `str` | Nombre del producto ingresado por el usuario (normalizado a minúsculas). |
| `cantidad` | `int` | Cantidad de unidades vendidas del producto ingresado en la transacción actual. |
| `total_unidades` | `int` | Acumulador manual para la cantidad total de unidades vendidas (reemplaza a `sum()`). |
| `producto_mas_vendido`| `str` | Clave del producto que registra la mayor cantidad acumulada de ventas. |
| `cantidad_maxima` | `int` | Centinela para almacenar la frecuencia de ventas del producto estrella (reemplaza a `max()`). |
| `prod` | `str` | Variable de iteración que representa la clave (nombre del producto) en `ventas.items()`. |
| `cant` | `int` | Variable de iteración que representa el valor (cantidad) en `ventas.items()`. |

---

#### Lógica de la Solución
1. **Estructura Clave-Valor Dinámica (Diccionario):** Se utiliza un diccionario `ventas = {}` porque permite la indexación directa por cadenas de texto (`str`). Esto facilita buscar si un producto ya ha sido vendido previamente y actualizar su valor de forma inmediata sin recorrer toda la colección.
2. **Ciclo Invalidador y Normalización de Cadenas:** Se captura la entrada del producto y se procesa con `.strip().lower()` para eliminar espacios sobrantes y evitar que "Manzana", "manzana" y "MANZANA " sean consideradas claves separadas en el diccionario.
3. **Control Acumulativo de Claves Existentes:** Al ingresar una venta, se verifica la presencia de la clave usando el operador de pertenencia `if producto in ventas`. Si existe, se suma al valor anterior; en caso contrario, se inicializa la clave con la cantidad actual en el diccionario.
4. **Algoritmo de Recorrido Manual Exhaustivo:** Cumpliendo estrictamente las consideraciones pedagógicas del curso, se itera sobre los pares clave-valor del diccionario mediante `ventas.items()`. Se calcula la suma global y el máximo absoluto de manera secuencial, empleando centinelas manuales en vez de funciones directas de Python.

---

#### Explicación Línea por Línea
- **Línea 5:** `ventas = {}`: Inicializa un diccionario vacío para almacenar las ventas consolidadas.
- **Línea 7:** `while True:`: Inicia el ciclo principal de duración indefinida para la recepción continua de transacciones.
- **Línea 8:** `producto = input(...).strip().lower()`: Captura la entrada del producto, removiendo espacios en los extremos con `.strip()` y convirtiéndolo a minúsculas con `.lower()` para homologar las claves del diccionario.
- **Línea 9:** `if producto == "fin":`: Evalúa la condición de término de la caja registradora. Si se cumple, ejecuta un `break` para salir del bucle de captura.
- **Línea 11:** `if not producto:`: Cláusula de seguridad que impide registrar productos con nombres vacíos (presionar Enter directamente).
- **Línea 15:** `while True:`: Bucle interno de validación para asegurar el ingreso de una cantidad correcta.
- **Líneas 16 a 22:** `try-except ValueError`: Captura entradas que no correspondan a números enteros. Valida que `cantidad > 0`, ya que no se pueden vender cantidades negativas o nulas en la feria. Si es correcta, rompe el bucle de validación con `break`.
- **Línea 25:** `if producto in ventas:`: Operador de pertenencia que consulta si la clave ya existe en el diccionario.
- **Línea 26:** `ventas[producto] += cantidad`: De existir la clave, incrementa de manera acumulativa su valor previo.
- **Línea 28:** `ventas[producto] = cantidad`: Si la clave es nueva, la añade al diccionario y le asigna la cantidad ingresada.
- **Línea 32:** `total_unidades = 0`: Inicializa a cero el acumulador global de mercancías vendidas.
- **Línea 33:** `producto_mas_vendido = ""`: Inicializa la cadena para registrar el nombre del producto estrella.
- **Línea 34:** `cantidad_maxima = -1`: Establece el centinela del máximo con un valor inferior al rango de validación para asegurar la asignación del primer elemento del recorrido.
- **Línea 36:** `print("\n--- Detalle de Ventas del Día ---")`: Encabezado del reporte diario de la feria.
- **Línea 37:** `for prod, cant in ventas.items():`: Recorre simultáneamente las tuplas de clave y valor provistas por el método `.items()` de la colección.
- **Línea 38:** `print(...)`: Imprime la clave formateada con la primera letra en mayúscula usando `.capitalize()`, junto con su cantidad asociada.
- **L...39:** `total_unidades += cant`: Suma de forma acumulativa la cantidad vendida al total del día.
- **Líneas 41 a 43:** `if cant > cantidad_maxima:`: Evalúa si la cantidad del producto actual es estrictamente mayor que la guardada en el centinela. Si se cumple, actualiza la `cantidad_maxima` y el `producto_mas_vendido`.
- **Líneas 46 a 51:** `if ventas:`: Bloque condicional que evalúa si el diccionario contiene elementos. Si es así, despliega el consolidado de métricas obtenidas manualmente; si está vacío, informa que no hubo actividad comercial en la jornada.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Caja Registradora de Feria Agrícola (Diccionario Acumulativo)
# ==============================================================================

print("--- Caja Registradora de Feria Agrícola ---")

# Diccionario para almacenar el stock acumulativo de ventas
ventas = {}

# Etapa 1: Captura de Transacciones (Ciclo Indefinido)
while True:
    producto = input("Ingrese nombre del producto vendido (o 'fin' para finalizar): ").strip().lower()
    
    # Condición de salida del sistema
    if producto == "fin":
        break
        
    # Impedir ingresos vacíos
    if not producto:
        print("El nombre del producto no puede quedar vacío.")
        continue
        
    # Validación de cantidad vendida (entero positivo)
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad vendida de {producto.capitalize()}: "))
            if cantidad > 0:
                break
            print("La cantidad vendida debe ser mayor a cero.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Registro acumulativo en el diccionario
    if producto in ventas:
        ventas[producto] += cantidad
    else:
        ventas[producto] = cantidad
    print(f"-> Registrados {cantidad} unidad(es) de {producto.capitalize()}.\")

# Etapa 2: Análisis Estadístico Manual (Evitando max() y sum())
total_unidades = 0
producto_mas_vendido = ""
cantidad_maxima = -1

print("\n--- Detalle de Ventas del Día ---")
for prod, cant in ventas.items():
    print(f"* {prod.capitalize()}: {cant} unidades")
    total_unidades += cant  # Suma manual
    
    # Búsqueda manual de máximo absoluto
    if cant > cantidad_maxima:
        cantidad_maxima = cant
        producto_mas_vendido = prod

# Mostrar reporte consolidado de la feria agrícola
if ventas:
    print(f"\nTotal acumulado de unidades vendidas en la feria: {total_unidades} unidades")
    print(f"Producto estrella del día: {producto_mas_vendido.capitalize()} (con {cantidad_maxima} unidades)")
else:
    print("\nNo se registraron ventas en la jornada.")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Venta Diversa y Acumulación Completa
```text
--- Caja Registradora de Feria Agrícola ---
Ingrese nombre del producto vendido (o 'fin' para finalizar): manzana
Ingrese la cantidad vendida de Manzana: 12
-> Registrados 12 unidad(es) de Manzana.
Ingrese nombre del producto vendido (o 'fin' para finalizar): papa
Ingrese la cantidad vendida de Papa: 50
-> Registrados 50 unidad(es) de Papa.
Ingrese nombre del producto vendido (o 'fin' para finalizar): manzana
Ingrese la cantidad vendida de Manzana: 8
-> Registrados 8 unidad(es) de Manzana.
Ingrese nombre del producto vendido (o 'fin' para finalizar): tomate
Ingrese la cantidad vendida de Tomate: 15
-> Registrados 15 unidad(es) de Tomate.
Ingrese nombre del producto vendido (o 'fin' para finalizar): fin

--- Detalle de Ventas del Día ---
* Manzana: 20 unidades
* Papa: 50 unidades
* Tomate: 15 unidades

Total acumulado de unidades vendidas en la feria: 85 unidades
Producto estrella del día: Papa (con 50 unidades)
```

##### Caso 2: Manejo de Errores e Ingresos Inválidos
```text
--- Caja Registradora de Feria Agrícola ---
Ingrese nombre del producto vendido (o 'fin' para finalizar): 
El nombre del producto no puede quedar vacío.
Ingrese nombre del producto vendido (o 'fin' para finalizar): lechuga
Ingrese la cantidad vendida de Lechuga: -5
La cantidad vendida debe ser mayor a cero.
Ingrese la cantidad vendida de Lechuga: abc
Entrada inválida. Por favor, ingrese un número entero.
Ingrese la cantidad vendida de Lechuga: 5
-> Registrados 5 unidad(es) de Lechuga.
Ingrese nombre del producto vendido (o 'fin' para finalizar): fin

--- Detalle de Ventas del Día ---
* Lechuga: 5 unidades

Total acumulado de unidades vendidas en la feria: 5 unidades
Producto estrella del día: Lechuga (con 5 unidades)
```
