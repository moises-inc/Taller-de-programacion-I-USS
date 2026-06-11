from machine import Pin, PWM
from utime import sleep

# Configuración de pines
led_rojo = Pin(0, Pin.OUT)
led_amarillo = Pin(1, Pin.OUT)
led_verde = Pin(2, Pin.OUT)

# Nuevos componentes: Botón y Buzzer
boton = Pin(3, Pin.IN, Pin.PULL_DOWN)
buzzer = PWM(Pin(4))

def sonar_buzzer(frecuencia, duracion):
    """Función auxiliar para emitir un tono"""
    buzzer.freq(frecuencia)
    buzzer.duty_u16(32768)  # 50% de ciclo de trabajo
    sleep(duracion)
    buzzer.duty_u16(0)

def secuencia_peaton():
    """Ejecuta la secuencia de cambio cuando se presiona el botón"""
    print("\nSolicitud de cruce recibida.")
    
    # 1. Verde -> Amarillo
    print("Estado: AMARILLO")
    led_verde.off()
    led_amarillo.on()
    sonar_buzzer(440, 0.5) # Tono de aviso
    sleep(2)
    
    # 2. Amarillo -> Rojo
    print("Estado: ROJO (Cruce peatonal permitido)")
    led_amarillo.off()
    led_rojo.on()
    
    # Sonido intermitente para peatones
    for i in range(10):
        sonar_buzzer(880, 0.1)
        sleep(0.2)
    
    # 3. Regreso a Verde
    print("Estado: VERDE")
    led_rojo.off()
    led_verde.on()

# Inicio del sistema
print("Iniciando Semáforo Inteligente con Botón...")
led_rojo.off()
led_amarillo.off()
led_verde.on()

while True:
    # El semáforo permanece en verde hasta que se presiona el botón
    if boton.value() == 1:
        secuencia_peaton()
    
    sleep(0.1) # Pequeña pausa para evitar rebotes y saturación del CPU
