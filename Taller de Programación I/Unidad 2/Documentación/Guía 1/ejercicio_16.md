### Ejercicio 16: Calculador de Índice de Masa Corporal (IMC)

#### Enunciado del Problema
Desarrolla un script que pida el peso en kilogramos y la estatura en metros de una persona. Luego, debe calcular el Índice de Masa Corporal (IMC) usando la fórmula:
$$\text{IMC} = \frac{\text{peso}}{\text{estatura}^2}$$
Después, debe mostrar la clasificación correspondiente según la Organización Mundial de la Salud (OMS):
* **Bajo peso:** menor a $18.5$
* **Normal:** desde $18.5$ hasta $24.9$
* **Sobrepeso:** $25.0$ o más

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `peso` | `float` | Almacena la masa corporal de la persona en kilogramos (validada estrictamente $> 2.0$ kg). |
| `estatura` | `float` | Almacena la estatura de la persona en metros (validada estrictamente $> 0.5$ m). |
| `imc` | `float` | Almacena el resultado aritmético del cálculo del Índice de Masa Corporal. |
| `clasificacion` | `str` | Almacena la etiqueta descriptiva del estado nutricional establecida por la OMS. |

#### Lógica de la Solución
El algoritmo soluciona de forma rigurosa y segura el cálculo del IMC. En desarrollos médicos y de salud, se requiere **validación antropométrica realista**. Si bien un usuario podría ingresar un peso de $0$ o una estatura de $0$, esto provocaría un error fatal de división por cero (`ZeroDivisionError`) o resultados absurdos. Por lo tanto:
1. Se valida de forma independiente que el peso sea estrictamente superior a $2.0$ kg.
2. Se valida que la estatura sea estrictamente superior a $0.5$ metros.

Ambas variables aceptan decimales (`float`) y se encapsulan en bucles de validación `while True` con control de excepciones `ValueError`. 

Tras obtener datos plausibles, se ejecuta la ecuación matemática $\text{IMC} = \frac{\text{peso}}{\text{estatura}^2}$ (en Python: `peso / (estatura ** 2)`).
Finalmente, se evalúa en cascada la clasificación de la OMS utilizando `if-elif-else`:
* $\text{IMC} < 18.5 \implies$ Bajo Peso.
* $18.5 \le \text{IMC} < 25.0 \implies$ Peso Normal.
* $\text{IMC} \ge 25.0 \implies$ Sobrepeso.

#### Explicación Línea por Línea
* **Línea 5 (`while True:`):** Inicia el bucle de validación interactivo para la masa corporal.
* **Línea 6 (`try:`):** Bloque protegido para la entrada del peso.
* **Línea 7 (`peso = float(input(...))`):** Captura el peso e intenta transformarlo a decimal (`float`).
* **Línea 8 (`if peso > 2.0:`):** Evalúa si la masa ingresada supera el límite biológico mínimo de 2 kg.
* **Línea 9 (`break`):** Rompe la iteración del peso al conseguir una entrada realista.
* **Línea 10 (`else:`):** Se ejecuta si el peso es menor o igual a 2.
* **Línea 11 (`print(...)`):** Muestra el mensaje educativo pidiendo un peso viable.
* **Línea 12 (`except ValueError:`):** Atrapa texto u otros formatos incompatibles.
* **Línea 13 (`print(...)`):** Informa del error de formato en el peso.
* **Líneas 15-23 (`while True...`):** Bucle idéntico al anterior, diseñado para capturar la estatura, forzando a que sea un decimal estrictamente superior a $0.5$ metros para evitar divisiones por cero.
* **Línea 26 (`imc = peso / (estatura ** 2)`):** Calcula aritméticamente el IMC elevando la estatura al cuadrado usando el operador exponente (`**`).
* **Líneas 29-34 (`if-elif-else`):** Evalúa los límites del IMC en cascada según el estándar de la OMS para catalogar el estado nutricional de la persona.
* **Líneas 36-40 (`print(...)`):** Despliega de forma limpia la ficha nutricional de la persona, acotando el IMC resultante a exactamente dos decimales (`:.2f`).

#### Código Completo
```python
# Calculador de IMC con estándares de la OMS

print("--- Calculador de Índice de Masa Corporal (IMC) ---")

# Validación estructurada del peso corporal
while True:
    try:
        peso = float(input("Ingrese su peso en kilogramos (ej: 72.5): "))
        if peso > 2.0:
            break
        else:
            print("Por favor, ingrese un peso válido mayor a 2 kg.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Validación estructurada de la estatura
while True:
    try:
        estatura = float(input("Ingrese su estatura en metros (ej: 1.75): "))
        if estatura > 0.5:
            break
        else:
            print("Por favor, ingrese una estatura válida mayor a 0.5 metros.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número decimal o entero.")

# Cálculo matemático de IMC
imc = peso / (estatura ** 2)

# Clasificación oficial de la OMS
if imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc < 25.0:
    clasificacion = "Peso Normal"
else:
    clasificacion = "Sobrepeso (se aconseja realizar chequeos preventivos)"

# Ficha de reporte final
print(f"\n--- Reporte Nutricional ---")
print(f"Peso ingresado: {peso} kg")
print(f"Estatura ingresada: {estatura} m")
print(f"Su IMC es: {imc:.2f}")
print(f"Estado Nutricional (OMS): {clasificacion}")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Peso Normal):
* **Entrada esperada:** `70` (peso), `1.75` (estatura)
* **Salida del programa:**
  ```text
  --- Reporte Nutricional ---
  Peso ingresado: 70.0 kg
  Estatura ingresada: 1.75 m
  Su IMC es: 22.86
  Estado Nutricional (OMS): Peso Normal
  ```

##### Caso de Uso 2 (Bajo Peso):
* **Entrada esperada:** `50` (peso), `1.70` (estatura)
* **Salida del programa:**
  ```text
  --- Reporte Nutricional ---
  Peso ingresado: 50.0 kg
  Estatura ingresada: 1.70 m
  Su IMC es: 17.30
  Estado Nutricional (OMS): Bajo Peso
  ```

##### Caso de Uso 3 (Sobrepeso):
* **Entrada esperada:** `90` (peso), `1.80` (estatura)
* **Salida del programa:**
  ```text
  --- Reporte Nutricional ---
  Peso ingresado: 90.0 kg
  Estatura ingresada: 1.80 m
  Su IMC es: 27.78
  Estado Nutricional (OMS): Sobrepeso (se aconseja realizar chequeos preventivos)
  ```

##### Caso de Uso 4 (Error inicial y reintento en cascada):
* **Entrada esperada:** `cero` (peso) -> *Error* -> `1` (peso) -> *Error* -> `80`, `0.4` (estatura) -> *Error* -> `1.85`
* **Salida del programa:**
  ```text
  Ingrese su peso en kilogramos (ej: 72.5): cero
  Entrada no válida. Por favor, ingrese un número decimal o entero.
  Ingrese su peso en kilogramos (ej: 72.5): 1
  Por favor, ingrese un peso válido mayor a 2 kg.
  Ingrese su peso en kilogramos (ej: 72.5): 80
  Ingrese su estatura en metros (ej: 1.75): 0.4
  Por favor, ingrese una estatura válida mayor a 0.5 metros.
  Ingrese su estatura en metros (ej: 1.75): 1.85
  
  --- Reporte Nutricional ---
  Peso ingresado: 80.0 kg
  Estatura ingresada: 1.85 m
  Su IMC es: 23.37
  Estado Nutricional (OMS): Peso Normal
  ```
