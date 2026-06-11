"""
Módulo de Lectura del Sensor de Ultrasonido HC-SR04
Asignatura: Taller de Programación I (USS)
Unidad 3: Microcontroladores y MicroPython

Este script implementa la lógica para medir la distancia a un obstáculo
calculando el tiempo de respuesta de un pulso ultrasónico.
"""

from machine import Pin
import time

# --- Configuración de Pines ---
TRIG = Pin(18, Pin.OUT)
ECHO = Pin(19, Pin.IN)

def inicializar_sensor():
    """
    Asegura que el pin Trigger esté apagado inicialmente.
    """
    TRIG.value(0)
    time.sleep_ms(50)

def obtener_distancia() -> float:
    """
    Envía un pulso de trigger y mide la duración del pulso de echo para calcular la distancia en cm.
    :return: Distancia en centímetros (float). Retorna -1.0 en caso de error o fuera de rango.
    """
    # 1. Asegurar que el trigger está bajo
    TRIG.value(0)
    time.sleep_us(2)
    
    # 2. Generar un pulso de 10 microsegundos en TRIG
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)
    
    # 3. Medir el tiempo de inicio y fin del pulso en ECHO
    # Esperar a que el pin pase a ALTO (inicio del eco)
    limite_tiempo = time.ticks_us()
    while ECHO.value() == 0:
        if time.ticks_diff(time.ticks_us(), limite_tiempo) > 20000: # 20 ms de timeout
            return -1.0
            
    t_inicio = time.ticks_us()
    
    # Esperar a que el pin pase a BAJO (fin del eco)
    limite_tiempo = time.ticks_us()
    while ECHO.value() == 1:
        if time.ticks_diff(time.ticks_us(), limite_tiempo) > 20000: # 20 ms de timeout
            return -1.0
            
    t_fin = time.ticks_us()
    
    # 4. Calcular la duración total del viaje en microsegundos
    duracion = time.ticks_diff(t_fin, t_inicio)
    
    # 5. Calcular la distancia:
    # Velocidad del sonido = 343 m/s o 0.0343 cm/us.
    # Dividimos entre 2 porque la onda va y regresa.
    distancia = (duracion * 0.0343) / 2
    
    # Rango típico de operación del HC-SR04: 2 cm a 400 cm
    if 2.0 <= distancia <= 400.0:
        return round(distancia, 2)
    else:
        return -1.0

# --- Código de Prueba / Ejemplo de Uso ---
if __name__ == "__main__":
    print("Inicializando sensor de ultrasonido...")
    inicializar_sensor()
    
    try:
        while True:
            dist = obtener_distancia()
            if dist != -1.0:
                print(f"Distancia al obstáculo: {dist} cm")
            else:
                print("Fuera de rango o lectura fallida.")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\nMedición finalizada por el usuario.")
