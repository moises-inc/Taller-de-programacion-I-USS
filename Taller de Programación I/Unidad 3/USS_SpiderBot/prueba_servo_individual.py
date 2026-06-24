# ============================================================
# USS SPIDERBOT — Prueba de 8 Servomotores (ESP8266)
# Diseñado para probar servos en los pines D0, D1, D2, D4, D5, D6, D7 y D8.
# Ejecutar en Thonny e ingresar los comandos en la consola.
# ============================================================

from machine import Pin, PWM
import time

# Mapeo de pines físicos de la ESP8266 (NodeMCU / WeMos D1 Mini)
# D0 -> GPIO 16, D1 -> GPIO 5, D2 -> GPIO 4, D4 -> GPIO 2
# D5 -> GPIO 14, D6 -> GPIO 12, D7 -> GPIO 13, D8 -> GPIO 15
PINES_ACTIVOS = {
    "D0": 16,
    "D1": 5,
    "D2": 4,
    "D4": 2,
    "D5": 14,
    "D6": 12,
    "D7": 13,
    "D8": 15
}

servos = {}

print("Inicializando canales PWM a 50Hz...")
for nombre, pin_num in PINES_ACTIVOS.items():
    try:
        servos[nombre] = PWM(Pin(pin_num), freq=50)
        print(f"  [OK] Servo {nombre} configurado en GPIO {pin_num}")
    except Exception as e:
        print(f"  [ERROR] No se pudo inicializar {nombre} (GPIO {pin_num}): {e}")

def mover_servo(nombre, angulo):
    """Establece el ángulo (0-180) para un servo específico"""
    if nombre not in servos:
        print(f"[ERROR] El servo {nombre} no está inicializado.")
        return
        
    # Limitar el rango por seguridad
    angulo = max(0, min(180, angulo))
    
    # Rango calibrado de Duty (10-bit en ESP8266: 0-1023)
    min_duty = 30  # ~0.6ms (0 grados)
    max_duty = 130 # ~2.5ms (180 grados)
    
    duty = int(min_duty + (angulo / 180.0) * (max_duty - min_duty))
    servos[nombre].duty(duty)
    print(f"[MOVER] {nombre} -> Ángulo: {angulo}° | Duty: {duty}")

def mover_todos(angulo):
    """Mueve todos los servos configurados al mismo ángulo"""
    print(f"\nMoviendo todos los servos a {angulo}°...")
    for nombre in PINES_ACTIVOS.keys():
        mover_servo(nombre, angulo)

def test_barrido():
    """Realiza un barrido secuencial en todos los servos para prueba rápida"""
    print("\n--- Iniciando barrido automático secuencial ---")
    for nombre in PINES_ACTIVOS.keys():
        print(f"\nProbando canal: {nombre}")
        for ang in [90, 45, 90, 135, 90]:
            mover_servo(nombre, ang)
            time.sleep_ms(400)
    print("\n--- Barrido automático finalizado ---")

def main():
    if not servos:
        print("[ERROR] No hay ningún servo inicializado correctamente.")
        return
        
    print("\n=======================================================")
    print("  Prueba Controladora de 8 Servos - ESP8266 (D0, D1, D2, D4, D5, D6, D7, D8)  ")
    print("=======================================================")
    print("Opciones de comando:")
    print("  1. Escribe un ángulo (0-180) para mover TODOS los servos (ej: 90).")
    print("  2. Escribe '<PIN> <ANGULO>' para mover uno solo (ej: D2 45 o D5 120).")
    print("  3. Escribe 'b' para iniciar un barrido secuencial de prueba.")
    print("  4. Escribe 'salir' para terminar.")
    
    # Centrar todos al iniciar
    mover_todos(90)
    
    while True:
        try:
            entrada = input("\nIngrese comando: ").strip().upper()
            
            if entrada == 'SALIR':
                print("Finalizando prueba de servos.")
                break
            elif entrada == 'B':
                test_barrido()
            elif entrada == '':
                continue
            
            # Intentar procesar comandos del tipo "D2 45"
            elif " " in entrada:
                partes = entrada.split()
                if len(partes) == 2:
                    pin = partes[0]
                    if pin in PINES_ACTIVOS:
                        try:
                            angulo = int(partes[1])
                            if 0 <= angulo <= 180:
                                mover_servo(pin, angulo)
                            else:
                                print("[ALERTA] Ángulo fuera de rango (0-180).")
                        except ValueError:
                            print("[ERROR] El ángulo debe ser un número entero.")
                    else:
                        print(f"[ERROR] Pin no válido. Opciones: {list(PINES_ACTIVOS.keys())}")
                else:
                    print("[ERROR] Formato incorrecto. Use '<PIN> <ANGULO>' (ej: D2 90).")
                    
            # Intentar procesar un ángulo global (ej: 90)
            else:
                try:
                    angulo = int(entrada)
                    if 0 <= angulo <= 180:
                        mover_todos(angulo)
                    else:
                        print("[ALERTA] Ángulo fuera de rango (0-180).")
                except ValueError:
                    print("[ERROR] Comando no reconocido. Escriba un número, '<PIN> <ANGULO>', 'b' o 'salir'.")
                    
        except ValueError:
            print("[ERROR] Entrada no válida.")
        except KeyboardInterrupt:
            print("\nPrueba interrumpida por teclado.")
            break

if __name__ == "__main__":
    main()
