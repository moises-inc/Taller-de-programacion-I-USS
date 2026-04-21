# Akumi - Primer modelo de IA
import json
import os
import sys
import pyttsx3

# Intentar usar pyttsx3, si no está disponible se usa solo print
try:
    import pyttsx3
    _voz = pyttsx3.init()
    _voz.setProperty('rate', 170)
    _voz.setProperty('volume', 1.0)
    def hablar(texto):
        print("Akumi:", texto)
        _voz.say(texto)
        _voz.runAndWait()
except Exception:
    def hablar(texto):
        print("Akumi:", texto)

# Diagnóstico e intento de configurar reconocimiento por micrófono (SpeechRecognition)
mic_disponible = False
_sr_error_msg = None
try:
    import speech_recognition as sr
    _r = sr.Recognizer()
    try:
        # prueba rápida de micrófono
        with sr.Microphone() as src:
            mic_disponible = True
    except Exception as e:
        mic_disponible = False
        _sr_error_msg = str(e)
except Exception as e:
    mic_disponible = False
    _sr_error_msg = str(e)

def mostrar_diagnostico():
    print("\n--- Diagnóstico de reconocimiento de voz ---")
    if mic_disponible:
        print("Micrófono: disponible")
    else:
        print("Micrófono: NO disponible")
    print("speech_recognition import error / detalle:", _sr_error_msg)
    print("Sugerencias de instalación en Windows (terminal de VS Code):")
    print("  1) Asegúrate de usar el intérprete correcto en VS Code (Python: Select Interpreter).")
    print("  2) Instala dependencias:")
    print("     python -m pip install SpeechRecognition pyttsx3")
    print("     python -m pip install pipwin")
    print("     python -m pipwin install pyaudio")
    print("  3) Si pipwin falla, descarga el wheel de PyAudio para tu versión de Python desde:")
    print("     https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio")
    print("     y luego: python -m pip install <archivo_whl>\n")

def escuchar(timeout=5, phrase_time_limit=6):
    """Retorna el texto reconocido en minúsculas o None si falla."""
    if not mic_disponible:
        return None
    try:
        with sr.Microphone() as source:
            _r.adjust_for_ambient_noise(source, duration=0.6)
            print("Escuchando... (habla ahora)")
            audio = _r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        texto = _r.recognize_google(audio, language="es-ES")
        print("Reconocido:", texto)
        return texto.lower().strip()
    except sr.WaitTimeoutError:
        print("Tiempo de espera agotado.")
        return None
    except sr.UnknownValueError:
        print("No entendí, intenta de nuevo.")
        return None
    except sr.RequestError as e:
        print("Error con el servicio de reconocimiento:", e)
        return None
    except Exception as e:
        print("Error de micrófono:", e)
        return None

FILE = "memoria.json"

# Cargar memoria si existe
if os.path.exists(FILE):
    with open(FILE, "r", encoding="utf-8") as f:
        memoria = json.load(f)
else:
    memoria = {}

# Si el reconocimiento no funciona, mostrar diagnóstico y permitir al usuario decidir
if not mic_disponible:
    hablar("Aviso: el reconocimiento por micrófono no está disponible.")
    mostrar_diagnostico()
    usar_mic = input("¿Quieres intentar usar el micrófono de todas formas? (s = intentar / n = usar solo teclado): ").strip().lower()
    if usar_mic != "s":
        mic_disponible = False
    else:
        # si quiso intentar, volver a probar una vez más
        try:
            if 'sr' in globals():
                with sr.Microphone() as src:
                    mic_disponible = True
            else:
                mic_disponible = False
        except Exception as e:
            mic_disponible = False
            print("Reintento de micrófono falló:", e)
            print("Se seguirá con entrada por teclado.\n")

hablar("Hola, soy Akumi. ¿En qué puedo ayudarte? (di 'salir' para terminar)")

while True:
    # si hay micrófono intentamos escuchar, si no se usa input()
    if mic_disponible:
        mensaje = escuchar()
        if mensaje is None:
            # si no se reconoció nada, dar la opción de teclear
            usar_teclado = input("No se reconoció audio. ¿Quieres escribir? (s/n) o 'd' para ver diagnóstico: ").strip().lower()
            if usar_teclado == "d":
                mostrar_diagnostico()
                continue
            if usar_teclado == "s":
                mensaje = input("Tú: ").lower().strip()
            else:
                continue
    else:
        mensaje = input("Tú: ").lower().strip()

    if not mensaje:
        continue

    if mensaje == "salir":
        hablar("Hasta luego, ¡cuídate!")
        break

    # Pedirle a Akumi que muestre lo que recuerde
    if ("dime lo que te dije" in mensaje
        or "lo que te dije anteriormente" in mensaje
        or "dime lo que te dije anteriormente" in mensaje
        or mensaje.startswith("akumi, dime lo que te dije")):
        if not memoria:
            hablar("No recuerdo nada todavía.")
        else:
            hablar("Esto es lo que recuerdo:")
            for clave, valor in memoria.items():
                print(f"- {clave}: {valor}")
        continue

    # Detectar si estás enseñándole algo ("recuerda" / "aprende")
    if "recuerda" in mensaje or "aprende" in mensaje:
        dato = mensaje.replace("recuerda que", "").replace("recuerda", "").replace("aprende que", "").replace("aprende", "").strip()
        partes = dato.split(" es ")
        if len(partes) == 2:
            clave_raw, valor = partes
            clave = clave_raw.strip().lower()
            memoria[clave] = valor.strip()
            hablar(f"Ok, recordaré que {clave_raw.strip()} es {valor.strip()}.")
        else:
            clave = dato.strip().lower()
            if clave:
                memoria[clave] = dato.strip()
                hablar("Perfecto, lo recordaré.")
            else:
                hablar("Dime algo como: 'Recuerda que mi color favorito es azul'.")
    else:
        # Buscar coincidencias con la memoria
        respuesta = None
        for clave, valor in memoria.items():
            if clave in mensaje:
                respuesta = f"Sí, recuerdo que {clave} es {valor}."
                break

        if not respuesta:
            # respuestas sencillas
            if "hola" in mensaje:
                respuesta = "¡Hola! ¿Cómo te sientes hoy?"
            elif "cómo estás" in mensaje or "como estas" in mensaje:
                respuesta = "Estoy bien, gracias por preguntar."
            elif "te gusta" in mensaje:
                respuesta = "No lo sé todavía, pero puedo aprender de ti."
            else:
                respuesta = "Hmm, cuéntame más, quiero conocerte mejor."

        hablar(respuesta)

    # Guardar la memoria
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(memoria, f, ensure_ascii=False, indent=2)