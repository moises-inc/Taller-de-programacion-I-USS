### Ejercicio 1: Cálculo de total de compra con funciones

#### Enunciado del Problema
Crear una función que reciba el precio unitario de un producto y la cantidad de unidades a comprar, y retorne el monto total de la compra. El programa debe solicitar interactivamente los datos al usuario en la consola, validarlos para asegurar que no sean negativos ni incorrectos, e invocar la función para mostrar el resultado final con un formato legible.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `precio` | `float` | Parámetro de la función | Representa el valor monetario unitario de un artículo. |
| `cantidad` | `int` | Parámetro de la función | Representa el número total de unidades que se desean comprar. |
| `p` | `float` | Variable local (programa principal) | Almacena de manera temporal el precio digitado por el usuario tras ser validado. |
| `c` | `int` | Variable local (programa principal) | Almacena de manera temporal la cantidad digitada por el usuario tras ser validada. |
| `total` | `float` | Variable local (programa principal) | Guarda el resultado devuelto por la función `calcular_total`. |

---

#### Lógica de la Solución
El ejercicio implementa los principios de **modularidad** y **robustez**:
1. **Modularización:** Se encapsula el cálculo matemático básico ($Total = Precio \times Cantidad$) en la función `calcular_total(precio, cantidad)`. De esta forma, el motor de cálculo queda independiente de la interfaz de consola.
2. **Ciclo de Validación con Manejo de Excepciones:** En el flujo de control del programa principal, se implementa un bucle infinito `while True` interactivo. Dentro de este, una estructura `try-except` captura los posibles errores de conversión de tipos (`ValueError`) si el usuario introduce texto en vez de valores numéricos.
3. **Restricción Lógica:** Se aplica una condición lógica con `if p >= 0 and c >= 0` para impedir que se calculen compras con montos o unidades de carácter negativo. El bucle solo se rompe (`break`) cuando todas las entradas cumplen con ser válidas y positivas.
4. **Visualización Formateada:** Tras obtener el valor de retorno, se imprime formateado con separadores de miles y límite de dos decimales utilizando el formato estándar en pesos chilenos (CLP).

---

#### Explicación Línea por Línea

1. **`def calcular_total(precio, cantidad):`**  
   Define la función constructora del cálculo denominada `calcular_total`, la cual requiere dos parámetros posicionales: `precio` y `cantidad`.
2. **`"""Calcula el total a pagar basándose en el precio unitario y la cantidad."""`**  
   Bloque de documentación (*docstring*) que especifica con claridad didáctica el comportamiento y propósito matemático de la función.
3. **`return precio * cantidad`**  
   Línea ejecutora que multiplica el precio unitario por la cantidad de unidades solicitadas y devuelve inmediatamente el resultado flotante al flujo donde fue llamada.
4. **`# Programa principal`**  
   Comentario explicativo que indica el inicio del código cliente de ejecución secuencial en la consola.
5. **`print("--- Ejercicio 1: Cálculo de Compra ---")`**  
   Muestra un título estético y descriptivo en la salida estándar para guiar al usuario.
6. **`while True:`**  
   Inicia un bucle de control de entrada interactivo infinito que continuará repitiéndose hasta que la validación sea exitosa y se invoque la instrucción de salida `break`.
7. **`try:`**  
   Bloque de prueba que intenta ejecutar las instrucciones de lectura y conversión de datos, monitoreando cualquier falla imprevista de tipo sintáctico.
8. **`p = float(input("Ingrese el precio unitario del producto ($): "))`**  
   Captura la entrada de la terminal mediante `input()`, remueve los saltos de línea e intenta transformarla a un número real con decimales (`float`). Si el usuario ingresa caracteres no numéricos, aborta el bloque `try` y lanza una excepción `ValueError`.
9. **`c = int(input("Ingrese la cantidad de unidades a comprar: "))`**  
   Captura la cantidad de artículos de la terminal e intenta convertirla a un entero (`int`). El ingreso de cadenas de texto o valores decimales generará una excepción `ValueError`.
10. **`if p >= 0 and c >= 0:`**  
   Evalúa que las dos variables numéricas ingresadas representen montos comercialmente coherentes (valores positivos o cero).
