### Ejercicio 2: Control de temperatura en invernadero agrícola

#### Enunciado del Problema
En la agricultura chilena, especialmente en zonas donde se producen hortalizas bajo invernadero, es importante controlar la temperatura para evitar pérdidas en los cultivos.
Desarrolla un script en Python que permita analizar las temperaturas registradas durante una jornada dentro de un invernadero.
El programa debe:
- Crear una tupla con 12 temperaturas registradas durante el día. Puedes ingresarlas manualmente o generarlas usando `random` en un rango entre 8 y 35 grados.
- Recorrer la tupla y mostrar:
    + La temperatura más baja.
    + La temperatura más alta.
    + Cuántas mediciones estuvieron bajo los 12 grados.
    + Cuántas mediciones estuvieron sobre los 30 grados.

Consideraciones:
- Usa una tupla porque las mediciones ya fueron registradas y no deberían modificarse.
- Se recomienda calcular manualmente el promedio, mínimo y máximo para practicar recorridos.
- El programa debe mostrar un pequeño mensaje final, por ejemplo: “Jornada estable”, “Riesgo por frío” o “Riesgo por exceso de calor”.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `modo` | `int` | Opción del menú interactivo seleccionada (1 para manual, 2 para aleatorio). |
| `lista_temp` | `list (float)` | Lista dinámica auxiliar usada para recolectar las temperaturas. |
| `temp` | `float` | Almacena temporalmente una medición de temperatura en procesamiento. |
| `temperaturas` | `tuple (float)` | Estructura inmutable final que contiene las 12 temperaturas de la jornada. |
| `suma_temp` | `float` | Acumulador aritmético manual de temperaturas. |
| `temp_baja` | `float` | Centinela para almacenar la menor temperatura registrada en la tupla. |
| `temp_alta` | `float` | Centinela para almacenar la mayor temperatura registrada en la tupla. |
| `mediciones_bajo_12` | `int` | Contador de mediciones que registran frío extremo (menos de 12°C). |
| `mediciones_sobre_30` | `int` | Contador de mediciones que registran calor extremo (más de 30°C). |
| `promedio` | `float` | Media aritmética calculada del total de mediciones del día. |
| `diagnostico` | `str` | Cadena descriptiva del estado de alerta agroclimático de la jornada. |

---

#### Lógica de la Solución
1. **Recolección en Contenedor Dinámico y Conversión Inmutable:** Para evitar la concatenación ineficiente de tuplas en memoria (lo cual crea copias constantes de la estructura en cada iteración), las temperaturas se recopilan en una lista auxiliar `lista_temp`. Posteriormente, se convierten a una tupla inmutable definitiva mediante `tuple()`.
2. **Ciclos de Validación e Interactividad:** Se aplican menús robustos con captura de errores ValueError e intervalos válidos para el cultivo (8°C a 35°C).
3. **Procesamiento Lineal de un Solo Recorrido:** Se diseña un algoritmo de un solo paso (*single pass*) en el que un ciclo `for` calcula simultáneamente la suma de las temperaturas, actualiza los valores mínimos y máximos mediante comparaciones de centinela, y clasifica las temperaturas en los contadores críticos (<12°C y >30°C).
4. **Sistema Inteligente de Diagnóstico:** En base a los conteos críticos recopilados y la media global, el script evalúa las condiciones e imprime un diagnóstico agronómico de alerta.

---

