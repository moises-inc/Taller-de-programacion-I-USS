### Ejercicio 8: Análisis térmico y límites de seguridad

#### Enunciado del Problema
Escribir un programa modular que analice los registros térmicos de un invernadero para garantizar las condiciones de seguridad biológica de las plantas. Para ello, se deben implementar dos funciones independientes:
1.  `calcular_promedio_temp(lista_temps)`: Recibe la lista de temperaturas y calcula el promedio térmico del día, implementando programación defensiva contra divisiones por cero.
2.  `contar_fuera_rango(lista_temps)`: Recibe la lista de temperaturas y retorna la cantidad de mediciones que quedan fuera de la zona de seguridad. El rango de seguridad térmica está definido inclusivamente entre $10^\circ\text{C}$ y $30^\circ\text{C}$ ($10 \le \text{temperatura} \le 30$). Las mediciones que estén por debajo de $10^\circ\text{C}$ o por encima de $30^\circ\text{C}$ se catalogan como fuera de rango.

El programa principal debe inicializar una lista con las lecturas térmicas del día, invocar las funciones y reportar los datos analizados junto con el conteo de alarmas térmicas.

---

#### Análisis de Variables y Parámetros

| Nombre | Tipo de Dato | Ámbito / Rol | Función en el Código |
| :--- | :--- | :--- | :--- |
| `lista_temps` | `list` | Parámetro de las funciones | Almacena la colección de lecturas térmicas reales enviadas a las funciones de análisis. |
| `suma` | `float` | Variable local (de `calcular_promedio_temp`) | Acumulador flotante para sumar progresivamente las lecturas térmicas. |
| `t` | `float` | Variable de control de ciclo `for` | Representa el valor térmico individual analizado en cada iteración del bucle. |
| `contador` | `int` | Variable local (de `contar_fuera_rango`) | Variable contadora entera que acumula los eventos térmicos fuera de rango. |
| `temps_dia` | `list` | Variable local (programa principal) | Lista declarada de forma estática con diez lecturas térmicas reales para simular el caso de uso. |
| `promedio` | `float` | Variable local (programa principal) | Recibe el valor decimal del promedio térmico devuelto por `calcular_promedio_temp`. |
| `fuera_rango` | `int` | Variable local (programa principal) | Recibe la cantidad de mediciones que generaron anomalías térmicas. |

---

#### Lógica de la Solución
Este programa simula un **sistema lógico de alerta e instrumentalización en invernaderos**:
1. **Separación de Responsabilidades:** La tarea matemática clásica de la media se aísla por completo del análisis de eventos críticos y de la visualización en la terminal.
2. **Defensa contra Errores de División:** La función `calcular_promedio_temp` verifica mediante `len(lista_temps) == 0` si no existen lecturas en la lista. Si es así, retorna `0.0` para evitar el error fatal `ZeroDivisionError` en caso de que ocurra un corte en las comunicaciones del sensor.
3. **Disyunción Lógica en Límites Críticos:** Para auditar cuántas temperaturas se salen del intervalo normal, se utiliza el operador lógico `or` dentro de la función `contar_fuera_rango`. La condición `t < 10 or t > 30` captura de forma precisa anomalías en ambos extremos críticos de la escala térmica (frío extremo o calor sofocante), incrementando la variable contadora ante cualquiera de estos estados.
4. **Visualización y Precisión Decimal:** Muestra las lecturas de los sensores en la terminal e imprime el promedio térmico acotado a una precisión fija de un decimal mediante la sintaxis `:.1f`.

---

#### Explicación Línea por Línea

1. **`def calcular_promedio_temp(lista_temps):`**  
   Define la función clasificadora llamada `calcular_promedio_temp`, la cual requiere un listado térmico para operar.
2. **`"""Calcula la temperatura promedio diaria."""`**  
   Docstring incorporado que documenta el cómputo de la media diaria.
3. **`if len(lista_temps) == 0:`**  
   Evaluación condicional de seguridad para inspeccionar si la lista de lecturas se encuentra vacía.
4. **`return 0.0`**  
   Si el listado está vacío, la función retorna de inmediato `0.0` de forma segura, abortando el resto de las operaciones aritméticas de la función.
5. **`suma = 0.0`**  
   Inicializa la variable local flotante acumuladora `suma` en cero.
6. **`for t in lista_temps:`**  
   Bucle `for` diseñado para iterar secuencialmente a través de cada lectura numérica de la colección `lista_temps`.
7. **`suma += t`**  
   Suma y acumula la lectura térmica actual en la variable local `suma`.
8. **`return float(suma / len(lista_temps))`**  
   Realiza la división entre el acumulado total y el número total de lecturas, forzando su conversión a flotante, y retorna el promedio calculado.
9. **`def contar_fuera_rango(lista_temps):`**  
   Define la firma de la función `contar_fuera_rango` responsable de la auditoría de alarmas de rango de seguridad.
10. **`"""Cuenta cuántas temperaturas registradas salen del rango de 10°C a 30°C."""`**  
    Docstring descriptivo que detalla la lógica de extremos térmicos inseguros.
11. **`contador = 0`**  
    Inicializa en cero la variable local contadora `contador`.
12. **`for t in lista_temps:`**  
    Bucle iterador lineal para analizar individualmente cada medición térmica.
