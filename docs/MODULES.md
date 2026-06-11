---
title: Modules - MicroPython ESP32 Projects
date: 2026-06-11
tags:
  - modules
  - micropython
  - esp32
aliases:
  - Component Dictionary
  - Code API Reference
---

# Diccionario de Componentes (Módulos)

> [!info] Estructura de Módulos
> El repositorio se organiza en dos directorios con el mismo código fuente:
> - `/Códigos/`: Directorio principal de entrega.
> - `/Ejercicios/Códigos/MicroPython/`: Directorio de trabajo / desarrollo.
> 
> A continuación se detallan los módulos clave y sus componentes.

---

## 1. `ejercicio1_led.py` (Parpadeo de LED)

Este script hace parpadear un LED de forma periódica con intervalos de 1 segundo. Es el clásico "Hello World" de sistemas embebidos.

### Funciones Principales

#### `setup_led(pin_number)`
- **Propósito**: Configura el pin especificado como salida digital.
- **Parámetros**:
  - `pin_number (int)`: Número del pin GPIO.
- **Retorno**: `machine.Pin` objeto configurado como `Pin.OUT`.
- **Dependencias**: `machine.Pin`

#### `blink_led(led)`
- **Propósito**: Ejecuta un ciclo completo de encendido/apagado con retardo de 1 segundo por estado.
- **Parámetros**:
  - `led (machine.Pin)`: Objeto Pin que controla el LED.
- **Dependencias**: `utime.sleep`

#### `main()`
- **Propósito**: Orquesta la inicialización y ejecuta el bucle de control infinito. Soporta salida limpia mediante interrupción por teclado.
- **Dependencias**: `setup_led`, `blink_led`

---

## 2. `ejercicio3_pulsador.py` (Control de LED con Pulsador)

Controla un LED (GPIO 2) en función de un botón/pulsador conectado a un pin configurado con `PULL_UP` interno (GPIO 4).

### Lógica de Control (Active-Low)
El pin del botón tiene `PULL_UP` habilitado. Esto significa que cuando el botón **no está presionado**, el pin lee `1` (VCC). Cuando **se presiona**, el circuito se cierra a masa y lee `0` (GND). El LED se enciende al leer un `0`.

### Funciones Principales

#### `setup_components()`
- **Propósito**: Configura el Pin 2 como salida (LED) y el Pin 4 como entrada con resistencia Pull-Up interna (Pulsador).
- **Retorno**: `(machine.Pin, machine.Pin)` tuple de objetos configurados.
- **Dependencias**: `machine.Pin`

#### `update_led_state(led, pulsador)`
- **Propósito**: Realiza la lectura del pulsador y actualiza el estado del LED aplicando la lógica Active-Low.
- **Parámetros**:
  - `led (machine.Pin)`: Pin del LED.
  - `pulsador (machine.Pin)`: Pin del Pulsador.
- **Dependencias**: `machine.Pin.value`

#### `main()`
- **Propósito**: Inicializa los componentes y ejecuta el bucle continuo con un retardo de `50ms` para amortiguar el efecto rebote (debounce).
- **Dependencias**: `setup_components`, `update_led_state`, `utime.sleep_ms`

---

## 3. `semaforo_inteligente.py` (Secuencia Semáforo de 3 Vías)

Implementa un semáforo básico de tres luces (Rojo, Amarillo, Verde) con cambio de estado secuencial temporizado.

### Secuencia del Ciclo
1. **Verde**: Encendido por 5 segundos.
2. **Amarillo**: Encendido por 2 segundos.
3. **Rojo**: Encendido por 5 segundos.

### Pines Utilizados
- **Verde**: GPIO 21
- **Amarillo**: GPIO 22
- **Rojo**: GPIO 23

### Detalle del Bucle
El programa no utiliza funciones; corre directamente la lógica secuencial dentro de un `while True:` infinito utilizando la función estándar `utime.sleep` para la temporización.

---

## 4. `Ejercicio 2.py` (Semáforo Inteligente con Botón y Buzzer)

Evolución del semáforo temporizado. Permite la interrupción de la fase verde mediante la activación de un botón de solicitud de cruce peatonal (GPIO 3, configurado en `PULL_DOWN`). Al presionarse, ejecuta una secuencia de cruce acompañada de tonos intermitentes por un Buzzer (GPIO 4).

### Funciones Principales

#### `sonar_buzzer(frecuencia, duracion)`
- **Propósito**: Emite un tono sonoro con la frecuencia especificada y lo detiene tras transcurrir la duración indicada.
- **Parámetros**:
  - `frecuencia (int)`: Frecuencia en Hz.
  - `duracion (float)`: Tiempo en segundos que durará el tono.
- **Dependencias**: `machine.PWM`, `utime.sleep`

#### `secuencia_peaton()`
- **Propósito**: Ejecuta la secuencia ordenada de transición vial cuando se recibe la señal de cruce:
  - Cambia Verde a Amarillo con tono de aviso largo.
  - Cambia Amarillo a Rojo (Cruce permitido) y emite un sonido intermitente rápido (10 iteraciones de tonos agudos).
  - Regresa el semáforo al estado Verde original.
