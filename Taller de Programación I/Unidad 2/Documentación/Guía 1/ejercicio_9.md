### Ejercicio 9: Sistema de Cobro de Estacionamiento

#### Enunciado del Problema
Desarrolla un script que pida la patente de un vehículo y la cantidad de horas enteras estacionado. El estacionamiento cobra según el siguiente criterio:
* Hasta $2$ horas, cobra $\$2.000$ en total.
* Más de $2$ horas y hasta $5$ horas, cobra $\$3.500$ en total.
* Más de $5$ horas, cobra $\$5.000$ en total.

El script debe mostrar la patente y el valor a pagar.

#### Análisis de Variables y Parámetros
| Nombre de Variable | Tipo de Dato | Función en el Código |
| :--- | :--- | :--- |
| `patente` | `str` | Almacena el identificador o placa del vehículo (sanitizada en mayúsculas y libre de espacios). |
| `horas` | `int` | Almacena el tiempo que el vehículo permaneció estacionado (validado no negativo). |
| `costo` | `int` | Almacena el costo final calculado según los rangos tarifarios vigentes. |

#### Lógica de la Solución
El algoritmo soluciona el cálculo aplicando de forma rigurosa el principio **DRY (Don't Repeat Yourself)**. A diferencia de implementaciones redundantes que imprimen la salida dentro de cada bloque condicional, esta solución condensa el flujo lógico definiendo únicamente el valor de la variable de destino `costo` dentro del condicional (`if-elif-else`) para posteriormente delegar la impresión a un único bloque unificado final.

Los tramos de cobro se evalúan secuencialmente:
1. **Tramo 1 (Corto):** Si las horas son $\le 2 \implies \text{Costo} = \$2.000$.
2. **Tramo 2 (Medio):** Si no se cumple la anterior, pero las horas son $\le 5 \implies \text{Costo} = \$3.500$.
3. **Tramo 3 (Prolongado):** Si las horas superan el límite de 5 horas $\implies \text{Costo} = \$5.000$.

La captura incluye la sanitización de la patente (conversión a mayúsculas automática con `.upper()`) y el rechazo de valores de horas negativos.

#### Explicación Línea por Línea
* **Línea 5 (`print(...)`):** Despliega el título del punto de control del estacionamiento.
* **Línea 7 (`patente = input(...).strip().upper()`):** Solicita la patente, remueve espacios en los extremos y convierte la cadena a letras mayúsculas con `.upper()`.
* **Línea 8 (`while not patente:`):** Bucle interactivo que se ejecuta indefinidamente si la patente está vacía.
* **Línea 9 (`patente = ...`):** Reitera la solicitud de patente en caso de omisión.
* **Línea 11 (`while True:`):** Declara el bucle de validación para las horas de arriendo.
* **Línea 12 (`try:`):** Apertura de la zona segura de captura numérica.
* **Línea 13 (`horas = int(input(...))`):** Captura e intenta convertir el valor de entrada a un número entero (`int`).
* **Línea 14 (`if horas >= 0:`):** Verifica que las horas no sean un valor negativo insostenible comercialmente.
* **Línea 15 (`break`):** Rompe la iteración al conseguir un entero no negativo de horas.
* **Línea 16 (`else:`):** Rama en caso de enteros negativos.
* **Línea 17 (`print(...)`):** Advierte sobre el ingreso de tiempos negativos.
* **Línea 18 (`except ValueError:`):** Atrapa ingresos incorrectos como texto libre o caracteres decimales.
* **Línea 19 (`print(...)`):** Despliega la advertencia sobre el tipo de dato.
* **Líneas 22-23 (`if horas <= 2:`):** Primera rama condicional. Si las horas son menor o igual a 2, asigna `costo = 2000`.
* **Líneas 24-25 (`elif horas <= 5:`):** Si supera las 2 horas pero es menor o igual a 5 horas, asigna `costo = 3500`.
* **Líneas 26-27 (`else:`):** Por descarte (horas mayores estrictas a 5), asigna `costo = 5000`.
* **Líneas 30-32 (`print(...)`):** Bloque único final de salida. Imprime los detalles del recibo formateando el costo con comas como separadores de miles de forma clara y estética en moneda chilena (`${costo:,}`).

#### Código Completo
```python
# Cálculo de cobro de estacionamiento (Optimizado con DRY)

print("--- Sistema de Cobro de Estacionamiento ---")

# Solicita patente y aplica sanitización básica
patente = input("Ingrese la patente del vehículo: ").strip().upper()
while not patente:
    patente = input("La patente es obligatoria. Ingrese la patente: ").strip().upper()

# Captura y validación robusta de horas enteras
while True:
    try:
        horas = int(input("Ingrese la cantidad de horas enteras estacionado: "))
        if horas >= 0:
            break
        else:
            print("Las horas no pueden ser negativas.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Determinación condicional de costos
if horas <= 2:
    costo = 2000
elif horas <= 5:
    costo = 3500
else:
    costo = 5000

# Salida única formateada (DRY) con separador de miles
print(f"\nVehículo Patente: {patente}")
print(f"Tiempo estacionado: {horas} hora(s)")
print(f"Total a pagar: ${costo:,} CLP")
```

#### Casos de Uso de Ejemplo
##### Caso de Uso 1 (Hasta 2 horas):
* **Entrada esperada:** `bbdd12` (patente), `2` (horas)
* **Salida del programa:**
  ```text
  Vehículo Patente: BBDD12
  Tiempo estacionado: 2 hora(s)
  Total a pagar: $2,000 CLP
  ```

##### Caso de Uso 2 (Entre 2 y 5 horas):
* **Entrada esperada:** `XXYY99` (patente), `4` (horas)
* **Salida del programa:**
  ```text
  Vehículo Patente: XXYY99
  Tiempo estacionado: 4 hora(s)
  Total a pagar: $3,500 CLP
  ```

##### Caso de Uso 3 (Más de 5 horas):
* **Entrada esperada:** `ab-cd-12` (patente), `8` (horas)
* **Salida del programa:**
  ```text
  Vehículo Patente: AB-CD-12
  Tiempo estacionado: 8 hora(s)
  Total a pagar: $5,000 CLP
  ```

##### Caso de Uso 4 (Errores de entrada y resolución):
* **Entrada esperada:** `` (vacío) -> `CCFF44`, `dos` (horas) -> *Error* -> `-1` (horas) -> *Error* -> `1` (horas)
* **Salida del programa:**
  ```text
  Ingrese la patente del vehículo: 
  La patente es obligatoria. Ingrese la patente: CCFF44
  Ingrese la cantidad de horas enteras estacionado: dos
  Entrada no válida. Por favor, ingrese un número entero.
  Ingrese la cantidad de horas enteras estacionado: -1
  Las horas no pueden ser negativas.
  Ingrese la cantidad de horas enteras estacionado: 1
  
  Vehículo Patente: CCFF44
  Tiempo estacionado: 1 hora(s)
  Total a pagar: $2,000 CLP
  ```
