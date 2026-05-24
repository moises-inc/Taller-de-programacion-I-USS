### Ejercicio 10: Sistema de operación diaria en centro de distribución

#### Enunciado del Problema
Un centro de distribución en Chile gestiona diariamente pedidos de distintos clientes. Cada pedido incluye productos, cantidades y un estado (por ejemplo: “pendiente”, “despachado”, “entregado”).
Desarrolla un script en Python que simule la operación de un día completo. El programa debe:
- Permitir registrar pedidos de forma repetitiva hasta que el usuario decida finalizar.
- Para cada pedido se debe ingresar:
    + Nombre del cliente.
    + Lista de productos (pueden ser varios por pedido).
    + Cantidad por producto.
    + Estado del pedido.
- Durante el registro, el sistema debe permitir:
    + Agregar múltiples productos a un mismo pedido.
    + Registrar múltiples pedidos en el día.

Al finalizar, el programa debe mostrar:
- Cantidad total de pedidos registrados.
- Cantidad total de productos despachados (sumando todas las cantidades).
- Cantidad de pedidos por estado.
- Cliente con mayor cantidad total de productos solicitados.
- Listado completo de pedidos con su detalle.

Consideraciones:
- El registro de pedidos debe realizarse con un ciclo de duración desconocida (`while`).
- Para agregar múltiples productos a un pedido, se debe utilizar otro ciclo anidado.
- Se deben recorrer estructuras para realizar los cálculos finales.
- El estudiante debe decidir cómo representar cada pedido, los productos dentro de un pedido y el conjunto total de pedidos.
- Validar que las cantidades ingresadas sean mayores que cero.
- Pensar en cómo acumular información por cliente para el análisis final.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `pedidos` | `list (dict)` | Almacena todos los pedidos guardados en la jornada (lista de diccionarios). |
| `estados_validos` | `list (str)` | Lista que define los tres estados admisibles de entrega para validación. |
| `cliente` | `str` | Nombre del cliente del pedido en turno. Actúa como centinela final si es "fin". |
| `productos_pedido` | `dict` | Diccionario temporal por pedido. Mapea el producto (`str`) con su cantidad (`int`). |
| `producto` | `str` | Nombre del producto ingresado (se valida y normaliza). Actúa como centinela si es "hecho". |
| `cant` | `int` | Cantidad física de unidades solicitadas del producto actual en el pedido. |
| `estado` | `str` | Estado operativo del pedido, validado contra `estados_validos`. |
| `total_pedidos` | `int` | Frecuencia total de pedidos registrados calculada con `len()`. |
| `total_productos_despachados`| `int` | Acumulador de la suma global de unidades despachadas en la jornada. |
| `conteos_estados` | `dict` | Diccionario contador para clasificar la frecuencia de pedidos por estado. |
| `productos_por_cliente`| `dict` | Diccionario de consolidación acumulada de unidades demandadas por cliente. |
| `unidades_este_pedido`| `int` | Contador local que suma el volumen de unidades cargadas en el pedido en curso. |
| `cliente_top` | `str` | Nombre del cliente que registró la mayor cantidad consolidada de unidades. |
| `max_unidades_cliente`| `int` | Centinela para almacenar la máxima cantidad acumulada de unidades por cliente. |

---

#### Lógica de la Solución
1. **Diseño de Estructura de Datos Anidada (Jerárquica):** Se modela el problema utilizando una arquitectura de colecciones anidadas: `list[dict[str, dict[str, int]]]`. 
   - La colección raíz es una lista `pedidos = []`.
   - Cada elemento es un diccionario que representa un pedido: `{"cliente": cliente, "productos": productos_pedido, "estado": estado}`.
   - La propiedad `"productos"` contiene un diccionario interno `productos_pedido = {producto: cantidad}` para registrar múltiples ítems y acumular de forma automática las cantidades de productos duplicados dentro del mismo pedido.