- **Dependencias**: `sonar_buzzer`, `machine.Pin.off`, `machine.Pin.on`, `utime.sleep`

---

## 5. `alarma_ultrasonica.py` (Alarma por Proximidad)

Monitorea la distancia a objetos cercanos usando el sensor ultrasónico HC-SR04. Si detecta un objeto dentro del umbral crítico (<= 20 cm), activa una alarma lumínica (LED Rojo, GPIO 2) y una sonora (Buzzer, GPIO 15).

### Pines Utilizados
- **TRIG (Trigger)**: GPIO 5 (Salida)
- **ECHO**: GPIO 18 (Entrada)
- **LED Alarma**: GPIO 2 (Salida)
- **Buzzer**: GPIO 15 (Salida)

### Funciones Principales

#### `medir_distancia()`
- **Propósito**: Controla el disparo ultrasónico y calcula el tiempo de retorno de la onda reflejada.
- **Fórmula de distancia**: $d = \frac{t \times 0.0343}{2} \approx \frac{t}{58}$ (en cm, donde $t$ es el tiempo de ida y vuelta en microsegundos).
- **Control de Error**: Utiliza `time_pulse_us` con un timeout de 30,000 µs (~5 metros de alcance máximo). Si expira el tiempo o falla, retorna `-1`.
- **Retorno**: `float` con la distancia medida o `-1` si hay error.
- **Dependencias**: `machine.Pin`, `machine.time_pulse_us`, `utime.sleep_us`

---

## 6. `sonar_sensor.py` (Módulo de Medición HC-SR04)

Módulo reutilizable y optimizado para la lectura del sensor ultrasónico HC-SR04. A diferencia de `alarma_ultrasonica.py`, implementa un algoritmo manual de polling temporal mediante `time.ticks_us()` y calcula la distancia con mayor precisión decimal.

### Pines Utilizados
- **TRIG**: GPIO 18 (Salida)
- **ECHO**: GPIO 19 (Entrada)

### Funciones Principales

#### `inicializar_sensor()`
- **Propósito**: Asegura el estado apagado del Trigger y da una pequeña ventana de asentamiento (50ms).
- **Dependencias**: `machine.Pin`, `time.sleep_ms`

#### `obtener_distancia()`
- **Propósito**: Dispara un pulso ultrasónico de 10 microsegundos y calcula el tiempo de vuelo de la señal utilizando `time.ticks_us` y `time.ticks_diff`.
- **Características**:
  - Cuenta con un timeout de seguridad de 20ms para evitar bucles infinitos en caso de desconexión del pin Echo.
  - Valida el rango operacional físico del transductor (2 cm a 400 cm).
- **Retorno**: `float` con la distancia redondeada a dos decimales o `-1.0` en caso de error.
- **Dependencias**: `machine.Pin`, `time.ticks_us`, `time.ticks_diff`

---

## 7. `motor_control.py` (Controlador de Motores Puente H L298N)

Proporciona la biblioteca de comandos básicos para el control de tracción diferencial en un robot móvil de dos ruedas (chasis 2WD). Controla dirección con señales digitales y velocidad con modulación por ancho de pulsos (PWM) a una frecuencia fija de 1000 Hz.

### Configuración del Puente H
- **Motor Izquierdo**: `IN1` (GPIO 12), `IN2` (GPIO 13), `ENA` (GPIO 14, PWM)
- **Motor Derecho**: `IN3` (GPIO 15), `IN4` (GPIO 16), `ENB` (GPIO 17, PWM)

### Funciones Principales

#### `establecer_velocidad(velocidad_izq, velocidad_der)`
- **Propósito**: Escala y aplica el porcentaje de velocidad (0% - 100%) al ciclo de trabajo de MicroPython (0 - 65535).
- **Parámetros**:
  - `velocidad_izq (int)`: Porcentaje (0 a 100) para motor izquierdo.
  - `velocidad_der (int)`: Porcentaje (0 a 100) para motor derecho.
- **Dependencias**: `machine.PWM.duty_u16`

#### `avanzar(velocidad=60)`
- **Propósito**: Hace rodar ambas ruedas en sentido horario estableciendo la velocidad especificada.

#### `retroceder(velocidad=60)`
- **Propósito**: Invierte el giro de ambas ruedas para retroceder.

#### `girar_izquierda(velocidad=50)` / `girar_derecha(velocidad=50)`
- **Propósito**: Invierte el sentido de giro de un motor con respecto al otro para lograr un giro rápido sobre su propio eje.

#### `detener()`
- **Propósito**: Detiene ambos motores de inmediato apagando las entradas digitales y estableciendo el ciclo PWM a `0`.

---

🔗 [[_Agent_Sync/Task_Board]]
🔗 [[_Agent_Sync/Active_Context]]