11. **`break`**  
   Sentencia de control que finaliza y sale de manera inmediata del bucle `while` al haberse ingresado correctamente datos lógicos y coherentes.
12. **`print("Error: El precio y la cantidad no pueden ser negativos.")`**  
   Imprime un aviso restrictivo en caso de que las variables no pasen la prueba del `if` (es decir, si al menos una de ellas es negativa). El bucle continuará activo.
13. **`except ValueError:`**  
   Atrapa cualquier excepción del tipo `ValueError` que se haya generado en las líneas 8 o 9 debido a un tipo de entrada incompatible con la conversión requerida.
14. **`print("Error: Ingrese valores numéricos válidos.")`**  
   Informa al usuario que su entrada no es procesable y permite que el bucle comience una nueva iteración de solicitud sin romper o congelar la ejecución del programa.
15. **`total = calcular_total(p, c)`**  
   Invoca a la función enviándole los valores validados `p` (precio) y `c` (cantidad). El valor obtenido como respuesta se guarda en la variable `total`.
16. **`print(f"Monto total final a pagar: ${total:,.2f} CLP")`**  
   Imprime el resultado final formateando la salida mediante cadenas literales de Python (`f-strings`). La sintaxis `:,.2f` le da al número decimal un formato visual elegante con separador de miles (coma) y precisión fija a dos decimales.

---

#### Código Completo con Comentarios Pedagógicos

```python
# Definición de la función de cálculo comercial
def calcular_total(precio, cantidad):
    """
    Calcula el precio final multiplicando los parámetros recibidos.
    Multiplica un número flotante (precio) por un entero (cantidad).
    """
    return precio * cantidad

# --- Flujo del Programa Principal ---
print("--- Ejercicio 1: Cálculo de Compra ---")

# Bucle interactivo robusto para la captura segura de datos
while True:
    try:
        # Se solicita el precio como float para admitir centavos
        p = float(input("Ingrese el precio unitario del producto ($): "))
        # Se solicita la cantidad como int (unidades enteras discretas)
        c = int(input("Ingrese la cantidad de unidades a comprar: "))
        
        # Validar consistencia matemática en un contexto comercial
        if p >= 0 and c >= 0:
            break  # Datos correctos: salimos del bucle
        
        # Error lógico si ingresan números negativos
        print("Error: El precio y la cantidad no pueden ser negativos.")
    except ValueError:
        # Controlar ingresos que no se puedan convertir a números
        print("Error: Ingrese valores numéricos válidos.")

# Invocación de la función pasándole los argumentos validados
total = calcular_total(p, c)

# Muestra del resultado con formato monetario estándar
print(f"Monto total final a pagar: ${total:,.2f} CLP")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ejecución Correcta Estándar
*   **Entrada en Consola:**
    ```text
    Ingrese el precio unitario del producto ($): 15990.50
    Ingrese la cantidad de unidades a comprar: 3
    ```
*   **Salida del Programa:**
    ```text
    Monto total final a pagar: $47,971.50 CLP
    ```

##### Caso de Uso 2: Entrada Errónea de Tipo (Letras) y Recuperación
*   **Entrada en Consola:**
    ```text
    Ingrese el precio unitario del producto ($): gratis
    Error: Ingrese valores numéricos válidos.
    Ingrese el precio unitario del producto ($): 4500
    Ingrese la cantidad de unidades a comprar: 2.5
    Error: Ingrese valores numéricos válidos.
    Ingrese la cantidad de unidades a comprar: 4
    ```
*   **Salida del Programa:**
    ```text
    Monto total final a pagar: $18,000.00 CLP
    ```

##### Caso de Uso 3: Entrada Errónea Lógica (Valores Negativos)
*   **Entrada en Consola:**
    ```text
    Ingrese el precio unitario del producto ($): -500
    Ingrese la cantidad de unidades a comprar: 10
    Error: El precio y la cantidad no pueden ser negativos.
    Ingrese el precio unitario del producto ($): 1200
    Ingrese la cantidad de unidades a comprar: -2
    Error: El precio y la cantidad no pueden ser negativos.
    Ingrese el precio unitario del producto ($): 1200
    Ingrese la cantidad de unidades a comprar: 5
    ```
*   **Salida del Programa:**
    ```text
    Monto total final a pagar: $6,000.00 CLP
    ```
