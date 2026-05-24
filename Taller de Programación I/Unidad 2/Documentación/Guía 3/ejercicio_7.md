### Ejercicio 7: Control de stock en distribuidora de gas

#### Enunciado del Problema
Una distribuidora de gas necesita llevar el control del stock de cilindros durante la jornada. Existen distintos formatos de cilindros (por ejemplo: 5kg, 11kg, 15kg, 45kg), y durante el día se registran ventas y reposiciones.
Desarrolla un script en Python que permita gestionar esta situación. El programa debe:
- Inicializar los tipos de cilindros disponibles y su stock inicial.
- Permitir al usuario, mediante un menú repetitivo:
    1. Ver stock actual.
    2. Registrar venta de cilindros.
    3. Registrar reposición de cilindros.
    4. Ver historial de movimientos.
    5. Salir.
- Cada vez que se registre una venta o reposición, se debe guardar el movimiento realizado.
- Al finalizar el programa, se debe mostrar:
    + El stock final de cada tipo de cilindro.
    + El tipo de cilindro con menor stock.
    + La cantidad total de movimientos realizados durante el día.

Consideraciones:
- El programa debe mantenerse en ejecución hasta que el usuario decida salir (ciclo de duración desconocida).
- Se deben recorrer estructuras de datos para: Mostrar el stock, Analizar cuál tiene menor cantidad y Mostrar el historial de movimientos.
- Validar que no se puedan realizar ventas si no hay suficiente stock.
- El estudiante debe decidir qué estructuras de datos utilizar para representar los tipos de cilindros, el stock y los movimientos.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `stock_cilindros` | `dict` | Asocia cada formato de cilindro (`str`) con su stock disponible en bodega (`int`). |
| `historial_movimientos`| `list (dict)` | Lista que almacena diccionarios con el registro de cada movimiento realizado en el día. |
| `opcion` | `str` | Opción del menú interactivo (1-5) ingresada por el operario. |
| `formato` | `str` | Formato del cilindro seleccionado (5kg, 11kg, 15kg o 45kg), normalizado a minúsculas. |
| `cant` | `int` | Cantidad de cilindros a vender o reponer en la transacción actual. |
| `mov` | `dict` | Diccionario temporal que representa un movimiento: `{"tipo": tipo, "formato": formato, "cantidad": cant}`. |
| `formato_menor_stock`| `str` | Formato que presenta la menor cantidad disponible en bodega al cerrar la jornada. |
| `menor_stock` | `int` | Centinela manual numérico para hallar el menor stock final (inicializado en un valor muy alto). |

---

#### Lógica de la Solución
1. **Modelado Avanzado de Datos (Estructuras Híbridas):** Se utiliza un diccionario `stock_cilindros` para la manipulación y actualización inmediata de las existencias, y una lista de diccionarios `historial_movimientos` para registrar la bitácora de transacciones del día, permitiendo modelar operaciones complejas de bases de datos.
2. **Ciclo de Menú de Duración Indefinida:** Un ciclo `while True` mantiene activo el portal de control hasta que el usuario digita de forma explícita la opción 5.
3. **Validación de Regla de Negocio (Control de Quiebres):** Al registrar una venta (Opción 2), se verifica que el stock en bodega sea mayor o igual que la demanda solicitada. Si no se cuenta con existencias suficientes, se aborta la transacción y se informa el error al operario, evitando saldos negativos.
4. **Algoritmo de Mínimo Manual sobre Diccionarios:** Durante la fase de cierre de caja (Opción 5), se itera secuencialmente sobre `stock_cilindros.items()` para buscar de forma manual el formato con menor cantidad disponible en bodega mediante un valor centinela alto.

---