2. **Ciclos Anidados y Doble Centinela:** Un ciclo externo `while True` controla el registro de los distintos pedidos del día hasta ingresar el centinela `"fin"`. Dentro de este, un ciclo interno `while True` permite la carga ilimitada de productos para el cliente actual hasta introducir el centinela de control `"hecho"`.
3. **Consolidación Logística Acumulativa:** Dado que un mismo cliente puede realizar múltiples pedidos independientes a lo largo de la jornada, se implementa un diccionario auxiliar `productos_por_cliente = {}`. Al recorrer los pedidos, se calcula el tamaño de cada pedido y se asocia de forma consolidada al cliente, lo cual permite realizar una búsqueda manual exacta del cliente estrella sumando todas sus compras del día.

---

#### Explicación Línea por Línea
- **Línea 5:** `pedidos = []`: Inicializa la base de datos de despachos como una lista vacía.
- **Línea 6:** `estados_validos = [...]`: Catálogo estándar de control del flujo logístico.
- **Línea 8:** `while True:`: Ciclo externo principal de duración desconocida para capturar pedidos.
- **Línea 9:** `cliente = input(...).strip()`: Captura y remueve espacios en los extremos del nombre del cliente.
- **Líneas 10 y 11:** `if cliente.lower() == "fin":`: Evalúa con tolerancia a mayúsculas si se ha ingresado el centinela de cierre.
- **Línea 15:** `productos_pedido = {}`: Inicializa un diccionario vacío exclusivo para el pedido del cliente en curso.
- **Línea 18:** `while True:`: Ciclo anidado interno para capturar múltiples productos en el mismo pedido.
- **Línea 19:** `producto = input(...).strip().lower()`: Captura y normaliza el producto, permitiendo terminar la carga al escribir `"hecho"`.
- **Líneas 20 a 24:** `if producto == "hecho":`: Valida que el pedido no se guarde vacío. Si tiene productos, rompe el bucle de captura interno con `break`.
- **Líneas 25 a 27:** `if not producto:`: Deniega el registro si el nombre del producto está vacío.
- **Línea 29:** `while True:`: Bucle de validación para la cantidad física solicitada.
- **Líneas 30 a 36:** `try-except ValueError`: Captura entradas no enteras y obliga a ingresar valores estrictamente mayores a cero.
- **Línea 39:** `if producto in productos_pedido:`: Operador de pertenencia que revisa si el producto ya existe en el pedido.
- **Línea 40:** `productos_pedido[producto] += cant`: Acumula unidades si el producto ya estaba cargado.
- **Línea 42:** `productos_pedido[producto] = cant`: Agrega una nueva clave con su cantidad al pedido.
- **Línea 45:** `while True:`: Bucle de validación para la entrada del estado del pedido.
- **Líneas 46 a 49:** `estado = input(...).strip().lower()` y `if estado in estados_validos:`: Solicita el estado y verifica si pertenece al catálogo para romper el bucle.
- **Líneas 52 a 56:** `pedidos.append({...})`: Empaqueta la información en un diccionario y lo anexa a la lista de pedidos de la jornada, confirmando el éxito de la operación.
- **Líneas 60 a 63:** Inicializa los contadores estadísticos de la fase de análisis final.
- **Líneas 65 a 67:** Imprime el encabezado formal del reporte de operaciones.
- **Línea 69:** `for idx, ped in enumerate(pedidos):`: Recorre los pedidos usando `enumerate()` para imprimir el número de orden de compra correlativo.
- **Línea 70 a 72:** Descompone las propiedades del pedido: cliente (`cli`), estado (`est`) y diccionario de productos (`prods`).
- **Línea 74:** `print(...)`: Imprime la cabecera del pedido del cliente con su estado en mayúsculas.
- **Línea 77:** `conteos_estados[est] += 1`: Clasifica el pedido en su respectivo estado dentro del diccionario contador.
- **Línea 80:** `unidades_este_pedido = 0`: Inicializa el subtotal de unidades de este pedido específico.
- **Línea 81:** `for prod, cant in prods.items():`: Recorre el diccionario interno de productos del pedido en curso.
- **Línea 82:** `print(...)`: Presenta en pantalla el detalle de los productos y sus unidades.
- **Líneas 83 y 84:** Incrementa de forma paralela el acumulador global del centro de distribución y el contador local del pedido.
- **Líneas 87 a 90:** `if cli in productos_por_cliente:`: Acumula el volumen consolidado del cliente actual en el diccionario auxiliar de consolidación.
- **Líneas 93 a 95:** Inicializa las variables para buscar de forma manual al cliente líder de la jornada sobre el diccionario consolidado.
- **Línea 96:** `for cli, total_un in productos_por_cliente.items():`: Itera en paralelo sobre las claves y valores consolidados.
- **Líneas 97 a 99:** `if total_un > max_unidades_cliente:`: Compara y actualiza las variables del cliente top de la jornada.
- **Líneas 101 a 112:** `print(...)`: Despliega las métricas clave consolidadas e identifica al cliente con mayor volumen demandado de la jornada logística.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Simulación Operativa de Centro de Distribución (Estructuras Anidadas)
# ==============================================================================

