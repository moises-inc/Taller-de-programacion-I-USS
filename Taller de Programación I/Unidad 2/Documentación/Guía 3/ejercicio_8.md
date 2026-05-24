### Ejercicio 8: Planificación de entregas en empresa de agua purificada

#### Enunciado del Problema
Una empresa de agua purificada realiza entregas diarias a distintos clientes de la ciudad. Cada entrega tiene un sector, una cantidad de botellones y un estado, por ejemplo: “pendiente”, “entregado” o “con deuda”.
Desarrolla un script en Python que permita registrar y analizar las entregas del día. El programa debe:
- Permitir registrar entregas de forma repetitiva hasta que el usuario decida terminar.
- Para cada entrega, se debe ingresar:
    + Nombre del cliente.
    + Sector.
    + Cantidad de botellones.
    + Estado de la entrega.
- Al finalizar, mostrar:
    + Cantidad total de entregas registradas.
    + Cantidad total de botellones entregados.
    + Cantidad de entregas por estado.
    + Sectores donde se realizaron entregas.
    + Cliente con mayor cantidad de botellones solicitados.

Consideraciones:
- El programa debe usar un ciclo de duración desconocida para registrar entregas.
- Se deben recorrer las estructuras de datos para calcular los resultados finales.
- El estudiante debe decidir cómo representar cada entrega y cómo almacenar el conjunto de entregas.
- Validar que la cantidad de botellones sea mayor que cero.
- Validar que el estado ingresado corresponda a una opción permitida.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `entregas` | `list (dict)` | Lista principal de la jornada. Almacena cada pedido como un diccionario individual. |
| `estados_permitidos` | `list (str)` | Colección de control de estados válidos en la empresa ("pendiente", "entregado", "con deuda"). |
| `cliente` | `str` | Nombre del cliente del despacho actual. Funciona como centinela final si es igual a "fin". |
| `sector` | `str` | Sector geográfico del despacho (normalizado a minúsculas). |
| `cant` | `int` | Cantidad de botellones solicitados (debe ser mayor a 0). |
| `estado` | `str` | Estado operativo del despacho del cliente. |
| `total_entregas` | `int` | Frecuencia total de entregas procesadas obtenida mediante `len()`. |
| `total_botellones` | `int` | Acumulador del volumen total de botellones de agua despachados en la jornada. |
| `conteos_por_estado` | `dict` | Diccionario contador para clasificar la cantidad de entregas por estado operacional. |
| `sectores_visitados` | `set (str)` | Conjunto (*set*) que acumula de forma única los sectores del mapa de despacho sin duplicados. |
| `cliente_estrella` | `str` | Nombre del cliente que solicitó el mayor volumen de botellones en un solo pedido. |
| `max_botellones` | `int` | Centinela para almacenar la máxima cantidad de botellones en la búsqueda manual. |

---

#### Lógica de la Solución
1. **Modelado Híbrido Avanzado (Lista de Diccionarios y Conjuntos):** Se representa la base diaria de despachos en una lista de diccionarios `entregas = []`. Cada elemento modela los atributos de un pedido mediante un diccionario. A su vez, para los sectores geográficos, se utiliza la estructura matemática de conjunto (`set()`), la cual tiene la propiedad intrínseca de no admitir duplicados. Esto permite consolidar de forma automática e inmediata la cobertura de distribución sin rutinas manuales de descarte de duplicados.
2. **Ciclo Indefinido con Validaciones Cruzadas:** El ingreso se controla mediante un ciclo `while` indefinido. Se valida que el cliente no contenga nombres vacíos, que el sector no quede en blanco, que la cantidad de botellones sea entera y estrictamente mayor que cero, y que el estado pertenezca estrictamente al catálogo operativo.
3. **Análisis Integral en un Solo Recorrido:** Se itera sobre `entregas` para:
   - Acumular el total general de botellones.
   - Clasificar las entregas en el diccionario de conteos por estado.
   - Insertar los sectores en el conjunto único `sectores_visitados` con el método `.add()`.
   - Realizar la búsqueda manual del pedido con mayor volumen usando la comparación de centinelas.

