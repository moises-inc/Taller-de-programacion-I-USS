### Ejercicio 4: Cálculo de promedio de notas con validación

#### Enunciado del Problema
Diseñar un programa modular que permita calcular la media aritmética de un conjunto variable de notas de estudiantes. El programa debe:
1.  Solicitar interactivamente la cantidad de calificaciones que se van a promediar, validando que sea un número entero positivo.
2.  Solicitar y validar cada una de las calificaciones ingresadas por teclado, asegurando que representen valores reales dentro del rango académico de la escala chilena (entre $1.0$ y $7.0$, inclusive).
3.  Implementar una función que calcule y retorne el promedio de las notas. La función debe protegerse contra divisiones por cero en caso de recibir una lista vacía.
4.  Mostrar la lista de notas recolectadas y el promedio final con formato de dos decimales.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista_notas` | `list` | Parámetro de la función | Almacena el conjunto de valores numéricos de las notas a promediar. |
| `suma` | `float` | Variable local (de la función) | Acumula la suma aritmética de todos los elementos contenidos en `lista_notas`. |
| `nota` | `float` | Variable local (de la función) | Variable de control utilizada para examinar secuencialmente cada valor de la lista. |
| `cant` | `int` | Variable local (programa principal) | Almacena la cantidad total de estudiantes/notas a ingresar, validada como entero positivo. |
| `notas` | `list` | Variable local (programa principal) | Lista inicialmente vacía que almacena progresivamente las notas validadas del usuario. |
| `i` | `int` | Variable local (programa principal) | Variable contadora del ciclo `for` utilizada para iterar hasta completar el ingreso total solicitado. |
| `n` | `float` | Variable local (programa principal) | Almacena transitoriamente la calificación digitada antes de confirmar si cumple con el rango de $1.0$ a $7.0$. |
| `promedio` | `float` | Variable local (programa principal) | Almacena el promedio resultante devuelto al invocar a la función `calcular_promedio`. |

---

#### Lógica de la Solución
Este programa destaca por implementar técnicas sólidas de **programación defensiva** y **control estricto de entrada de datos**:
1. **Modularización y Prevención Aritmética:** La función `calcular_promedio(lista_notas)` calcula el promedio clásico de forma pura. Sin embargo, para evitar que una lista vacía provoque una caída fatal del software debido a la división por cero (`ZeroDivisionError`), se añade un control preliminar con `len(lista_notas) == 0` que retorna `0.0`.
2. **Validación en Dos Fases:**
    *   **Fase 1 (Dimensión de Datos):** El programa exige ingresar un número entero de notas estrictamente superior a cero (`cant > 0`). Se controla que el dato sea de tipo entero mediante `try-except` para atrapar problemas de tipado (`ValueError`).
    *   **Fase 2 (Rango Académico):** Para cargar cada calificación en la lista, se utiliza un bucle anidado `while True` que condiciona la inserción únicamente si el flotante ingresado cumple con la desigualdad de rango $1.0 \le n \le 7.0$.
3. **Presentación de Resultados:** Muestra la lista original recolectada para verificación del usuario y el promedio matemático formateado a dos decimales con `:.2f`.

---

#### Explicación Línea por Línea

1. **`def calcular_promedio(lista_notas):`**  
   Define la función `calcular_promedio` encargada de computar la media aritmética de las notas recibidas en sus parámetros.
2. **`"""Calcula la media aritmética de una lista de notas. Evita divisiones por cero."""`**  
   Comentario interno (*docstring*) que documenta el comportamiento seguro de la función.
3. **`if len(lista_notas) == 0:`**  
   Estructura condicional de protección que verifica si la colección de notas está vacía.
4. **`return 0.0`**  
   En caso de que la lista no contenga ningún dato, la función retorna inmediatamente `0.0` impidiendo que se ejecute una división por cero en las líneas subsecuentes.
5. **`suma = 0.0`**  
   Inicializa la variable local flotante `suma` en cero para ir acumulando las calificaciones de forma limpia.
6. **`for nota in lista_notas:`**  
   Bucle iterador que recorre linealmente cada valor almacenado en la colección `lista_notas`.
7. **`suma += nota`**  
   Suma el valor actual de `nota` al acumulador `suma`.
8. **`return float(suma / len(lista_notas))`**  
   Divide el acumulado total por la cantidad de notas (dada por la función `len()`), fuerza su tipado a decimal (`float`) y devuelve el promedio final calculado.
9. **`# Programa principal`**  
   Identificador que marca el inicio del flujo interactivo y entrada en consola.