print("--- Portal Logístico: Centro de Distribución ---")

# Base de datos global de la jornada (Lista de Diccionarios Anidados)
pedidos = []
estados_validos = ["pendiente", "despachado", "entregado"]

# ETAPA 1: Registro e Ingreso de Pedidos (Ciclos anidados)
while True:
    cliente = input("Ingrese el nombre del cliente para el nuevo pedido (o 'fin' para cerrar la jornada): ").strip()
    
    # Condición de cierre de caja
    if cliente.lower() == "fin":
        break
    if not cliente:
        print("El nombre del cliente no puede estar vacío.")
        continue
        
    # Diccionario local para recolectar productos del pedido actual
    productos_pedido = {}
    
    # Ciclo Anidado Interno: Carga de múltiples productos por cliente
    while True:
        producto = input(f"Ingrese nombre del producto a añadir para {cliente} (o 'hecho' para cerrar este pedido): ").strip().lower()
        
        # Condición para finalizar la carga del pedido actual
        if producto == "hecho":
            if not productos_pedido:
                print("¡Atención! Debe registrar al menos un producto para guardar el pedido.")
                continue
            break
            
        if not producto:
            print("El nombre del producto no puede estar vacío.")
            continue
            
        # Validación de unidades del producto actual
        while True:
            try:
                cant = int(input(f"Cantidad de unidades para {producto.capitalize()}: "))
                if cant > 0:
                    break
                print("La cantidad de unidades debe ser mayor a cero.")
            except ValueError:
                print("Ingrese un número entero positivo.")
        
        # Acumulación de cantidades dentro del pedido actual (evita duplicar claves)
        if producto in productos_pedido:
            productos_pedido[producto] += cant
        else:
            productos_pedido[producto] = cant
        print(f"-> Añadido {producto.capitalize()} ({cant} un) al pedido.")
        
    # Validación del estado del pedido
    while True:
        estado = input(f"Ingrese el estado del pedido de {cliente} (pendiente / despachado / entregado): ").strip().lower()
        if estado in estados_validos:
            break
        print("Estado no reconocido. Marque 'pendiente', 'despachado' o 'entregado'.")
        
    # Empaquetado y almacenamiento del pedido completo en la base de datos
    pedidos.append({
        "cliente": cliente,
        "productos": productos_pedido,
        "estado": estado
    })
    print(f"\n¡Pedido para {cliente} guardado exitosamente con {len(productos_pedido)} artículo(s)!\n")

# ETAPA 2: Análisis Final General (Recorrido manual exhaustivo)
total_pedidos = len(pedidos)
total_productos_despachados = 0
conteos_estados = {"pendiente": 0, "despachado": 0, "entregado": 0}
productos_por_cliente = {}  # Diccionario auxiliar para consolidar compras por cliente

print("\n=============================================")
print("  REPORTE INTEGRAL DE OPERACIONES LOGÍSTICAS")
print("=============================================")