---

#### Explicación Línea por Línea
- **Línea 5:** `entregas = []`: Inicializa la lista que recopilará los diccionarios de despachos.
- **Línea 6:** `estados_permitidos = [...]`: Define el catálogo de validación de estados permitidos.
- **Línea 8:** `while True:`: Bucle indefinido principal para la carga de despachos.
- **Línea 9:** `cliente = input(...).strip()`: Captura y remueve espacios en los extremos del nombre del cliente.
- **Líneas 10 y 11:** `if cliente.lower() == "fin":`: Evalúa de manera flexible el ingreso del centinela de cierre de jornada.
- **Línea 15:** `sector = input(...).strip().lower()`: Captura y normaliza el sector a minúsculas.
- **Líneas 16 y 17:** `while not sector:`: Bucle de validación interactiva que impide campos de sector vacíos en la planificación de la ruta.
- **Línea 19:** `while True:`: Inicia la validación del número de botellones.
- **Líneas 20 a 26:** `try-except ValueError`: Captura excepciones y valida que `cant > 0`.
- **Línea 28:** `while True:`: Inicia la validación del estado del despacho.
- **Líneas 29 a 32:** `estado = input(...).strip().lower()` y `if estado in estados_permitidos:`: Solicita el estado y verifica si forma parte del catálogo. De ser correcto, rompe el bucle de validación actual.
- **Líneas 35 a 40:** `entregas.append({...})`: Crea y anexa un diccionario a la lista `entregas` con las propiedades capturadas.
- **Línea 44:** `total_entregas = len(entregas)`: Determina la cantidad total de pedidos.
- **Línea 45:** `total_botellones = 0`: Inicializa el acumulador de botellones.
- **Línea 46:** `conteos_por_estado = {...}`: Crea un diccionario contador para las tres categorías válidas.
- **Línea 47:** `sectores_visitados = set()`: Inicializa el conjunto vacío para almacenar sectores de distribución únicos.
- **Líneas 49 y 50:** `cliente_estrella = ""` y `max_botellones = -1`: Inicializa las variables para la búsqueda manual del pedido de mayor volumen.
- **Línea 52:** `for ent in entregas:`: Bucle secuencial para recorrer los diccionarios de despachos.
- **Línea 53:** `total_botellones += ent["botellones"]`: Incrementa el volumen global despachado.
- **Línea 54:** `conteos_por_estado[ent["estado"]] += 1`: Clasifica el pedido en su respectiva categoría de estado dentro del diccionario contador.
- **Línea 55:** `sectores_visitados.add(ent["sector"])`: Inserta el sector en el conjunto único de forma segura. Si el sector ya existía, el conjunto no sufrirá alteración alguna de forma nativa.
- **Líneas 58 a 60:** `if ent["botellones"] > max_botellones:`: Evaluación del pedido máximo registrado.
- **Líneas 63 a 71:** `print(...)`: Formatea y despliega los consolidados estadísticos diarios. Emplea la función `', '.join()` para transformar el conjunto de sectores en una cadena en mayúsculas cómoda para lectura.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Planificación Logística AquaPure (Lista de Diccionarios y Conjuntos)
# ==============================================================================

print("--- Planificador de Entregas: AquaPure ---")

# Base de datos de despachos diarios
entregas = []
estados_permitidos = ["pendiente", "entregado", "con deuda"]