10. **`print("--- Ejercicio 4: Promedio de Notas ---")`**  
    Imprime un encabezado descriptivo en la salida estándar de la consola.
11. **`while True:`**  
    Inicia un bucle indefinido para forzar al usuario a proporcionar una cantidad válida de notas para el cálculo.
12. **`try:`**  
    Comienza el monitoreo de excepciones para evitar caídas del programa por errores de tipeo.
13. **`cant = int(input("¿Cuántas notas desea promediar hoy?: "))`**  
    Captura y convierte a entero (`int`) la cantidad de notas indicadas por el usuario. Si se ingresa texto, se salta a la excepción `ValueError`.
14. **`if cant > 0:`**  
    Comprueba si el valor ingresado corresponde a un entero estrictamente positivo.
15. **`break`**  
    Si la condición se cumple, detiene el ciclo de solicitud de cantidad (`break`) para proceder al ingreso de notas.
16. **`print("Error: Debe ingresar al menos una nota.")`**  
    Muestra un aviso correctivo al usuario en caso de ingresar números menores o iguales a cero.
17. **`except ValueError:`**  
    Atrapa fallas si se digitan tipos incompatibles con un entero.
18. **`print("Error: Ingrese un entero válido.")`**  
    Explica de forma didáctica el error de conversión y comienza un ciclo nuevo de petición de cantidad.
19. **`notas = []`**  
    Crea una lista vacía llamada `notas` donde se irán guardando las calificaciones validadas.
20. **`for i in range(cant):`**  
    Ciclo repetitivo acotado que se ejecuta exactamente la cantidad de veces especificada en `cant` utilizando el índice `i`.
21. **`while True:`**  
    Bucle interactivo interno diseñado para la validación persistente de la calificación del estudiante actual en el rango correcto.
22. **`try:`**  
    Inicia la detección de excepciones para la entrada de calificaciones.
23. **`n = float(input(f"Ingrese la nota del estudiante {i+1} de {cant} (1.0 a 7.0): "))`**  
    Solicita la nota del estudiante `i+1` (1-indexed para el usuario) y la convierte a decimal (`float`). Lanza `ValueError` ante ingresos no numéricos.
24. **`if 1.0 <= n <= 7.0:`**  
    Evalúa si la nota decimal digitada se encuentra dentro del rango de aprobación y reprobación oficial de Chile ($[1.0, 7.0]$).
25. **`notas.append(n)`**  
    Si la nota está en el rango correcto, se inserta al final del contenedor dinámico `notas` con el método `.append()`.
26. **`break`**  
    Rompe el ciclo de validación interactiva interna de la nota actual e incrementa el ciclo principal.
27. **`print("Error: Rango académico de notas en Chile es de 1.0 a 7.0.")`**  
    Indica al usuario que el número ingresado no representa una nota chilena válida en la escala académica.
28. **`except ValueError:`**  
    Captura las fallas de conversión a flotante.
29. **`print("Error: Ingrese una nota decimal válida.")`**  
    Informa amigablemente al usuario sobre el error y vuelve a solicitar el valor decimal correcto.
30. **`promedio = calcular_promedio(notas)`**  
    Invoca a la función `calcular_promedio` pasando la lista `notas` totalmente validada y asigna su respuesta a la variable `promedio`.
31. **`print(f"\nNotas registradas: {notas}")`**  
    Imprime en pantalla la lista definitiva de las notas con las que se realizó el cómputo.
32. **`print(f"Promedio final calculado: {promedio:.2f}")`**  
    Muestra el resultado promedio en consola formateado exactamente a dos cifras decimales.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de cálculo académico