#### Explicación Línea por Línea
- **Líneas 6 a 11:** `stock_cilindros = {...}`: Inicializa el inventario base en un diccionario con existencias preestablecidas para 5kg, 11kg, 15kg y 45kg.
- **Línea 13:** `historial_movimientos = []`: Inicializa la lista vacía que funcionará como el libro diario de movimientos.
- **Línea 15:** `while True:`: Inicia el bucle operativo que controla el menú de la distribuidora.
- **Líneas 16 a 21:** `print(...)`: Presenta las opciones del panel en pantalla.
- **Línea 23:** `opcion = input(...).strip()`: Captura la opción del menú y remueve espacios en blanco.
- **Línea 25:** `if opcion == "1":`: Rama que despliega las existencias físicas actuales en bodega.
- **Líneas 27 y 28:** `for formato, cantidad in stock_cilindros.items():`: Recorre la colección e imprime la disponibilidad formateando los anchos de columna (`{formato:5}`).
- **Línea 30:** `elif opcion == "2":`: Rama para la facturación y despacho de ventas.
- **Líneas 32 a 35:** `formato = input(...).strip().lower()` y `if formato not in stock_cilindros:`: Captura el formato y valida su existencia mediante la pertenencia a las claves del diccionario.
- **Línea 36:** `while True:`: Bucle de validación para la cantidad vendida.
- **Líneas 37 a 43:** `try-except ValueError`: Captura entradas no enteras y obliga a ingresar valores estrictamente mayores a cero.
- **Líneas 46 a 51:** `if stock_cilindros[formato] >= cant:`: Verifica el stock disponible. Si se cumple, resta la cantidad, registra la transacción agregando un diccionario a la lista de movimientos y notifica al usuario. De lo contrario, advierte el quiebre de stock sin modificar los inventarios.
- **Línea 53:** `elif opcion == "3":`: Rama para registrar ingresos de reposiciones del proveedor.
- **Líneas 55 a 67:** Carga y valida el formato y la cantidad a reponer de la misma forma que en la venta, pero incrementando el stock en `stock_cilindros[formato] += cant` y guardando el evento en la bitácora.
- **Línea 69:** `elif opcion == "4":`: Rama que expone el historial de movimientos de inventario de la jornada.
- **Líneas 71 y 72:** `if not historial_movimientos:`: Indica si no se han registrado transacciones aún.
- **Líneas 73 a 75:** `for idx, mov in enumerate(historial_movimientos):`: Recorre secuencialmente la bitácora usando `enumerate()` para imprimir el número de registro correlativo junto con el desglose del tipo de transacción, formato y cantidad.
- **Línea 77:** `elif opcion == "5":`: Rama que ejecuta el consolidado financiero y cierre de caja, rompiendo el bucle principal.
- **Líneas 81 y 82:** `formato_menor_stock = ""` y `menor_stock = 9999999`: Inicializa variables centinelas para el cálculo manual del mínimo.
- **Línea 84:** `for formato, cantidad in stock_cilindros.items():`: Recorre el inventario de bodega para mostrar el stock de cierre e identificar cuál tiene menor stock.
- **Líneas 86 a 88:** `if cantidad < menor_stock:`: Actualiza el centinela si el elemento en curso es inferior al mínimo actual.
- **Líneas 90 y 91:** `print(...)`: Muestra el cilindro con menor stock final y la cantidad total de transacciones registradas usando `len(historial_movimientos)`.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Control de Stock y Bitácora de Movimientos (Estructuras Híbridas)
# ==============================================================================

print("--- Portal de Control: GasExpress ---")

# Inventario inicial en bodega (Diccionario Clave-Valor)
stock_cilindros = {
    "5kg": 25,
    "11kg": 30,
    "15kg": 20,
    "45kg": 10
}

# Bitácora diaria de transacciones (Lista de Diccionarios)
historial_movimientos = []

