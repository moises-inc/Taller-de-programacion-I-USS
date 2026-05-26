### Caso G: Calculadora de Planilla de Sueldos (Ingeniería USS)

#### Enunciado del Problema
Una pequeña empresa de construcción necesita calcular de forma automatizada la planilla de sueldos mensual de sus trabajadores. La liquidación se computa dinámicamente según las horas trabajadas en el mes y una tarifa por hora individual para cada empleado.

*   **Reglas comerciales de negocio:**
    *   Las primeras 45 horas mensuales se pagan bajo tarifa normal.
    *   Las horas que excedan la jornada normal (sobre 45) se pagan con un **recargo por horas extras del 50%** (Tarifa Horaria × 1.5).
    *   `Pago Total = Pago Base + Pago Extra`
*   **Resultados esperados:**
    *   Tabla consolidada alineada con: Nombre, Horas Normales, Horas Extra, Pago Base, Pago Extra y Pago Total.
    *   Suma global de toda la planilla (gasto total en remuneraciones).
    *   Identificación manual del trabajador con mayor y menor sueldo de la nómina.
*   **Restricciones de arquitectura:**
    *   Uso de **listas paralelas** independientes para almacenar la información de los trabajadores.
    *   Diseño modular separando responsabilidades mediante **funciones específicas**.
    *   **Validación robusta** contra ingresos de tipos no numéricos y control de valores no negativos.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `HORAS_BASE` | `int` | Constante Global | Define el límite de la jornada laboral normal sin recargos ($45$ horas). |
| `RECARGO_EXTRA` | `float` | Constante Global | Factor multiplicativo para el recargo de horas extras ($1.5$). |
| `SEPARADOR` | `str` | Constante Global | Cadena divisoria para embellecer los reportes impresos en consola. |
| `mensaje` | `str` | Parámetro (de `ingresar_numero`) | Mensaje instructivo desplegado para solicitar datos al usuario. |
| `minimo` | `float` | Parámetro (de `ingresar_numero`) | Límite inferior admisible para validaciones numéricas (por defecto $0.01$). |
| `valor` | `float` | Variable local (de `ingresar_numero`) | Almacena temporalmente el número ingresado tras ser validado contra errores de tipo. |
| `n` | `int` | Variable local (de `ingresar_trabajadores`) | Cantidad total de trabajadores a registrar en la jornada ($n \ge 2$). |
| `nombres` | `list` | Colección local / Retorno | Lista paralela para guardar los nombres de los trabajadores (`str`). |
| `horas` | `list` | Colección local / Retorno | Lista paralela para guardar las horas del mes (`float`). |
| `tarifas` | `list` | Colección local / Retorno | Lista paralela para guardar las tarifas por hora (`float`). |
| `horas_normales` | `float` | Variable local (de `calcular_pago`) | Horas trabajadas que se liquidarán bajo tarifa base. |
| `horas_extra` | `float` | Variable local (de `calcular_pago`) | Horas excedentes liquidadas con el recargo comercial. |
| `pago_base` | `float` | Variable local / Retorno | Remuneración obtenida por las horas normales trabajadas. |
| `pago_extra` | `float` | Variable local / Retorno | Remuneración obtenida por las horas extra con recargo. |
| `pago_total` | `float` | Variable local / Retorno | Gasto total de remuneración individual (`pago_base + pago_extra`). |
| `pagos` | `list` | Parámetro (de `encontrar_extremo`) | Colección con los sueldos totales para buscar extremos. |
| `buscar_maximo` | `bool` | Parámetro (de `encontrar_extremo`) | Conmutador: `True` para buscar el mayor sueldo, `False` para el menor. |
| `idx_extremo` | `int` | Variable local (de `encontrar_extremo`) | Índice del elemento que representa de forma provisional el sueldo extremo. |

---

