### Ejercicio 9: Gestión modular y registro de clientes

#### Enunciado del Problema
Diseñar un sistema de información modular interactivo en memoria para administrar la base de datos de clientes de un negocio. Para ello, se deben implementar tres funciones con responsabilidades específicas:
1.  `agregar_cliente(lista_clientes, nombre_cliente)`: Recibe la lista de clientes y un nombre. Inserta el nuevo cliente de forma segura únicamente si el nombre no es una cadena vacía y no existe previamente en el registro para evitar duplicados. Retorna un valor booleano (`True` si se registró con éxito, o `False` si falló la validación).
2.  `mostrar_clientes(lista_clientes)`: Recibe la lista y la presenta de manera estética y numerada por consola, utilizando un orden secuencial amigable para el usuario.
3.  `contar_clientes(lista_clientes)`: Recibe la lista y retorna la cantidad de clientes registrados en total.

El programa principal debe inicializar una lista vacía, guiar al usuario mediante un bucle interactivo controlado por la palabra centinela `"fin"`, sanitizar las entradas de texto eliminando espacios superfluos e informar detalladamente de los aciertos y fallas del sistema.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista_clientes` | `list` | Parámetro de las funciones | Estructura de tipo lista sobre la cual se registran, consultan y leen los clientes. |
| `nombre_cliente` | `str` | Parámetro (de `agregar_cliente`) | Nombre de tipo cadena que se desea añadir a la base de clientes. |
| `idx` | `int` | Variable de control de bucle `for` | Índice entero provisto por la función `enumerate` (inicia en $0$) para indexar la lista. |
| `c` | `str` | Variable de control de bucle `for` | Cadena de texto que representa el nombre del cliente analizado actual en la iteración. |
| `base_clientes` | `list` | Variable local (programa principal) | Lista dinámica inicializada como vacía encargada de hospedar el registro de clientes del negocio. |
| `cli` | `str` | Variable local (programa principal) | Almacena provisionalmente el nombre ingresado por el usuario, libre de espacios adicionales. |
| `agregado` | `bool` | Variable local (programa principal) | Variable lógica que almacena el retorno booleano de la función `agregar_cliente`. |
| `total_clientes` | `int` | Variable local (programa principal) | Almacena la cantidad final de clientes devuelta por la función `contar_clientes`. |

---

#### Lógica de la Solución
Este programa implementa un **CRUD básico (Create, Read) interactivo en memoria** aplicando reglas estrictas de integridad de datos:
1. **Control de Integridad de Datos (Integrity Rules):**
    *   **Prevención de Duplicidad:** La función `agregar_cliente` comprueba mediante `nombre_cliente not in lista_clientes` que el registro sea único.
    *   **Prevención de Registros Vacíos:** Se verifica que el nombre contenga texto real antes de permitir su inserción.
2. **Uso de Enumeradores para Visualización Premium:** En `mostrar_clientes`, en lugar de usar variables contadoras externas para enumerar la salida, se utiliza la función incorporada de Python `enumerate()`. Esta devuelve tuplas conteniendo el índice entero y el elemento en curso, logrando una presentación numerada e indexada en un formato amigable 1-indexed (`idx + 1`).
3. **Manejo de Centinelas e Interactividad:** En el flujo principal, se implementa un bucle interactivo infinito `while True` que finaliza cuando el usuario digita la señal centinela `"fin"` (normalizada con `.lower()` para no distinguir mayúsculas). Se usa el método `.strip()` para sanitizar las entradas de espacios vacíos superfluos a los lados.

---

#### Explicación Línea por Línea

1. **`def agregar_cliente(lista_clientes, nombre_cliente):`**  
   Define la función encargada de realizar la inserción segura de nuevos registros.
2. **`"""Añade un cliente a la lista si no está vacío ni duplicado."""`**  
   Docstring explicativo de la validación preventiva de duplicados.
3. **`if nombre_cliente and nombre_cliente not in lista_clientes:`**  
   Evalúa que la cadena no esté vacía (`nombre_cliente` evalúa como verdadero si contiene caracteres) **y** que no exista de manera previa en la lista (`not in`).
4. **`lista_clientes.append(nombre_cliente)`**  
   Si pasa con éxito la validación condicional doble, inserta la cadena al final de la lista de clientes usando el método dinámico `.append()`.
5. **`return True`**  
   Retorna el valor lógico `True` informando del éxito del registro.
6. **`return False`**  
   En caso de fallar cualquiera de las condiciones (duplicidad o campo vacío), retorna `False` e interrumpe el flujo.
7. **`def mostrar_clientes(lista_clientes):`**  
   Define la función encargada de desplegar visualmente la base de clientes.
8. **`"""Muestra secuencialmente todos los clientes registrados."""`**  
   Docstring explicativo del formato de lectura del listado.
9.  **`print("\n--- Listado Oficial de Clientes ---")`**  
    Imprime un encabezado decorativo en la terminal.
10. **`for idx, c in enumerate(lista_clientes):`**  
    Bucle `for` que recorre linealmente la lista de clientes extrayendo en cada vuelta el índice secuencial en la variable `idx` y el elemento en `c` gracias a `enumerate()`.
11. **`print(f" {idx+1}. {c}")`**  
    Imprime en pantalla la lista numerada usando `idx+1` para presentar un formato 1-indexed.
12. **`def contar_clientes(lista_clientes):`**  
   Define la función `contar_clientes` para cuantificar registros.
13. **`"""Retorna la cantidad total de clientes registrados."""`**  
   Docstring explicativo de la longitud de la colección.
14. **`return len(lista_clientes)`**  
    Retorna la longitud o cantidad total de elementos dentro de la lista utilizando la función estándar `len()`.
15. **`# Programa principal`**  
    Comentario académico que deslinda el inicio del script principal interactivo.
