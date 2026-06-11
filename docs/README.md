---
title: Code Wiki - MicroPython ESP32 Projects
date: 2026-06-11
tags:
  - micropython
  - esp32
  - documentation
  - workshop
aliases:
  - Wiki Index
  - Project Documentation
---

# Code Wiki: MicroPython ESP32 Projects (Taller de Programación I)

> [!info] Resumen Ejecutivo
> Este repositorio contiene los scripts desarrollados para la asignatura **Taller de Programación I** (Universidad San Sebastián), correspondientes a la **Solemne 3**. Los códigos están escritos en **MicroPython** para la plataforma **ESP32** y cubren ejercicios progresivos de control de GPIO, sensores ultrasónicos, control de motores DC y semáforos inteligentes.

---

## 🛠 Stack Tecnológico

| Categoría | Tecnología / Librería | Versión / Detalle |
|-----------|----------------------|-------------------|
| **Lenguaje** | MicroPython | Optimizado para ESP32 |
| **Plataforma** | Espressif ESP32 | ESP32 DevKit V1 / WROOM-32 |
| **IDE** | Thonny IDE | MicroPython plugin |
| **Librerías Core** | `machine`, `utime`/`time` | Estándar MicroPython |
| **Hardware** | LEDs, Pulsadores, HC-SR04, L298N, Buzzer | Ver [MODULES.md](MODULES.md#configuraci%C3%B3n-de-pines) |

---

## 📂 Tabla de Contenidos

| Documento | Descripción |
|-----------|-------------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Vista global de arquitectura, diagramas de flujo y patrones de diseño |
| [MODULES.md](MODULES.md) | Diccionario detallado de módulos, funciones y dependencias |

---

## 🚀 Ejercicios Implementados

| # | Script | Descripción | Pines Principales |
|---|--------|-------------|-------------------|
| 1 | `ejercicio1_led.py` | Parpadeo básico de LED (Blink) | GPIO 2 |
| 2 | `Ejercicio 2.py` | Semáforo inteligente con botón y buzzer | GPIO 0-4 |
| 3 | `ejercicio3_pulsador.py` | Control de LED con pulsador (PULL_UP) | GPIO 2, 4 |
| 4 | `semaforo_inteligente.py` | Secuencia semáforo temporizada (3 LEDs) | GPIO 21, 22, 23 |
| 5 | `alarma_ultrasonica.py` | Alarma por proximidad (HC-SR04 + LED + Buzzer) | GPIO 2, 5, 15, 18 |
| 6 | `sonar_sensor.py` | Módulo reutilizable de lectura HC-SR04 | GPIO 18, 19 |
| 7 | `motor_control.py` | Control motores DC con puente H L298N + PWM | GPIO 12-17 |

---

## 📋 Patrones de Diseño Identificados

- **Modularidad**: Separación de configuración, lógica y bucle principal
- **Inicialización Segura**: Estados por defecto `OFF`/`LOW` al arranque
- **Manejo de Interrupciones**: `try/except KeyboardInterrupt` para apagado limpio
- **Debounce por Software**: `sleep_ms(50)` en lecturas de entrada digital
- **Funciones Puras**: Lógica de negocio separada de I/O hardware

---

## 🔗 Enlaces Rápidos

- [Ver Arquitectura](ARCHITECTURE.md)
- [Ver Módulos](MODULES.md)
- [Task Board](_Agent_Sync/Task_Board)
- [Active Context](_Agent_Sync/Active_Context)

---

🔗 [[_Agent_Sync/Task_Board]]
🔗 [[_Agent_Sync/Active_Context]]