### Ejercicio 3: Contar números mayores a un valor de corte

#### Enunciado del Problema
Dada una lista que contiene una serie de datos numéricos, diseñar un algoritmo que determine cuántos de estos elementos superan un umbral predefinido. Para ello, se debe implementar una función que reciba como parámetros la lista de números y el valor de corte, y retorne la cantidad de elementos estrictamente mayores. En el programa principal, se debe inicializar una lista muestra, definir un límite y presentar el resultado del conteo.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista` | `list` | Parámetro de la función | Colección estructurada de elementos numéricos que se desea analizar. |
| `valor` | `float` / `int` | Parámetro de la función | Umbral numérico (límite) que define la frontera de comparación. |
| `contador` | `int` | Variable local (de la función) | Funciona como acumulador entero para contar los valores válidos. |
| `num` | `float` / `int` | Variable local (de la función) | Variable de control de iteración en el ciclo `for` que representa el elemento analizado actual. |
| `muestra` | `list` | Variable local (programa principal) | Lista estática declarada para simular el conjunto de entrada en la consola. |
| `limite` | `float` | Variable local (programa principal) | Valor constante que determina el corte o filtro de los datos. |
| `cantidad` | `int` | Variable local (programa principal) | Almacena el resultado que retorna la función `contar_mayores`. |

---

#### Lógica de la Solución
El ejercicio aborda el patrón de diseño clásico de **filtrado e incremento secuencial** en colecciones lineales:
1. **Encapsulamiento del Algoritmo:** La lógica del conteo se aísla por completo en la función `contar_mayores(lista, valor)`. Esta función no interactúa con la terminal, haciéndola versátil y reutilizable.
2. **Patrón Acumulador:** Se inicializa un registro o variable contadora a cero (`contador = 0`). Esta almacena el estado parcial del cálculo.
3. **Complejidad Temporal Lineal $O(N)$:** Mediante el bucle iterativo `for`, el procesador lee uno a uno los elementos de la secuencia de manera ordenada y secuencial, garantizando que el consumo de recursos sea proporcional a la cantidad de elementos en la lista.
4. **Validación Condicional:** En cada paso del bucle se compara si el valor iterado es mayor de forma estricta que el parámetro de corte (`if num > valor:`). Si es verdadera, se aplica un incremento unario al acumulador (`contador += 1`).
5. **Retorno de Estado:** Al finalizar la lectura de la lista, la función retorna el entero acumulado.

---

#### Explicación Línea por Línea

1. **`def contar_mayores(lista, valor):`**  
   Establece la firma de la función `contar_mayores`, que requiere dos parámetros: la estructura secuencial a recorrer (`lista`) y la constante de corte (`valor`).
2. **`"""Cuenta cuántos elementos de la lista superan el valor de corte dado."""`**  
   Bloque descriptivo (*docstring*) incorporado para detallar el funcionamiento conceptual del filtrado.
3. **`contador = 0`**  
   Establece a cero la variable local `contador` que registrará las coincidencias lógicas del programa.
4. **`for num in lista:`**  
   Inicia la estructura repetitiva `for` que examinará de manera exhaustiva todos los elementos que componen la lista, asignando temporalmente cada valor a la variable `num` en cada iteración.
5. **`if num > valor:`**  
   Instrucción condicional evaluadora que comprueba si la variable de control `num` es numéricamente superior a la cota dada por `valor`.
6. **`contador += 1`**  
   Aplica un incremento unario directo en la variable `contador` únicamente si el elemento analizado pasa con éxito la evaluación lógica previa.
7. **`return contador`**  
   Usa la palabra reservada `return` para entregar al final el conteo resultante acumulado y terminar de ejecutar la función.
8. **`# Programa principal`**  
   Indica mediante un comentario el inicio de las pruebas de ejecución interactiva.
9. **`print("--- Ejercicio 3: Contar Mayores ---")`**  
   Imprime un encabezado estético para separar la salida en la terminal.
10. **`muestra = [10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]`**  
    Declara e inicializa la variable `muestra` como una lista conteniendo diez números reales y enteros desordenados.
11. **`limite = 35.0`**  
    Establece la constante flotante `35.0` en la variable `limite` para definir la frontera de filtración.
12. **`cantidad = contar_mayores(muestra, limite)`**  
    Invoca a la función modular pasándole los argumentos definidos. El resultado de retorno se guarda en la variable `cantidad`.
13. **`print(f"Muestra analizada: {muestra}")`**  
    Muestra en pantalla el listado de datos originales mediante una cadena literal formateada.
14. **`print(f"Valor límite de comparación: {limite}")`**  
    Imprime en la terminal el límite configurado para que el usuario conozca la cota de filtro.
15. **`print(f"Cantidad de elementos mayores a {limite}: {cantidad}")`**  
    Presenta de forma legible el total de valores que superan la cota especificada.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de recuento y filtrado
def contar_mayores(lista, valor):
    """
    Recorre secuencialmente una lista y calcula cuántos elementos 
    superan el valor de corte especificado.
    """
    # Inicialización del acumulador en cero
    contador = 0
    
    # Recorrido lineal (complejidad temporal O(N))
    for num in lista:
        # Validación de la condición lógica restrictiva
        if num > valor:
            contador += 1  # Incremento unario del acumulador
            
    # Retorno del valor entero acumulado final
    return contador

# --- Flujo del Programa Principal ---
print("--- Ejercicio 3: Contar Mayores ---")

# Inicialización de la muestra estadística y la cota
muestra = [10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]
limite = 35.0

# Invocación de la lógica modular
cantidad = contar_mayores(muestra, limite)

# Impresión interactiva y descriptiva del análisis
print(f"Muestra analizada: {muestra}")
print(f"Valor límite de comparación: {limite}")
print(f"Cantidad de elementos mayores a {limite}: {cantidad}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ejecución con Límite Estándar
*   **Muestra Analizada:** `[10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]`
*   **Límite de Corte:** `35.0`
*   **Salida del Programa:**
    ```text
    Muestra analizada: [10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]
    Valor límite de comparación: 35.0
    Cantidad de elementos mayores a 35.0: 5
    ```
    *(Nota: Los elementos que superan 35.0 son 45.0, 78.2, 99.1, 50.0 y 88.8).*

##### Caso de Uso 2: Límite Alto (Sin elementos que coincidan)
*   **Modificación en el Programa:** `limite = 100.0`
*   **Salida del Programa:**
    ```text
    Muestra analizada: [10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]
    Valor límite de comparación: 100.0
    Cantidad de elementos mayores a 100.0: 0
    ```

##### Caso de Uso 3: Límite Bajo (Todos los elementos coinciden)
*   **Modificación en el Programa:** `limite = 0.0`
*   **Salida del Programa:**
    ```text
    Muestra analizada: [10.5, 45.0, 78.2, 5.4, 99.1, 12.0, 33.3, 50.0, 88.8, 2.1]
    Valor límite de comparación: 0.0
    Cantidad de elementos mayores a 0.0: 10
    ```