16. **`print("--- Ejercicio 9: Gestión de Clientes ---")`**  
    Imprime por pantalla la cabecera correspondiente al módulo.
17. **`base_clientes = []`**  
    Crea la lista vacía `base_clientes` para simular la base de datos local en memoria.
18. **`print("Ingrese clientes. Escriba 'fin' para finalizar la carga.")`**  
    Imprime las instrucciones indicando la palabra centinela de término.
19. **`while True:`**  
    Inicia un bucle infinito interactivo para solicitar los nombres de los clientes.
20. **`cli = input("Nombre del cliente a registrar: ").strip()`**  
    Captura el nombre del cliente y aplica el método `.strip()` para limpiar la entrada de espacios vacíos redundantes.
21. **`if cli.lower() == "fin":`**  
    Condicional que evalúa si el usuario digitó la palabra centinela de detención (insensible a mayúsculas con `.lower()`).
22. **`break`**  
    Detiene de inmediato el bucle interactivo de carga si el centinela fue activado.
23. **`if not cli:`**  
    Evalúa si el string ingresado quedó completamente vacío tras el `.strip()`.
24. **`print("Error: El nombre del cliente no puede estar en blanco.")`**  
    Muestra un mensaje de advertencia correctivo para el usuario.
25. **`continue`**  
    Sentencia de salto que interrumpe la iteración actual del bucle `while` volviendo al punto de solicitud.
26. **`agregado = agregar_cliente(base_clientes, cli)`**  
    Invoca a la función de inserción y guarda su retorno booleano en la variable `agregado`.
27. **`if agregado:`**  
    Condicional que evalúa si la inserción fue exitosa.
28. **`print(f"-> Cliente '{cli}' añadido exitosamente.")`**  
    Informa al usuario que el cliente ha sido registrado.
29. **`else:`**  
    Rama del condicional si `agregado` es falso.
30. **`print("-> Error: Cliente ya se encuentra registrado.")`**  
    Informa al usuario de la duplicidad detectada impidiendo el registro repetido.
31. **`total_clientes = contar_clientes(base_clientes)`**  
    Llama a la función de cuantificación pasando la lista definitiva y guarda el resultado.
32. **`mostrar_clientes(base_clientes)`**  
    Llama a la función modular encargada de la salida formateada por consola.
33. **`print(f"\nTotal general de clientes registrados: {total_clientes}")`**  
    Muestra al operador comercial el consolidado numérico total de registros en la base.

---

#### Código Completo con Comentarios Pedagógicos

