### Ejercicio 5: Clasificador de Rangos Etarios en Chile

#### Enunciado del Problema
Desarrolla un script que pida la edad de una persona e indique si corresponde a menor de edad, mayor de edad, adulto mayor o cuarta edad en Chile. Para ello, el estudiante debe investigar previamente los rangos etarios y aplicarlos correctamente en el script.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `edad` | `int` | Almacena la edad en años del usuario. Se utiliza para la clasificación en los rangos biológicos y legales. |

#### Lógica de la Solución
El programa clasifica la edad ingresada dentro de los marcos demográficos y legales vigentes en Chile. Los rangos etarios aplicados son:
* **Menor de edad:** $0$ a $17$ años.
* **Mayor de edad / Adulto:** $18$ a $59$ años.
* **Adulto mayor:** $60$ a $79$ años (definido por el SENAMA).
* **Cuarta edad:** $80$ años o más (sector que requiere políticas públicas de acompañamiento geriátrico específico).

El algoritmo de solución incorpora una validación estricta del rango biológico. No basta con validar que el tipo de dato sea entero (`int`), sino que además debe encontrarse en un intervalo realista ($[0, 120]$ años). Si la edad es negativa o ridículamente alta, el sistema la rechaza. La clasificación definitiva se resuelve en cascada con una estructura condicional múltiple (`if-elif-else`).

#### Explicación Línea por Línea
* **Línea 5 (`print(...)`):** Muestra el banner inicial del programa por consola.
* **Línea 7 (`while True:`):** Declara el bucle interactivo infinito para la captura y control del dato.
* **Línea 8 (`try:`):** Apertura de la zona protegida para la lectura y casteo del valor.
* **Línea 9 (`edad = int(input(...))`):** Captura el valor por teclado y lo convierte a tipo entero (`int`).
* **Línea 10 (`if 0 <= edad <= 120:`):** Evalúa si el número ingresado se encuentra en el rango de edad humana realista y lógicamente viable.
* **Línea 11 (`break`):** Si la condición se cumple, detiene el ciclo de validación.
* **Línea 12 (`else:`):** Se activa si el entero está fuera del rango realista (ej: `-5` o `150`).
* **Línea 13 (`print(...)`):** Explica en pantalla el límite aceptado y solicita reingresar el valor.
* **Línea 14 (`except ValueError:`):** Captura los errores de conversión causados por texto o decimales.
* **Línea 15 (`print(...)`):** Notifica del tipo de dato incorrecto y reinicia la petición en el bucle.
* **Líneas 22-23 (`if edad < 18:`):** Si la edad es menor de 18, concluye que es menor de edad legal en Chile e imprime el resultado.
* **Líneas 24-25 (`elif 18 <= edad < 60:`):** Evaluado en cascada, si es menor a 60 años, clasifica como mayor de edad/adulto.
* **Líneas 26-27 (`elif 60 <= edad < 80:`):** Si se encuentra en el rango de $[60, 79]$, clasifica como adulto mayor.
* **Líneas 28-29 (`else:`):** Ejecutado por descarte acumulativo (edad $\ge 80$), clasifica a la persona en la cuarta edad.

#### Código Completo
```python
# Clasificador de rangos etarios en Chile (incluye Cuarta Edad)

print("--- Clasificación de Edades (Chile) ---")

while True:
    try:
        # Se solicita la edad y se fuerza a tipo entero
        edad = int(input("Ingrese la edad (0 a 120 años): "))
        # Validación del límite biológico humano realista
        if 0 <= edad <= 120:
            break  # Sale del bucle de validación
        else:
            print("Edad fuera del rango realista. Por favor, ingrese un valor entre 0 y 120.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Estructura selectiva anidada basada en la legislación y sociología chilena:
# - Menor de edad: 0 a 17 años
# - Mayor de edad / Adulto: 18 a 59 años
# - Adulto mayor: 60 a 79 años
# - Cuarta edad: 80 años o más
if edad < 18:
    print(f"Con {edad} años, eres menor de edad.")
elif 18 <= edad < 60:
    print(f"Con {edad} años, eres mayor de edad.")
elif 60 <= edad < 80:
    print(f"Con {edad} años, eres adulto mayor.")
else:
    print(f"Con {edad} años, perteneces a la cuarta edad.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Menor de edad):
* **Entrada esperada:** `15`
* **Salida del programa:** `Con 15 años, eres menor de edad.`

##### Caso de Uso 2 (Mayor de edad / Adulto):
* **Entrada esperada:** `34`
* **Salida del programa:** `Con 34 años, eres mayor de edad.`

##### Caso de Uso 3 (Adulto mayor):
* **Entrada esperada:** `71`
* **Salida del programa:** `Con 71 años, eres adulto mayor.`

##### Caso de Uso 4 (Cuarta edad):
* **Entrada esperada:** `85`
* **Salida del programa:** `Con 85 años, perteneces a la cuarta edad.`

##### Caso de Uso 5 (Validación y recuperación):
* **Entrada esperada:** `-3` (luego) `125` (luego) `22`
* **Salida del programa:**
  ```text
  Ingrese la edad (0 a 120 años): -3
  Edad fuera del rango realista. Por favor, ingrese un valor entre 0 y 120.
  Ingrese la edad (0 a 120 años): 125
  Edad fuera del rango realista. Por favor, ingrese un valor entre 0 y 120.
  Ingrese la edad (0 a 120 años): 22
  Con 22 años, eres mayor de edad.
  ```
