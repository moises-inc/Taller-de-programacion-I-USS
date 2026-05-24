### Ejercicio 14: Verificador de Año Bisiesto

#### Enunciado del Problema
Desarrolla un script que pida un año e indique si corresponde a un año bisiesto o no bisiesto, aplicando la siguiente regla:
*Un año es bisiesto si es divisible por 4, pero no por 100, salvo que también sea divisible por 400.*

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `ano` | `int` | Representa el año calendario ingresado por el usuario (validado estrictamente $> 0$). |
| `es_bisiesto` | `bool` | Variable booleana (`True` o `False`) que almacena la resolución lógica de las condiciones del año bisiesto. |

#### Lógica de la Solución
El algoritmo evalúa la bisiestidad astronómica basándose en las reglas del calendario gregoriano. Las condiciones para clasificar un año como bisiesto (366 días en lugar de 365) se combinan mediante álgebra booleana en una sola expresión analítica simplificada:
1. El año debe ser divisible exactamente por $4$ (operación: `ano % 4 == 0`).
2. El año **no** debe ser divisible por $100$ (operación: `ano % 100 != 0`).
3. Como excepción a la regla de 100, si el año es divisible por $400$, **sí** vuelve a ser bisiesto (operación: `ano % 400 == 0`).

La combinación de estas reglas se traduce en Python como:
$$\text{es\_bisiesto} = (\text{ano} \pmod 4 == 0 \land \text{ano} \pmod{100} \ne 0) \lor (\text{ano} \pmod{400} == 0)$$
Es decir: `es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`.

La entrada de datos se encapsula dentro de un ciclo interactivo con captura de excepciones para forzar el ingreso de enteros estrictamente mayores que $0$.

#### Explicación Línea por Línea
* **Línea 5 (`while True:`):** Declara el bucle de validación infinita de datos.
* **Línea 6 (`try:`):** Abre la zona de captura segura de la excepción de formato.
* **Línea 7 (`ano = int(input(...))`):** Pide la entrada y la transforma a entero. Si se ingresa una cadena no numérica, salta inmediatamente a la línea 12.
* **Línea 8 (`if ano > 0:`):** Valida que el año sea una cantidad cronológica real (mayor a cero).
* **Línea 9 (`break`):** Interrumpe el ciclo interactivo de validación al obtener un año correcto.
* **Línea 10 (`else:`):** Rama ejecutada si el número entero es $\le 0$.
* **Línea 11 (`print(...)`):** Muestra el mensaje explicando el requerimiento lógico de los años.
* **Línea 12 (`except ValueError:`):** Atrapa ingresos del usuario que no correspondan a un entero.
* **Línea 13 (`print(...)`):** Muestra el error de tipo de entrada.
* **Línea 16 (`es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`):** Aplica la regla booleana estructurada, combinando prioridad de operadores relacionales y conectores lógicos (`and` y `or`).
* **Línea 18 (`if es_bisiesto:`):** Bifurcación condicional basada en el resultado de la variable lógica.
* **Línea 19 (`print(...)`):** Despliega el resultado afirmativo (año bisiesto con 366 días).
* **Línea 20 (`else:`):** Rama en caso de que la variable lógica resulte falsa.
* **Línea 21 (`print(...)`):** Despliega el resultado negativo (año no bisiesto de 365 días).

#### Código Completo
```python
# Verificador de Año Bisiesto

print("--- Analizador de Año Bisiesto ---")

# Captura de datos con filtro estricto de enteros positivos
while True:
    try:
        ano = int(input("Ingrese el año a evaluar (entero mayor a 0): "))
        if ano > 0:
            break
        else:
            print("Por favor, ingrese un año mayor a cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un año en formato numérico entero.")

# Regla matemática para determinar año bisiesto
es_bisiesto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Impresión interactiva final del diagnóstico
if es_bisiesto:
    print(f"El año {ano} ES bisiesto (tiene 366 días).")
else:
    print(f"El año {ano} NO es bisiesto (tiene 365 días).")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Año bisiesto básico):
* **Entrada esperada:** `2024`
* **Salida del programa:** `El año 2024 ES bisiesto (tiene 366 días).`

##### Caso de Uso 2 (Año fin de siglo no bisiesto):
* **Entrada esperada:** `1900`
* **Salida del programa:** `El año 1900 NO es bisiesto (tiene 365 días).`

##### Caso de Uso 3 (Año divisible por 400 - Bisiesto excepcional):
* **Entrada esperada:** `2000`
* **Salida del programa:** `El año 2000 ES bisiesto (tiene 366 días).`

##### Caso de Uso 4 (Error y reintento):
* **Entrada esperada:** `-200` (luego) `bisiesto` (luego) `2026`
* **Salida del programa:**
  ```text
  Ingrese el año a evaluar (entero mayor a 0): -200
  Por favor, ingrese un año mayor a cero.
  Ingrese el año a evaluar (entero mayor a 0): bisiesto
  Entrada no válida. Por favor, ingrese un año en formato numérico entero.
  Ingrese el año a evaluar (entero mayor a 0): 2026
  El año 2026 NO es bisiesto (tiene 365 días).
  ```
