### Ejercicio 3: Producción diaria en planta lechera

#### Enunciado del Problema
En una planta lechera del sur de Chile, se registra diariamente la cantidad de litros de leche entregados por distintos productores.
Desarrolla un script en Python que permita analizar la producción del día. El programa debe:
- Crear una lista de tuplas, donde cada tupla tenga el formato: `(nombre_productor, litros_entregados)`.
- Debes trabajar con al menos 8 productores (puedes generarlos manualmente o con valores aleatorios usando `random` entre 100 y 1000 litros).
- Mostrar:
    + El total de litros recolectados en el día.
    + El productor que entregó más leche.
    + El productor que entregó menos leche.
    + Cuántos productores entregaron más de 500 litros.

Consideraciones:
- Se recomienda recorrer la estructura para calcular los resultados (evitar resolver todo directo con funciones de alto nivel).
- Debes acceder correctamente a los elementos de cada tupla (nombre y litros).
- Piensa cómo vas a comparar valores mientras recorres la lista.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `modo` | `int` | Selección del menú (1 para manual, 2 para automático). |
| `produccion` | `list (tuple)` | Lista contenedora de las tuplas `(str, float)` que modelan a cada productor y su entrega. |
| `n` | `int` | Cantidad total de productores a ingresar manualmente (debe ser $\ge 8$). |
| `nombre` | `str` | Almacena el nombre del productor durante la captura. |
| `litros` | `float` | Almacena los litros aportados por un productor durante la captura. |
| `productores_ejemplo`| `list (str)` | Lista de nombres de fundos y cooperativas chilenas de prueba para la simulación. |
| `total_litros` | `float` | Acumulador decimal del volumen total de leche recolectado. |
| `prod_max` | `tuple (str, float)`| Tupla centinela que representa al productor con mayor aporte de leche. |
| `prod_min` | `tuple (str, float)`| Tupla centinela que representa al productor con menor aporte de leche. |
| `productores_mas_500`| `int` | Contador de productores cuyas entregas son estrictamente mayores a 500 litros. |

---

#### Lógica de la Solución
1. **Estructura Compuesta (Lista de Tuplas):** La información se organiza en una lista que almacena tuplas bidimensionales de tipo `(nombre, litros)`. Las tuplas se seleccionan debido a que el vínculo asociativo entre el nombre del productor y su entrega registrada debe permanecer inmutable durante el ciclo del reporte.
2. **Carga Escalable con Restricciones:** Se implementa un menú que valida la normativa de operar con un tamaño de muestra de al menos 8 elementos mediante control de flujos iterativos.
3. **Desempaquetado de Tuplas en Recorrido (*Unpacking*):** En el ciclo de análisis, se aplica la técnica de desempaquetado de tuplas `nombre, litros = productor` para mejorar sustancialmente la legibilidad del código.
4. **Búsqueda Manual de Extremos sobre Tuplas:** Se inicializan las tuplas centinelas `prod_max` y `prod_min` con el primer elemento de la lista. En el bucle de recorrido, se comparan sus litros (segundo componente de la tupla, índice `[1]`) con los del elemento evaluado para actualizar, en caso necesario, la tupla completa del productor extremo.

---