#### Lógica de la Solución
El ejercicio representa un modelo robusto de desarrollo estructurado académico bajo **listas paralelas** y **modularización avanzada**:
1. **Evitar Código Redundante (DRY):** Al implementar `ingresar_numero()`, encapsulamos las estructuras `try-except` de captura en una sola subfunción parametrizada. Esto previene escribir capturas repetidas para horas, tarifas y cantidad de personal.
2. **Listas Paralelas:** Para representar un registro complejo de trabajadores sin usar diccionarios o programación orientada a objetos, se poblan de forma síncrona colecciones independientes de igual longitud. La correspondencia se mantiene mediante el **índice de ciclo** (ej: `nombres[i]` corresponde a `horas[i]`).
3. **Control de Extremos Lineal:** En lugar de importar métodos embebidos como `min()` o `max()`, se implementa un algoritmo de recorrido lineal $O(N)$ manual. Este inicializa una variable índice en 0 y recorre secuencialmente la lista actualizando el valor extremo de forma condicionada por un parámetro booleano, resolviendo las dos búsquedas con una sola función.
4. **Presentación Visual Consistente:** Las liquidaciones se tabulan usando formateadores de ancho de columna (`{nombres[i]:<20}`) y formateadores de moneda con separadores de miles y decimales (`:>10,.0f`), logrando un acabado profesional en la consola.

---

#### Explicación Línea por Línea del Código

1.  **`HORAS_BASE = 45`**: Definición de la constante global del límite de horas ordinarias mensuales.
2.  **`RECARGO_EXTRA = 1.5`**: Constante del recargo por horas extras (50% de recargo).
3.  **`def ingresar_numero(mensaje, minimo=0.01):`**: Firma de la función validadora de números flotantes.
4.  **`while True:`**: Bucle infinito que repetirá la petición hasta capturar un dato correcto.
5.  **`try: valor = float(input(mensaje))`**: Intento de captura y conversión a tipo `float`. Si el usuario ingresa caracteres de texto, lanza un `ValueError` y salta al bloque `except`.
6.  **`if valor < minimo: print(...)`**: Restricción matemática para forzar que el valor sea igual o superior al umbral mínimo de seguridad.
7.  **`else: return valor`**: Retorno seguro del número validado, rompiendo automáticamente el bucle infinito.
8.  **`except ValueError:`**: Captura los fallos de conversión de tipo y evita el congelamiento de consola.
9.  **`def ingresar_trabajadores():`**: Firma de la función encargada de leer e incorporar los trabajadores.
10. **`n = int(input(...))`**: Solicita el número entero de personal bajo try-except para asegurar que sea numérico y mayor o igual a 2.
11. **`nombres = []; horas = []; tarifas = []`**: Inicialización de las tres listas colectoras en paralelo.
12. **`for i in range(n):`**: Ciclo indexado que iterará `n` veces.
13. **`nombre = input(...).strip()`**: Captura el nombre removiendo espacios laterales. Se obliga a que el campo no quede en blanco mediante un ciclo `while not nombre`.
14. **`h = ingresar_numero(" Horas del mes : ", 1)`**: Invoca la función auxiliar validando que las horas sean al menos 1.
15. **`t = ingresar_numero(" Tarifa ($/hora) : ", 1)`**: Solicita la tarifa horaria forzando valores válidos.
16. **`nombres.append(nombre); ...`**: Inserta de forma síncrona cada dato al final de su respectiva lista paralela.
17. **`def calcular_pago(horas, tarifa):`**: Firma de la función para el cálculo matemático modular.
18. **`if horas <= HORAS_BASE:`**: Condicional que determina si el trabajador no cumplió horas extras.
19. **`horas_normales = horas; horas_extra = 0`**: Asigna las horas completas a la jornada ordinaria.
20. **`else: horas_normales = HORAS_BASE; horas_extra = horas - HORAS_BASE`**: Topa las horas ordinarias en 45 y asigna el remanente a la jornada extraordinaria.
21. **`pago_base = horas_normales * tarifa`**: Multiplica las horas normales por la tarifa horaria ordinaria.
22. **`pago_extra = horas_extra * tarifa * RECARGO_EXTRA`**: Computa las horas extras aplicando la bonificación del factor 1.5.
23. **`pago_total = pago_base + pago_extra`**: Suma de ambos subtotales.
24. **`return pago_base, pago_extra, pago_total`**: Devuelve los tres cálculos en formato de tupla.
25. **`def encontrar_extremo(nombres, pagos, buscar_maximo):`**: Firma de la función para extremos.
26. **`idx_extremo = 0`**: Asume de forma provisional que el primer trabajador (índice 0) es el extremo de comparación.
27. **`for i in range(1, len(pagos)):`**: Recorre secuencialmente el listado desde el índice 1.
28. **`if buscar_maximo and pagos[i] > pagos[idx_extremo]: idx_extremo = i`**: Si buscamos el mayor y el sueldo evaluado supera al actual, actualiza el índice apuntador.
29. **`if not buscar_maximo and pagos[i] < pagos[idx_extremo]: idx_extremo = i`**: Si buscamos el menor y el sueldo evaluado es inferior, actualiza el índice apuntador.
30. **`return nombres[idx_extremo], pagos[idx_extremo]`**: Retorna los dos campos correspondientes en paralelo tras concluir el ciclo.
31. **`def mostrar_resultados(...)`**: Imprime la planilla, calcula totales usando `sum()` e informa sobre el sueldo más alto y bajo invocando la función modular de extremos.