while True:
    print("\n=== MENÚ OPERATIVO DIARIO ===")
    print("1. Ver stock actual")
    print("2. Registrar venta de cilindros")
    print("3. Registrar reposición de cilindros")
    print("4. Ver historial de movimientos")
    print("5. Salir y Cerrar Caja")
    
    opcion = input("Ingrese su opción (1-5): ").strip()
    
    if opcion == "1":
        print("\n--- Stock Actual de Cilindros ---")
        for formato, cantidad in stock_cilindros.items():
            print(f"- Cilindro {formato:5}: {cantidad} unidad(es) en bodega")
            
    elif opcion == "2":
        print("\n--- Registrar Venta ---")
        formato = input("Ingrese formato a vender (5kg, 11kg, 15kg, 45kg): ").strip().lower()
        if formato not in stock_cilindros:
            print("Formato no reconocido. Intente nuevamente.")
            continue
        while True:
            try:
                cant = int(input(f"Cantidad de cilindros de {formato} a vender: "))
                if cant > 0:
                    break
                print("La cantidad de venta debe ser positiva.")
            except ValueError:
                print("Ingrese un número entero válido.")
        
        # Validación de Stock en Bodega para evitar quiebres o saldos negativos
        if stock_cilindros[formato] >= cant:
            stock_cilindros[formato] -= cant
            # Guardamos el movimiento en la lista
            historial_movimientos.append({"tipo": "Venta", "formato": formato, "cantidad": cant})
            print(f"¡Venta registrada! Se despacharon {cant} cilindros de {formato}.")
        else:
            print(f"¡Error de Stock! Solo quedan {stock_cilindros[formato]} unidades de {formato} en bodega.")
            
    elif opcion == "3":
        print("\n--- Registrar Reposición (Ingreso de Proveedor) ---")
        formato = input("Ingrese formato a reponer (5kg, 11kg, 15kg, 45kg): ").strip().lower()
        if formato not in stock_cilindros:
            print("Formato no reconocido. Intente nuevamente.")
            continue
        while True:
            try:
                cant = int(input(f"Cantidad de cilindros de {formato} a reponer: "))
                if cant > 0:
                    break
                print("La cantidad de reposición debe ser positiva.")
            except ValueError:
                print("Ingrese un número entero.")
        
        # Incremento del inventario y registro en bitácora
        stock_cilindros[formato] += cant
        historial_movimientos.append({"tipo": "Reposición", "formato": formato, "cantidad": cant})
        print(f"¡Reposición exitosa! Se ingresaron {cant} cilindros de {formato} al inventario.")
        
    elif opcion == "4":
        print("\n--- Historial de Movimientos de la Jornada ---")
        if not historial_movimientos:
            print("No se han registrado movimientos de inventario todavía.")
        else:
            for idx, mov in enumerate(historial_movimientos):
                print(f"{idx+1:2}. [{mov['tipo']:10}] {mov['cantidad']:3} cilindro(s) de {mov['formato']}")
                
    elif opcion == "5":
        print("\n--- CONSOLIDADO Y CIERRE DE CAJA ---")
        print("Inventario Final en Bodega:")
        
        # Algoritmo de búsqueda manual del mínimo sobre claves del diccionario
        formato_menor_stock = ""
        menor_stock = 9999999
        
        for formato, cantidad in stock_cilindros.items():
            print(f"* {formato:5}: {cantidad} unidades")
            if cantidad < menor_stock:
                menor_stock = cantidad
                formato_menor_stock = formato
                
        print(f"\nCilindro con menor disponibilidad física en bodega: {formato_menor_stock} (con {menor_stock} unidades)")
        print(f"Cantidad total de movimientos realizados en el día: {len(historial_movimientos)}")
        print("¡Jornada finalizada! Saliendo del sistema.")
        break
    else:
        print("Opción inválida. Marque un número del 1 al 5.")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Flujo Operativo Completo de Transacciones
```text
--- Portal de Control: GasExpress ---

=== MENÚ OPERATIVO DIARIO ===
1. Ver stock actual
2. Registrar venta de cilindros
3. Registrar reposición de cilindros
4. Ver historial de movimientos
5. Salir y Cerrar Caja
Ingrese su opción (1-5): 1

--- Stock Actual de Cilindros ---
- Cilindro 5kg  : 25 unidad(es) en bodega
- Cilindro 11kg : 30 unidad(es) en bodega
- Cilindro 15kg : 20 unidad(es) en bodega
- Cilindro 45kg : 10 unidad(es) en bodega

=== MENÚ OPERATIVO DIARIO ===
...
Ingrese su opción (1-5): 2

--- Registrar Venta ---
Ingrese formato a vender (5kg, 11kg, 15kg, 45kg): 11kg
Cantidad de cilindros de 11kg a vender: 5
¡Venta registrada! Se despacharon 5 cilindros de 11kg.

=== MENÚ OPERATIVO DIARIO ===
...
Ingrese su opción (1-5): 3

--- Registrar Reposición (Ingreso de Proveedor) ---
Ingrese formato a reponer (5kg, 11kg, 15kg, 45kg): 45kg
Cantidad de cilindros de 45kg a reponer: 10
¡Reposición exitosa! Se ingresaron 10 cilindros de 45kg al inventario.

=== MENÚ OPERATIVO DIARIO ===
...
Ingrese su opción (1-5): 4

--- Historial de Movimientos de la Jornada ---
 1. [Venta     ]   5 cilindro(s) de 11kg
 2. [Reposición]  10 cilindro(s) de 45kg

=== MENÚ OPERATIVO DIARIO ===
...
Ingrese su opción (1-5): 5

--- CONSOLIDADO Y CIERRE DE CAJA ---
Inventario Final en Bodega:
* 5kg  : 25 unidades
* 11kg : 25 unidades
* 15kg : 20 unidades
* 45kg : 20 unidades

Cilindro con menor disponibilidad física en bodega: 15kg (con 20 unidades)
Cantidad total de movimientos realizados en el día: 2
¡Jornada finalizada! Saliendo del sistema.
```