#### Explicación Línea por Línea
- **Línea 3:** `import random`: Importa el generador pseudoaleatorio de Python.
- **Líneas 5 a 7:** `print(...)`: Presenta en la consola el menú de opciones para la simulación.
- **Líneas 9 a 16:** `while True:` y `try-except ValueError`: Bucle interactivo que valida que la opción elegida sea exclusivamente `1` o `2`.
- **Línea 18:** `produccion = []`: Inicializa la lista que contendrá las tuplas de los productores.
- **Línea 20:** `if modo == 1:`: Rama que procesa el ingreso de datos de forma manual.
- **Línea 21:** `while True:`: Bucle de validación para el tamaño de la muestra de productores.
- **Líneas 22 a 27:** `try-except ValueError`: Captura entradas no enteras y obliga a cumplir la condición `n >= 8` para cumplir con las especificaciones del problema.
- **Línea 29:** `for i in range(n):`: Itera exactamente `n` veces para capturar la información del lote.
- **Líneas 30 a 32:** `nombre = input(...).strip()` y `while not nombre:`: Solicita el nombre del productor eliminando espacios al inicio y final con `strip()`, garantizando que no se ingresen nombres vacíos.
- **Línea 33:** `while True:`: Bucle de validación para la entrada de litros.
- **Líneas 34 a 41:** `try-except ValueError`: Captura entradas no numéricas decimales e impone el rango industrial de producción en calderas de la planta lechera (entre 100 y 1000 litros). Si la cantidad es válida, añade la tupla `(nombre, litros)` mediante `append()` y sale del validador con `break`.
- **Línea 42:** `else:`: Rama alternativa para la generación aleatoria de prueba.
- **Línea 43:** `productores_ejemplo = [...]`: Define un catálogo de 8 nombres de productores reales típicos del sur de Chile (Osorno, Llanquihue, Frutillar).
- **Líneas 45 a 47:** `for prod in productores_ejemplo:`: Itera sobre los nombres del catálogo, genera un volumen de litros aleatorio en $[100, 1000]$ con un decimal y anexa la tupla correspondiente.
- **Línea 50:** `total_litros = 0.0`: Inicializa a cero el acumulador del volumen de la planta.
- **Líneas 51 a 52:** `prod_max = produccion[0]` y `prod_min = produccion[0]`: Inicializa las tuplas centinelas con la primera tupla de la lista.
- **Línea 53:** `productores_mas_500 = 0`: Inicializa el contador del segmento superior de producción.
- **Línea 55:** `for productor in produccion:`: Recorre ordenadamente cada una de las tuplas contenidas en la lista.
- **Línea 56:** `nombre, litros = productor`: Realiza el desempaquetado automático (*unpacking*) de la tupla para evitar accesos oscuros mediante subíndices numéricos directos (como `productor[0]` o `productor[1]`), mejorando la legibilidad académica.
- **Línea 57:** `total_litros += litros`: Acumula los litros del productor evaluado.
- **Líneas 60 a 63:** `if litros > prod_max[1]:` y `if litros < prod_min[1]:`: Realiza la evaluación comparando los litros del elemento actual con el componente numérico de las tuplas centinelas. Si se cumple, actualiza la tupla completa del productor.
- **Líneas 65 a 66:** `if litros > 500.0:`: Evalúa la condición de superación del umbral de 500 litros e incrementa el contador en consecuencia.
- **Líneas 69 a 75:** `print(...)`: Emite el listado de productores recorriendo la lista e imprime los resultados formateados con un decimal.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Planificación y Análisis de Producción Láctea (Lista de Tuplas)
# ==============================================================================
import random

print("--- Planta Lechera: Registro de Productores ---")
print("1. Carga manual de registros")
print("2. Carga automática aleatoria (8 productores de prueba)")

# Validar opción de interfaz de usuario
while True:
    try:
        modo = int(input("Seleccione su opción (1 o 2): "))
        if modo in [1, 2]:
            break
        print("Opción inválida. Ingrese 1 o 2.")
    except ValueError:
        print("Por favor, ingrese un número entero.")

produccion = []

# Carga de datos
if modo == 1:
    while True:
        try:
            n = int(input("¿Cuántos productores registrará hoy? (Mínimo 8): "))
            if n >= 8:
                break
            print("La normativa exige analizar al menos 8 productores.")
        except ValueError:
            print("Ingrese un número entero válido.")
            
    for i in range(n):
        nombre = input(f"Nombre del productor {i+1}: ").strip()
        while not nombre:
            nombre = input(f"El nombre es requerido. Nombre {i+1}: ").strip()
        while True:
            try:
                litros = float(input(f"Litros entregados por {nombre} (100 a 1000 L): "))
                if 100 <= litros <= 1000:
                    produccion.append((nombre, litros))
                    break
                print("Cantidad fuera del rango autorizado por la planta lechera (100 a 1000 L).")
            except ValueError:
                print("Ingrese un valor numérico.")