---

#### Código Completo con Comentarios Docentes

```python
# =====================================================================
# CASO G: CALCULADORA DE PLANILLA DE SUELDOS (T. Programación I)
# =====================================================================

# --- 1. Constantes del programa ---
HORAS_BASE = 45         # Límite ordinario de horas mensuales
RECARGO_EXTRA = 1.5     # Incremento tarifario para horas extras (50% recargo)
SEPARADOR = "=" * 68    # Separador visual estético para consola

# --- 2. Función auxiliar de validación (DRY) ---
def ingresar_numero(mensaje, minimo=0.01):
    """
    Solicita interactivamente un número de punto decimal mayor o igual a 'minimo'.
    Implementa un bucle infinito y control de errores por excepciones.
    """
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo:
                print(f"   [Error] Ingrese un valor mayor o igual a {minimo}.")
            else:
                return valor  # Entrada válida: retorna y finaliza la función
        except ValueError:
            print("   [Error] Ingrese un número válido (use punto decimal).")

# --- 3. Registro interactivo con listas paralelas ---
def ingresar_trabajadores():
    """
    Gestiona la carga de la nómina de trabajadores en memoria.
    Retorna tres listas paralelas: nombres, horas y tarifas.
    """
    while True:
        try:
            n = int(input(" Cantidad de trabajadores (min 2): "))
            if n >= 2:
                break
            print("   [Error] Debe ingresar al menos 2 trabajadores.")
        except ValueError:
            print("   [Error] Ingrese un número entero válido.")

    nombres = []
    horas = []
    tarifas = []

    for i in range(n):
        print(f"\n Trabajador {i+1} de {n}")
        
        # Validación de nombre no vacío
        nombre = input(" Nombre : ").strip()
        while not nombre:
            nombre = input("   [Error] El nombre no puede estar vacío. Nombre : ").strip()
            
        h = ingresar_numero(" Horas del mes : ", 1)
        t = ingresar_numero(" Tarifa ($/hora) : ", 1)

        # Inserción síncrona en listas paralelas
        nombres.append(nombre)
        horas.append(h)
        tarifas.append(t)

    return nombres, horas, tarifas

# --- 4. Cálculo modular de liquidaciones ---
def calcular_pago(horas, tarifa):
    """
    Computa el sueldo base, extra y neto individual de un trabajador.
    Retorna la tupla de liquidación: (pago_base, pago_extra, pago_total)
    """
    if horas <= HORAS_BASE:
        horas_normales = horas
        horas_extra = 0
    else:
        horas_normales = HORAS_BASE
        horas_extra = horas - HORAS_BASE

    pago_base = horas_normales * tarifa
    pago_extra = horas_extra * tarifa * RECARGO_EXTRA
    pago_total = pago_base + pago_extra

    return pago_base, pago_extra, pago_total

# --- 5. Algoritmo lineal de búsqueda de extremos ---
def encontrar_extremo(nombres, pagos, buscar_maximo):
    """
    Busca de forma lineal (complejidad O(N)) el sueldo mayor o menor en la lista.
    Conmutador: buscar_maximo=True para sueldo máximo, False para sueldo mínimo.
    """
    idx_extremo = 0  # Inicialización provisoria en el índice cero
    
    for i in range(1, len(pagos)):
        if buscar_maximo and pagos[i] > pagos[idx_extremo]:
            idx_extremo = i
        if not buscar_maximo and pagos[i] < pagos[idx_extremo]:
            idx_extremo = i
            
    return nombres[idx_extremo], pagos[idx_extremo]

# --- 6. Impresión de Reportes Formateados ---
def mostrar_resultados(nombres, horas, pagos_base, pagos_extra, pagos_totales):
    """
    Imprime de forma alineada por columnas el reporte consolidad de liquidaciones.
    """
    print(f"\n{SEPARADOR}")
    print(" PLANILLA DE SUELDOS MENSUAL")
    print(SEPARADOR)
    
    # Encabezado estructurado con anchos fijos
    print(f" {'NOMBRE':<20} {'H.NORM':>6} {'H.EXT':>6} {'PAGO BASE':>10} {'P.EXTRA':>9} {'TOTAL':>10}")
    print(" " + "-" * 64)

    for i in range(len(nombres)):
        h_norm = min(horas[i], HORAS_BASE)
        h_extra = max(0, horas[i] - HORAS_BASE)
        # Formateo monetario con coma para miles
        print(f" {nombres[i]:<20} {h_norm:>6.0f} {h_extra:>6.0f} "
              f"{pagos_base[i]:>10,.0f} {pagos_extra[i]:>9,.0f} {pagos_totales[i]:>10,.0f}")

    total_planilla = sum(pagos_totales)
    print(f"\n TOTAL PLANILLA : ${total_planilla:,.0f}")

    # Invocación de extremos
    nombre_max, pago_max = encontrar_extremo(nombres, pagos_totales, True)
    nombre_min, pago_min = encontrar_extremo(nombres, pagos_totales, False)

    print(f" Mayor sueldo : {nombre_max} --> ${pago_max:,.0f}")
    print(f" Menor sueldo : {nombre_min} --> ${pago_min:,.0f}")
    print(SEPARADOR)

# --- 7. Orquestador de Flujo Principal ---
def main():
    print(SEPARADOR)
    print(" CALCULADORA DE PLANILLA DE SUELDOS")
    print(SEPARADOR)

    # Paso 1: Lectura paralela
    nombres, horas, tarifas = ingresar_trabajadores()

    # Inicialización de listas colectoras
    pagos_base = []
    pagos_extra = []
    pagos_totales = []

    # Paso 2: Procesamiento secuencial
    for i in range(len(nombres)):
        base, extra, total = calcular_pago(horas[i], tarifas[i])
        pagos_base.append(base)
        pagos_extra.append(extra)
        pagos_totales.append(total)

    # Paso 3: Informe por consola
    mostrar_resultados(nombres, horas, pagos_base, pagos_extra, pagos_totales)

if __name__ == "__main__":
    main()
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Nómina Estándar USS
*   **Entrada de Datos en Consola:**
    ```text
    Cantidad de trabajadores (min 2): 3

    Trabajador 1 de 3
     Nombre : Carlos Soto
     Horas del mes : 50
     Tarifa ($/hora) : 4500

    Trabajador 2 de 3
     Nombre : Ana Pérez
     Horas del mes : 45
     Tarifa ($/hora) : 5200

    Trabajador 3 de 3
     Nombre : Luis Mora
     Horas del mes : 38
     Tarifa ($/hora) : 4800
    ```
*   **Salida de Planilla en Pantalla:**
    ```text
    ====================================================================
     PLANILLA DE SUELDOS MENSUAL
    ====================================================================
     NOMBRE               H.NORM  H.EXT  PAGO BASE  P.EXTRA      TOTAL
     ----------------------------------------------------------------
     Carlos Soto              45      5    202,500   33,750    236,250
     Ana Pérez                45      0    234,000        0    234,000
     Luis Mora                38      0    182,400        0    182,400

     TOTAL PLANILLA : $652,650
     Mayor sueldo : Carlos Soto --> $236,250
     Menor sueldo : Luis Mora --> $182,400
    ====================================================================
    ```
