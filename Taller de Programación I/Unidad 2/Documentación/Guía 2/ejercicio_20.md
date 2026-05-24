### Ejercicio 20: Cálculo de peso en n objetos celestes

#### Enunciado del Problema
Desarrolla un script que pida al usuario un número n, correspondiente a la cantidad de objetos a analizar. Para cada objeto, debe pedir: Masa en kilogramos y Cuerpo celeste (Tierra, Luna, Marte o Júpiter). El cálculo del peso debe realizarse con peso = masa * gravedad (Tierra: 9.8, Luna: 1.62, Marte: 3.71, Júpiter: 24.79). Mostrar el peso calculado y al final: promedio de pesos y cantidad de veces que se eligió cada cuerpo.

#### Análisis de Variables y Parámetros
| Variable / Parámetro | Tipo de Dato | Función en el Código |
| --- | --- | --- |
| `n` | `int` | Variable de control ingresada por el usuario que parametriza dinámicamente el total de masas a evaluar. |
| `tierra_cnt` | `int` | Contador incremental de selecciones de la constante de gravedad de la Tierra. |
| `luna_cnt` | `int` | Contador incremental de selecciones de la constante de gravedad de la Luna. |
| `marte_cnt` | `int` | Contador incremental de selecciones de la constante de gravedad de Marte. |
| `jupiter_cnt` | `int` | Contador incremental de selecciones de la constante de gravedad de Júpiter. |
| `suma_pesos` | `float` | Acumulador decimal del total de peso físico calculado en Newtons en toda la secuencia para promediar. |
| `i` | `int` | Variable de iteración del ciclo `for` (0 a n-1). |
| `masa` | `float` | Masa en kilogramos del objeto actual evaluado en el ciclo, validada estrictamente mayor a cero. |
| `cuerpo` | `str` | Identificación textual del cuerpo celeste seleccionado, limpia de espacios y capitalizada. |
| `g` | `float` | Aceleración gravitacional asignada de manera condicionada según el cuerpo celeste en m/s². |
| `peso` | `float` | Fuerza de peso calculada en Newtons en el objeto actual evaluado. |
| `promedio_peso` | `float` | Media de los pesos físicos calculados en Newtons en el grupo analizado. |


## Lógica de la Solución
El programa calcula la fuerza gravitacional del peso en Newtons ($P = m \cdot g$) para un grupo variable de `n` objetos y los distribuye estadísticamente en diferentes cuerpos del Sistema Solar. 1. **Validación de n:** Se solicita el total de objetos `n` asegurando que sea un entero estrictamente positivo con control de excepciones.2. **Bucle Parametrizado:** Se corre un ciclo `for` de `n` iteraciones evaluando cada objeto: - **Masa:** Se captura y valida mediante `try-except` que sea flotante y estrictamente mayor a cero (`masa > 0`).- **Cuerpo Celeste:** Se solicita la identificación textual del planeta/satélite, aplicando `.strip().capitalize()` para normalizar la entrada y prevenir fallos por mayúsculas. Se anida un bucle `while True` interactivo que valida la membresía en los cuatro cuerpos autorizados (Tierra, Luna, Marte, Júpiter), asignando la constante gravitatoria `g` respectiva e incrementando su contador.3. **Cálculo y Acumulación:** Se realiza la multiplicación de la masa por la gravedad del cuerpo celeste (`peso = masa * g`), se muestra el desglose inmediato en Newtons y se añade al acumulador global `suma_pesos`. Al finalizar las `n` evaluaciones, se calcula el promedio de pesos del grupo en Newtons y se genera un reporte interplanetario consolidated.

