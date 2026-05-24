### Ejercicio 2: Evaluación modular de temperatura

#### Enunciado del Problema
Crear una función que reciba una temperatura expresada en grados Celsius (°C) y retorne una clasificación de texto de acuerdo con los siguientes rangos térmicos:
*   **'Frío':** Si la temperatura es estrictamente menor a 12°C.
*   **'Templado':** Si la temperatura se encuentra en el rango inclusivo entre 12°C y 25°C ($12 \le \text{temperatura} \le 25$).
*   **'Calor':** Si la temperatura es estrictamente superior a 25°C.

El programa debe solicitar interactivamente el valor decimal en la consola, validar la entrada usando manejo de excepciones y mostrar la etiqueta térmica correspondiente.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `temperatura` | `float` | Parámetro de la función | Recibe el valor numérico decimal a clasificar dentro de la función. |
| `t` | `float` | Variable local (programa principal) | Almacena la temperatura leída e interpretada desde el teclado tras pasar el filtro `try-except`. |
| `resultado` | `str` | Variable local (programa principal) | Guarda la etiqueta de clasificación de retorno devuelta por la función. |

---

#### Lógica de la Solución
El algoritmo se basa en una clasificación condicional estructurada mediante la separación de responsabilidades:
1. **Separación de Capas:** La función `evaluar_temperatura` no realiza tareas de entrada o salida (I/O). Únicamente aplica lógica de control sobre un parámetro numérico y retorna una respuesta.
2. **Evaluación de Intervalos:** Se utiliza la estructura condicional anidada `if-elif-else`. Al evaluar secuencialmente, si la primera condición (`temperatura < 12`) es falsa, automáticamente se deduce en la siguiente línea (`elif temperatura <= 25`) que el número es mayor o igual a 12. Esto permite definir de forma limpia un rango acotado sin necesidad de operadores lógicos redundantes como `and`.
3. **Manejo de Errores en la Captura:** El programa principal implementa un ciclo de captura interactiva controlado por un bloque `try-except` para prever que el usuario digite cadenas vacías, letras u otros caracteres inválidos en la terminal.

---

#### Explicación Línea por Línea

1. **`def evaluar_temperatura(temperatura):`**  
   Define la función llamada `evaluar_temperatura`, la cual está diseñada para recibir un único valor decimal representando la temperatura actual.
2. **`"""Clasifica la temperatura en Frío, Templado o Calor."""`**  
   Cadena de documentación (*docstring*) incorporada dentro de la estructura de la función para describir su comportamiento lógico.
3. **`if temperatura < 12:`**  
   Evalúa si la variable `temperatura` es estrictamente menor al límite de 12.
4. **`return "Frío"`**  
   Si se cumple la condición del `if`, la función retorna inmediatamente la cadena "Frío" y aborta cualquier ejecución restante del cuerpo de la función.
5. **`elif temperatura <= 25:`**  
   Esta línea se ejecuta únicamente si la condición anterior fue falsa ($temperatura \ge 12$). Valida de forma simplificada si la variable es menor o igual a 25. De cumplirse, clasifica el valor dentro del rango inclusivo $[12, 25]$.
6. **`return "Templado"`**  
   Retorna la cadena "Templado" y finaliza la ejecución de la función.
7. **`else:`**  
   Se ejecuta por descarte si todas las evaluaciones previas dieron falso. Significa que la temperatura es estrictamente mayor que 25.
8. **`return "Calor"`**  
   Retorna la etiqueta "Calor", terminando la ejecución de la función.
9. **`# Programa principal`**  
   Delimitador visual en formato comentario que indica el inicio del código cliente interactivo.
10. **`print("--- Ejercicio 2: Clasificación de Temperatura ---")`**  
    Imprime un encabezado estético descriptivo del programa.
11. **`while True:`**  
    Instrucción para crear un bucle interactivo que insistirá en la solicitud del dato hasta que el usuario entregue un tipo compatible.
