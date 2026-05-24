### Ejercicio 5: Búsqueda secuencial de productos en inventario

#### Enunciado del Problema
Escribir un programa modular que verifique la existencia de un producto determinado dentro de una lista que representa el inventario de una bodega.
El programa debe:
1.  Implementar una función que reciba la lista de inventario y el nombre del producto, y devuelva un valor booleano (`True` si el artículo existe, o `False` si no se encuentra).
2.  Garantizar que la búsqueda sea insensible a las diferencias entre mayúsculas y minúsculas (búsqueda *case-insensitive*).
3.  Solicitar el término de búsqueda al usuario, validando que no sea una cadena de texto vacía o compuesta únicamente de espacios en blanco.
4.  Mostrar un mensaje informativo definitivo según el resultado de la consulta.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista_inventario` | `list` | Parámetro de la función | Almacena la colección de productos registrados de tipo cadena (`str`) sobre la que se busca. |
| `producto` | `str` | Parámetro de la función | Representa la palabra clave o artículo que se desea localizar en el inventario. |
| `item` | `str` | Variable local (de la función) | Almacena temporalmente el elemento del inventario analizado durante el ciclo. |
| `inventario` | `list` | Variable local (programa principal) | Lista declarada estáticamente con los productos disponibles en bodega. |
| `busqueda` | `str` | Variable local (programa principal) | Almacena el texto de búsqueda digitado por el usuario, sin espacios superfluos. |
| `existe` | `bool` | Variable local (programa principal) | Variable lógica que almacena el retorno final de la función (`True` o `False`). |

---

#### Lógica de la Solución
Este ejercicio aplica una de las técnicas fundamentales del diseño de algoritmos de búsqueda:
1. **Insensibilidad a Mayúsculas y Minúsculas (Case Insensitivity):** Para robustecer la experiencia del usuario, la comparación de textos se normaliza convirtiendo ambos extremos (el producto en el inventario `item` y la búsqueda `producto`) a minúsculas con el método incorporado `.lower()`. Esto previene fallas si el usuario ingresa textos con formatos variados como "ARROZ", "Arroz" o "arroz".
2. **Algoritmo de Búsqueda Lineal y Retorno Temprano (Early Return):** Se recorre el inventario elemento a elemento mediante un bucle `for`. Si se halla una coincidencia, se interrumpe inmediatamente el bucle retornando `True`. Si el ciclo termina y recorrió todos los elementos sin disparar la coincidencia, se concluye con un retorno de `False`. Esto garantiza una complejidad óptima para listas desordenadas: $O(N)$ en el peor de los casos y $O(1)$ en el mejor.
3. **Validación de la Entrada (Sanitización):** Mediante el método `.strip()`, se eliminan espacios vacíos accidentales al inicio y al final de la entrada. Un ciclo `while not busqueda` asegura que la consulta no proceda si está en blanco.

---

#### Explicación Línea por Línea

1. **`def buscar_producto(lista_inventario, producto):`**  
   Define la firma de la función `buscar_producto`, la cual requiere la lista de elementos en inventario y la cadena de texto de búsqueda.
2. **`"""Verifica si un ítem específico existe en el inventario."""`**  
   Docstring interno descriptivo de la labor de localización y comparación secuencial.
3. **`for item in lista_inventario:`**  
   Bucle `for` diseñado para iterar secuencialmente a través de cada cadena de la lista de inventario.
4. **`if item.lower() == producto.lower():`**  
   Evalúa si el producto de la bodega coincide con la palabra clave buscada. Convierte ambas cadenas a minúsculas con el método `.lower()` para realizar una comparación justa y libre de diferencias de escritura.
5. **`return True`**  
   Si se encuentra una coincidencia, retorna inmediatamente el booleano `True`, finalizando de inmediato la función y deteniendo el bucle.
6. **`return False`**  
   Esta instrucción se ejecuta únicamente si el bucle `for` completó todo su recorrido lineal sin encontrar coincidencias. Informa que el elemento buscado no existe en la bodega.
7. **`# Programa principal`**  
   Comentario pedagógico que indica el inicio del código interactivo en la terminal.
8. **`print("--- Ejercicio 5: Inventario ---")`**  
   Muestra un título estético y organizador por pantalla.