## Explicación Línea por Línea
- **`while True: (primero)`**: Inicia el bucle de validación interactiva para capturar de forma robusta la variable de control `n`.
- **`n = int(input(...))`**: Solicita la cantidad de objetos, las fuerza a tipo entero con `int()` y las guarda en `n`.
- **`if n > 0:`**: Verifica lógicamente que la cantidad de objetos a evaluar sea estrictamente positiva.
- **`break`**: Sale del bucle de validación de `n` e inicia el procesamiento gravitatorio.
- **`except ValueError: (primero)`**: Atrapa excepciones de tipo si se introduce texto en la variable controladora `n`.
- **`tierra_cnt = 0`**: Inicializa el acumulador estadístico para las selecciones terrestres.
- **`luna_cnt = 0`**: Inicializa el acumulador estadístico para las selecciones lunares.
- **`marte_cnt = 0`**: Inicializa el acumulador estadístico para las selecciones marcianas.
- **`jupiter_cnt = 0`**: Inicializa el acumulador estadístico para las selecciones jovianas.
- **`suma_pesos = 0.0`**: Inicializa en 0.0 la variable acumuladora flotante para registrar la sumatoria total de los pesos calculados.
- **`for i in range(n):`**: Inicia el ciclo principal determinado que procesará exactamente a los `n` objetos físicos de la secuencia.
- **`while True: (segundo)`**: Bucle interactivo interno de validación para capturar y blindar el ingreso de la masa corporal.
- **`masa = float(input(...))`**: Solicita y convierte a decimal la masa en kilogramos del objeto, guardándola en `masa`.
- **`if masa > 0:`**: Verifica lógicamente que el cuerpo físico posea masa real y positiva.
- **`break`**: Sale del bucle de validación interna de masa actual al ser correcta.
- **`while True: (tercero)`**: Bucle interactivo interno de validación para capturar el cuerpo celeste y normalizarlo.
- **`cuerpo = input(...).strip().capitalize()`**: Captura el cuerpo celeste, remueve espacios y coloca la primera letra en mayúscula con `.capitalize()`.
- **`if cuerpo == "Tierra":`**: Evalúa si se seleccionó la Tierra.
- **`g = 9.80`**: Asigna la constante gravitacional terrestre de 9.80 m/s².
- **`tierra_cnt += 1`**: Suma 1 unidad al contador de selecciones de la Tierra.
- **`break`**: Rompe el ciclo de validación del cuerpo celeste al ser válido e inicia el cálculo.
- **`elif cuerpo == "Luna":`**: Evalúa si se seleccionó la Luna.
- **`g = 1.62`**: Asigna la constante gravitacional lunar de 1.62 m/s².
- **`luna_cnt += 1`**: Suma 1 unidad al contador de selecciones de la Luna.
- **`break`**: Rompe el ciclo de validación del cuerpo celeste.
- **`elif cuerpo == "Marte":`**: Evalúa si se seleccionó Marte.
- **`g = 3.71`**: Asigna la constante gravitacional marciana de 3.71 m/s².
- **`marte_cnt += 1`**: Suma 1 unidad al contador de selecciones marcianas.
- **`break`**: Rompe el ciclo de validación del cuerpo celeste.
- **`elif cuerpo in ["Júpiter", "Jupiter"]:`**: Evalúa si se seleccionó Júpiter (contemplando variantes con o sin tilde).
- **`g = 24.79`**: Asigna la constante gravitacional joviana de 24.79 m/s².
- **`jupiter_cnt += 1`**: Suma 1 unidad al contador de selecciones de Júpiter.
- **`break`**: Rompe el ciclo de validación del cuerpo celeste.
- **`else:`**: Bloque ejecutado al escribirse un cuerpo no admitido.
- **`print("Cuerpo celeste no...")`**: Informa que se requiere exclusivamente seleccionar entre los cuatro cuerpos planetarios autorizados.
- **`peso = masa * g`**: Calcula aritméticamente el peso físico en Newtons mediante multiplicación simple.
- **`suma_pesos += peso`**: Suma el peso calculado del objeto actual a la bolsa de sumatorias acumuladoras del grupo.
- **`print(f"Masa: {masa}... Peso...")`**: Informa al instante los desgloses físicos del objeto procesado con dos decimales.
- **`promedio_peso = suma_pesos / n`**: Calcula el promedio del peso en Newtons del grupo dividiendo la sumatoria acumulada por el total `n`.
- **`print("\n--- Reporte Interplanetario ---")`**: Encabezado impreso en la terminal al completarse los `n` ciclos del programa.
- **`print(...)`**: Imprime los reportes del promedio de peso grupal en Newtons y las frecuencias de cuerpos seleccionados.


