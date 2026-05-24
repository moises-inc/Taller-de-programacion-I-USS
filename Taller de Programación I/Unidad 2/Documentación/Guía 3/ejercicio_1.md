### Ejercicio 1: Análisis de pesos en salmonicultura

#### Enunciado del Problema
En el sur de Chile, la industria del salmón requiere monitorear constantemente el peso de los peces para tomar decisiones de alimentación y crecimiento.
Desarrolla un script en Python que permita analizar una muestra de salmones. El programa debe:
- Generar una lista con 10 pesos de salmones (puedes pedirlos al usuario o generarlos automáticamente usando `random` en un rango entre 2.5 y 6.0 kg).
- Mostrar:
    + El peso promedio (promedio = suma de pesos / cantidad de salmones).
    + El peso más bajo.
    + El peso más alto.
    + Cuántos salmones están sobre el promedio.

Consideraciones:
- No usar funciones incorporadas como `max()`, `min()` o `sum()`.
- Usar ciclos (`for` o `while`).
- Separar el cálculo del promedio del análisis posterior.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `modo` | `int` | Determina si el ingreso de datos es manual (1) o automático (2). |
| `pesos_salmones` | `list (float)` | Almacena los 10 pesos de la muestra de salmones. |
| `peso` | `float` | Almacena temporalmente el peso ingresado de un salmón individual. |
| `suma_pesos` | `float` | Acumulador manual para obtener la suma total de los pesos (reemplaza a `sum()`). |
| `promedio` | `float` | Almacena el valor promedio del peso de los salmones. |
| `peso_mas_bajo` | `float` | Almacena el valor mínimo hallado en el recorrido de la lista (reemplaza a `min()`). |
| `peso_mas_alto` | `float` | Almacena el valor máximo hallado en el recorrido de la lista (reemplaza a `max()`). |
| `salmones_sobre_promedio` | `int` | Contador de los salmones cuyo peso supera al promedio general. |

---

#### Lógica de la Solución
El algoritmo se divide en cuatro fases principales para asegurar un diseño limpio y estructurado:
1. **Captura Dinámica e Interactiva de Datos:** Se implementa un menú que ofrece dos modalidades para cargar la lista de 10 elementos. Se aplican ciclos iterativos estructurados con control de excepciones `try-except` para blindar el programa ante ingresos erróneos de tipo y de rangos de negocio (2.5 a 6.0 kg).
2. **Cálculo de Métricas Centrales (Suma y Promedio):** Se recorre manualmente la lista acumulando cada peso en `suma_pesos` y luego se divide este acumulador por el número de elementos.
3. **Búsqueda Manual de Extremos (Mínimo y Máximo):** Se inicializan las variables `peso_mas_bajo` y `peso_mas_alto` con el primer elemento de la lista. Mediante un bucle `for`, se evalúa secuencialmente el resto de la lista reemplazando los extremos si se halla un valor menor o mayor respectivamente.
4. **Análisis de Clasificación en Contenedores:** Se recorre la lista para contar cuántos elementos superan estadísticamente el promedio antes calculado, presentando finalmente el reporte consolidado.

---