else:
    # Catálogo geográfico de productores del sur de Chile
    productores_ejemplo = [
        "Fundo El Rosedal", "Lechería Osorno", "Agrícola Valdivia", "Estancia del Sur", 
        "Lácteos Llanquihue", "Fundo Las Rosas", "Productor Alianza", "Cooperativa Frutillar"
    ]
    for prod in productores_ejemplo:
        litros = round(random.uniform(100.0, 1000.0), 1)
        produccion.append((prod, litros))
    print("\nDatos de 8 productores cargados automáticamente.")

# Algoritmo de cálculo estadístico manual (Evitando sum(), min(), max())
total_litros = 0.0
prod_max = produccion[0]
prod_min = produccion[0]
productores_mas_500 = 0

for productor in produccion:
    # Desempaquetado de tuplas (Unpacking)
    nombre, litros = productor
    total_litros += litros
    
    # Comparación manual de volúmenes máximos y mínimos
    if litros > prod_max[1]:
        prod_max = productor
    if litros < prod_min[1]:
        prod_min = productor
        
    # Clasificación por volumen crítico
    if litros > 500.0:
        productores_mas_500 += 1

# Emisión formal de Resultados
print("\n--- Reporte General de Recolección Láctea ---")
for p in produccion:
    print(f"- {p[0]}: {p[1]:.1f} Litros")
    
print(f"\nTotal de litros recolectados en el día: {total_litros:.1f} L")
print(f"Productor estrella (Máxima entrega): {prod_max[0]} con {prod_max[1]:.1f} L")
print(f"Productor con menor volumen: {prod_min[0]} con {prod_min[1]:.1f} L")
print(f"Productores con entrega sobre 500 litros: {productores_mas_500}")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Carga Aleatoria y Simulación Automática
```text
--- Planta Lechera: Registro de Productores ---
1. Carga manual de registros
2. Carga automática aleatoria (8 productores de prueba)
Seleccione su opción (1 o 2): 2

Datos de 8 productores cargados automáticamente.

--- Reporte General de Recolección Láctea ---
- Fundo El Rosedal: 750.5 Litros
- Lechería Osorno: 120.4 Litros
- Agrícola Valdivia: 980.2 Litros
- Estancia del Sur: 450.0 Litros
- Lácteos Llanquihue: 510.3 Litros
- Fundo Las Rosas: 320.8 Litros
- Productor Alianza: 890.1 Litros
- Cooperativa Frutillar: 605.5 Litros

Total de litros recolectados en el día: 4627.8 L
Productor estrella (Máxima entrega): Agrícola Valdivia con 980.2 L
Productor con menor volumen: Lechería Osorno con 120.4 L
Productores con entrega sobre 500 litros: 5
```

##### Caso 2: Carga Manual Mínima (8 Productores) con Errores de Validación
```text
--- Planta Lechera: Registro de Productores ---
1. Carga manual de registros
2. Carga automática aleatoria (8 productores de prueba)
Seleccione su opción (1 o 2): 1
¿Cuántos productores registrará hoy? (Mínimo 8): 5
La normativa exige analizar al menos 8 productores.
¿Cuántos productores registrará hoy? (Mínimo 8): 8
Nombre del productor 1: Fundo Osorno
Litros entregados por Fundo Osorno (100 a 1000 L): 50
Cantidad fuera del rango autorizado por la planta lechera (100 a 1000 L).
Litros entregados por Fundo Osorno (100 a 1000 L): 600
... [Ingreso del resto de los productores] ...
Nombre del productor 8: Fundo Puyehue
Litros entregados por Fundo Puyehue (100 a 1000 L): 420.5

--- Reporte General de Recolección Láctea ---
- Fundo Osorno: 600.0 Litros
- Fundo Ranco: 750.0 Litros
- Agrícola Sur: 300.0 Litros
- Cooperativa: 890.0 Litros
- Lechería X: 150.0 Litros
- Productor Y: 520.0 Litros
- Fundo Rupanco: 910.0 Litros
- Fundo Puyehue: 420.5 Litros

Total de litros recolectados en el día: 4540.5 L
Productor estrella (Máxima entrega): Fundo Rupanco con 910.0 L
Productor con menor volumen: Lechería X con 150.0 L
Productores con entrega sobre 500 litros: 5
```