# ETAPA 1: Captura e Ingreso de Datos (Bucle de duración indefinida)
while True:
    cliente = input("Ingrese nombre del cliente (o 'fin' para finalizar): ").strip()
    
    # Condición de cierre de operaciones
    if cliente.lower() == "fin":
        break
        
    if not cliente:
        print("El nombre del cliente no puede estar vacío.")
        continue
        
    # Registro de sector geográfico
    sector = input(f"Ingrese sector geográfico para la entrega de {cliente}: ").strip().lower()
    while not sector:
        sector = input("El sector es requerido para la ruta. Ingrese sector: ").strip().lower()
        
    # Validación de botellones solicitados
    while True:
        try:
            cant = int(input(f"Cantidad de botellones solicitados por {cliente}: "))
            if cant > 0:
                break
            print("La cantidad de botellones debe ser mayor a cero.")
        except ValueError:
            print("Ingrese un número entero positivo.")
            
    # Validación del estado de despacho
    while True:
        estado = input("Ingrese estado de la entrega (pendiente / entregado / con deuda): ").strip().lower()
        if estado in estados_permitidos:
            break
        print("Estado no reconocido. Marque 'pendiente', 'entregado' o 'con deuda'.")
        
    # Registro de entrega mediante estructura estructurada dictionary
    entregas.append({
        "cliente": cliente,
        "sector": sector,
        "botellones": cant,
        "estado": estado
    })
    print(f"-> Entrega de {cant} botellón(es) para {cliente} registrada con éxito.")

# ETAPA 2: Análisis Estadístico e Integral
total_entregas = len(entregas)
total_botellones = 0
conteos_por_estado = {"pendiente": 0, "entregado": 0, "con deuda": 0}
sectores_visitados = set()  # Estructura óptima set para eliminar duplicados de forma nativa

cliente_estrella = ""
max_botellones = -1

for ent in entregas:
    total_botellones += ent["botellones"]
    conteos_por_estado[ent["estado"]] += 1
    sectores_visitados.add(ent["sector"])  # Acumulación única y veloz
    
    # Búsqueda manual de máximo absoluto
    if ent["botellones"] > max_botellones:
        max_botellones = ent["botellones"]
        cliente_estrella = ent["cliente"]

# ETAPA 3: Reporte Logístico Final Consolidado
print("\n--- Reporte Logístico de Entregas del Día ---")
print(f"Cantidad total de entregas planificadas: {total_entregas}")
print(f"Cantidad total de botellones movilizados  : {total_botellones}")

print(f"\nDesglose de entregas por Estado:")
for est, conteo in conteos_por_estado.items():
    print(f"- {est.capitalize():12}: {conteo} entrega(s)")
    
# Mostrar el conjunto único de sectores mapeados en mayúsculas
sectores_formateados = [s.capitalize() for s in sectores_visitados]
print(f"\nSectores de despacho registrados: {', '.join(sectores_formateados)}")

if entregas:
    print(f"Cliente top (Mayor solicitud): {cliente_estrella} con {max_botellones} botellones.")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Ingreso de Despachos y Sectores Repetidos (Generación Única)
```text
--- Planificador de Entregas: AquaPure ---
Ingrese nombre del cliente (o 'fin' para finalizar): Juan
Ingrese sector geográfico para la entrega de Juan: Providencia
Cantidad de botellones solicitados por Juan: 5
Ingrese estado de la entrega (pendiente / entregado / con deuda): entregado
-> Entrega de 5 botellón(es) para Juan registrada con éxito.
Ingrese nombre del cliente (o 'fin' para finalizar): Andrea
Ingrese sector geográfico para la entrega de Andrea: Providencia
Cantidad de botellones solicitados por Andrea: 12
Ingrese estado de la entrega (pendiente / entregado / con deuda): pendiente
-> Entrega de 12 botellón(es) para Andrea registrada con éxito.
Ingrese nombre del cliente (o 'fin' para finalizar): Carlos
Ingrese sector geográfico para la entrega de Carlos: Las Condes
Cantidad de botellones solicitados por Carlos: 3
Ingrese estado de la entrega (pendiente / entregado / con deuda): con deuda
-> Entrega de 3 botellón(es) para Carlos registrada con éxito.
Ingrese nombre del cliente (o 'fin' para finalizar): fin

--- Reporte Logístico de Entregas del Día ---
Cantidad total de entregas planificadas: 3
Cantidad total de botellones movilizados  : 20

Desglose de entregas por Estado:
- Pendiente   : 1 entrega(s)
- Entregado   : 1 entrega(s)
- Con deuda   : 1 entrega(s)

Sectores de despacho registrados: Providencia, Las condes
Cliente top (Mayor solicitud): Andrea con 12 botellones.
```
