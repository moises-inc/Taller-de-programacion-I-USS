"""
Ejercicio 3: Control de LED con Pulsador
Asignatura: Taller de Programación I
Plataforma: ESP32 (MicroPython)

Descripción:
Controla un LED (GPIO 2) usando un pulsador (GPIO 4).
El pulsador se configura con resistencia PULL_UP interna.
El LED se enciende solo cuando se presiona el botón.
"""
import machine
import utime

def setup_components():
    """
    Configura los pines para el LED y el pulsador.
    
    Returns:
        tuple: (Objeto Pin del LED, Objeto Pin del Pulsador)
    """
    # El LED es un actuador, configuramos como salida.
    led = machine.Pin(2, machine.Pin.OUT)
    
    # El pulsador es un sensor/entrada. 
    # Usamos PULL_UP interno para que su estado en reposo sea 1 (HIGH).
    # Al ser presionado conectará a GND, cerrando el circuito y leyendo un 0 (LOW).
    pulsador = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
    
    return led, pulsador

def update_led_state(led, pulsador):
    """
    Lee el estado del pulsador y actualiza el LED en consecuencia.
    
    Args:
        led (machine.Pin): Objeto Pin del actuador (LED).
        pulsador (machine.Pin): Objeto Pin del sensor (pulsador).
    """
    estado_boton = pulsador.value()

    # Lógica Active-Low (Activo en bajo) dictada por la resistencia PULL-UP
    if estado_boton == 0:
        # Si el botón está presionado el pin se va a masa (0) -> Encendemos el LED
        led.value(1)
    else:
        # Si el botón no está presionado, PULL-UP mantiene VCC (1) -> Apagamos el LED
        led.value(0)

def main():
    """
    Función principal que inicializa el hardware y ejecuta el bucle infinito de control.
    """
    led, pulsador = setup_components()

    print("Sistema iniciado correctamente.")
    print("Mantenga presionado el botón (GPIO 4) para encender el LED (GPIO 2).")

    try:
        while True:
            update_led_state(led, pulsador)
            # Retardo de 50ms para evitar saturación del procesador y dar efecto "debounce" (antirrebote básico)
            utime.sleep_ms(50) 
    except KeyboardInterrupt:
        # Procedimiento seguro al interrumpir el programa (Ctrl+C en Thonny)
        led.value(0)
        print("Ejecución detenida por el usuario.")

# Punto de entrada del script
if __name__ == '__main__':
    main()