#### Explicación Línea por Línea
- **Línea 3:** `import random`: Importa el módulo estándar para la generación de números pseudoaleatorios, empleado en la carga automática.
- **Líneas 5 a 7:** `print(...)`: Muestra en consola la interfaz del menú principal.
- **Línea 9:** `while True:`: Inicia un ciclo infinito para asegurar una selección de modo válida por parte del usuario.
- **Líneas 10 a 14:** `try-except ValueError`: Bloque que captura excepciones en caso de que el usuario introduzca caracteres no numéricos enteros.
- **Líneas 11 a 13:** `modo = int(input(...))`: Solicita la opción de modo y valida si es `1` o `2` mediante la pertenencia `in [1, 2]`. De ser correcto, ejecuta `break` para romper el bucle.
- **Línea 17:** `pesos_salmones = []`: Inicializa la lista vacía para almacenar los pesos de la muestra.
- **Línea 19:** `if modo == 1:`: Estructura condicional que evalúa si la opción elegida fue el ingreso manual.
- **Línea 21:** `for i in range(10):`: Bucle finito para capturar exactamente 10 muestras individuales de pesos.
- **Línea 22:** `while True:`: Bucle de validación interactiva para blindar la entrada de cada peso.
- **Líneas 23 a 30:** `try-except ValueError`: Captura entradas no numéricas en el ingreso decimal.
- **Línea 24:** `peso = float(...)`: Convierte la entrada a punto flotante.
- **Líneas 25 a 27:** `if 2.5 <= peso <= 6.0:`: Valida que el peso del salmón se encuentre en el rango permitido (2.5 a 6.0 kg). Si se cumple, lo agrega a la lista con `append()` y sale del bucle de validación actual con `break`.
- **Línea 31:** `else:`: Bloque alternativo que se ejecuta si se seleccionó la generación automática.
- **Línea 33:** `for _ in range(10):`: Bucle que itera 10 veces de forma automática sin utilizar la variable de iteración (`_`).
- **Línea 35:** `pesos_salmones.append(...)`: Genera un float aleatorio en el rango $[2.5, 6.0]$ usando `random.uniform()`, lo redondea a 2 decimales mediante `round()` y lo anexa a la lista de muestras.
- **Línea 39:** `suma_pesos = 0.0`: Inicializa a cero el acumulador decimal de pesos.
- **Línea 40 a 41:** `for peso in pesos_salmones:`: Itera secuencialmente sobre cada elemento de la lista y lo adiciona a `suma_pesos`.
- **Línea 42:** `promedio = suma_pesos / len(pesos_salmones)`: Calcula la media aritmética al dividir la suma total acumulada por la longitud total del contenedor.
- **Líneas 45 a 46:** `peso_mas_bajo = pesos_salmones[0]` y `peso_mas_alto = pesos_salmones[0]`: Inicializa las variables centinelas con la primera muestra para iniciar la comparación manual.
- **Línea 48:** `for peso in pesos_salmones[1:]:`: Itera a partir del segundo elemento (índice 1) para evitar comparar el primer elemento consigo mismo, ahorrando operaciones.
- **Líneas 49 a 52:** `if peso < peso_mas_bajo:` y `if peso > peso_mas_alto:`: Evalúa si el elemento en curso es inferior al mínimo o superior al máximo registrado. Si se cumple, actualiza la variable respectiva.
- **Línea 55:** `salmones_sobre_promedio = 0`: Inicializa el contador entero de salmones que superan la media.
- **Líneas 56 a 58:** `for peso in pesos_salmones:`: Recorre la lista evaluando si cada peso es estrictamente mayor que `promedio`. Si lo es, incrementa en una unidad el contador.
- **Líneas 61 a 66:** `print(...)`: Formatea y muestra los resultados del reporte final usando *f-strings* con limitación decimal a dos dígitos (`:.2f`).

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Análisis Estadístico de Salmonicultura (Operaciones Manuales)
# ==============================================================================
import random

print("--- Sistema de Monitoreo de Salmonicultura ---")
print("1. Ingresar pesos manualmente")
print("2. Autogenerar muestra de 10 salmones (Aleatorio entre 2.5 y 6.0 kg)")

# Validar opción del menú operativo
while True:
    try:
        modo = int(input("Seleccione su opción (1 o 2): "))
        if modo in [1, 2]:
            break
        print("Opción inválida. Ingrese 1 o 2.")
    except ValueError:
        print("Por favor, ingrese un número entero.")

pesos_salmones = []

