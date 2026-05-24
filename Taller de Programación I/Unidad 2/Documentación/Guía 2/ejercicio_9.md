### Ejercicio 9: Cálculo de cobro de estacionamiento (DRY)

#### Enunciado del Problema
Desarrolla un script que pida la patente de un vehículo y la cantidad de horas enteras estacionado. El estacionamiento cobra según el siguiente criterio:
- Hasta 2 horas, cobra $2.000 en total.
- Más de 2 horas y hasta 5 horas, cobra $3.500 en total.
- Más de 5 horas, cobra $5.000 en total.
El script debe mostrar la patente y el valor a pagar.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `patente` | `str` | Almacena la patente del vehículo en mayúsculas y limpia de espacios periféricos. |
| `horas` | `int` | Horas enteras de permanencia en el recinto (debe ser no negativa). |
| `costo` | `int` | Variable de salida que almacena el costo a pagar según la escala de tiempo determinada. |


## Lógica de la Solución
El algoritmo calcula la tarifa de cobro aplicando el principio DRY (*Don't Repeat Yourself* o 'No te repitas'). En lugar de colocar comandos de impresión en cada rama de la bifurcación condicional, se define una variable intermediaria llamada `costo`. El condicional evalúa el tramo de horas y asigna el precio correspondiente a la variable `costo`. Al final del script, se implementa una única salida consolidada y formateada. Para lograr un flujo robusto: - Se limpia y transforma la patente a mayúsculas con `.strip().upper()`, asegurando que no se ingrese en blanco.- Se validan las horas de estacionamiento para que correspondan a un entero mayor o igual a cero, protegiendo al script con `try-except`.

## Explicación Línea por Línea
- **`patente = input(...).strip().upper()`**: Solicita la patente, remueve espacios vacíos al inicio y al final con `.strip()` y la convierte en mayúsculas sostenidas usando `.upper()`.
- **`while not patente:`**: Ciclo iterativo de control que rechaza el envío de patentes en blanco.
- **`patente = input(...).strip().upper()`**: Vuelve a requerir la patente en la terminal si se omitió inicialmente.
- **`while True:`**: Ciclo interactivo infinito para validar la cantidad de horas estacionado.
- **`try:`**: Región del bloque que vigila el tipo de dato ingresado por el usuario.
- **`horas = int(input(...))`**: Solicita las horas, las fuerza a tipo entero con `int()` y las guarda en la variable `horas`.
- **`if horas >= 0:`**: Verifica lógicamente que las horas no sean un número negativo.
- **`break`**: Sale del ciclo de validación al obtener un entero correcto no negativo.
- **`else:`**: Se ejecuta si las horas son un número negativo.
- **`print("Las horas no pueden...")`**: Mensaje de advertencia ante horas negativas.
- **`except ValueError:`**: Captura las excepciones si se ingresa texto o decimales con punto.
- **`print("Entrada no válida...")`**: Informa que se requiere ingresar estrictamente un número entero.
- **`if horas <= 2:`**: Evalúa si las horas pertenecen al primer tramo (menores o iguales a 2 horas).
- **`costo = 2000`**: Asigna a la variable intermedia `costo` el valor de $2.000 pesos si se cumple el primer tramo.
- **`elif horas <= 5:`**: Evaluación en cascada para el tramo secundario (horas mayores a 2 y menores o iguales a 5).
- **`costo = 3500`**: Asigna a la variable intermedia `costo` el valor de $3.500 pesos si se cumple la condición.
- **`else:`**: Bloque ejecutado si las horas superan las 5 unidades.
- **`costo = 5000`**: Asigna el costo máximo de tarifa de $5.000 pesos al superar las 5 horas.
- **`print(f"\nVehículo Patente...")`**: Muestra la salida consolidada y formateada. Utiliza `costo:,` para incluir el punto separador de miles dinámicamente en pesos chilenos.


#### Código Completo
```python
# Captura de patente con depuración de espacios y mayúsculas obligatorias
patente = input("Ingrese la patente del vehículo: ").strip().upper()
while not patente:
    patente = input("La patente es obligatoria. Ingrese la patente: ").strip().upper()

# Captura y validación lógica de horas estacionado
while True:
    try:
        horas = int(input("Ingrese la cantidad de horas enteras estacionado: "))
        if horas >= 0:
            break
        else:
            print("Las horas no pueden ser negativas.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")

# Lógica de cálculo DRY (Determinación del costo en variable intermedia)
if horas <= 2:
    costo = 2000
elif horas <= 5:
    costo = 3500
else:
    costo = 5000

# Salida única formateada respetando DRY con separador de miles
print(f"\nVehículo Patente: {patente} | Horas estacionado: {horas} hr(s) | Total a pagar: ${costo:,} CLP")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese la patente del vehículo:    xx-yy-11  
Ingrese la cantidad de horas enteras estacionado: -3
Las horas no pueden ser negativas.
Ingrese la cantidad de horas enteras estacionado: 4
```
**Salida:**
```text
Vehículo Patente: XX-YY-11 | Horas estacionado: 4 hr(s) | Total a pagar: $3,500 CLP
```