12. **`try:`**  
    Inicializa el monitor de excepciones encargado de resguardar al intérprete ante errores de transformación de datos.
13. **`t = float(input("Ingrese la temperatura en grados Celsius (°C): "))`**  
    Solicita la temperatura a través de la terminal y la convierte a un número con punto decimal (`float`). De ingresarse texto incompatible, se gatilla una excepción del tipo `ValueError`.
14. **`break`**  
    Finaliza y sale inmediatamente del ciclo `while` debido a que la lectura y conversión se realizaron exitosamente sin lanzar errores.
15. **`except ValueError:`**  
    Bloque de contingencia que se ejecuta en el instante en que falla la instrucción `float(input())`.
16. **`print("Error: Ingrese un valor numérico decimal.")`**  
    Imprime un mensaje didáctico de error para invitar al usuario a corregir la entrada y comenzar el ciclo de nuevo.
17. **`resultado = evaluar_temperatura(t)`**  
    Llama a la función `evaluar_temperatura` pasando el valor de `t` como argumento y asigna la cadena resultante a la variable `resultado`.
18. **`print(f"La temperatura de {t}°C está clasificada como: {resultado}")`**  
    Presenta al usuario en consola el resultado consolidado mediante cadenas interpoladas, imprimiendo la temperatura leída y la etiqueta de clasificación.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de clasificación climática
def evaluar_temperatura(temperatura):
    """
    Clasifica un valor numérico de temperatura en tres categorías posibles.
    La evaluación es secuencial por lo que no requiere validar límites dobles.
    """
    if temperatura < 12:
        return "Frío"         # Retorno inmediato si es menor a 12°C
    elif temperatura <= 25:
        return "Templado"     # Retorno inmediato si se encuentra entre 12°C y 25°C
    else:
        return "Calor"        # Retorno por defecto si es mayor a 25°C

# --- Flujo del Programa Principal ---
print("--- Ejercicio 2: Clasificación de Temperatura ---")

# Bucle interactivo con control estricto de entrada
while True:
    try:
        # Se solicita entrada y se fuerza conversión a decimal (float)
        t = float(input("Ingrese la temperatura en grados Celsius (°C): "))
        break  # Si la conversión fue exitosa, rompemos el bucle
    except ValueError:
        # En caso de ingresar letras o caracteres especiales
        print("Error: Ingrese un valor numérico decimal.")

# Invocación de la función modular
resultado = evaluar_temperatura(t)

# Visualización pedagógica del resultado en consola
print(f"La temperatura de {t}°C está clasificada como: {resultado}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Rango 'Frío'
*   **Entrada en Consola:**
    ```text
    Ingrese la temperatura en grados Celsius (°C): 8.5
    ```
*   **Salida del Programa:**
    ```text
    La temperatura de 8.5°C está clasificada como: Frío
    ```

##### Caso de Uso 2: Rango 'Templado' (Caso Límite)
*   **Entrada en Consola:**
    ```text
    Ingrese la temperatura en grados Celsius (°C): 12.0
    ```
*   **Salida del Programa:**
    ```text
    La temperatura de 12.0°C está clasificada como: Templado
    ```

##### Caso de Uso 3: Rango 'Calor'
*   **Entrada en Consola:**
    ```text
    Ingrese la temperatura en grados Celsius (°C): 28.3
    ```
*   **Salida del Programa:**
    ```text
    La temperatura de 28.3°C está clasificada como: Calor
    ```

##### Caso de Uso 4: Entrada Errónea de Tipo y Recuperación
*   **Entrada en Consola:**
    ```text
    Ingrese la temperatura en grados Celsius (°C): veinticinco
    Error: Ingrese un valor numérico decimal.
    Ingrese la temperatura en grados Celsius (°C): 25.0
    ```
*   **Salida del Programa:**
    ```text
    La temperatura de 25.0°C está clasificada como: Templado
    ```
