### Ejercicio 2: Identificador de Números Pares e Impares

#### Enunciado del Problema
Desarrolla un script que pida un número entero al usuario e identifique si es par o impar utilizando el operador módulo (`%`).

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `numero` | `int` | Almacena el número entero ingresado por el usuario para evaluar su paridad matemática. |

#### Lógica de la Solución
El algoritmo se sustenta en la definición matemática de paridad: un número entero es clasificado como **par** si al dividirlo por $2$ el residuo de la división es exactamente igual a $0$. En caso contrario, el número es **impar**.
El residuo se obtiene directamente a través del operador módulo (`%`). Para garantizar la validez conceptual de la operación, el programa fuerza el ingreso de números enteros (`int`), controlando excepciones mediante un bloque iterativo `try-except` que rechaza valores con punto decimal o texto.

#### Explicación Línea por Línea
* **Línea 3 (`while True:`):** Declara una estructura repetitiva infinita para asegurar el control de la calidad del dato de entrada.
* **Línea 4 (`try:`):** Inicia la zona protegida para la captura e interpretación del dato de entrada.
* **Línea 5 (`numero = int(input(...))`):** Solicita la entrada al usuario, la convierte a un número de tipo entero (`int`) y la asigna a la variable `numero`. Si el usuario ingresa un decimal (ej: `4.5`) o texto, la función lanza un `ValueError`.
* **Línea 6 (`break`):** Rompe la iteración del ciclo si no ocurrieron excepciones en la asignación del número entero.
* **Línea 7 (`except ValueError:`):** Intercepta la excepción `ValueError` producida al intentar formatear un tipo incompatible a entero.
* **Línea 8 (`print(...)`):** Despliega en pantalla la instrucción correcta para reintentar la operación.
* **Línea 10 (`if numero % 2 == 0:`):** Evalúa el residuo de la operación aritmética `numero % 2`. Si es igual a $0$, significa divisibilidad perfecta por 2.
* **Línea 11 (`print(...)`):** Informa por consola mediante un *f-string* que el número es de naturaleza par.
* **Línea 12 (`else:`):** Establece el flujo alternativo directo (cuando el residuo de la división entera por 2 es $1$ o $-1$).
* **Línea 13 (`print(...)`):** Muestra por consola que el número analizado es impar.

#### Código Completo
```python
# Identificador de números pares e impares

while True:
    try:
        # Se solicita estrictamente un número entero para evaluar paridad
        numero = int(input("Ingrese un número entero: "))
        break  # Sale del bucle de validación si la conversión a int es exitosa
    except ValueError:
        # Captura el error si el usuario ingresa un flotante o un string
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Uso del operador módulo (%) para verificar el residuo de la división entre 2
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Entrada de par positivo):
* **Entrada esperada:** `8`
* **Salida del programa:** `El número 8 es par.`

##### Caso de Uso 2 (Entrada de impar positivo):
* **Entrada esperada:** `13`
* **Salida del programa:** `El número 13 es impar.`

##### Caso de Uso 3 (Entrada de par negativo):
* **Entrada esperada:** `-42`
* **Salida del programa:** `El número -42 es par.`

##### Caso de Uso 4 (Entrada con decimal y recuperación):
* **Entrada esperada:** `4.5` (luego) `10`
* **Salida del programa:**
  ```text
  Entrada no válida. Por favor, ingrese un número entero.
  Ingrese un número entero: 10
  El número 10 es par.
  ```
