"""
Ejercicio 1: Parpadeo de LED (Blink)
Asignatura: Taller de Programación I
Plataforma: ESP32 (MicroPython)

Descripción:
Este script hace parpadear un LED conectado al GPIO 2.
El LED se enciende durante 1 segundo y se apaga durante 1 segundo.
"""
import machine
import utime

def setup_led(pin_number):
    """
    Configura el pin especificado como salida digital.
    
    Args:
        pin_number (int): El número de pin GPIO a configurar.
        
    Returns:
        machine.Pin: Objeto Pin configurado como salida.
    """
    # Se inicializa el pin como salida (Pin.OUT)
    return machine.Pin(pin_number, machine.Pin.OUT)

def blink_led(led):
    """
    Ejecuta un ciclo de encendido y apagado del LED.
    Cada estado tiene una duración de 1 segundo.
    
    Args:
        led (machine.Pin): El objeto Pin del LED a controlar.
    """
    led.value(1)       # Enciende el LED (nivel lógico alto)
    utime.sleep(1)     # Mantiene el estado por 1 segundo
    led.value(0)       # Apaga el LED (nivel lógico bajo)
    utime.sleep(1)     # Mantiene el estado por 1 segundo

def main():
    """
    Función principal que orquesta la configuración y el ciclo infinito.
    """
    # Configuración inicial del hardware
    pin_led_integrado = 2
    led = setup_led(pin_led_integrado)
    
    print("Iniciando secuencia de parpadeo (Blink)...")
    
    # Bucle principal del programa
    try:
        while True:
            blink_led(led)
    except KeyboardInterrupt:
        # Manejo de la interrupción del usuario (Ctrl+C en la consola / Thonny IDE)
        led.value(0) # Apagamos el LED por seguridad y evitar consumos parásitos
        print("Ejecución detenida por el usuario.")

# Punto de entrada del script
if __name__ == '__main__':
    main()
