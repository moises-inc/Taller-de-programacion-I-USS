### Ejercicio 6: Control de asistencia de trabajadores en faena minera

#### Enunciado del Problema
En una faena minera del norte de Chile, se necesita registrar la asistencia diaria de los trabajadores para efectos de control operativo.
Desarrolla un script en Python que permita gestionar esta información. El programa debe:
- Registrar trabajadores usando un diccionario, donde:
    + Clave = nombre del trabajador.
    + Valor = estado de asistencia ("presente" o "ausente").
- Permitir ingresar trabajadores de forma repetitiva hasta que el usuario escriba "fin".
- Validar que el estado ingresado sea solo "presente" o "ausente".

Al finalizar, el programa debe mostrar:
- Cantidad total de trabajadores registrados.
- Cantidad de trabajadores presentes.
- Cantidad de trabajadores ausentes.
- Lista de trabajadores ausentes.

Consideraciones:
- Usar un ciclo de duración desconocida (`while`) para el ingreso de datos.
- Usar un `for` para recorrer el diccionario y hacer los conteos.
- Separar claramente la etapa de registro y la etapa de análisis.

---

#### Análisis de Variables y Parámetros

| Variable/Parámetro | Tipo de Dato | Función |
| :--- | :--- | :--- |
| `registro_asistencia`| `dict` | Almacena a los trabajadores como clave (`str`) y su estado como valor (`str`). |
| `nombre` | `str` | Nombre del trabajador ingresado en consola (se valida que no esté vacío). |
| `estado` | `str` | Estado de asistencia del trabajador ("presente" o "ausente"), validado y normalizado. |
| `total_trabajadores` | `int` | Frecuencia total de trabajadores registrados en la base de datos (con `len()`). |
| `presentes` | `int` | Contador de personal activo que marcó asistencia como "presente". |
| `ausentes` | `int` | Contador de personal inactivo que marcó asistencia como "ausente". |
| `lista_ausentes` | `list (str)` | Contenedor dinámico que almacena los nombres de los trabajadores inactivos. |
| `trabajador` | `str` | Variable de iteración que almacena el nombre del trabajador en `registro_asistencia.items()`. |

---

#### Lógica de la Solución
1. **Estructura de Datos Indexable (Diccionario):** Se utiliza un diccionario `registro_asistencia = {}` para modelar de forma única las llaves de acceso (nombres de los trabajadores) y su respectiva propiedad (estado de asistencia), lo cual previene que un mismo trabajador sea ingresado dos veces con estados distintos (el segundo ingreso sobreescribiría al primero de forma nativa).
2. **Carga Robusta y Limpieza de Cadenas:** Se aplica la limpieza `.strip()` para evitar guardar nombres conformados únicamente por espacios. Asimismo, se implementa una validación anidada mediante el operador `in ["presente", "ausente"]` para blindar la entrada del estado del trabajador.
3. **Separación de Etapas:** El script segmenta explícitamente el código en dos fases:
   - **Fase de Registro:** Un bucle `while` infinito que captura datos de entrada hasta que se introduce el centinela `"fin"`.
   - **Fase de Análisis:** Un recorrido lineal e interactivo mediante `for ... in ...items()` para categorizar las métricas y compilar la nómina física de ausentes en un contenedor `list`.
4. **Presentación Premium:** En la etapa final de resultados, se genera una salida condicionada que despliega la lista formateada con comas mediante el uso de `', '.join()` o bien emite una felicitación en caso de asistencia perfecta.

---

#### Explicación Línea por Línea
- **Línea 4:** `registro_asistencia = {}`: Inicializa el diccionario de control operacional.
- **Línea 7:** `while True:`: Inicia el ciclo indefinido para la carga de operarios.
- **Línea 8:** `nombre = input(...).strip()`: Captura y limpia el nombre del trabajador de espacios en blanco al inicio y al final.
- **Líneas 9 y 10:** `if nombre.lower() == "fin":`: Evalúa de forma tolerante a mayúsculas si se ha ingresado el centinela para romper el bucle con `break`.
- **Líneas 11 y 12:** `if not nombre:`: Cláusula de seguridad para denegar el registro si la entrada está en blanco.
- **Línea 14:** `while True:`: Inicia el ciclo de validación de estado por operario.
- **Línea 15:** `estado = input(...).strip().lower()`: Captura, limpia y homologa a minúsculas la asistencia ("presente"/"ausente").
- **Líneas 16 a 18:** `if estado in ["presente", "ausente"]:`: Valida si la entrada pertenece al conjunto permitido. De ser así, guarda el registro en el diccionario `registro_asistencia[nombre] = estado` y rompe el ciclo validador interno.
- **Línea 20:** `else:`: Bloque que se ejecuta si la entrada no coincide con los estados estandarizados.
- **Línea 23:** `total_trabajadores = len(registro_asistencia)`: Mide el tamaño del diccionario para obtener el universo del personal.
- **Líneas 24 a 26:** `presentes = 0`, `ausentes = 0` y `lista_ausentes = []`: Inicializan los acumuladores estadísticos manuales y la lista de ausencias.
- **Línea 28:** `for trabajador, estado in registro_asistencia.items():`: Recorre en paralelo las llaves y valores almacenados en la colección de asistencia diaria.
- **Líneas 29 a 30:** `if estado == "presente":`: Condición que evalúa si el operario se encuentra presente e incrementa el contador.
- **Líneas 31 a 33:** `else:`: Se activa si el estado es ausente. Incrementa el respectivo contador de inactividad y anexa el nombre a `lista_ausentes`.
- **Líneas 36 a 39:** `print(...)`: Formatea e imprime los totales de trabajadores, presentes y ausentes en la terminal.
- **Líneas 40 a 43:** `if-else`: Si existen ausentes, une los elementos de la lista en una cadena elegante separada por comas usando `', '.join(lista_ausentes)`. De lo contrario, emite un aviso destacado de asistencia perfecta del 100%.

