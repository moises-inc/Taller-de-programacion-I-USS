### Ejercicio 8: Calculador de edad actual

#### Enunciado del Problema
Desarrolla un script que pida el nombre de un usuario y su año de nacimiento, y luego muestre un mensaje indicando el nombre de la persona y la edad que tiene actualmente.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `ano_actual` | `int` | Variable generada automáticamente por el sistema con el año cronológico en curso. |
| `nombre` | `str` | Almacena la identificación textual del usuario sin espacios residuales. |
| `ano_nacimiento` | `int` | Guarda el año de nacimiento del usuario como número entero. |
| `edad` | `int` | Almacena el cálculo aritmético resultante de la resta del año actual y el año de nacimiento. |


## Lógica de la Solución
El script realiza un cálculo de edad dinámico sin depender de una constante estática fija en el código, lo que volvería obsoleto al script al cambiar de año de calendario. Para lograr esto, se importa la librería del sistema `datetime` y se extrae el año en curso mediante `datetime.datetime.now().year`. El algoritmo posee dos validaciones clave: 1. **Validación del nombre:** Utiliza un ciclo `while not nombre` y la función `.strip()` para limpiar espacios vacíos e impedir que el campo de nombre sea enviado en blanco.2. **Validación del año:** Se solicita el año de nacimiento forzando tipo entero en el rango cerrado de `1900 <= ano_nacimiento <= ano_actual` dentro de un bloque de captura de errores `try-except`.

## Explicación Línea por Línea
- **`import datetime`**: Importa el módulo estándar de Python que permite interactuar con marcas temporales y fechas del sistema.
- **`ano_actual = datetime.datetime.now().year`**: Invoca la función que extrae el año en curso del reloj del computador y lo almacena como entero.
- **`nombre = input("Ingrese su nombre: ").strip()`**: Captura el nombre del usuario y remueve espacios en blanco accidentales en los extremos usando `.strip()`.
- **`while not nombre:`**: Inicia un ciclo iterativo que continuará preguntando mientras la variable `nombre` evalúe como vacía (falsedad lógica de cadena vacía).
- **`nombre = input(...).strip()`**: Solicita nuevamente el nombre dentro del bucle si el usuario solo presionó la tecla Enter o ingresó puros espacios.
- **`while True:`**: Establece el ciclo para asegurar la correcta validación del año de nacimiento.
- **`try:`**: Abre el bloque de prueba para capturar ingresos de caracteres que no correspondan a un entero.
- **`ano_nacimiento = int(input(...))`**: Solicita el año de nacimiento, intenta transformarlo a un entero (`int`) y lo asigna a `ano_nacimiento`.
- **`if 1900 <= ano_nacimiento <= ano_actual:`**: Comprueba si el año de nacimiento se ubica entre 1900 y el año actual del sistema operativo.
- **`break`**: Sale del ciclo de validación interactiva al comprobarse que el año ingresado está en el rango correcto.
- **`else:`**: Se ejecuta si el entero ingresado se encuentra fuera del rango realista especificado.
- **`print(f"El año debe ser válido...")`**: Advierte sobre el rango admisible de fechas.
- **`except ValueError:`**: Captura los errores de conversión causados al ingresar datos que no son enteros.
- **`print("Entrada no válida...")`**: Informa que se requiere digitar un año en formato de número entero.
- **`edad = ano_actual - ano_nacimiento`**: Calcula aritméticamente los años del usuario restando el año de nacimiento al año actual.
- **`print(f"Hola {nombre}...")`**: Despliega en pantalla el saludo final consolidando el nombre del usuario y su edad de forma interactiva.


#### Código Completo
```python
import datetime

# Obtención dinámica del año en curso a través del reloj del sistema
ano_actual = datetime.datetime.now().year

# Captura y depuración del nombre para evitar registros vacíos
nombre = input("Ingrese su nombre: ").strip()
while not nombre:
    nombre = input("El nombre no puede estar vacío. Ingrese su nombre: ").strip()

# Validación robusta del año de nacimiento
while True:
    try:
        ano_nacimiento = int(input(f"Ingrese su año de nacimiento (entre 1900 y {ano_actual}): "))
        if 1900 <= ano_nacimiento <= ano_actual:
            break  # Año correcto y lógico, sale de la validación
        else:
            print(f"El año debe ser válido y de este siglo o el anterior (1900 a {ano_actual}).")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un año en formato entero.")

# Operación aritmética de resta
edad = ano_actual - ano_nacimiento
print(f"Hola {nombre}, según tu año de nacimiento, tu edad actual es: {edad} años.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese su nombre:    
El nombre no puede estar vacío. Ingrese su nombre: Martín
Ingrese su año de nacimiento (entre 1900 y 2026): 2030
El año debe ser válido y de este siglo o el anterior (1900 a 2026).
Ingrese su año de nacimiento (entre 1900 y 2026): 2004
```
**Salida:**
```text
Hola Martín, según tu año de nacimiento, tu edad actual es: 22 años.
```