```python
# --- Función 1: Registro Seguro e Inserción Única ---
def agregar_cliente(lista_clientes, nombre_cliente):
    """
    Añade un cliente a la lista si no está vacío ni duplicado.
    Retorna True si la inserción fue exitosa, o False si falló.
    """
    # Verificación de integridad lógica
    if nombre_cliente and nombre_cliente not in lista_clientes:
        lista_clientes.append(nombre_cliente)  # Inserción
        return True
        
    return False  # Rechazado por vacío o duplicado

# --- Función 2: Visualización Indexada y Estética ---
def mostrar_clientes(lista_clientes):
    """
    Recorre la lista utilizando un enumerador e imprime los registros 
    numerados secuencialmente desde el 1.
    """
    print("\n--- Listado Oficial de Clientes ---")
    # enumerate() extrae el índice (0-based) y el valor
    for idx, c in enumerate(lista_clientes):
        print(f" {idx+1}. {c}")  # idx+1 convierte a 1-indexed

# --- Función 3: Conteo Cuantitativo ---
def contar_clientes(lista_clientes):
    """
    Abstrae el cálculo de longitud de la lista de clientes.
    """
    return len(lista_clientes)

# --- Flujo del Programa Principal ---
print("--- Ejercicio 9: Gestión de Clientes ---")

# Inicialización del almacenamiento local
base_clientes = []
print("Ingrese clientes. Escriba 'fin' para finalizar la carga.")

# Bucle interactivo robusto de captura de registros
while True:
    # Captura y sanitización con remoción de espacios innecesarios
    cli = input("Nombre del cliente a registrar: ").strip()
    
    # Comprobación de centinela insensible a mayúsculas/minúsculas
    if cli.lower() == "fin":
        break  # Término de la carga
        
    # Validación de campo vacío
    if not cli:
        print("Error: El nombre del cliente no puede estar en blanco.")
        continue  # Reintento
        
    # Invocación modular de la inserción y análisis del resultado
    agregado = agregar_cliente(base_clientes, cli)
    
    if agregado:
        print(f"-> Cliente '{cli}' añadido exitosamente.")
    else:
        print("-> Error: Cliente ya se encuentra registrado.")

# Cómputo final y despliegue del reporte
total_clientes = contar_clientes(base_clientes)
mostrar_clientes(base_clientes)

print(f"\nTotal general de clientes registrados: {total_clientes}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Registro Exitoso de Clientes
*   **Entrada en Consola:**
    ```text
    Ingrese clientes. Escriba 'fin' para finalizar la carga.
    Nombre del cliente a registrar: Moises Vasquez
    -> Cliente 'Moises Vasquez' añadido exitosamente.
    Nombre del cliente a registrar: Andrea Perez
    -> Cliente 'Andrea Perez' añadido exitosamente.
    Nombre del cliente a registrar: fin
    ```
*   **Salida del Programa:**
    ```text
    --- Listado Oficial de Clientes ---
     1. Moises Vasquez
     2. Andrea Perez

    Total general de clientes registrados: 2
    ```

##### Caso de Uso 2: Intento de Registros Duplicados y Sanitización
*   **Entrada en Consola:**
    ```text
    Ingrese clientes. Escriba 'fin' para finalizar la carga.
    Nombre del cliente a registrar: Moises
    -> Cliente 'Moises' añadido exitosamente.
    Nombre del cliente a registrar: Moises
    -> Error: Cliente ya se encuentra registrado.
    Nombre del cliente a registrar:    Moises   
    -> Error: Cliente ya se encuentra registrado.
    Nombre del cliente a registrar: fin
    ```
    *(Nota: El tercer ingreso limpia los espacios, convirtiéndose en 'Moises', detectando la duplicidad exitosamente).*

##### Caso de Uso 3: Intento de Registros Vacíos
*   **Entrada en Consola:**
    ```text
    Ingrese clientes. Escriba 'fin' para finalizar la carga.
    Nombre del cliente a registrar: 
    Error: El nombre del cliente no puede estar en blanco.
    Nombre del cliente a registrar: Carlos
    -> Cliente 'Carlos' añadido exitosamente.
    Nombre del cliente a registrar: fin
    ```
