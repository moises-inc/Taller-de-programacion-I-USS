### Ejercicio 20: Cálculo de Peso Gravitacional en el Espacio

#### Enunciado del Problema
Desarrolla un script que calcule el peso de un objeto en distintos cuerpos celestes. El programa debe pedir la masa del objeto en kilogramos y luego pedir el cuerpo celeste donde se desea calcular el peso: Tierra, Luna, Marte o Júpiter.
El cálculo debe realizarse con la fórmula:
$$\text{peso} = \text{masa} \times \text{gravedad}$$
Usa los siguientes valores de gravedad:
* **Tierra:** $9.8\text{ m/s²}$
* **Luna:** $1.62\text{ m/s²}$
* **Marte:** $3.71\text{ m/s²}$
* **Júpiter:** $24.79\text{ m/s²}$

El script debe mostrar la masa ingresada, el cuerpo celeste seleccionado y el peso calculado. Si el cuerpo celeste no corresponde a una opción válida, debe mostrar: *“Cuerpo celeste no válido”*.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `gravedades` | `dict` | Estructura de mapeo asociativo que vincula cada astro (clave, `str`) con su factor de aceleración de gravedad (valor, `float`). |
| `masa` | `float` | Almacena la masa física del objeto medida en kilogramos (validada estrictamente $> 0$). |
| `cuerpo` | `str` | Almacena la entrada de texto del usuario, sanitizada y normalizada en minúsculas. |
| `g` | `float` | Almacena el valor físico de la gravedad recuperado dinámicamente del diccionario. |
| `peso` | `float` | Almacena el resultado aritmético del producto de la masa por la gravedad en Newtons (N). |

#### Lógica de la Solución
El algoritmo modela de forma eficiente la ley de gravitación de la física clásica en el sistema planetario. 
Para optimizar el diseño y evitar estructuras condicionales `if-elif` anidadas y extensas para asignar la gravedad, el script utiliza un **Diccionario (`dict`)** asociativo de Python. Esta estructura permite buscar constantes físicas de forma limpia y con una complejidad temporal de $O(1)$.

El flujo metodológico es:
1. **Validación Física:** Captura e interactividad mediante un ciclo `try-except` para garantizar que la masa sea un número de punto flotante real estrictamente superior a cero ($0$).
2. **Sanitización del Astro:** Estandariza la entrada de texto libre aplicando `.strip().lower()` y manejando de forma preventiva la posible acentuación en `"júpiter"`.
3. **Validación y Cálculo:** Verifica la existencia de la clave del cuerpo celeste dentro del diccionario mediante el operador de membresía `in`. Si existe, recupera su valor de gravedad, calcula el peso utilizando la fórmula $P = m \cdot g$ en Newtons, y despliega la ficha física. Si la clave no forma parte del diccionario, muestra el mensaje condicionado: *“Cuerpo celeste no válido”*.

#### Explicación Línea por Línea
* **Línea 5 (`gravedades = {...}`):** Inicializa el diccionario mapeando los astros disponibles con sus constantes de aceleración gravitatoria exactas.
* **Línea 11 (`while True:`):** Declara el bucle de validación infinita de la masa del objeto.
* **Línea 12 (`try:`):** Apertura de la zona protegida de conversión decimal.
* **Línea 13 (`masa = float(input(...))`):** Solicita la masa y la convierte a decimal (`float`).
* **Línea 14 (`if masa > 0:`):** Valida que la magnitud de la masa sea positiva en la física macroscópica.
* **Línea 15 (`break`):** Rompe el bucle interactivo al conseguir una masa válida.
* **Línea 16 (`else:`):** Rama para masas no positivas.
* **Línea 17 (`print(...)`):** Muestra el mensaje explicando la condición indispensable de masa positiva.
* **Línea 18 (`except ValueError:`):** Atrapa ingresos no numéricos.
* **Línea 19 (`print(...)`):** Informa acerca del formato del dato numérico.
* **Línea 21 (`cuerpo = input(...).strip().lower()`):** Solicita el cuerpo celeste sanitizando espacios adicionales y convirtiendo la cadena a minúsculas.
* **Línea 23 (`if cuerpo == "júpiter":`):** Condicional preventivo que intercepta y estandariza la tilde gramatical.
* **Línea 24 (`cuerpo = "jupiter"`):** Reasigna la cadena sin tildes para poder ser indexada en el diccionario de forma precisa.
* **Línea 26 (`if cuerpo in gravedades:`):** Comprueba si el cuerpo celeste ingresado está registrado como clave en el diccionario `gravedades`.
* **Línea 27 (`g = gravedades[cuerpo]`):** Recupera dinámicamente la aceleración de gravedad asociada al cuerpo en tiempo de ejecución.
* **Línea 28 (`peso = masa * g`):** Calcula aritméticamente el peso resultante multiplicando la masa por la gravedad.
* **Líneas 29-33 (`print(...)`):** Despliega por consola la ficha analítica de resultados del cálculo físico, mostrando el peso final en Newtons con una precisión acotada de dos decimales (`:.2f`) y capitalizando el nombre del cuerpo celeste (`.capitalize()`).
* **Línea 34 (`else:`):** Se activa si el cuerpo celeste provisto por el usuario no forma parte de las opciones declaradas en el diccionario.
* **Línea 35 (`print(...)`):** Informa por consola con la advertencia reglamentaria: “Cuerpo celeste no válido”.