9. **`inventario = ["arroz", "aceite", "tallarines", "azucar", "leche", "cafe"]`**  
   Inicializa la lista de bodega con un catálogo inicial de productos disponibles.
10. **`busqueda = input("Ingrese el producto a buscar en bodega: ").strip()`**  
    Solicita el producto al usuario en consola y aplica el método `.strip()` para limpiar la entrada de espacios en blanco accidentales al inicio o al final.
11. **`while not busqueda:`**  
    Bucle interactivo de validación de campo vacío. En Python, una cadena de texto vacía (`""`) se evalúa como falsa. El operador `not` la invierte a verdadera, activando el ciclo de advertencia.
12. **`busqueda = input("Error: La búsqueda no puede estar vacía. Reintente: ").strip()`**  
    Informa del error y solicita nuevamente una entrada no vacía, sanitizándola de inmediato.
13. **`existe = buscar_producto(inventario, busqueda)`**  
    Invoca la función modular enviando el inventario actual y el término de búsqueda con formato corregido. Su respuesta booleana se guarda en `existe`.
14. **`if existe:`**  
    Evalúa la variable lógica resultante.
15. **`print(f"El producto '{busqueda}' SÍ existe en bodega.")`**  
    Presenta un mensaje de éxito indicando que el producto consultado se encuentra registrado en el stock.
16. **`else:`**  
    Rama alternativa en caso de que la búsqueda sea infructuosa.
17. **`print(f"El producto '{busqueda}' NO está registrado en bodega.")`**  
    Reporta de manera clara que el elemento consultado no forma parte del inventario actual.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de búsqueda secuencial
def buscar_producto(lista_inventario, producto):
    """
    Recorre linealmente una lista y compara su contenido con una cadena de búsqueda.
    Normaliza los textos convirtiéndolos a minúsculas (búsqueda case-insensitive).
    """
    for item in lista_inventario:
        # Normalización y comparación lógica de strings
        if item.lower() == producto.lower():
            return True  # Retorno temprano apenas se encuentra coincidencia
            
    # Si el bucle finaliza y no encontró nada, retorna False
    return False

# --- Flujo del Programa Principal ---
print("--- Ejercicio 5: Inventario ---")

# Catálogo estático inicial en bodega
inventario = ["arroz", "aceite", "tallarines", "azucar", "leche", "cafe"]

# Captura de datos con remoción preventiva de espacios externos (.strip)
busqueda = input("Ingrese el producto a buscar en bodega: ").strip()

# Bucle interactivo defensivo para evitar cadenas vacías
while not busqueda:
    busqueda = input("Error: La búsqueda no puede estar vacía. Reintente: ").strip()

# Invocación de la lógica de búsqueda
existe = buscar_producto(inventario, busqueda)

# Presentación estructurada de resultados según el estado booleano
if existe:
    print(f"El producto '{busqueda}' SÍ existe en bodega.")
else:
    print(f"El producto '{busqueda}' NO está registrado en bodega.")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Coincidencia Perfecta (Minúsculas)
*   **Entrada en Consola:**
    ```text
    Ingrese el producto a buscar en bodega: arroz
    ```
*   **Salida del Programa:**
    ```text
    El producto 'arroz' SÍ existe en bodega.
    ```

##### Caso de Uso 2: Coincidencia con Formato Mixto y Espacios (Case Insensitive)
*   **Entrada en Consola:**
    ```text
    Ingrese el producto a buscar en bodega:   LeCHe   
    ```
*   **Salida del Programa:**
    ```text
    El producto 'LeCHe' SÍ existe en bodega.
    ```
    *(Nota: El programa limpia los espacios extremos y coincide 'leche' con 'leche').*

##### Caso de Uso 3: Búsqueda de Producto Inexistente
*   **Entrada en Consola:**
    ```text
    Ingrese el producto a buscar en bodega: fideos
    ```
*   **Salida del Programa:**
    ```text
    El producto 'fideos' NO está registrado en bodega.
    ```

##### Caso de Uso 4: Evitar Búsquedas Vacías
*   **Entrada en Consola:**
    ```text
    Ingrese el producto a buscar en bodega:         
    Error: La búsqueda no puede estar vacía. Reintente: cafe
    ```
*   **Salida del Programa:**
    ```text
    El producto 'cafe' SÍ existe en bodega.
    ```