---

#### Código Completo

```python
# ==============================================================================
# ALGORITMO: Control de Asistencia Operativa de Faena (Diccionario y Nómina)
# ==============================================================================

print("--- Control de Asistencia - Faena Minera ---")

# Diccionario para almacenar el estado de la plantilla de operarios
registro_asistencia = {}

# ETAPA 1: Registro y Carga de Personal (Ciclo Indefinido)
while True:
    nombre = input("Ingrese nombre del trabajador (o 'fin' para terminar): ").strip()
    
    # Condición de salida
    if nombre.lower() == "fin":
        break
        
    # Validar entrada vacía
    if not nombre:
        print("El nombre es obligatorio.")
        continue
        
    # Validación robusta del estado de asistencia por trabajador
    while True:
        estado = input(f"Ingrese estado de asistencia para {nombre} (presente/ausente): ").strip().lower()
        if estado in ["presente", "ausente"]:
            registro_asistencia[nombre] = estado
            break
        else:
            print("Estado inválido. Debe ingresar estrictamente 'presente' o 'ausente'.")
            
# ETAPA 2: Análisis Estadístico (Recorrido manual del Diccionario)
total_trabajadores = len(registro_asistencia)
presentes = 0
ausentes = 0
lista_ausentes = []

for trabajador, estado in registro_asistencia.items():
    if estado == "presente":
        presentes += 1
    else:
        ausentes += 1
        lista_ausentes.append(trabajador)

# Presentación formal del Reporte Operativo de Faena
print("\n--- Reporte de Operaciones de Faena ---")
print(f"Total de personal registrado hoy: {total_trabajadores}")
print(f"Personal Activo (Presentes)     : {presentes}")
print(f"Personal Inactivo (Ausentes)    : {ausentes}")

# Mostrar de forma elegante la nómina de trabajadores ausentes
if lista_ausentes:
    # Capitalizar los nombres al mostrar el listado
    ausentes_formateados = [nom.capitalize() for nom in lista_ausentes]
    print(f"Nómina de trabajadores ausentes : {', '.join(ausentes_formateados)}")
else:
    print("¡Excelente! Asistencia perfecta (100% de personal presente).")
```

---

#### Casos de Uso de Ejemplo

##### Caso 1: Asistencia Perfecta
```text
--- Control de Asistencia - Faena Minera ---
Ingrese nombre del trabajador (o 'fin' para terminar): moises
Ingrese estado de asistencia para moises (presente/ausente): presente
Ingrese nombre del trabajador (o 'fin' para terminar): andrea
Ingrese estado de asistencia para andrea (presente/ausente): presente
Ingrese nombre del trabajador (o 'fin' para terminar): fin

--- Reporte de Operaciones de Faena ---
Total de personal registrado hoy: 2
Personal Activo (Presentes)     : 2
Personal Inactivo (Ausentes)    : 0
¡Excelente! Asistencia perfecta (100% de personal presente).
```

##### Caso 2: Registro con Ausencias y Validación de Entrada
```text
--- Control de Asistencia - Faena Minera ---
Ingrese nombre del trabajador (o 'fin' para terminar): juan
Ingrese estado de asistencia para juan (presente/ausente): tal vez
Estado inválido. Debe ingresar estrictamente 'presente' o 'ausente'.
Ingrese estado de asistencia para juan (presente/ausente): ausente
Ingrese nombre del trabajador (o 'fin' para terminar): pedro
Ingrese estado de asistencia para pedro (presente/ausente): presente
Ingrese nombre del trabajador (o 'fin' para terminar): maria
Ingrese estado de asistencia para maria (presente/ausente): ausente
Ingrese nombre del trabajador (o 'fin' para terminar): fin

--- Reporte de Operaciones de Faena ---
Total de personal registrado hoy: 3
Personal Activo (Presentes)     : 1
Personal Inactivo (Ausentes)    : 2
Nómina de trabajadores ausentes : Juan, Maria
```