13. **`if t < 10 or t > 30:`**  
    Condición con operador disyuntivo `or`. Evalúa si la temperatura actual está por debajo del límite de frío ($t < 10$) **o** por encima del límite de calor ($t > 30$).
14. **`contador += 1`**  
    Incrementa en uno la cuenta de alarmas térmicas si se cumple cualquiera de las dos condiciones de peligro térmico.
15. **`return contador`**  
    Retorna la cantidad final acumulada de mediciones térmicas inseguras.
16. **`# Programa principal`**  
    Comentario académico que deslinda el inicio del script ejecutable en la terminal.
17. **`print("--- Ejercicio 8: Análisis Térmico ---")`**  
    Imprime en pantalla la cabecera correspondiente al programa.
18. **`temps_dia = [11.5, 9.8, 25.4, 32.1, 8.5, 15.0, 22.3, 29.9, 30.5, 12.0]`**  
    Inicializa la variable `temps_dia` como una lista con diez valores numéricos decimales que representan las temperaturas registradas por el sensor.
19. **`promedio = calcular_promedio_temp(temps_dia)`**  
    Invoca la función de cálculo térmico entregándole el listado de las lecturas y guarda el promedio resultante en `promedio`.
20. **`fuera_rango = contar_fuera_rango(temps_dia)`**  
    Invoca el recuento de anomalías pasándole la muestra diaria y guarda la cuenta de alarmas en la variable `fuera_rango`.
21. **`print(f"Mediciones térmicas: {temps_dia}")`**  
    Presenta en la salida estándar la colección original de datos térmicos.
22. **`print(f"Temperatura promedio: {promedio:.1f}°C")`**  
    Muestra la media aritmética calculada de temperatura formateada a un solo decimal de precisión.
23. **`print(f"Mediciones fuera de rango de seguridad (10°C - 30°C): {fuera_rango}")`**  
    Reporta de manera clara la cantidad total de mediciones que salieron de los límites de seguridad configurados.

---

#### Código Completo con Comentarios Pedagógicos

```python
# --- Función 1: Promedio de Temperatura Seguro ---
def calcular_promedio_temp(lista_temps):
    """
    Calcula el promedio de una lista de temperaturas.
    Previene el error ZeroDivisionError si la lista está vacía.
    """
    if len(lista_temps) == 0:
        return 0.0  # Retorno preventivo seguro
        
    suma = 0.0
    for t in lista_temps:
        suma += t  # Acumulación lineal
        
    return float(suma / len(lista_temps))

# --- Función 2: Recuento de Alarmas de Seguridad ---
def contar_fuera_rango(lista_temps):
    """
    Cuenta cuántas lecturas térmicas quedan fuera de la zona segura [10°C, 30°C].
    Utiliza el operador lógico disyuntivo 'or' para evaluar ambos extremos.
    """
    contador = 0
    for t in lista_temps:
        # Alerta si es muy frío (< 10) O muy caluroso (> 30)
        if t < 10 or t > 30:
            contador += 1  # Incremento por anomalía
            
    return contador

# --- Flujo del Programa Principal ---
print("--- Ejercicio 8: Análisis Térmico ---")

# Registro diario de temperaturas simulado en el invernadero
temps_dia = [11.5, 9.8, 25.4, 32.1, 8.5, 15.0, 22.3, 29.9, 30.5, 12.0]

# Invocación de las funciones de procesamiento matemático
promedio = calcular_promedio_temp(temps_dia)
fuera_rango = contar_fuera_rango(temps_dia)

# Despliegue estructurado del Reporte de Seguridad Climática
print(f"Mediciones térmicas: {temps_dia}")
print(f"Temperatura promedio: {promedio:.1f}°C")
print(f"Mediciones fuera de rango de seguridad (10°C - 30°C): {fuera_rango}")
```

---

#### Casos de Uso de Ejemplo

##### Caso de Uso 1: Ejecución con Datos Estándar del Día
*   **Lecturas de Sensores:** `[11.5, 9.8, 25.4, 32.1, 8.5, 15.0, 22.3, 29.9, 30.5, 12.0]`
*   **Salida del Programa:**
    ```text
    Mediciones térmicas: [11.5, 9.8, 25.4, 32.1, 8.5, 15.0, 22.3, 29.9, 30.5, 12.0]
    Temperatura promedio: 19.7°C
    Mediciones fuera de rango de seguridad (10°C - 30°C): 4
    ```
    *(Nota: Las 4 mediciones anómalas fuera del rango de 10 a 30 son 9.8, 32.1, 8.5 y 30.5).*

##### Caso de Uso 2: Día Estable (Todas las mediciones seguras)
*   **Lecturas modificadas:** `[12.0, 15.5, 20.0, 22.3, 25.0, 28.9, 29.0, 18.2]`
*   **Salida del Programa:**
    ```text
    Mediciones térmicas: [12.0, 15.5, 20.0, 22.3, 25.0, 28.9, 29.0, 18.2]
    Temperatura promedio: 21.4°C
    Mediciones fuera de rango de seguridad (10°C - 30°C): 0
    ```

##### Caso de Uso 3: Sensor sin datos (Falla de red)
*   **Lecturas modificadas:** `[]`
*   **Salida del Programa:**
    ```text
    Mediciones térmicas: []
    Temperatura promedio: 0.0°C
    Mediciones fuera de rango de seguridad (10°C - 30°C): 0
    ```