#### Código Completo
```python
# Cálculo de peso en cuerpos celestes

print("--- Cálculo de Peso Gravitacional en el Espacio ---")

# Diccionario asociativo de constantes físicas (g en m/s²)
gravedades = {
    "tierra": 9.8,
    "luna": 1.62,
    "marte": 3.71,
    "jupiter": 24.79
}

# Validación estructurada de la masa del objeto
while True:
    try:
        masa = float(input("Ingrese la masa del objeto en kilogramos (ej: 12.8): "))
        if masa > 0:
            break
        else:
            print("La masa del objeto debe ser mayor que cero.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Captura y normalización de la cadena de texto del astro
cuerpo = input("Ingrese el cuerpo celeste (Tierra / Luna / Marte / Júpiter): ").strip().lower()

# Normalización manual de la tilde gramatical
if cuerpo == "júpiter":
    cuerpo = "jupiter"

# Comprobación de existencia en diccionario
if cuerpo in gravedades:
    g = gravedades[cuerpo]
    peso = masa * g
    
    # Ficha del reporte físico
    print(f"\n--- Ficha de Cálculo Físico ---")
    print(f"Masa ingresada: {masa} kg")
    print(f"Cuerpo celeste seleccionado: {cuerpo.capitalize()}")
    print(f"Aceleración de gravedad g: {g} m/s²")
    print(f"Peso calculado: {peso:.2f} Newtons (N)")
else:
    print("\nCuerpo celeste no válido.")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Cálculo regular en la Tierra):
* **Entrada esperada:** `10` (masa), `Tierra` (cuerpo celeste)
* **Salida del programa:**
  ```text
  --- Ficha de Cálculo Físico ---
  Masa ingresada: 10.0 kg
  Cuerpo celeste seleccionado: Tierra
  Aceleración de gravedad g: 9.8 m/s²
  Peso calculado: 98.00 Newtons (N)
  ```

##### Caso de Uso 2 (Cálculo en Júpiter con tilde):
* **Entrada esperada:** `5.5` (masa), `Júpiter` (cuerpo celeste)
* **Salida del programa:**
  ```text
  --- Ficha de Cálculo Físico ---
  Masa ingresada: 5.5 kg
  Cuerpo celeste seleccionado: Jupiter
  Aceleración de gravedad g: 24.79 m/s²
  Peso calculado: 136.35 Newtons (N)
  ```

##### Caso de Uso 3 (Cuerpo celeste no válido):
* **Entrada esperada:** `25` (masa), `Saturno` (cuerpo celeste)
* **Salida del programa:** `Cuerpo celeste no válido.`

##### Caso de Uso 4 (Error inicial y reintento):
* **Entrada esperada:** `-10` (masa) -> *Error* -> `12.5` (masa), `luna` (cuerpo celeste)
* **Salida del programa:**
  ```text
  Ingrese la masa del objeto en kilogramos (ej: 12.8): -10
  La masa del objeto debe ser mayor que cero.
  Ingrese la masa del objeto en kilogramos (ej: 12.8): 12.5
  Ingrese el cuerpo celeste (Tierra / Luna / Marte / Júpiter): luna
  
  --- Ficha de Cálculo Físico ---
  Masa ingresada: 12.5 kg
  Cuerpo celeste seleccionado: Luna
  Aceleración de gravedad g: 1.62 m/s²
  Peso calculado: 20.25 Newtons (N)
  ```
