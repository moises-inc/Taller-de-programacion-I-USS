### Ejercicio 14: Clasificador censal de 40 personas

#### Enunciado del Problema
Desarrolla un script que solicite la edad de 40 personas. Para cada una, debe clasificarla en: Menor de edad, Mayor de edad, Adulto mayor, Cuarta edad en Chile. Al final, debe mostrar cuántas personas hay en cada categoría.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `menor_cnt` | `int` | Contador incremental de personas menores de edad (0 a 17 años). |
| `mayor_cnt` | `int` | Contador incremental de personas mayores de edad (adultos de 18 a 59 años). |
| `adulto_mayor_cnt` | `int` | Contador de adultos mayores (60 a 79 años). |
| `cuarta_edad_cnt` | `int` | Contador de personas pertenecientes a la cuarta edad (80 o más años). |
| `i` | `int` | Variable de control del ciclo `for` que identifica de forma incremental a la persona actual (0 a 39). |
| `edad` | `int` | Variable temporal que almacena la edad de la persona actual, validada en el rango `[0, 120]`. |


## Lógica de la Solución
El script automatiza el levantamiento de un censo etario rápido procesando de forma determinada la edad de 40 personas mediante un bucle `for i in range(40)`. Para asegurar la calidad estadística de los datos del programa: - Se implementa una validación sintáctica interactiva con `while True` y `try-except` para blindar el flujo de ingresos de texto.- Se restringen lógicamente las edades al intervalo realista `0 <= edad <= 120`.Con cada edad correcta, el script evalúa y clasifica los datos acumulando la estadística en su respectivo contador demográfico chileno (menor de edad, mayor de edad, adulto mayor o cuarta edad). Al finalizar los 40 ciclos, se presenta una tabla estadística de distribución.

## Explicación Línea por Línea
- **`menor_cnt = 0`**: Inicializa en cero el contador de personas menores de 18 años.
- **`mayor_cnt = 0`**: Inicializa en cero el contador de personas adultas de entre 18 y 59 años.
- **`adulto_mayor_cnt = 0`**: Inicializa el acumulador de estadísticas para la tercera edad (60 a 79 años).
- **`cuarta_edad_cnt = 0`**: Inicializa el acumulador de estadísticas para la cuarta edad (80 años o más).
- **`for i in range(40):`**: Inicia el bucle determinista general que repetirá el registro 40 veces consecutivas.
- **`while True:`**: Bucle infinito interactivo para validar la entrada y asegurar la obtención de una edad real.
- **`try:`**: Región del bucle de validación encargada de atrapar errores sintácticos de entrada.
- **`edad = int(input(...))`**: Solicita la edad de la persona `i+1` del censo, convirtiéndola forzadamente a entero y guardándola.
- **`if 0 <= edad <= 120:`**: Comprueba si la edad es lógica y biológicamente posible.
- **`break`**: Sale del bucle de validación al confirmarse un número entero en el rango cerrado de 0 a 120.
- **`print("Error: Ingrese una edad...")`**: Muestra advertencia en pantalla si el entero está fuera del rango lógico.
- **`except ValueError:`**: Atrapa excepciones causadas al ingresar decimales o texto.
- **`print("Error: Ingrese un entero.")`**: Advierte que la edad debe declararse en formato entero sin comas o letras.
- **`if edad < 18:`**: Evalúa si la edad clasifica en el segmento infantil/juvenil.
- **`menor_cnt += 1`**: Suma 1 unidad al contador de menores de edad.
- **`elif edad < 60:`**: Evaluación en cascada para el segmento adulto (edad mayor o igual a 18 y menor a 60 años).
- **`mayor_cnt += 1`**: Suma 1 unidad al contador de mayores de edad.
- **`elif edad < 80:`**: Evaluación para el segmento de la tercera edad (entre 60 y 79 años).
- **`adulto_mayor_cnt += 1`**: Suma 1 unidad al contador de adultos mayores.
- **`else:`**: Bloque ejecutado al descartarse las condiciones anteriores (para edades de 80 años o superiores).
- **`cuarta_edad_cnt += 1`**: Suma 1 unidad al contador de personas en la cuarta edad.
- **`print("\n--- Distribución Demográfica ---")`**: Encabezado del informe demográfico consolidado final al salir de los 40 ciclos.
- **`print(...)`**: Imprime los resultados de las frecuencias por rango etario censados.


#### Código Completo
```python
print("--- Clasificador de Edades (40 Personas) ---")
menor_cnt = 0
mayor_cnt = 0
adulto_mayor_cnt = 0
cuarta_edad_cnt = 0

# Ciclo determinado para recopilar 40 edades
for i in range(40):
    # Validación robusta de entrada de datos
    while True:
        try:
            edad = int(input(f"Ingrese la edad de la persona {i+1} (0 a 120 años): "))
            if 0 <= edad <= 120:
                break  # Edad válida y dentro de rango, sale del bucle interno
            print("Error: Ingrese una edad realista entre 0 y 120 años.")
        except ValueError:
            print("Error: Ingrese un número entero.")

    # Clasificación estructurada en cascada
    if edad < 18:
        menor_cnt += 1
    elif edad < 60:
        mayor_cnt += 1
    elif edad < 80:
        adulto_mayor_cnt += 1
    else:
        cuarta_edad_cnt += 1

# Despliegue de resultados demográficos consolidados
print("\n--- Distribución Demográfica ---")
print(f"Menores de edad (0-17 años): {menor_cnt}")
print(f"Mayores de edad (18-59 años): {mayor_cnt}")
print(f"Adultos mayores (60-79 años): {adulto_mayor_cnt}")
print(f"Personas de la cuarta edad (>=80 años): {cuarta_edad_cnt}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Clasificador de Edades (40 Personas) ---
Ingrese la edad de la persona 1 (0 a 120 años): 12
Ingrese la edad de la persona 2 (0 a 120 años): 45
[... Se ingresan las edades de las personas 3 al 39 ...]
Ingrese la edad de la persona 40 (0 a 120 años): 85
```
**Salida:**
```text
--- Distribución Demográfica ---
Menores de edad (0-17 años): 10
Mayores de edad (18-59 años): 20
Adultos mayores (60-79 años): 7
Personas de la cuarta edad (>=80 años): 3
```
