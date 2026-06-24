# ============================================================
# USS SPIDERBOT — Script de Prueba de Servomotores (ESP32 / ESP8266)
# Diseñado para ejecutarse interactiva o automáticamente en Thonny IDE.
# ============================================================

from machine import I2C, Pin, PWM
import time
import sys

# Mapeo descriptivo de canales y nombres
NOMBRES_SERVOS = {
    0: "Canal 0 (Pata FR - Coxa/Cadera)",
    1: "Canal 1 (Pata FR - Fémur/Rodilla)",
    2: "Canal 2 (Pata FL - Coxa/Cadera)",
    3: "Canal 3 (Pata FL - Fémur/Rodilla)",
    4: "Canal 4 (Pata RL - Coxa/Cadera)",
    5: "Canal 5 (Pata RL - Fémur/Rodilla)",
    6: "Canal 6 (Pata RR - Coxa/Cadera)",
    7: "Canal 7 (Pata RR - Fémur/Rodilla)"
}

# Auto-detectar plataforma para asignar pines directos seguros
es_esp8266 = sys.platform == "esp8266"

# Forzar modo de control directo por GPIO (sin buscar la controladora PCA9685 I2C)
# Útil si tienes los servos conectados directamente a D1/D2 y no quieres usar I2C.
FORZAR_GPIO_DIRECTO = True

if es_esp8266:
    # Mapeo de los 8 servos directamente a los pines físicos indicados:
    # D0 -> GPIO16, D1 -> GPIO5, D2 -> GPIO4, D4 -> GPIO2
    # D5 -> GPIO14, D6 -> GPIO12, D7 -> GPIO13, D8 -> GPIO15
    PINE_GPIO_DIRECTOS = {
        0: 16, 1: 5,  # D0, D1 (Pata FR - Coxa y Fémur)
        2: 4,  3: 2,  # D2, D4 (Pata FL - Coxa y Fémur)
        4: 14, 5: 12, # D5, D6 (Pata RL - Coxa y Fémur)
        6: 13, 7: 15  # D7, D8 (Pata RR - Coxa y Fémur)
    }
else:
    PINE_GPIO_DIRECTOS = {
        0: 13, 1: 12, # Pata FR
        2: 15, 3: 2,  # Pata FL
        4: 4,  5: 5,  # Pata RL
        6: 23, 7: 25  # Pata RR
    }

# Clase mínima para PCA9685
class PCA9685Driver:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.i2c.writeto_mem(self.address, 0x00, bytes([0x00])) # MODE1 normal
        self.set_pwm_freq(50)
        
    def set_pwm_freq(self, freq):
        prescaleval = 25000000.0 / 4096.0 / float(freq) - 1.0
        prescale = int(prescaleval + 0.5)
        oldmode = self.i2c.readfrom_mem(self.address, 0x00, 1)[0]
        newmode = (oldmode & 0x7F) | 0x10
        self.i2c.writeto_mem(self.address, 0x00, bytes([newmode]))
        self.i2c.writeto_mem(self.address, 0xFE, bytes([prescale]))
        self.i2c.writeto_mem(self.address, 0x00, bytes([oldmode]))
        time.sleep_us(500)
        self.i2c.writeto_mem(self.address, 0x00, bytes([oldmode | 0xa1]))
        
    def set_pwm(self, channel, on, off):
        self.i2c.writeto_mem(self.address, 0x06 + 4 * channel, bytes([on & 0xFF]))
        self.i2c.writeto_mem(self.address, 0x07 + 4 * channel, bytes([(on >> 8) & 0xFF]))
        self.i2c.writeto_mem(self.address, 0x08 + 4 * channel, bytes([off & 0xFF]))
        self.i2c.writeto_mem(self.address, 0x09 + 4 * channel, bytes([(off >> 8) & 0xFF]))

    def set_angle(self, channel, angle):
        angle = max(0, min(180, angle))
        min_pulse = 130  # ~0.6ms
        max_pulse = 530  # ~2.6ms
        off_tick = int(min_pulse + (angle / 180.0) * (max_pulse - min_pulse))
        self.set_pwm(channel, 0, off_tick)

# Clase mínima para GPIO Directo
class GPIOServoDriver:
    def __init__(self, pins):
        self.pwms = {}
        for ch, pin_num in pins.items():
            try:
                self.pwms[ch] = PWM(Pin(pin_num), freq=50)
            except Exception as e:
                print(f"[ERROR] No se pudo inicializar PWM en GPIO {pin_num}: {e}")
                
    def set_angle(self, channel, angle):
        if channel in self.pwms:
            angle = max(0, min(180, angle))
            if es_esp8266:
                # El PWM del ESP8266 en MicroPython usa rango 0-1023 (10-bit)
                min_duty = 30   # ~0.6ms (30/1023)
                max_duty = 130  # ~2.5ms (130/1023)
                duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
                self.pwms[channel].duty(duty)
            else:
                # ESP32 usa rango 0-65535 (16-bit)
                min_duty = 1638  # ~0.5ms (1638/65535)
                max_duty = 8192  # ~2.5ms (8192/65535)
                duty = int(min_duty + (angle / 180.0) * (max_duty - min_duty))
                self.pwms[channel].duty_u16(duty)

