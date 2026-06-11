from machine import Pin, time_pulse_us
from utime import sleep_us, sleep_ms

# Configuración de pines según la guía (Ejercicio 4)
trigger = Pin(5, Pin.OUT)     # Pin TRIG del sensor ultrasónico
echo = Pin(18, Pin.IN)        # Pin ECHO del sensor ultrasónico
led_rojo = Pin(2, Pin.OUT)    # LED de alarma
buzzer = Pin(15, Pin.OUT)     # Buzzer de alarma

# Estado inicial: salidas apagadas
trigger.off()
led_rojo.off()
buzzer.off()

def medir_distancia():
    """Envía un pulso ultrasónico y calcula la distancia en centímetros."""
    # 1. Asegurar que el trigger está en bajo
    trigger.off()
    sleep_us(2)
    
    # 2. Enviar pulso de 10 microsegundos por el TRIG
    trigger.on()
    sleep_us(10)
    trigger.off()
    
    # 3. Medir cuánto tiempo el pin ECHO se mantiene en ALTO (en microsegundos)
    # Se añade un timeout de 30000 us (~5 metros máximo)
    duracion_us = time_pulse_us(echo, 1, 30000)
    
    if duracion_us < 0:
        return -1 # Retorna -1 si hubo un error o está fuera de rango
        
    # 4. Fórmula para calcular la distancia en cm: tiempo (us) / 58
    distancia_cm = duracion_us / 58
    return distancia_cm

print("Iniciando Sistema de Alarma...")

while True:
    distancia = medir_distancia()
    
    if distancia != -1:
        print("Distancia detectada: {:.1f} cm".format(distancia))
        
        # 5. Lógica de decisión
        if distancia <= 20:
            # Objeto detectado a 20 cm o menos: Activar Alarma
            led_rojo.on()
            buzzer.on()
        else:
            # Zona segura: Apagar Alarma
            led_rojo.off()
            buzzer.off()
    else:
        print("Lectura fuera de rango.")
        
    # Espera antes de la siguiente medición para evitar colisión de ecos
    sleep_ms(200)
