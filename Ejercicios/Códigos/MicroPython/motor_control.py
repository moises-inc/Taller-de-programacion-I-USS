"""
Módulo de Control de Motores DC (Puente H L298N)
Asignatura: Taller de Programación I (USS)
Unidad 3: Microcontroladores y MicroPython

Este script proporciona las funciones básicas para controlar la dirección
y velocidad de dos motores DC en un chasis robótico móvil.
"""

from machine import Pin, PWM
import time

# --- Configuración de Pines del Puente H L298N ---
# Motor Izquierdo
IN1 = Pin(12, Pin.OUT)
IN2 = Pin(13, Pin.OUT)
ENA = PWM(Pin(14))  # Control de velocidad (PWM)

# Motor Derecho
IN3 = Pin(15, Pin.OUT)
IN4 = Pin(16, Pin.OUT)
ENB = PWM(Pin(17))  # Control de velocidad (PWM)

# Configurar frecuencia de PWM (típica para motores: 1000 Hz)
ENA.freq(1000)
ENB.freq(1000)

def establecer_velocidad(velocidad_izq: int, velocidad_der: int):
    """
    Ajusta el ciclo de trabajo de los pines de habilitación (PWM) para controlar la velocidad.
    :param velocidad_izq: Entero de 0 a 100 (porcentaje de velocidad motor izquierdo)
    :param velocidad_der: Entero de 0 a 100 (porcentaje de velocidad motor derecho)
    """
    # Escalar porcentaje (0-100) al rango del ciclo de trabajo de MicroPython (0-65535)
    duty_izq = int((velocidad_izq / 100) * 65535)
    duty_der = int((velocidad_der / 100) * 65535)
    
    ENA.duty_u16(duty_izq)
    ENB.duty_u16(duty_der)

def avanzar(velocidad: int = 60):
    """
    Hace que el robot avance en línea recta a la velocidad especificada.
    """
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    establecer_velocidad(velocidad, velocidad)

def retroceder(velocidad: int = 60):
    """
    Hace que el robot retroceda en línea recta.
    """
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(1)
    establecer_velocidad(velocidad, velocidad)

def girar_izquierda(velocidad: int = 50):
    """
    Gira el robot sobre su propio eje hacia la izquierda (rueda izq atrás, rueda der adelante).
    """
    IN1.value(0)
    IN2.value(1)
    IN3.value(1)
    IN4.value(0)
    establecer_velocidad(velocidad, velocidad)

def girar_derecha(velocidad: int = 50):
    """
    Gira el robot sobre su propio eje hacia la derecha (rueda izq adelante, rueda der atrás).
    """
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    establecer_velocidad(velocidad, velocidad)

def detener():
    """
    Detiene inmediatamente ambos motores.
    """
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    establecer_velocidad(0, 0)

# --- Código de Prueba / Ejemplo de Uso ---
if __name__ == "__main__":
    print("Iniciando prueba de motores...")
    
    print("Avanzando al 60% de velocidad por 2 segundos...")
    avanzar(60)
    time.sleep(2)
    
    print("Girando a la derecha por 1 segundo...")
    girar_derecha(50)
    time.sleep(1)
    
    print("Retrocediendo al 40% de velocidad por 2 segundos...")
    retroceder(40)
    time.sleep(2)
    
    print("Deteniendo motores.")
    detener()