#### Explicación Línea por Línea
- **Línea 3:** `import random`: Carga el módulo matemático para generar temperaturas simuladas.
- **Líneas 5 a 7:** `print(...)`: Emite en consola las opciones del menú.
- **Línea 9:** `while True:`: Garantiza la selección correcta de modo de operación.
- **Líneas 10 a 16:** `try-except ValueError`: Captura entradas no enteras al seleccionar modo y valida la entrada correcta.
- **Línea 18:** `lista_temp = []`: Inicializa una lista vacía para acumular de forma eficiente en memoria las temperaturas.
- **Línea 20:** `if modo == 1:`: Condición para capturar manualmente 12 temperaturas.
- **Línea 21:** `for i in range(12):`: Bucle finito iterativo para las 12 muestras correspondientes a intervalos de 2 horas.
- **Línea 22:** `while True:`: Validador de rangos para blindar la entrada del usuario.
- **Líneas 23 a 30:** `try-except ValueError`: Captura entradas no numéricas en el ingreso decimal.
- **Línea 24:** `temp = float(...)`: Convierte la entrada a flotante.
- **Líneas 25 a 27:** `if 8 <= temp <= 35:`: Comprueba límites de medición física. Si es correcto, anexa con `append()` a la lista y rompe el ciclo interno con `break`.
- **Línea 31:** `else:`: Se activa si la opción elegida es autogeneración aleatoria.
- **Línea 32:** `for _ in range(12):`: Bucle que corre 12 iteraciones independientes.
- **Línea 33:** `lista_temp.append(...)`: Genera valores flotantes en $[8.0, 35.0]$ usando `random.uniform()`, limita a un decimal y los inserta en la lista.
- **Línea 37:** `temperaturas = tuple(lista_temp)`: Optimización clave. Convierte la lista mutable en una tupla inmutable en una sola instrucción, protegiendo los datos contra mutaciones accidentales.
- **Línea 40:** `suma_temp = 0.0`: Inicializa a cero el acumulador para la suma aritmética.
- **Líneas 41 a 42:** `temp_baja = temperaturas[0]` y `temp_alta = temperaturas[0]`: Inicializa los extremos usando el primer elemento.
- **Líneas 43 a 44:** `mediciones_bajo_12 = 0` y `mediciones_sobre_30 = 0`: Inicializa los acumuladores de frecuencias.
- **Línea 46:** `for temp in temperaturas:`: Recorre de forma secuencial cada temperatura registrada.
- **Línea 47:** `suma_temp += temp`: Suma de forma iterativa el registro.
- **Líneas 48 a 51:** `if temp < temp_baja:` y `if temp > temp_alta:`: Actualiza dinámicamente los límites térmicos mínimo y máximo si el elemento actual supera a los centinelas.
- **Líneas 52 a 55:** `if temp < 12:` y `elif temp > 30:`: Valida e incrementa los contadores críticos en caso de helada o sobrecalentamiento.
- **Línea 57:** `promedio = suma_temp / len(temperaturas)`: Calcula la media matemática del día.
- **Líneas 60 a 67:** `if-elif-else`: Evalúa múltiples criterios estadísticos lógicos para asignar un diagnóstico preciso sobre el ecosistema del invernadero.
- **Líneas 70 a 77:** `print(...)`: Formatea con un decimal (`:.1f`) e imprime el reporte final en consola.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Analizador Térmico de Invernaderos Agrícolas (Tuplas e Inmutabilidad)
# ==============================================================================
import random

print("--- Analizador Térmico de Invernaderos ---")
print("1. Ingreso manual de 12 registros de temperatura")
print("2. Carga automática aleatoria (8°C a 35°C)")

# Validar opción de interfaz de usuario
while True:
    try:
        modo = int(input("Seleccione su opción (1 o 2): "))
        if modo in [1, 2]:
            break
        print("Opción inválida. Ingrese 1 o 2.")
    except ValueError:
        print("Por favor, ingrese un número entero.")

lista_temp = []

# Carga de datos
if modo == 1:
    for i in range(12):
        while True:
            try:
                temp = float(input(f"Ingrese temperatura de la medición {i+1} (8°C a 35°C): "))
                if 8 <= temp <= 35:
                    lista_temp.append(temp)
                    break
                print("Temperatura fuera de rango del sensor (8 a 35°C).")
            except ValueError:
                print("Entrada no válida. Ingrese un número.")
else:
    for _ in range(12):
        lista_temp.append(round(random.uniform(8.0, 35.0), 1))
    print("\nJornada térmica autogenerada exitosamente.")

# Conversión eficiente y óptima a tupla inmutable para proteger los registros históricos
temperaturas = tuple(lista_temp)