#### Código Completo
```python
print("--- Calculadora Física Interplanetaria ---")
# Captura y validación de la variable controladora de objetos n
while True:
    try:
        n = int(input("¿Cuántos objetos desea evaluar?: "))
        if n > 0:
            break
        print("Error: La cantidad de objetos debe ser mayor a cero.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

tierra_cnt = 0
luna_cnt = 0
marte_cnt = 0
jupiter_cnt = 0
suma_pesos = 0.0

# Bucle dinámico principal parametrizado por la variable n
for i in range(n):
    print(f"\n--- Objeto {i+1} de {n} ---")
    # Validación interactiva interna de masa física en kg
    while True:
        try:
            masa = float(input("Ingrese masa del objeto en kilogramos (mayor a 0): "))
            if masa > 0:
                break
            print("Error: La masa debe ser mayor a cero.")
        except ValueError:
            print("Error: Ingrese un valor numérico.")

    # Validación interactiva interna de cuerpo celeste y normalización de texto
    while True:
        cuerpo = input("Seleccione cuerpo celeste (Tierra / Luna / Marte / Júpiter): ").strip().capitalize()
        if cuerpo == "Tierra":
            g = 9.80
            tierra_cnt += 1
            break
        elif cuerpo == "Luna":
            g = 1.62
            luna_cnt += 1
            break
        elif cuerpo == "Marte":
            g = 3.71
            marte_cnt += 1
            break
        elif cuerpo in ["Júpiter", "Jupiter"]:
            g = 24.79
            jupiter_cnt += 1
            break
        else:
            print("Cuerpo celeste no válido. Reintente.")

    # Operación física de peso y acumulación
    peso = masa * g
    suma_pesos += peso
    print(f"Masa: {masa} kg | Cuerpo: {cuerpo} (g = {g} m/s²) | Peso: {peso:.2f} N")

# Reporte interplanetario consolidated final
promedio_peso = suma_pesos / n
print("\n--- Reporte Interplanetario ---")
print(f"Promedio de pesos calculados: {promedio_peso:.2f} N")
print(f"Selecciones de la Tierra: {tierra_cnt}")
print(f"Selecciones de la Luna  : {luna_cnt}")
print(f"Selecciones de la Marte : {marte_cnt}")
print(f"Selecciones de la Júpiter: {jupiter_cnt}")
```

#### Casos de Uso de Ejemplo
**Entrada:**
```text
--- Calculadora Física Interplanetaria ---
¿Cuántos objetos desea evaluar?: 2

--- Objeto 1 de 2 ---
Ingrese masa del objeto en kilogramos (mayor a 0): 10
Seleccione cuerpo celeste (Tierra / Luna / Marte / Júpiter): luna
Masa: 10.0 kg | Cuerpo: Luna (g = 1.62 m/s²) | Peso: 16.20 N

--- Objeto 2 de 2 ---
Ingrese masa del objeto en kilogramos (mayor a 0): 5.5
Seleccione cuerpo celeste (Tierra / Luna / Marte / Júpiter): júpiter
Masa: 5.5 kg | Cuerpo: Júpiter (g = 24.79 m/s²) | Peso: 136.35 N
```
**Salida:**
```text
--- Reporte Interplanetario ---
Promedio de pesos calculados: 76.28 N
Selecciones de la Tierra: 0
Selecciones de la Luna  : 1
Selecciones de la Marte : 0
Selecciones de la Júpiter: 1
```
