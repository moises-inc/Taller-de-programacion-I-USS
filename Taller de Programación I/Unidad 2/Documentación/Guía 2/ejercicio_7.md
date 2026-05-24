### Ejercicio 7: Validador de notas y estado académico

#### Enunciado del Problema
Desarrolla un script que pida una nota final en escala de 1.0 a 7.0 e indique si el estudiante está aprobado o reprobado, considerando que en Chile se aprueba con nota 4.0 o superior.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `nota` | `float` | Guarda la nota final decimal del estudiante que debe ubicarse en el intervalo formal `[1.0, 7.0]`. |


## Lógica de la Solución
El script realiza un control académico formal bajo las normas de calificación chilenas. Se solicita una nota expresada con números decimales. Primero, es crucial asegurar que la calificación sea válida, lo cual se logra limitando el rango lógicamente a `1.0 <= nota <= 7.0` e integrando un control de excepciones. Una vez verificado que el dato se encuentra en este intervalo cerrado, se aplica una sencilla bifurcación lógica: si la nota es inferior a 4.0 el estudiante reprueba, y si es igual o superior aprueba. Se incluye formateo de salida de un decimal mediante la directiva de cadena `:.1f`.

## Explicación Línea por Línea
- **`while True:`**: Define el ciclo interactivo infinito para blindar la entrada del script ante fallos de usuario.
- **`try:`**: Región del código que vigila la sintaxis ante conversiones erróneas de tipo de datos.
- **`nota = float(input(...))`**: Solicita la nota al usuario, la convierte en tipo decimal flotante (`float`) y la asigna a la variable `nota`.
- **`if 1.0 <= nota <= 7.0:`**: Filtro de integridad lógico: comprueba que la nota esté dentro de la escala oficial de 1.0 a 7.0.
- **`break`**: Sale del bucle al cumplirse tanto la validez sintáctica de flotante como el límite del rango oficial.
- **`else:`**: Ejecutado si el número ingresado no pertenece al intervalo de notas chileno.
- **`print("Nota inválida...")`**: Notifica al usuario que la nota se sale del estándar reglamentario.
- **`except ValueError:`**: Captura la excepción de caracteres extraños introducidos que impiden la conversión decimal.
- **`print("Entrada no válida...")`**: Muestra error e invita a ingresar un dato numérico.
- **`if nota < 4.0:`**: Evalúa si la nota obtenida es menor a la nota mínima de aprobación chilena (4.0).
- **`print(f"El estudiante... Reprobado.")`**: Se ejecuta en el bloque del `if`, informando la reprobación del estudiante formateando la nota a un decimal mediante `:.1f`.
- **`else:`**: Se ejecuta por descarte si el estudiante obtuvo un 4.0 o superior en su calificación final.
- **`print(f"El estudiante... Aprobado.")`**: Informa que el alumno ha superado satisfactoriamente el curso con estado Aprobado.


#### Código Completo
```python
while True:
    try:
        # Solicita la nota al usuario con posibilidad de decimales
        nota = float(input("Ingrese la nota del estudiante (1.0 a 7.0): "))
        # Verifica el cumplimiento del rango legal académico en Chile
        if 1.0 <= nota <= 7.0:
            break  # La nota es válida, rompe el bucle de solicitud
        else:
            print("Nota inválida. El rango académico en Chile es exclusivamente de 1.0 a 7.0.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal.")

# Determinación de estado con nota límite 4.0
if nota < 4.0:
    print(f"El estudiante ha obtenido nota {nota:.1f}: Reprobado.")
else:
    print(f"El estudiante ha obtenido nota {nota:.1f}: Aprobado.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese la nota del estudiante (1.0 a 7.0): 3.95
```
**Salida:**
```text
El estudiante ha obtenido nota 4.0: Aprobado.
```
