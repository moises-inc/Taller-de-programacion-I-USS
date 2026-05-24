### Ejercicio 9: Registro de capturas en pesca artesanal

#### Enunciado del Problema
En una caleta del sur de Chile, los pescadores registran sus capturas diarias indicando el tipo de recurso extraído (por ejemplo: merluza, congrio, luga, erizo) y la cantidad obtenida en kilos.
Desarrolla un script en Python que permita registrar y analizar las capturas del día. El programa debe:
- Permitir ingresar capturas de forma repetitiva hasta que el usuario indique que desea finalizar.
- En cada registro se debe ingresar:
    + Nombre del recurso.
    + Cantidad capturada en kilos.
- Si un recurso ya fue registrado anteriormente, se debe acumular su cantidad total.
- Al finalizar, el programa debe mostrar:
    + Total de kilos capturados en el día.
    + Cuántos tipos de recursos distintos fueron capturados.
    + El recurso con mayor cantidad capturada.
    + Un listado de todos los recursos con sus respectivos totales.

Consideraciones:
- El registro debe realizarse con un ciclo de duración desconocida (`while`).
- Se deben recorrer las estructuras para calcular los resultados finales.
- El estudiante debe decidir cómo almacenar la información de las capturas.
- Validar que las cantidades ingresadas sean mayores que cero.
- Pensar cómo acumular valores cuando un recurso se repite.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `capturas` | `dict` | Estructura clave-valor para asociar el recurso extraído (`str`) con su cantidad acumulada en kilos (`float`). |
| `recurso` | `str` | Nombre del recurso marino capturado (se limpia con `.strip()` y normaliza a minúsculas). |
| `kilos` | `float` | Peso del recurso extraído en el lote actual (validado para ser mayor a 0). |
| `total_kilos` | `float` | Acumulador del peso global de pesca del día (reemplaza a `sum()`). |
| `recurso_top` | `str` | Nombre del recurso con el mayor volumen de captura acumulado del día. |
| `kilos_max` | `float` | Centinela manual que guarda el peso del recurso más capturado del día (reemplaza a `max()`). |
| `total_especies` | `int` | Frecuencia de especies distintas de recursos marinos regulados registradas (longitud del diccionario). |
| `rec` | `str` | Variable de iteración para la clave (nombre del recurso) en `capturas.items()`. |
| `kg` | `float` | Variable de iteración para el valor (cantidad en kilos) en `capturas.items()`. |

---

#### Lógica de la Solución
1. **Selección Óptima de Estructura (Diccionario Acumulativo):** Al igual que en el ejercicio de la feria agrícola, el diccionario es la estructura de datos ideal. Permite buscar el recurso de forma instantánea usando el nombre como clave única y acumular de forma directa sus pesos con `capturas[recurso] += kilos`, simplificando la lógica algorítmica sin necesidad de buscar en listas complejas.
2. **Ciclo de Recepción y Control de Excepciones:** Un bucle `while True` captura las entradas, implementando validaciones robustas mediante `try-except` para evitar caídas catastróficas del sistema en caso de ingresos no decimales de peso, controlando además el centinela de cierre `"fin"`.
3. **Análisis e Iteración Exhaustiva:** Una vez cerrado el registro, se realiza un recorrido lineal sobre `capturas.items()`. En este ciclo, se consolida la suma total de kilos y se actualiza mediante comparaciones con un valor centinela (`kilos_max = -1.0`) la especie líder de pesca de la jornada.

---

#### Explicación Línea por Línea
- **Línea 5:** `capturas = {}`: Inicializa un diccionario vacío para guardar los recursos de pesca del día.
- **Línea 7:** `while True:`: Inicia el ciclo operativo indefinido de SERNAPESCA.
- **Línea 8:** `recurso = input(...).strip().lower()`: Solicita el nombre del recurso, removiendo espacios exteriores y homologando caracteres a minúsculas.
- **Líneas 9 y 10:** `if recurso == "fin":`: Cláusula que rompe el ciclo principal si se ingresa el centinela.
- **Líneas 11 y 12:** `if not recurso:`: Deniega el registro si el nombre del recurso está en blanco.
- **Línea 14:** `while True:`: Inicia el bucle validador para la carga del peso del recurso.
- **Líneas 15 a 21:** `try-except ValueError`: Convierte el valor a punto flotante (`float`) y valida que `kilos > 0`, obligando a reingresar el valor decimal en caso de error. Si la cantidad es válida, rompe el bucle de validación.
- **Línea 24:** `if recurso in capturas:`: Verifica si el recurso marino ya cuenta con registros previos en el diccionario.
- **Línea 25:** `capturas[recurso] += kilos`: Si ya existe, incrementa el valor de la clave con la nueva cantidad capturada.
- **Línea 27:** `capturas[recurso] = kilos`: Si es un recurso nuevo del día, inicializa la clave con la cantidad ingresada.
- **Línea 31:** `total_kilos = 0.0`: Inicializa a cero el acumulador global de kilos del día.
- **Línea 32:** `recurso_top = ""`: Inicializa el nombre del recurso estrella de la jornada.
- **Línea 33:** `kilos_max = -1.0`: Establece el centinela numérico máximo en un valor inferior al rango de validación.
- **Línea 34:** `total_especies = len(capturas)`: Obtiene la cantidad de claves del diccionario.
- **Línea 36:** `print("\n--- Reporte Consolidado de Capturas del Día ---")`: Imprime el encabezado del reporte.
- **Línea 37:** `for rec, kg in capturas.items():`: Recorre en paralelo las claves y valores de la colección de pesca.
- **Línea 38:** `print(...)`: Presenta en pantalla el recurso y su peso con alineación visual (`{rec.capitalize():15}`) y limitación a un decimal (`{kg:8.1f} kg`).
- **Línea 39:** `total_kilos += kg`: Suma manual acumulativa de los kilos totales.
- **Líneas 40 a 42:** `if kg > kilos_max:`: Compara el peso del recurso en curso con el centinela. Si se cumple la condición, actualiza las variables del recurso líder.
- **Líneas 44 a 49:** `if capturas:`: Muestra los resultados consolidados de pesca. Si no se registraron capturas, informa la inactividad de la caleta.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Monitoreo de Pesca Artesanal SERNAPESCA (Diccionario Acumulativo)
# ==============================================================================