def calcular_promedio(lista_notas):
    """
    Calcula el promedio de una lista de notas.
    Implementa programación defensiva contra errores de división por cero.
    """
    # Si la lista recibida está vacía, evitamos dividir por cero
    if len(lista_notas) == 0:
        return 0.0
        
    suma = 0.0
    # Recorrido secuencial para sumar los valores numéricos
    for nota in lista_notas:
        suma += nota
        
    # Retorna la media aritmética
    return float(suma / len(lista_notas))

# --- Flujo del Programa Principal ---
print("--- Ejercicio 4: Promedio de Notas ---")

# Fase 1: Solicitud interactiva y validación del tamaño de muestra
while True:
    try:
        cant = int(input("¿Cuántas notas desea promediar hoy?: "))
        if cant > 0:
            break  # Valor válido: continuamos con la recolección
        print("Error: Debe ingresar al menos una nota.")
    except ValueError:
        print("Error: Ingrese un entero válido.")

# Fase 2: Recolección y validación estricta de las calificaciones
notas = []
for i in range(cant):
    while True:
        try:
            # Entrada de la nota actual (ej: Estudiante 1 de 3)
            n = float(input(f"Ingrese la nota del estudiante {i+1} de {cant} (1.0 a 7.0): "))
            
            # Validación del rango oficial de la escala académica chilena
            if 1.0 <= n <= 7.0:
                notas.append(n)  # Nota válida: la añadimos a la lista
                break            # Salimos del bucle para pedir la siguiente nota
            
            print("Error: Rango académico de notas en Chile es de 1.0 a 7.0.")
        except ValueError:
            print("Error: Ingrese una nota decimal válida.")

# Fase 3: Cálculo y visualización de resultados
promedio = calcular_promedio(notas)

print(f"\nNotas registradas: {notas}")
print(f"Promedio final calculado: {promedio:.2f}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ingreso de Notas Válidas Exitoso
*   **Entrada en Consola:**
    ```text
    ¿Cuántas notas desea promediar hoy?: 3
    Ingrese la nota del estudiante 1 de 3 (1.0 a 7.0): 6.8
    Ingrese la nota del estudiante 2 de 3 (1.0 a 7.0): 5.5
    Ingrese la nota del estudiante 3 de 3 (1.0 a 7.0): 4.0
    ```
*   **Salida del Programa:**
    ```text
    Notas registradas: [6.8, 5.5, 4.0]
    Promedio final calculado: 5.43
    ```

##### Caso de Uso 2: Entrada con Errores Lógicos de Rango
*   **Entrada en Consola:**
    ```text
    ¿Cuántas notas desea promediar hoy?: 2
    Ingrese la nota del estudiante 1 de 2 (1.0 a 7.0): 0.5
    Error: Rango académico de notas en Chile es de 1.0 a 7.0.
    Ingrese la nota del estudiante 1 de 2 (1.0 a 7.0): 7.2
    Error: Rango académico de notas en Chile es de 1.0 a 7.0.
    Ingrese la nota del estudiante 1 de 2 (1.0 a 7.0): 7.0
    Ingrese la nota del estudiante 2 de 2 (1.0 a 7.0): 5.0
    ```
*   **Salida del Programa:**
    ```text
    Notas registradas: [7.0, 5.0]
    Promedio final calculado: 6.00
    ```

##### Caso de Uso 3: Entrada Errónea de Tipado y Recuperación
*   **Entrada en Consola:**
    ```text
    ¿Cuántas notas desea promediar hoy?: cero
    Error: Ingrese un entero válido.
    ¿Cuántas notas desea promediar hoy?: 1
    Ingrese la nota del estudiante 1 de 1 (1.0 a 7.0): nota_seis
    Error: Ingrese una nota decimal válida.
    Ingrese la nota del estudiante 1 de 1 (1.0 a 7.0): 6.0
    ```
*   **Salida del Programa:**
    ```text
    Notas registradas: [6.0]
    Promedio final calculado: 6.00
    ```
