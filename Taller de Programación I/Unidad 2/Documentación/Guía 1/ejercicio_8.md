### Ejercicio 8: Calculador Dinámico de Edad Actual

#### Enunciado del Problema
Desarrolla un script que pida el nombre de un usuario y su año de nacimiento, y luego muestre un mensaje indicando el nombre de la persona y la edad que tiene actualmente.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `ano_actual` | `int` | Almacena de manera dinámica el año en curso consultado directamente al sistema operativo. |
| `nombre` | `str` | Almacena el nombre ingresado por el usuario, libre de espacios adicionales en los extremos. |
| `ano_nacimiento` | `int` | Almacena el año de nacimiento ingresado por el usuario (validado en un rango lógico). |
| `edad` | `int` | Almacena el resultado del cálculo matemático de la edad (`ano_actual - ano_nacimiento`). |

#### Lógica de la Solución
El algoritmo calcula la edad que una persona cumple durante el año calendario en curso. Con el fin de erradicar la obsolescencia y malas prácticas de desarrollo (como dejar el año actual fijo en el código), se importa la biblioteca nativa de Python `datetime`. Esto permite leer de forma dinámica el año del sistema a través de `datetime.datetime.now().year`.

La lógica del script ejecuta los siguientes pasos secuenciales:
1. **Captura y limpieza del nombre:** Solicita la cadena de texto, removiendo espacios vacíos con el método `.strip()`. Se encapsula en un bucle interactivo que impide que el usuario deje la entrada en blanco o ingrese puros espacios.
2. **Validación interactiva del año de nacimiento:** A través de un bucle `while True` con control de excepciones `ValueError`, se fuerza el casteo a entero (`int`) y se valida que el año se encuentre entre $1900$ y el año en curso.
3. **Cálculo Aritmético:** Aplica la fórmula lineal simple $\text{edad} = \text{año\_actual} - \text{año\_nacimiento}$.
4. **Despliegue pedagógico:** Imprime un mensaje por consola formateado de forma limpia con los resultados.

#### Explicación Línea por Línea
* **Línea 3 (`import datetime`):** Carga en memoria el módulo estándar de manipulación de fechas y tiempos de Python.
* **Línea 6 (`ano_actual = datetime.datetime.now().year`):** Obtiene la fecha y hora local del sistema operativo, extrae la propiedad del año en curso como entero y la asigna a `ano_actual`.
* **Línea 8 (`nombre = input(...).strip()`):** Lee el nombre por consola y elimina los espacios en blanco sobrantes a la izquierda y derecha mediante `.strip()`.
* **Línea 9 (`while not nombre:`):** Evalúa si la cadena resultante quedó vacía. Si es verdadera, entra en un bucle de repetición insistente.
* **Línea 10 (`nombre = input(...).strip()`):** Solicita el nombre nuevamente hasta que el usuario ingrese caracteres no vacíos.
* **Línea 12 (`while True:`):** Declara el ciclo infinito protector para el ingreso del año de nacimiento.
* **Línea 13 (`try:`):** Apertura de la zona segura de captura de errores numéricos.
* **Línea 14 (`ano_nacimiento = int(input(...))`):** Solicita el año de nacimiento e intenta castearlo a entero (`int`).
* **Línea 15 (`if 1900 <= ano_nacimiento <= ano_actual:`):** Evalúa si el año de nacimiento es plausible e históricamente coherente (no menor a 1900 ni en el futuro posterior al año actual).
* **Línea 16 (`break`):** Sale del ciclo de validación del año de nacimiento.
* **Línea 17 (`else:`):** Rama de control en caso de que el entero ingresado no cumpla la restricción cronológica.
* **Línea 18 (`print(...)`):** Muestra el mensaje explicando el rango realista permitido.
* **Línea 19 (`except ValueError:`):** Atrapa las excepciones producidas por el ingreso de datos de tipo float o de tipo string.
* **Línea 20 (`print(...)`):** Informa sobre el formato no válido y reinicia el ciclo.
* **Línea 22 (`edad = ano_actual - ano_nacimiento`):** Ejecuta la resta para calcular la edad teórica del usuario.
* **Línea 23 (`print(...)`):** Despliega el saludo personalizado y el resultado de la edad en consola.

#### Código Completo
```python
# Calculador dinámico de edad actual

import datetime

print("--- Cálculo de Edad Actual ---")
# Obtención dinámica del año del sistema operativo
ano_actual = datetime.datetime.now().year

# Captura de nombre con sanitización y rechazo de cadenas vacías
nombre = input("Ingrese su nombre: ").strip()
while not nombre:
    nombre = input("El nombre no puede estar vacío. Ingrese su nombre: ").strip()

# Captura estructurada y validada del año de nacimiento
while True:
    try:
        ano_nacimiento = int(input(f"Ingrese su año de nacimiento (entre 1900 y {ano_actual}): "))
        # Comprobación de límites cronológicos plausibles
        if 1900 <= ano_nacimiento <= ano_actual:
            break  # Entrada válida, rompe el bucle de validación
        else:
            print(f"El año debe ser válido y realista (1900 a {ano_actual}).")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un año en formato entero.")

# Cálculo aritmético final e impresión de resultados
edad = ano_actual - ano_nacimiento
print(f"\nHola {nombre}, según tu año de nacimiento, tu edad actual es: {edad} años (o los cumples este año).")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Cálculo regular):
* **Entrada esperada:** `Moises` (nombre), `1998` (año de nacimiento)
* **Salida del programa (considerando año del sistema 2026):** `Hola Moises, según tu año de nacimiento, tu edad actual es: 28 años (o los cumples este año).`

##### Caso de Uso 2 (Año en curso):
* **Entrada esperada:** `Sofía` (nombre), `2026` (año de nacimiento)
* **Salida del programa:** `Hola Sofía, según tu año de nacimiento, tu edad actual es: 0 años (o los cumples este año).`

##### Caso de Uso 3 (Recuperación ante errores de entrada):
* **Entrada esperada:** `  ` (nombre vacío) -> `Juan` (nombre), `mil novecientos` (año) -> *Error* -> `1850` (año) -> *Error* -> `2000` (año)
* **Salida del programa:**
  ```text
  Ingrese su nombre:   
  El nombre no puede estar vacío. Ingrese su nombre: Juan
  Ingrese su año de nacimiento (entre 1900 y 2026): mil novecientos
  Entrada no válida. Por favor, ingrese un año en formato entero.
  Ingrese su año de nacimiento (entre 1900 y 2026): 1850
  El año debe ser válido y realista (1900 a 2026).
  Ingrese su año de nacimiento (entre 1900 y 2026): 2000
  
  Hola Juan, según tu año de nacimiento, tu edad actual es: 26 años (o los cumples este año).
  ```
