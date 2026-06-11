from machine import Pin
from utime import sleep

# Configuración de pines según la guía (Ejercicio 2)
# Se asume la conexión del Ánodo (+) de cada LED a su respectivo pin y el Cátodo (-) a GND
led_rojo = Pin(23, Pin.OUT)
led_amarillo = Pin(22, Pin.OUT)
led_verde = Pin(21, Pin.OUT)

print("Iniciando secuencia del Semáforo Inteligente...")

while True:
    # 1. VERDE: Encendido por 5 segundos
    led_rojo.off()
    led_amarillo.off()
    led_verde.on()
    print("Estado: VERDE")
    sleep(5)
    
    # 2. AMARILLO: Encendido por 2 segundos
    led_verde.off()
    led_amarillo.on()
    print("Estado: AMARILLO")
    sleep(2)
    
    # 3. ROJO: Encendido por 5 segundos
    led_amarillo.off()
    led_rojo.on()
    print("Estado: ROJO")
    sleep(5)
