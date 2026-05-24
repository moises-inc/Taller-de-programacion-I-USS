### Ejercicio 5: Clasificador de rangos etarios en Chile (incluye Cuarta Edad)

#### Enunciado del Problema
Desarrolla un script que pida la edad de una persona e indique si corresponde a menor de edad, mayor de edad, adulto mayor o cuarta edad en Chile. Para ello, el estudiante debe investigar previamente los rangos etarios y aplicarlos correctamente en el script.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `edad` | `int` | Almacena los años de vida expresados en formato entero para la clasificación social. |


## Lógica de la Solución
El programa clasifica la edad de una persona de acuerdo con la legislación y los estándares de geriatría chilenos. Los límites vigentes son: - **Menor de edad:** Menores de 18 años (0 a 17 años).- **Mayor de edad (Adulto):** Desde los 18 hasta los 59 años.- **Adulto Mayor:** Desde los 60 hasta los 79 años.- **Cuarta Edad:** Desde los 80 años en adelante.Para robustez, el script implementa validación sintáctica (con `try-except` para enteros) y una validación lógica con un rango realista de `0 <= edad <= 120`. La clasificación se realiza utilizando condicionales excluyentes en cascada.

## Explicación Línea por Línea
- **`while True:`**: Establece el ciclo para asegurar la correcta entrada de datos.
- **`try:`**: Bloque de control de errores para verificar conversiones de texto a entero.
- **`edad = int(input(...))`**: Solicita la edad al usuario y la almacena convirtiéndola forzadamente a tipo entero (`int`).
- **`if 0 <= edad <= 120:`**: Aplica una validación lógica de rango que descarta números negativos o edades biológicamente imposibles.
- **`break`**: Sale del bucle de validación al comprobar que la edad es numérica y se encuentra en un rango coherente.
- **`else:`**: Se ejecuta si el número está fuera del rango de 0 a 120.
- **`print("Edad fuera del rango...")`**: Advierte al usuario sobre el valor irreal ingresado.
- **`except ValueError:`**: Captura excepciones si la edad ingresada no es un número entero válido.
- **`print("Entrada no válida...")`**: Notifica que el sistema solo admite enteros.
- **`if edad < 18:`**: Compara si la edad es menor a 18 años. De cumplirse, es menor de edad y se salta las demás condiciones.
- **`print(f"Con {edad} años, eres menor de edad...")`**: Imprime la categoría asignada.
- **`elif edad < 60:`**: Evaluación en cascada. Si no es menor a 18, verifica si es menor a 60 (es decir, entre 18 y 59 años).
- **`print(f"Con {edad} años, eres mayor de edad...")`**: Imprime la categoría de adulto.
- **`elif edad < 80:`**: Evaluación de tercer nivel. Verifica si la edad es menor a 80 años (es decir, entre 60 y 79 años).
- **`print(f"Con {edad} años, eres adulto mayor.")`**: Informa que pertenece al segmento de la tercera edad.
- **`else:`**: Bloque final ejecutado por descarte, aplicable a cualquier valor igual o superior a 80 años.
- **`print(f"Con {edad} años, perteneces a la cuarta edad...")`**: Muestra que pertenece a la cuarta edad.


#### Código Completo
```python
while True:
    try:
        # Captura la edad asegurando que sea un número entero
        edad = int(input("Ingrese la edad (0 a 120 años): "))
        # Valida que la edad esté en un rango biológico coherente
        if 0 <= edad <= 120:
            break  # Entrada correcta, continúa el flujo del programa
        else:
            print("Edad fuera del rango realista. Ingrese un valor entre 0 y 120.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Estructura condicional estructurada en cascada excluyente
if edad < 18:
    print(f"Con {edad} años, eres menor de edad en Chile.")
elif edad < 60:
    print(f"Con {edad} años, eres mayor de edad (Adulto).")
elif edad < 80:
    print(f"Con {edad} años, eres adulto mayor.")
else:
    print(f"Con {edad} años, perteneces a la cuarta edad en Chile.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese la edad (0 a 120 años): 135
Edad fuera del rango realista. Ingrese un valor entre 0 y 120.
Ingrese la edad (0 a 120 años): 84
```
**Salida:**
```text
Con 84 años, perteneces a la cuarta edad en Chile.
```
