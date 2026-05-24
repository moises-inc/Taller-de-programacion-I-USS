### Ejercicio 7: Validador y Clasificador de Notas Académicas

#### Enunciado del Problema
Desarrolla un script que pida una nota final en escala de 1.0 a 7.0 e indique si el estudiante está aprobado o reprobado, considerando que en Chile se aprueba con nota 4.0 o superior.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `nota` | `float` | Almacena la calificación final del alumno. Su rango de validez académica está restringido entre $1.0$ y $7.0$. |

#### Lógica de la Solución
El algoritmo modela el sistema de calificación académica chileno. La solución implementa un mecanismo robusto de doble filtro de validación en una sola estructura:
1. **Filtro de Tipo:** Asegura mediante `try-except` que el dato de entrada sea numérico de punto flotante (`float`).
2. **Filtro de Rango Académico:** Comprueba de forma condicional que la nota se encuentre estrictamente dentro de la escala oficial ($[1.0, 7.0]$). Si el valor ingresado es menor a $1.0$ o mayor a $7.0$, el programa lo rechaza informativamente y solicita reingreso.

Posteriormente, la aprobación o reprobación se evalúa de manera directa mediante una bifurcación de control condicional básica (`if-else`):
* Si la $\text{nota} < 4.0$, el estudiante se clasifica como **Reprobado**.
* Si la $\text{nota} \ge 4.0$, el estudiante se clasifica como **Aprobado**.

#### Explicación Línea por Línea
* **Línea 5 (`print(...)`):** Muestra el banner inicial del clasificador académico.
* **Línea 7 (`while True:`):** Inicializa el bucle infinito protector para capturar una nota correcta.
* **Línea 8 (`try:`):** Declaración del bloque protegido de captura.
* **Línea 9 (`nota = float(input(...))`):** Captura el valor de consola, lo convierte a decimal (`float`) y lo almacena.
* **Línea 10 (`if 1.0 <= nota <= 7.0:`):** Evalúa si el número decimal ingresado pertenece al intervalo cerrado de notas chilenas $[1.0, 7.0]$.
* **Línea 11 (`break`):** Rompe la iteración si la nota cumple con las condiciones de escala.
* **Línea 12 (`else:`):** Rama ejecutada si la nota es menor que $1.0$ o mayor que $7.0$.
* **Línea 13 (`print(...)`):** Explica los límites académicos formales al usuario y reinicia el bucle.
* **Línea 14 (`except ValueError:`):** Atrapa excepciones de formato de entrada (ej: ingresar letras o coma en vez de punto).
* **Línea 15 (`print(...)`):** Informa de la anomalía en el formato del dato numérico.
* **Línea 17 (`if nota < 4.0:`):** Evalúa si la nota obtenida no alcanza el umbral de aprobación establecido en $4.0$.
* **Línea 18 (`print(...)`):** Muestra en pantalla el estado de **Reprobado**, formateando la nota con un decimal (`:.1f`).
* **Línea 19 (`else:`):** Rama de control por descarte (para toda nota superior o igual a $4.0$).
* **Línea 20 (`print(...)`):** Despliega el estado de **Aprobado** formateado pedagógicamente.

#### Código Completo
```python
# Validador y clasificador de notas finales en Chile

print("--- Clasificación de Notas Académicas ---")

while True:
    try:
        # Captura y conversión del dato a punto flotante
        nota = float(input("Ingrese la nota del estudiante (1.0 a 7.0): "))
        # Validación de que la nota se ubique en la escala formal chilena
        if 1.0 <= nota <= 7.0:
            break  # Entrada válida, rompe el bucle
        else:
            print("Nota inválida. Recuerde que el rango en Chile es exclusivamente de 1.0 a 7.0.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal.")

# Evaluación del umbral de aprobación (nota 4.0)
if nota < 4.0:
    print(f"El estudiante ha obtenido nota {nota:.1f}: Reprobado.")
else:
    print(f"El estudiante ha obtenido nota {nota:.1f}: Aprobado.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Aprobación estricta):
* **Entrada esperada:** `4.0`
* **Salida del programa:** `El estudiante ha obtenido nota 4.0: Aprobado.`

##### Caso de Uso 2 (Reprobación):
* **Entrada esperada:** `3.8`
* **Salida del programa:** `El estudiante ha obtenido nota 3.8: Reprobado.`

##### Caso de Uso 3 (Aprobación con nota máxima):
* **Entrada esperada:** `7`
* **Salida del programa:** `El estudiante ha obtenido nota 7.0: Aprobado.`

##### Caso de Uso 4 (Entrada fuera de escala y corrección):
* **Entrada esperada:** `8.5` (luego) `0.5` (luego) `5.5`
* **Salida del programa:**
  ```text
  Ingrese la nota del estudiante (1.0 a 7.0): 8.5
  Nota inválida. Recuerde que el rango en Chile es exclusivamente de 1.0 a 7.0.
  Ingrese la nota del estudiante (1.0 a 7.0): 0.5
  Nota inválida. Recuerde que el rango en Chile es exclusivamente de 1.0 a 7.0.
  Ingrese la nota del estudiante (1.0 a 7.0): 5.5
  El estudiante ha obtenido nota 5.5: Aprobado.
  ```
