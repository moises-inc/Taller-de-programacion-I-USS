### Ejercicio 15: Validador y Clasificador de Triángulos por sus Lados

#### Enunciado del Problema
Desarrolla un script que pida las longitudes de los tres lados de un triángulo e indique si el triángulo es equilátero, isósceles o escaleno.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `a` | `float` | Almacena la longitud del primer lado (lado A) del triángulo. |
| `b` | `float` | Almacena la longitud del segundo lado (lado B) del triángulo. |
| `c` | `float` | Almacena la longitud del tercer lado (lado C) del triángulo. |
| `es_valido` | `bool` | Variable booleana que resulta de evaluar la Desigualdad Triangular. |
| `tipo` | `str` | Almacena la cadena descriptiva de clasificación geométrica del triángulo. |
| Parámetro: `nombre_lado` | `str` | Argumento que indica a la función qué lado se solicita en pantalla ("A", "B", "C"). |

#### Lógica de la Solución
El algoritmo soluciona de forma matemáticamente rigurosa el problema. No es correcto clasificar geométricamente un triángulo sin antes asegurar su factibilidad física tridimensional.
El script se estructura en tres fases clave:
1. **Captura Modular de Entradas:** Define una función local `solicitar_lado(nombre_lado)` que restringe las longitudes a números reales estrictamente mayores a cero ($>0$).
2. **Validación del Teorema de Desigualdad Triangular:** Verifica si los lados satisfacen la propiedad geométrica fundamental de que la suma de dos de sus lados siempre sea estrictamente mayor que el tercer lado:
   * $a + b > c$
   * $a + c > b$
   * $b + c > a$
   Si alguna de estas desigualdades es falsa, el programa aborta la ejecución con un mensaje informando que el triángulo es físicamente imposible.
3. **Clasificación Geométrica de Lados:**
   * **Equilátero:** Los tres lados son de idéntica longitud (`a == b == c`).
   * **Isósceles:** Posee exactamente dos lados congruentes (`a == b or b == c or a == c`).
   * **Escaleno:** Los tres lados poseen longitudes distintas (por descarte).

#### Explicación Línea por Línea
* **Línea 5 (`def solicitar_lado(nombre_lado):`):** Declara una función para la captura individualizada de cada lado bajo el principio DRY.
* **Línea 6 (`while True:`):** Bucle infinito de control de entrada de la función modular.
* **Línea 7 (`try:`):** Bloque protegido de conversión.
* **Línea 8 (`valor = float(input(...))`):** Captura el valor decimal del lado.
* **Línea 9 (`if valor > 0:`):** Comprueba que la magnitud de la longitud sea positiva.
* **Línea 10 (`return valor`):** Rompe la iteración de la función devolviendo la longitud correcta.
* **Línea 11 (`else:`):** Se activa para longitudes $\le 0$.
* **Línea 12 (`print(...)`):** Muestra mensaje explicativo de longitud inviable.
* **Línea 13 (`except ValueError:`):** Intercepta errores de tipo de dato.
* **Línea 14 (`print(...)`):** Informa sobre el formato inválido.
* **Líneas 16-18 (`a`, `b`, `c`):** Asigna las variables de los lados solicitando la entrada a la función modular.
* **Línea 21 (`es_valido = (a + b > c) and (a + c > b) and (b + c > a)`):** Evalúa la conjunción lógica booleana del Teorema de Desigualdad Triangular.
* **Línea 23 (`if not es_valido:`):** Condicional que detecta si el triángulo es imposible de construir en el espacio euclidiano.
* **Línea 24 (`print(...)`):** Despliega el error matemático con los lados ingresados.
* **Línea 25 (`else:`):** Rama ejecutada si el triángulo sí es factible físicamente.
* **Línea 27 (`if a == b == c:`):** Evalúa si los tres lados son equivalentes en longitud.
* **Línea 28 (`tipo = ...`):** Asigna la etiqueta "Equilátero".
* **Línea 29 (`elif a == b or b == c or a == c:`):** En cascada, evalúa si al menos dos de los tres lados son congruentes.
* **Línea 30 (`tipo = ...`):** Asigna la etiqueta "Isósceles".
* **Línea 31 (`else:`):** Si no cumple ninguna de las dos condiciones previas (todos los lados distintos).
* **Línea 32 (`tipo = ...`):** Asigna la etiqueta "Escaleno".
* **Línea 34 (`print(...)`):** Muestra el veredicto en pantalla.

#### Código Completo
```python
# Validador y Clasificador de Triángulos

print("--- Clasificador de Triángulos por sus Lados ---")

# Función modular para la captura sanitizada de longitudes
def solicitar_lado(nombre_lado):
    while True:
        try:
            valor = float(input(f"Ingrese longitud del lado {nombre_lado}: "))
            if valor > 0:
                return valor
            else:
                print("La longitud de un lado debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Captura de los tres lados
a = solicitar_lado("A")
b = solicitar_lado("B")
c = solicitar_lado("C")

# Validación geométrica de la existencia del triángulo (Desigualdad Triangular)
es_valido = (a + b > c) and (a + c > b) and (b + c > a)

if not es_valido:
    print(f"\nError: Con las longitudes {a}, {b} y {c} NO se puede formar un triángulo físico.")
else:
    # Clasificación geométrica según congruencia de lados
    if a == b == c:
        tipo = "Equilátero (3 lados iguales)"
    elif a == b or b == c or a == c:
        tipo = "Isósceles (2 lados iguales y 1 distinto)"
    else:
        tipo = "Escaleno (todos sus lados diferentes)"
        
    print(f"\nResultado: El triángulo es {tipo}.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Equilátero):
* **Entrada esperada:** `5` (lado A), `5` (lado B), `5` (lado C)
* **Salida del programa:** `Resultado: El triángulo es Equilátero (3 lados iguales).`

##### Caso de Uso 2 (Isósceles):
* **Entrada esperada:** `6` (lado A), `6` (lado B), `4` (lado C)
* **Salida del programa:** `Resultado: El triángulo es Isósceles (2 lados iguales y 1 distinto).`

##### Caso de Uso 3 (Escaleno):
* **Entrada esperada:** `3` (lado A), `4` (lado B), `5` (lado C)
* **Salida del programa:** `Resultado: El triángulo es Escaleno (todos sus lados diferentes).`

##### Caso de Uso 4 (Imposibilidad Geométrica):
* **Entrada esperada:** `1` (lado A), `2` (lado B), `10` (lado C)
* **Salida del programa:** `Error: Con las longitudes 1.0, 2.0 y 10.0 NO se puede formar un triángulo físico.`

##### Caso de Uso 5 (Captura no válida y resolución):
* **Entrada esperada:** `-2` (lado A) -> *Error* -> `4`, `tres` (lado B) -> *Error* -> `3`, `5` (lado C)
* **Salida del programa:**
  ```text
  Ingrese longitud del lado A: -2
  La longitud de un lado debe ser mayor que cero.
  Ingrese longitud del lado A: 4
  Ingrese longitud del lado B: tres
  Entrada no válida. Por favor, ingrese un número decimal o entero.
  Ingrese longitud del lado B: 3
  Ingrese longitud del lado C: 5
  
  Resultado: El triángulo es Escaleno (todos sus lados diferentes).
  ```
