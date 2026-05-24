### Ejercicio 7: Registro y control financiero de ventas del día

#### Enunciado del Problema
Diseñar un software de gestión financiera que registre y analice las transacciones comerciales del día. Para ello, se deben implementar tres funciones con responsabilidades modulares e independientes:
1.  `ingresar_ventas()`: Permite capturar de manera interactiva los montos de las ventas en un bucle interactivo. La captura debe finalizar en el instante en que el usuario ingrese el valor de $0$ o un valor negativo (criterio centinela). Debe incluir validaciones ante ingresos inválidos de tipo texto.
2.  `calcular_total_ventas(lista_ventas)`: Recibe la lista de ventas ingresadas y retorna el monto total acumulado de las ventas del día.
3.  `contar_ventas_mayor_10000(lista_ventas)`: Recibe la lista de ventas y retorna la cantidad de transacciones que superan estrictamente los $\$10.000$ CLP.

El programa principal debe coordinar el flujo secuencial invocando las funciones en orden y presentar un reporte consolidado formateado en pantalla.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `ventas` | `list` | Variable local (de `ingresar_ventas`) | Lista interna de acumulación que recopila secuencialmente las ventas validadas. |
| `monto` | `float` | Variable local (de `ingresar_ventas`) | Almacena provisionalmente el valor monetario ingresado en cada iteración. |
| `lista_ventas` | `list` | Parámetro de las funciones | Recibe por referencia la lista de transacciones recolectadas para ser analizada. |
| `total` | `float` | Variable local (de `calcular_total_ventas`) | Acumulador flotante para sumar progresivamente todos los montos de la lista. |
| `v` | `float` | Variable de control (de bucle `for`) | Representa el valor del elemento actual analizado en las iteraciones. |
| `contador` | `int` | Variable local (de `contar_ventas_mayor_10000`) | Cuenta la cantidad de registros que cumplen con ser mayores a $10.000$. |
| `registro_ventas` | `list` | Variable local (programa principal) | Almacena el listado definitivo de ventas retornado por `ingresar_ventas`. |
| `total_vendido` | `float` | Variable local (programa principal) | Almacena la suma acumulada total de dinero devuelta por `calcular_total_ventas`. |
| `ventas_top` | `int` | Variable local (programa principal) | Almacena la cantidad de ventas destacadas superior a $10.000$. |

---

#### Lógica de la Solución
Este programa ilustra la **arquitectura modular limpia** en el diseño de software interactivo:
1. **Modularidad Estricta:** Las tareas de recolección de datos (I/O), suma matemática y filtrado lógico por rango se implementan en funciones independientes. Ninguna función de cálculo interactúa con la terminal, manteniendo la cohesión de responsabilidades.
2. **Método de Control Centinela:** Se establece un valor o señal especial llamado "centinela" para detener la entrada indefinida de datos por parte del usuario. En este caso, el centinela es cualquier número menor o igual a cero (`monto <= 0`), lo cual es consistente comercialmente porque no existen ventas reales de monto negativo o nulo.
3. **Validación Anticaídas (Robustez):** Mediante `try-except`, se resguarda el proceso de facturación ante fallas del usuario al digitar letras o caracteres inesperados en la terminal.
4. **Análisis de Información y Formato:** Se procesa la lista con algoritmos de complejidad temporal $O(N)$ y se muestra formateada con separadores de miles y dos cifras decimales.

---

#### Explicación Línea por Línea

1. **`def ingresar_ventas():`**  
   Declara la función `ingresar_ventas`, responsable del ingreso interactivo de datos.
2. **`"""Registra ventas en un bucle interactivo hasta que el usuario decida finalizar."""`**  
   Docstring que explica con claridad el flujo dinámico interactivo con criterio centinela de la función.
3. **`ventas = []`**  
   Crea la lista local dinámica `ventas` inicialmente vacía.
4. **`print("Ingrese los montos de ventas. Escriba '0' o un valor menor para finalizar.")`**  
   Imprime las instrucciones en la consola detallando el uso del centinela de corte.
5. **`while True:`**  
   Inicia el bucle interactivo infinito para posibilitar una carga masiva y continua de datos en la caja registradora.
6. **`try:`**  
   Sección encargada de supervisar y capturar excepciones tipo ValueError.
7. **`monto = float(input("Ingrese monto de venta: $"))`**  
   Toma la entrada del teclado, la convierte a decimal flotante y la almacena en `monto`.
8. **`if monto <= 0:`**  
   Comprueba si la venta es menor o igual a cero (señal del centinela).
9. **`break`**  
   Rompe y finaliza inmediatamente la ejecución del ciclo `while` interactivo actual.
10. **`ventas.append(monto)`**  
    Añade el monto de la venta con formato flotante a la lista local con `.append()`.
11. **`except ValueError:`**  
    Atrapa fallas en la conversión flotante si el usuario ingresa textos o símbolos.
12. **`print("Error: Ingrese un monto numérico válido.")`**  
    Avisa del error tipográfico en pantalla para forzar un reintento limpio.
13. **`return ventas`**  
    Retorna la colección completa de montos válidos al programa principal.
14. **`def calcular_total_ventas(lista_ventas):`**  
   Declara la función `calcular_total_ventas` requiriendo la colección de datos como parámetro formal.
15. **`"""Calcula la suma total acumulada de las ventas."""`**  
   Docstring explicativo de la acumulación matemática lineal.
16. **`total = 0.0`**  
    Inicializa el acumulador local decimal `total` a `0.0`.
17. **`for v in lista_ventas:`**  
    Bucle `for` diseñado para recorrer secuencialmente cada número contenido en la lista de ventas.
18. **`total += v`**  
    Suma el valor de la venta en curso al acumulador `total`.