# Algoritmo de recorrido manual en un único ciclo
suma_temp = 0.0
temp_baja = temperaturas[0]
temp_alta = temperaturas[0]
mediciones_bajo_12 = 0
mediciones_sobre_30 = 0

for temp in temperaturas:
    suma_temp += temp
    # Evaluar temperatura extrema baja
    if temp < temp_baja:
        temp_baja = temp
    # Evaluar temperatura extrema alta
    if temp > temp_alta:
        temp_alta = temp
    # Contabilizar eventos térmicos críticos
    if temp < 12:
        mediciones_bajo_12 += 1
    elif temp > 30:
        mediciones_sobre_30 += 1

promedio = suma_temp / len(temperaturas)

# Sistema experto de diagnóstico agronómico
if mediciones_bajo_12 > 0 and mediciones_sobre_30 > 0:
    diagnostico = "Riesgo Crítico: Inestabilidad térmica extrema (heladas y golpes de calor en el mismo día)"
elif mediciones_bajo_12 > 3 or promedio < 15:
    diagnostico = "Riesgo por Frío: Activar sistemas de calefacción o invernadero cerrado"
elif mediciones_sobre_30 > 3 or promedio > 28:
    diagnostico = "Riesgo por Exceso de Calor: Activar ventiladores y extractores de aire"
else:
    diagnostico = "Jornada Estable: Condiciones óptimas para el cultivo agrícola"

# Reporte Diario
print("\n--- Reporte Diario de Invernadero ---")
print(f"Registro de temperaturas: {temperaturas}")
print(f"Temperatura Promedio: {promedio:.1f}°C")
print(f"Mínima registrada: {temp_baja}°C")
print(f"Máxima registrada: {temp_alta}°C")
print(f"Mediciones Críticas de Frío (<12°C): {mediciones_bajo_12}")
print(f"Mediciones Críticas de Calor (>30°C): {mediciones_sobre_30}")
print(f"Estado de Alerta del Día: {diagnostico.upper()}")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Estabilidad Térmica
```text
--- Analizador Térmico de Invernaderos ---
1. Ingreso manual de 12 registros de temperatura
2. Carga automática aleatoria (8°C a 35°C)
Seleccione su opción (1 o 2): 2

Jornada térmica autogenerada exitosamente.

--- Reporte Diario de Invernadero ---
Registro de temperaturas: (20.5, 21.2, 19.8, 22.0, 24.5, 23.1, 18.9, 17.5, 21.0, 22.4, 20.1, 19.0)
Temperatura Promedio: 20.8°C
Mínima registrada: 17.5°C
Máxima registrada: 24.5°C
Mediciones Críticas de Frío (<12°C): 0
Mediciones Críticas de Calor (>30°C): 0
Estado de Alerta del Día: JORNADA ESTABLE: CONDICIONES ÓPTIMAS PARA EL CULTIVO AGRÍCOLA
```

##### Caso 2: Alerta por Calor e Ingreso Inválido
```text
--- Analizador Térmico de Invernaderos ---
1. Ingreso manual de 12 registros de temperatura
2. Carga automática aleatoria (8°C a 35°C)
Seleccione su opción (1 o 2): 1
Ingrese temperatura de la medición 1 (8°C a 35°C): 45
Temperatura fuera de rango del sensor (8 a 35°C).
Ingrese temperatura de la medición 1 (8°C a 35°C): 32
... [Ingreso manual de temperaturas: 31, 33, 29, 28, 30, 31, 32, 29, 31, 30, 28] ...
Ingrese temperatura de la medición 12 (8°C a 35°C): 33

--- Reporte Diario de Invernadero ---
Registro de temperaturas: (32.0, 31.0, 33.0, 29.0, 28.0, 30.0, 31.0, 32.0, 29.0, 31.0, 30.0, 33.0)
Temperatura Promedio: 30.8°C
Mínima registrada: 28.0°C
Máxima registrada: 33.0°C
Mediciones Críticas de Frío (<12°C): 0
Mediciones Críticas de Calor (>30°C): 7
Estado de Alerta del Día: RIESGO POR EXCESO DE CALOR: ACTIVAR VENTILADORES Y EXTRACTORES DE AIRE
```