for idx, ped in enumerate(pedidos):
    cli = ped["cliente"]
    est = ped["estado"]
    prods = ped["productos"]
    
    print(f"\nPedido #{idx+1} - Cliente: {cli} | Estado: {est.upper()}")
    
    # Contabilizar pedidos por estado
    conteos_estados[est] += 1
    
    # Recorrido del detalle del pedido (productos)
    unidades_este_pedido = 0
    for prod, cant in prods.items():
        print(f"  * {prod.capitalize():15}: {cant} un")
        total_productos_despachados += cant
        unidades_este_pedido += cant
        
    # Consolidar volumen de compra por cliente (acumulando si tiene varios pedidos)
    if cli in productos_por_cliente:
        productos_por_cliente[cli] += unidades_este_pedido
    else:
        productos_por_cliente[cli] = unidades_este_pedido

# Búsqueda manual de cliente top sobre el diccionario consolidado (Evitando max())
cliente_top = ""
max_unidades_cliente = -1
for cli, total_un in productos_por_cliente.items():
    if total_un > max_unidades_cliente:
        max_unidades_cliente = total_un
        cliente_top = cli

# ETAPA 3: Reporte de Métricas Logísticas Consolidadas
print("\n=============================================")
print("               MÉTRICAS CLAVE")
print("=============================================")
print(f"Total de pedidos procesados: {total_pedidos}")
print(f"Suma global de unidades despachadas: {total_productos_despachados} unidades")
print(f"\nPedidos por estado:")
for est, cnt in conteos_estados.items():
    print(f"- {est.capitalize():12}: {cnt} pedido(s)")
    
if pedidos:
    print(f"\nCliente Top de la jornada (Mayor volumen acumulado): {cliente_top} con {max_unidades_cliente} unidades solicitadas.")
print("=============================================")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Carga de Múltiples Pedidos con Detalle de Productos
```text
--- Portal Logístico: Centro de Distribución ---
Ingrese el nombre del cliente para el nuevo pedido (o 'fin' para cerrar la jornada): Juan
Ingrese nombre del producto a añadir para Juan (o 'hecho' para cerrar este pedido): tornillo
Cantidad de unidades para Tornillo: 100
-> Añadido Tornillo (100 un) al pedido.
Ingrese nombre del producto a añadir para Juan (o 'hecho' para cerrar este pedido): tuerca
Cantidad de unidades para Tuerca: 50
-> Añadido Tuerca (50 un) al pedido.
Ingrese nombre del producto a añadir para Juan (o 'hecho' para cerrar este pedido): hecho
Ingrese el estado del pedido de Juan (pendiente / despachado / entregado): despachado

¡Pedido para Juan guardado exitosamente con 2 artículo(s)!

Ingrese el nombre del cliente para el nuevo pedido (o 'fin' para cerrar la jornada): Andrea
Ingrese nombre del producto a añadir para Andrea (o 'hecho' para cerrar este pedido): taladro
Cantidad de unidades para Taladro: 2
-> Añadido Taladro (2 un) al pedido.
Ingrese nombre del producto a añadir para Andrea (o 'hecho' para cerrar este pedido): hecho
Ingrese el estado del pedido de Andrea (pendiente / despachado / entregado): pendiente

¡Pedido para Andrea guardado exitosamente con 1 artículo(s)!

Ingrese el nombre del cliente para el nuevo pedido (o 'fin' para cerrar la jornada): fin

=============================================
  REPORTE INTEGRAL DE OPERACIONES LOGÍSTICAS
=============================================

Pedido #1 - Cliente: Juan | Estado: DESPACHADO
  * Tornillo       : 100 un
  * Tuerca         : 50 un

Pedido #2 - Cliente: Andrea | Estado: PENDIENTE
  * Taladro        : 2 un

=============================================
               MÉTRICAS CLAVE
=============================================
Total de pedidos procesados: 2
Suma global de unidades despachadas: 152 unidades

Pedidos por estado:
- Pendiente   : 1 pedido(s)
- Despachado  : 1 pedido(s)
- Entregado   : 0 pedido(s)

Cliente Top de la jornada (Mayor volumen acumulado): Juan con 150 unidades solicitadas.
=============================================
```