print("--- Registro de Pesca Artesanal - SERNAPESCA ---")

# Diccionario para almacenar de forma consolidada las capturas del día
capturas = {}

# ETAPA 1: Registro de Capturas (Ciclo indefinido)
while True:
    recurso = input("Ingrese nombre del recurso extraído (o 'fin' para terminar): ").strip().lower()
    
    # Condición de cierre
    if recurso == "fin":
        break
        
    # Impedir registros vacíos
    if not recurso:
        print("El nombre del recurso no puede quedar vacío.")
        continue
        
    # Validación interactiva y robusta del peso en kilos (Decimal positivo)
    while True:
        try:
            kilos = float(input(f"Ingrese cantidad de kilos extraídos de {recurso.capitalize()}: "))
            if kilos > 0:
                break
            print("La cantidad de kilos debe ser mayor a cero.")
        except ValueError:
            print("Entrada no válida. Ingrese un valor decimal.")
            
    # Registro y acumulación automática en el diccionario
    if recurso in capturas:
        capturas[recurso] += kilos
    else:
        capturas[recurso] = kilos
    print(f"-> Acumulados {kilos:.1f} kg de {recurso.capitalize()}.\n")

# ETAPA 2: Análisis Estadístico Manual (Evitando sum() y max())
total_kilos = 0.0
recurso_top = ""
kilos_max = -1.0
total_especies = len(capturas)

print("\n--- Reporte Consolidado de Capturas del Día ---")
for rec, kg in capturas.items():
    print(f"* {rec.capitalize():15}: {kg:8.1f} kg")
    total_kilos += kg  # Suma manual acumulativa
    
    # Búsqueda manual del máximo volumen de extracción
    if kg > kilos_max:
        kilos_max = kg
        recurso_top = rec

# Imprimir consolidación de resultados de la jornada
if capturas:
    print(f"\nPeso total extraído en la caleta: {total_kilos:.1f} kg")
    print(f"Tipos de recursos marinos regulados capturados: {total_especies}")
    print(f"Especie con mayor volumen de captura: {recurso_top.capitalize()} con {kilos_max:.1f} kg")
else:
    print("No se registraron capturas de pesca artesanal en este día.")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Captura de Múltiples Lotes del Mismo Recurso
```text
--- Registro de Pesca Artesanal - SERNAPESCA ---
Ingrese nombre del recurso extraído (o 'fin' para terminar): merluza
Ingrese cantidad de kilos extraídos de Merluza: 120.5
-> Acumulados 120.5 kg de Merluza.

Ingrese nombre del recurso extraído (o 'fin' para terminar): congrio
Ingrese cantidad de kilos extraídos de Congrio: 85.0
-> Acumulados 85.0 kg de Congrio.

Ingrese nombre del recurso extraído (o 'fin' para terminar): merluza
Ingrese cantidad de kilos extraídos de Merluza: 50.3
-> Acumulados 50.3 kg de Merluza.

Ingrese nombre del recurso extraído (o 'fin' para terminar): fin

--- Reporte Consolidado de Capturas del Día ---
* Merluza        :    170.8 kg
* Congrio        :     85.0 kg

Peso total extraído en la caleta: 255.8 kg
Tipos de recursos marinos regulados capturados: 2
Especie con mayor volumen de captura: Merluza con 170.8 kg
```

##### Caso 2: Manejo de Errores Decimales y de Carga
```text
--- Registro de Pesca Artesanal - SERNAPESCA ---
Ingrese nombre del recurso extraído (o 'fin' para terminar): erizo
Ingrese cantidad de kilos extraídos de Erizo: abc
Entrada no válida. Ingrese un valor decimal.
Ingrese cantidad de kilos extraídos de Erizo: -15
La cantidad de kilos debe ser mayor a cero.
Ingrese cantidad de kilos extraídos de Erizo: 45.6
-> Acumulados 45.6 kg de Erizo.

Ingrese nombre del recurso extraído (o 'fin' para terminar): fin

--- Reporte Consolidado de Capturas del Día ---
* Erizo          :     45.6 kg

Peso total extraído en la caleta: 45.6 kg
Tipos de recursos marinos regulados capturados: 1
Especie con mayor volumen de captura: Erizo con 45.6 kg
```