19. **`return total`**  
    Devuelve la suma total aritmética final.
20. **`def contar_ventas_mayor_10000(lista_ventas):`**  
   Declara la función encargada del conteo de auditoría de transacciones importantes.
21. **`"""Cuenta cuántas ventas del listado superan el valor límite de $10.000."""`**  
   Docstring descriptivo del umbral financiero evaluador.
22. **`contador = 0`**  
    Establece a cero el acumulador entero local `contador`.
23. **`for v in lista_ventas:`**  
    Recorre linealmente cada una de las ventas de la colección.
24. **`if v > 10000:`**  
    Valida si la venta en evaluación es estrictamente mayor que $10.000$ CLP.
25. **`contador += 1`**  
    Suma un entero unitario si el valor supera exitosamente el límite establecido en la condición.
26. **`return contador`**  
    Retorna el total de coincidencias.
27. **`# Programa principal`**  
    Marca el inicio del flujo secuencial del script principal.
28. **`print("--- Ejercicio 7: Registro y Control de Ventas ---")`**  
    Muestra la cabecera del módulo en la terminal.
29. **`registro_ventas = ingresar_ventas()`**  
    Llama a la primera función para iniciar la recolección, almacenando la lista final en `registro_ventas`.
30. **`total_vendido = calcular_total_ventas(registro_ventas)`**  
    Invoca a la función de cálculo pasándole la lista recolectada y guarda el total monetario.
31. **`ventas_top = contar_ventas_mayor_10000(registro_ventas)`**  
    Invoca la auditoría enviando la lista y guarda el recuento de ventas destacadas en `ventas_top`.
32. **`print("\n--- Reporte Consolidado de Ventas ---")`**  
    Imprime un divisor visual en la terminal para destacar el reporte definitivo.
33. **`print(f"Listado de ventas: {registro_ventas}")`**  
    Presenta de forma explícita el listado original de transacciones comerciales.
34. **`print(f"Suma total vendida: ${total_vendido:,.2f} CLP")`**  
    Presenta la recaudación global con un elegante formato que añade separador de miles y dos cifras decimales.
35. **`print(f"Cantidad de ventas sobre $10.000: {ventas_top}")`**  
    Informa en la consola la cantidad total de transacciones que superaron el umbral.

---

#### Código Completo con Comentarios Pedagógicos

```python
# --- Función 1: Recolección y Sanitización Interactiva ---
def ingresar_ventas():
    """
    Inicia un bucle de recolección interactiva.
    Finaliza cuando el usuario digita 0 o números negativos (criterio centinela).
    """
    ventas = []
    print("Ingrese los montos de ventas. Escriba '0' o un valor menor para finalizar.")
    
    while True:
        try:
            monto = float(input("Ingrese monto de venta: $"))
            
            # Evaluación del valor centinela de término
            if monto <= 0:
                break  # Detener bucle inmediatamente
                
            ventas.append(monto)  # Registro del monto válido
        except ValueError:
            print("Error: Ingrese un monto numérico válido.")
            
    return ventas  # Retorno de la colección final consolidada

# --- Función 2: Cómputo Aritmético Global ---
def calcular_total_ventas(lista_ventas):
    """
    Recorre secuencialmente la lista y calcula la suma acumulada de transacciones.
    """
    total = 0.0
    for v in lista_ventas:
        total += v
    return total

# --- Función 3: Auditoría y Conteo Acotado ---
def contar_ventas_mayor_10000(lista_ventas):
    """
    Examina secuencialmente la lista y cuenta los elementos que superan $10.000 CLP.
    """
    contador = 0
    for v in lista_ventas:
        if v > 10000:
            contador += 1
    return contador

# --- Flujo del Programa Principal ---
print("--- Ejercicio 7: Registro y Control de Ventas ---")

# Invocación coordinada y secuencial del software
registro_ventas = ingresar_ventas()
total_vendido = calcular_total_ventas(registro_ventas)
ventas_top = contar_ventas_mayor_10000(registro_ventas)

# Despliegue visual estructurado y académico del Reporte Final
print("\n--- Reporte Consolidado de Ventas ---")
print(f"Listado de ventas: {registro_ventas}")
print(f"Suma total vendida: ${total_vendido:,.2f} CLP")
print(f"Cantidad de ventas sobre $10.000: {ventas_top}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ejecución Comercial Completa
*   **Entrada en Consola:**
    ```text
    Ingrese los montos de ventas. Escriba '0' o un valor menor para finalizar.
    Ingrese monto de venta: $15500
    Ingrese monto de venta: $8990.50
    Ingrese monto de venta: $25000
    Ingrese monto de venta: $4500
    Ingrese monto de venta: $0
    ```
*   **Salida del Programa:**
    ```text
    --- Reporte Consolidado de Ventas ---
    Listado de ventas: [15500.0, 8990.5, 25000.0, 4500.0]
    Suma total vendida: $53,990.50 CLP
    Cantidad de ventas sobre $10.000: 2
    ```
    *(Nota: Las ventas mayores a $10.000 son 15500.0 y 25000.0).*

##### Caso de Uso 2: Entrada Errónea de Tipo y Recuperación
*   **Entrada en Consola:**
    ```text
    Ingrese los montos de ventas. Escriba '0' o un valor menor para finalizar.
    Ingrese monto de venta: diezmil
    Error: Ingrese un monto numérico válido.
    Ingrese monto de venta: 12000
    Ingrese monto de venta: -500
    ```
*   **Salida del Programa:**
    ```text
    --- Reporte Consolidado de Ventas ---
    Listado de ventas: [12000.0]
    Suma total vendida: $12,000.00 CLP
    Cantidad de ventas sobre $10.000: 1
    ```
