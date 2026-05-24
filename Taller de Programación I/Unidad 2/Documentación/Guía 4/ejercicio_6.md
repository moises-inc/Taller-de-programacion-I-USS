### Ejercicio 6: Filtrado manual de valores mayores a 50

#### Enunciado del Problema
Implementar un programa estructurado y modular que reciba una lista de datos numéricos y genere una nueva lista que contenga únicamente aquellos valores que sean estrictamente superiores a cincuenta ($50$). El programa principal debe inicializar una lista con valores desordenados de muestra, llamar a la función de filtrado y mostrar tanto el listado original como la nueva colección resultante para evidenciar los cambios.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista_original` | `list` | Parámetro de la función | Colección numérica original que sirve como insumo de lectura para la función. |
| `lista_filtrada` | `list` | Variable local (de la función) | Contenedor dinámico inicialmente vacío destinado a acumular los elementos seleccionados. |
| `val` | `float` / `int` | Variable local (de la función) | Variable de control utilizada para examinar de manera secuencial cada número de la lista. |
| `datos` | `list` | Variable local (programa principal) | Lista declarada estáticamente con los diez números de muestra para simular el caso práctico. |
| `filtrados` | `list` | Variable local (programa principal) | Almacena la nueva lista filtrada retornada por la función `filtrar_mayores_50`. |

---

#### Lógica de la Solución
Este ejercicio aplica uno de los patrones fundamentales del paradigma de programación estructurada: el **filtrado por acumulación en estructura externa con preservación de la inmutabilidad**:
1. **Preservación de la Estructura Original:** En lugar de alterar la lista original eliminando elementos directos (lo cual deforma los índices en plena iteración y es catalogado como una mala práctica de programación por provocar comportamientos erráticos), el algoritmo opta por dejar intacto el conjunto de datos de origen `lista_original` y trabajar sobre una estructura nueva llamada `lista_filtrada`.
2. **Complejidad Temporal Lineal $O(N)$:** Se implementa un ciclo secuencial de inspección mediante un bucle `for` de una única pasada sobre el conjunto completo de datos.
3. **Criterio de Selección Estricto:** La condición `if val > 50` evalúa si el elemento en curso es estrictamente mayor que $50$. De ser afirmativo, el valor es clonado e insertado al final del nuevo contenedor utilizando el método `.append(val)`. Nótese que el valor exacto de $50$ no cumple la condición, quedando correctamente excluido.

---

#### Explicación Línea por Línea

1. **`def filtrar_mayores_50(lista_original):`**  
   Declara la firma de la función `filtrar_mayores_50` la cual requiere una lista numérica como parámetro de entrada.
2. **`"""Filtra y retorna una nueva lista con valores estrictamente superiores a 50."""`**  
   Docstring de descripción metodológica de la función de filtrado.
3. **`lista_filtrada = []`**  
   Crea un contenedor de tipo lista inicialmente vacío (`[]`) asignado a `lista_filtrada` para almacenar de forma ordenada los elementos que pasen con éxito el criterio.
4. **`for val in lista_original:`**  
   Inicia la iteración secuencial a través del bucle `for` recorriendo linealmente cada número dentro de la colección original.
5. **`if val > 50:`**  
   Comprueba a nivel lógico si la variable en curso `val` representa un número estrictamente mayor que el límite de 50.
6. **`lista_filtrada.append(val)`**  
   Si la comparación lógica previa resulta verdadera, añade el número actual al final de la lista de salida empleando el método dinámico `.append()`.
7. **`return lista_filtrada`**  
   Una vez analizada la totalidad de los datos de entrada, la función retorna la nueva lista procesada, completando su ciclo de ejecución.
8. **`# Programa principal`**  
   Comentario explicativo que indica el inicio del código interactivo o ejecutable en consola.
9. **`print("--- Ejercicio 6: Filtrado de Datos (> 50) ---")`**  
   Imprime por consola la cabecera correspondiente al módulo.
10. **`datos = [12, 55, 78, 3, 99, 45, 50, 67, 2, 89]`**  
    Declara e inicializa la variable `datos` como una lista conteniendo diez números enteros desordenados.
11. **`filtrados = filtrar_mayores_50(datos)`**  
    Invoca la función de filtrado entregándole la lista original. Su retorno estructurado se asigna a la variable `filtrados`.
12. **`print(f"Datos originales: {datos}")`**  
    Imprime en pantalla la lista original para demostrar que permanece inalterada tras la operación.
13. **`print(f"Nueva lista filtrada: {filtrados}")`**  
    Muestra la nueva lista resultante conteniendo únicamente los valores superiores a cincuenta.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de filtrado secuencial
def filtrar_mayores_50(lista_original):
    """
    Analiza una lista de entrada y genera una nueva lista.
    Extrae únicamente los elementos estrictamente mayores a 50,
    dejando la lista original inalterada.
    """
    # Inicialización del nuevo contenedor vacío
    lista_filtrada = []
    
    # Recorrido lineal secuencial (complejidad temporal O(N))
    for val in lista_original:
        # Condicional de evaluación restrictiva
        if val > 50:
            lista_filtrada.append(val)  # Inserción en la sublista
            
    # Retorno de la nueva estructura resultante
    return lista_filtrada

# --- Flujo del Programa Principal ---
print("--- Ejercicio 6: Filtrado de Datos (> 50) ---")

# Inicialización de la muestra estadística desordenada
datos = [12, 55, 78, 3, 99, 45, 50, 67, 2, 89]

# Invocación de la función modular
filtrados = filtrar_mayores_50(datos)

# Impresión interactiva para contrastar los resultados obtenidos
print(f"Datos originales: {datos}")
print(f"Nueva lista filtrada: {filtrados}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ejecución con Muestra Estándar
*   **Datos de Entrada:** `[12, 55, 78, 3, 99, 45, 50, 67, 2, 89]`
*   **Salida del Programa:**
    ```text
    Datos originales: [12, 55, 78, 3, 99, 45, 50, 67, 2, 89]
    Nueva lista filtrada: [55, 78, 99, 67, 89]
    ```
    *(Nota: El valor 50 exacto ha sido excluido de forma correcta debido a la restricción estrictamente mayor).*

##### Caso de Uso 2: Muestra sin elementos que superen 50
*   **Datos de Entrada modificados:** `[5, 10, 15, 20, 25, 30, 45, 50]`
*   **Salida del Programa:**
    ```text
    Datos originales: [5, 10, 15, 20, 25, 30, 45, 50]
    Nueva lista filtrada: []
    ```

##### Caso de Uso 3: Muestra compuesta exclusivamente por números mayores a 50
*   **Datos de Entrada modificados:** `[51, 60, 75, 80, 95.8, 100]`
*   **Salida del Programa:**
    ```text
    Datos originales: [51, 60, 75, 80, 95.8, 100]
    Nueva lista filtrada: [51, 60, 75, 80, 95.8, 100]
    ```