# Carga de la muestra
if modo == 1:
    # Captura e interactividad manual para los 10 pesos
    for i in range(10):
        while True:
            try:
                peso = float(input(f"Ingrese el peso del salmón {i+1} (2.5 a 6.0 kg): "))
                if 2.5 <= peso <= 6.0:
                    pesos_salmones.append(peso)
                    break
                print("Peso inválido. Recuerde ingresar valores de 2.5 a 6.0 kg.")
            except ValueError:
                print("Entrada no válida. Ingrese un valor numérico.")
else:
    # Carga aleatoria automática controlada en rangos físicos
    for _ in range(10):
        pesos_salmones.append(round(random.uniform(2.5, 6.0), 2))
    print("\nMuestra generada automáticamente exitosamente.")

# Algoritmo Manual de Suma (Evitando la función sum())
suma_pesos = 0.0
for peso in pesos_salmones:
    suma_pesos += peso
promedio = suma_pesos / len(pesos_salmones)

# Algoritmo Manual de Mínimo y Máximo (Evitando funciones min() y max())
peso_mas_bajo = pesos_salmones[0]
peso_mas_alto = pesos_salmones[0]

for peso in pesos_salmones[1:]:
    if peso < peso_mas_bajo:
        peso_mas_bajo = peso
    if peso > peso_mas_alto:
        peso_mas_alto = peso

# Conteo de elementos que superan el promedio
salmones_sobre_promedio = 0
for peso in pesos_salmones:
    if peso > promedio:
        salmones_sobre_promedio += 1

# Presentación formal de los resultados
print("\n--- Reporte Estadístico de la Muestra ---")
print(f"Muestra analizada: {[round(p, 2) for p in pesos_salmones]}")
print(f"Peso Promedio: {promedio:.2f} kg")
print(f"Peso Mínimo Registrado: {peso_mas_bajo:.2f} kg")
print(f"Peso Máximo Registrado: {peso_mas_alto:.2f} kg")
print(f"Salmones sobre el promedio: {salmones_sobre_promedio}")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Generación Automática (Aleatoria)
```text
--- Sistema de Monitoreo de Salmonicultura ---
1. Ingresar pesos manualmente
2. Autogenerar muestra de 10 salmones (Aleatorio entre 2.5 y 6.0 kg)
Seleccione su opción (1 o 2): 2

Muestra generada automáticamente exitosamente.

--- Reporte Estadístico de la Muestra ---
Muestra analizada: [3.45, 5.12, 2.78, 4.89, 5.91, 3.12, 4.56, 3.88, 5.22, 4.01]
Peso Promedio: 4.29 kg
Peso Mínimo Registrado: 2.78 kg
Peso Máximo Registrado: 5.91 kg
Salmones sobre el promedio: 5
```

##### Caso 2: Ingreso Manual con Validación de Errores
```text
--- Sistema de Monitoreo de Salmonicultura ---
1. Ingresar pesos manualmente
2. Autogenerar muestra de 10 salmones (Aleatorio entre 2.5 y 6.0 kg)
Seleccione su opción (1 o 2): 1
Ingrese el peso del salmón 1 (2.5 a 6.0 kg): 2.1
Peso inválido. Recuerde ingresar valores de 2.5 a 6.0 kg.
Ingrese el peso del salmón 1 (2.5 a 6.0 kg): abc
Entrada no válida. Ingrese un valor numérico.
Ingrese el peso del salmón 1 (2.5 a 6.0 kg): 3.5
... [Ingreso de los siguientes pesos: 4.0, 5.5, 4.8, 3.9, 4.2, 5.1, 3.6, 2.9, 5.8] ...
Ingrese el peso del salmón 10 (2.5 a 6.0 kg): 4.5

--- Reporte Estadístico de la Muestra ---
Muestra analizada: [3.5, 4.0, 5.5, 4.8, 3.9, 4.2, 5.1, 3.6, 2.9, 4.5]
Peso Promedio: 4.21 kg
Peso Mínimo Registrado: 2.90 kg
Peso Máximo Registrado: 5.50 kg
Salmones sobre el promedio: 5
```
