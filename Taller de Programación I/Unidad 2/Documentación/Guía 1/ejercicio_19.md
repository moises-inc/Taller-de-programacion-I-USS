### Ejercicio 19: Mezclador de Colores Primarios

#### Enunciado del Problema
Desarrolla un script que pida dos colores primarios entre los siguientes: rojo, amarillo, azul.
El programa debe considerar estas reglas:
* Si ambos colores son iguales, mostrar: “No hay mezcla, es el mismo color”
* Si mezcla rojo + amarillo, mostrar: “naranja”
* Si mezcla rojo + azul, mostrar: “morado”
* Si mezcla amarillo + azul, mostrar: “verde”
* Para cualquier otro caso, mostrar: “Combinación no reconocida”

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `primarios_validos` | `list` | Colección que contiene los colores primarios admitidos (`["rojo", "amarillo", "azul"]`). |
| `c1` | `str` | Almacena el primer color primario sanitizado (libre de espacios y en minúsculas). |
| `c2` | `str` | Almacena el segundo color primario sanitizado (libre de espacios y en minúsculas). |
| `mezcla` | `set` | Estructura de tipo conjunto que agrupa ambos colores para **anular la relevancia de su orden de ingreso**. |
| `resultado` | `str` | Almacena la denominación del color secundario resultante de la mezcla. |
| Parámetro: `posicion` | `str` | Indica a la función modular si se está solicitando el "primer" o "segundo" color. |

#### Lógica de la Solución
El algoritmo soluciona de forma elegante y didáctica el mezclador cromático. Las combinaciones lógicas de textos libres son propensas a redundancia. Por ejemplo, en lógica básica se tendría que evaluar si el usuario ingresó `(rojo y azul)` O bien `(azul y rojo)` para concluir `"morado"`. Esta duplicación satura el código de condicionales.

Para optimizar y resolver esto con elegancia:
1. **Modularidad con DRY:** Se define la función `solicitar_color(posicion)` para capturar y validar el color, aplicando sanitización (`.strip().lower()`).
2. **Uso de Estructura de Conjunto (`set`):** Un conjunto es una colección desordenada de elementos únicos. Al declarar `mezcla = {c1, c2}`, el orden de los elementos queda anulado. De este modo, `{ "rojo", "azul" }` es matemáticamente idéntico a `{ "azul", "rojo" }`.
3. **Comparaciones Directas:** Se evalúa la igualdad del conjunto contra los conjuntos resultantes para obtener las mezclas:
   * `{"rojo", "amarillo"} \implies$ naranja`
   * `{"rojo", "azul"} \implies$ morado`
   * `{"amarillo", "azul"} \implies$ verde`

#### Explicación Línea por Línea
* **Línea 5 (`primarios_validos = [...]`):** Lista con los strings admisibles.
* **Línea 7 (`def solicitar_color(posicion):`):** Declara la función modular de captura de color.
* **Línea 8 (`while True:`):** Bucle infinito para insistir en la validez del color.
* **Línea 9 (`color = input(...).strip().lower()`):** Captura el texto, remueve espacios y convierte a minúsculas.
* **Línea 10 (`if color in primarios_validos:`):** Evalúa si la entrada forma parte de la lista autorizada.
* **Línea 11 (`return color`):** Retorna el string sanitizado y rompe la iteración modular.
* **Línea 12 (`else:`):** Rama para colores no autorizados.
* **Línea 13 (`print(...)`):** Notifica que el color ingresado no califica como primario válido.
* **Líneas 15-16 (`c1`, `c2`):** Llama modularmente a la función para capturar ambos colores primarios.
* **Líneas 18 (`print(...)`):** Despliega un mensaje descriptivo de la acción de mezcla.
* **Líneas 20-21 (`if c1 == c2:`):** Evalúa si ambos inputs son idénticos. Si es así, determina que no hay combinación e imprime el mensaje correspondiente.
* **Líneas 22 (`else:`):** Rama ejecutada si los dos colores son diferentes y por ende se generará una nueva mezcla cromática.
* **Línea 24 (`mezcla = {c1, c2}`):** Instancia un conjunto en Python (`set`) que almacena ambos elementos de forma desordenada.
* **Líneas 26-31 (`if-elif-else`):** Compara la igualdad de conjuntos de forma directa y compacta asignando el color secundario respectivo.
* **Línea 33 (`print(...)`):** Imprime en pantalla el resultado de la mezcla en mayúsculas mediante `.upper()`.

#### Código Completo
```python
# Mezclador de Colores Primarios con independencia de orden

print("--- Mezclador de Colores Primarios ---")
primarios_validos = ["rojo", "amarillo", "azul"]

# Función modular para capturar y sanitizar la entrada de colores
def solicitar_color(posicion):
    while True:
        color = input(f"Ingrese el {posicion} color primario (rojo/amarillo/azul): ").strip().lower()
        if color in primarios_validos:
            return color
        else:
            print("Color no reconocido como primario válido. Intente nuevamente.")

# Captura de datos modular
c1 = solicitar_color("primer")
c2 = solicitar_color("segundo")

print(f"\nMezclando: {c1} + {c2}...")

# Evaluación de redundancia cromática
if c1 == c2:
    print("Resultado: No hay mezcla, es el mismo color.")
else:
    # Creamos un conjunto (set) para anular el orden físico del ingreso de los datos
    mezcla = {c1, c2}
    
    # Comparación de conjuntos para definir mezcla cromática
    if mezcla == {"rojo", "amarillo"}:
        resultado = "naranja"
    elif mezcla == {"rojo", "azul"}:
        resultado = "morado"
    elif mezcla == {"amarillo", "azul"}:
        resultado = "verde"
    else:
        resultado = "Combinación no reconocida"
        
    print(f"Resultado de la combinación: {resultado.upper()}")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Mezcla de Rojo y Azul - Orden 1):
* **Entrada esperada:** `rojo` (primer), `azul` (segundo)
* **Salida del programa:**
  ```text
  Mezclando: rojo + azul...
  Resultado de la combinación: MORADO
  ```

##### Caso de Uso 2 (Mezcla de Rojo y Azul - Orden 2):
* **Entrada esperada:** `azul` (primer), `rojo` (segundo)
* **Salida del programa:**
  ```text
  Mezclando: azul + rojo...
  Resultado de la combinación: MORADO
  ```

##### Caso de Uso 3 (Mismo Color):
* **Entrada esperada:** `amarillo` (primer), `amarillo` (segundo)
* **Salida del programa:**
  ```text
  Mezclando: amarillo + amarillo...
  Resultado: No hay mezcla, es el mismo color.
  ```

##### Caso de Uso 4 (Error inicial y reintento):
* **Entrada esperada:** `verde` (primer) -> *Error* -> `rojo`, `amarillo` (segundo)
* **Salida del programa:**
  ```text
  Ingrese el primer color primario (rojo/amarillo/azul): verde
  Color no reconocido como primario válido. Intente nuevamente.
  Ingrese el primer color primario (rojo/amarillo/azul): rojo
  Ingrese el segundo color primario (rojo/amarillo/azul): amarillo
  
  Mezclando: rojo + amarillo...
  Resultado de la combinación: NARANJA
  ```