def realizar_barrido(driver, canal, nombre):
    print(f"\n---> Iniciando barrido en: {nombre}")
    print("Moviendo a 90 grados (Centro)...")
    driver.set_angle(canal, 90)
    time.sleep_ms(800)
    
    print("Moviendo a 45 grados...")
    driver.set_angle(canal, 45)
    time.sleep_ms(800)
    
    print("Moviendo a 135 grados...")
    driver.set_angle(canal, 135)
    time.sleep_ms(800)
    
    print("Regresando a 90 grados...")
    driver.set_angle(canal, 90)
    time.sleep_ms(800)
    print("Barrido terminado.")

def main():
    print("=====================================================")
    print(f"  Prueba de Servomotores - Platform: {sys.platform.upper()}   ")
    print("=====================================================")
    
    # Inicializar I2C dinámicamente según la plataforma o usar GPIO directo directamente
    pca_detectado = False
    if es_esp8266 and FORZAR_GPIO_DIRECTO:
        print("[INFO] Modo GPIO Directo activo. Omitiendo inicialización de I2C (evita conflictos en D1/D2).")
    else:
        if es_esp8266:
            # ESP8266 (NodeMCU): SCL=GPIO5 (D1), SDA=GPIO4 (D2)
            print("Iniciando bus I2C de Software (SCL=Pin 5 / D1, SDA=Pin 4 / D2)...")
            try:
                i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
                dispositivos = i2c.scan()
                print("Dispositivos I2C encontrados:", [hex(d) for d in dispositivos])
                pca_detectado = 0x40 in dispositivos
            except Exception as e:
                print("[WARNING] Falló escaneo I2C:", e)
        else:
            # ESP32: SCL=GPIO22, SDA=GPIO21
            print("Iniciando bus I2C de Hardware (SCL=Pin 22, SDA=Pin 21)...")
            try:
                i2c = I2C(0, sda=Pin(21), scl=Pin(22), freq=400000)
                dispositivos = i2c.scan()
                print("Dispositivos I2C encontrados:", [hex(d) for d in dispositivos])
                pca_detectado = 0x40 in dispositivos
            except Exception as e:
                print("[WARNING] Falló escaneo I2C:", e)
    
    if pca_detectado:
        print("[OK] PCA9685 detectado en 0x40. Usando driver I2C.")
        driver = PCA9685Driver(i2c, address=0x40)
    else:
        print("[INFO] Conmutando a modo de prueba GPIO directa (8 servos activos).")
        driver = GPIOServoDriver(PINE_GPIO_DIRECTOS)
        
    print("\nModos de prueba:")
    print("1. Barrido automático de todos los canales (0 al 7)")
    print("2. Barrido interactivo paso a paso (presionar ENTER para cambiar)")
    print("3. Posicionar todos los servos a 90 grados (Modo Armado/Calibración)")
    
    try:
        seleccion = input("\nSeleccione una opción (1, 2 o 3): ").strip()
    except Exception:
        seleccion = "1" # Fallback
        
    limite_canales = 8
        
    if seleccion == "3":
        print(f"\nColocando servos (0-{limite_canales-1}) a 90 grados...")
        for ch in range(limite_canales):
            driver.set_angle(ch, 90)
            time.sleep_ms(100)
        print("[OK] Todos los servos centrados a 90°. ¡Listo para el acople mecánico!")
        
    elif seleccion == "2":
        print("\n--- PRUEBA INTERACTIVA PASO A PASO ---")
        for ch in range(limite_canales):
            nombre = NOMBRES_SERVOS.get(ch, f"Canal {ch}")
            print(f"\nSiguiente servo a probar: {nombre}")
            input("Presione ENTER para iniciar el barrido del servo...")
            realizar_barrido(driver, ch, nombre)
        print("\n[OK] Fin de la prueba interactiva.")
        
    else:
        print("\n--- PRUEBA AUTOMÁTICA DE BARRIDO ---")
        for ch in range(limite_canales):
            nombre = NOMBRES_SERVOS.get(ch, f"Canal {ch}")
            realizar_barrido(driver, ch, nombre)
            time.sleep_ms(200)
        print("\n[OK] Fin de la prueba de barrido automático.")

if __name__ == "__main__":
    main()
