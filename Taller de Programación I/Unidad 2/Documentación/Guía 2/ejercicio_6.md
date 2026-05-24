### Ejercicio 6: Clasificador de temperaturas Celsius

#### Enunciado del Problema
Desarrolla un script que pida una temperatura en grados Celsius y la clasifique como bajo cero, fría, templada o caliente. El estudiante debe definir explícitamente los rangos para cada categoría antes de programar la solución.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `temperatura` | `float` | Guarda el valor numérico decimal que representa la temperatura en grados Celsius. |


## Lógica de la Solución
El programa clasifica un valor térmico real de acuerdo con cuatro zonas climáticas definidas convencionalmente: - **Bajo cero:** Temperaturas estrictamente menores a 0°C ($T < 0$).- **Fría:** Temperaturas desde 0°C hasta menos de 15°C ($0 \le T < 15$).- **Templada:** Temperaturas desde 15°C hasta menos de 30°C ($15 \le T < 30$).- **Caliente:** Temperaturas iguales o superiores a 30°C ($T \ge 30$).Para la robustez técnica, el script solicita la entrada con validación sintáctica de tipo flotante `float` y efectúa una evaluación en cascada excluyente con condicionales para dar salida al estado del clima.

## Explicación Línea por Línea
- **`while True:`**: Declara el bucle interactivo de solicitud de datos.
- **`try:`**: Define la región de control de tipos ante excepciones.
- **`temperatura = float(input(...))`**: Solicita la temperatura al usuario, permitiendo decimales mediante la conversión `float()`, y la guarda.
- **`break`**: Sale del bucle de validación tras confirmarse la transformación correcta a número decimal.
- **`except ValueError:`**: Captura los errores de conversión si la entrada posee caracteres inválidos.
- **`print("Entrada no válida...")`**: Informa que la entrada es inválida y solicita un número real.
- **`if temperatura < 0:`**: Evalúa si la temperatura física es estrictamente inferior a cero grados Celsius.
- **`print(f"La temperatura... es bajo cero.")`**: Se ejecuta en el condicional de primer nivel, mostrando que se encuentra congelada.
- **`elif temperatura < 15:`**: Filtro secundario en cascada. Determina si el valor es inferior a 15°C (ya habiendo descartado los valores negativos en el primer condicional).
- **`print(f"La temperatura... es fría.")`**: Imprime que la sensación térmica es fría si se cumple la condición anterior.
- **`elif temperatura < 30:`**: Filtro terciario. Evalúa si es menor a 30°C (es decir, en el intervalo térmico de 15°C a 29.9°C).
- **`print(f"La temperatura... es templada.")`**: Muestra que el ambiente se halla a una temperatura agradable y templada.
- **`else:`**: Bloque ejecutado al descartarse todas las categorías previas (temperaturas de 30°C o superiores).
- **`print(f"La temperatura... es caliente.")`**: Muestra en la consola de salida que el clima se reporta como caluroso.


#### Código Completo
```python
while True:
    try:
        # Captura la temperatura como número decimal (float)
        temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
        break  # Entrada correcta, sale del ciclo de validación
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número real.")

# Clasificación según los rangos establecidos de forma consecutiva
if temperatura < 0:
    print(f"La temperatura de {temperatura}°C es bajo cero.")
elif temperatura < 15:
    print(f"La temperatura de {temperatura}°C es fría.")
elif temperatura < 30:
    print(f"La temperatura de {temperatura}°C es templada.")
else:
    print(f"La temperatura de {temperatura}°C es caliente.")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
Ingrese la temperatura en grados Celsius: 22.8
```
**Salida:**
```text
La temperatura de 22.8°C es templada.
```
