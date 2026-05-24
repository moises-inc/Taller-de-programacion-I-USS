### Ejercicio 11: Control de notas para 30 estudiantes con ciclos

#### Enunciado del Problema
Desarrolla un script que solicite las notas finales de 30 estudiantes, en escala de 1.0 a 7.0. Para cada estudiante, debe indicar si está aprobado o reprobado. Al final, debe mostrar:
• Cantidad de aprobados
• Cantidad de reprobados
• Promedio general del curso

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `aprobados` | `int` | Contador incremental para cuantificar los estudiantes con nota aprobatoria (>= 4.0). |
| `reprobados` | `int` | Contador incremental para cuantificar los estudiantes reprobados (< 4.0). |
| `suma_notas` | `float` | Acumulador aritmético decimal para registrar la suma total de las notas ingresadas. |
| `i` | `int` | Variable de iteración del ciclo `for` que denota el índice del estudiante actual. |
| `nota` | `float` | Guarda temporalmente la calificación flotante en evaluación, validada en el rango `[1.0, 7.0]`. |
| `promedio` | `float` | Almacena la media aritmética final calculada al dividir la suma de notas por el número total de alumnos (30). |


## Lógica de la Solución
El programa procesa secuencialmente las calificaciones de un curso compuesto por 30 alumnos mediante un bucle determinado `for i in range(30)`. En cada iteración se solicita la nota final de un estudiante. Para garantizar la solidez de los datos: - Se anida un ciclo infinito `while True` con un bloque `try-except` para rechazar ingresos no numéricos.- Se incluye una validación lógica para descartar calificaciones fuera del rango `[1.0, 7.0]`.A medida que se ingresan las notas válidas: - Se acumulan en la variable `suma_notas`.- Se evalúa si el alumno está aprobado (nota >= 4.0) o reprobado (nota < 4.0), incrementando su respectivo contador y mostrando su estado inmediatamente en consola.Al finalizar el bucle general de 30 ciclos, se calcula la media aritmética general y se entrega un informe detallado del curso.

## Explicación Línea por Línea
- **`aprobados = 0`**: Inicializa en cero el contador acumulador para los alumnos con nota de aprobación.
- **`reprobados = 0`**: Inicializa en cero el contador acumulador para los alumnos reprobados.
- **`suma_notas = 0.0`**: Inicializa en 0.0 la variable acumuladora flotante destinada a sumar todas las notas.
- **`for i in range(30):`**: Declara un ciclo determinado `for` que se repetirá exactamente 30 veces (con índices de `i` de 0 a 29).
- **`while True:`**: Declara un ciclo interno de validación interactiva infinita para blindar el ingreso de la nota.
- **`try:`**: Región del bucle de validación encargada de detectar excepciones por tipo de dato.
- **`nota = float(input(...))`**: Solicita la nota al usuario, la convierte a decimal y la almacena temporalmente en `nota`.
- **`if 1.0 <= nota <= 7.0:`**: Valida si la calificación pertenece a la escala reglamentaria de Chile.
- **`break`**: Sale del bucle de validación interno al cumplirse todas las condiciones lógicas y sintácticas.
- **`print("Error: La nota...")`**: Mensaje que se ejecuta en el `else` de rango, indicando los límites válidos.
- **`except ValueError:`**: Atrapa errores causados al ingresar textos no numéricos en la entrada flotante.
- **`print("Error: Ingrese un decimal...")`**: Advierte sobre el ingreso erróneo de tipo de dato.
- **`suma_notas += nota`**: Acumulador. Suma el valor de la nota válida actual a la bolsa general de notas mediante el operador simplificado `+=`.
- **`if nota >= 4.0:`**: Evalúa si la nota individual del alumno cumple el criterio de aprobación (mayor o igual a 4.0).
- **`aprobados += 1`**: Suma 1 unidad al acumulador de aprobados.
- **`print(...) (en if)`**: Informa inmediatamente en consola que el alumno `i+1` está aprobado.
- **`else:`**: Rama ejecutada si la nota del estudiante es menor a 4.0.
- **`reprobados += 1`**: Incrementa en 1 unidad el contador de estudiantes con estado reprobado.
- **`print(...) (en else)`**: Despliega en la pantalla que el estudiante no aprobó el curso.
- **`promedio = suma_notas / 30`**: Calcula la media aritmética del curso dividiendo el acumulado decimal de notas por la constante del total de alumnos (30).
- **`print(...)`**: Muestra el consolidado de aprobados, reprobados y el promedio con formato de dos decimales usando la directiva `{promedio:.2f}`.


#### Código Completo
```python
print("--- Registro de Notas (30 Estudiantes) ---")
aprobados = 0
reprobados = 0
suma_notas = 0.0

# Ciclo determinado para procesar exactamente 30 notas
for i in range(30):
    # Ciclo de validación interactiva interna
    while True:
        try:
            nota = float(input(f"Ingrese la nota del estudiante {i+1} (1.0 a 7.0): "))
            if 1.0 <= nota <= 7.0:
                break  # Nota dentro del rango legal, continúa
            print("Error: La nota debe estar en el rango de 1.0 a 7.0.")
        except ValueError:
            print("Error: Ingrese un número decimal válido.")
    
    # Acumulación de notas en la suma total
    suma_notas += nota
    
    # Evaluación individual inmediata del estudiante
    if nota >= 4.0:
        aprobados += 1
        print(f"Estudiante {i+1} Aprobado con nota {nota:.1f}")
    else:
        reprobados += 1
        print(f"Estudiante {i+1} Reprobado con nota {nota:.1f}")

# Cálculos consolidados del curso e informe estadístico final
promedio = suma_notas / 30
print("\n--- Resumen del Curso ---")
print(f"Cantidad de aprobados: {aprobados}")
print(f"Cantidad de reprobados: {reprobados}")
print(f"Promedio general del curso: {promedio:.2f}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Registro de Notas (30 Estudiantes) ---
Ingrese la nota del estudiante 1 (1.0 a 7.0): 5.5
Estudiante 1 Aprobado con nota 5.5
Ingrese la nota del estudiante 2 (1.0 a 7.0): 3.2
Estudiante 2 Reprobado con nota 3.2
[... Se ingresan las notas de los estudiantes 3 al 29 ...]
Ingrese la nota del estudiante 30 (1.0 a 7.0): 6.8
Estudiante 30 Aprobado con nota 6.8
```
**Salida:**
```text
--- Resumen del Curso ---
Cantidad de aprobados: 21
Cantidad de reprobados: 9
Promedio general del curso: 4.87
```
