import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# IMPORTANTE: Importamos tu cerebro lógico y los datos de prueba
from motor_decisiones import MotorDecisionesAcademicas, mock_estudiantes_limpios, mock_asignaturas_limpias

# Inicializamos el motor en la memoria del bot
motor = MotorDecisionesAcademicas(mock_estudiantes_limpios, mock_asignaturas_limpias)

# 1. Cargar la caja fuerte de credenciales
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = int(os.getenv("AUTHORIZED_USER_ID", 0))

# 2. Función de Seguridad y Bienvenida
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # El Candado Zero Trust
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ Acceso denegado. Este agente es de uso interno estricto.")
        print(f"🔴 [ALERTA] Intento de acceso bloqueado del ID: {user_id}")
        return
        
    print(f"🟢 [LOG] Usuario autorizado ({user_id}) ha iniciado el bot.")
    await update.message.reply_text("✅ Autenticación exitosa. Bienvenido al sistema de evaluación Hermes Analytics.\n\nUse el comando /evaluar [RUT] [NRC] para analizar una solicitud.")

# 3. Función temporal para conectar el motor lógico
async def comando_evaluar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        return # Ignorar en silencio a usuarios no autorizados

    print(f"🟢 [LOG] Procesando comando /evaluar del usuario {user_id}...")

    # 1. Validar que el usuario haya enviado exactamente 2 parámetros (RUT y NRC)
    if len(context.args) < 2:
        await update.message.reply_text("⚠️ Formato incorrecto. Por favor usa: /evaluar [RUT] [NRC]")
        return

    # 2. Extraer las variables
    rut_alumno = context.args[0]
    nrc_asignatura = context.args[1]

    # 3. Pasar los datos al Motor Lógico (El "Backend")
    resultado_veredicto = motor.evaluar_solicitud(rut_alumno, nrc_asignatura)

    # 4. Enviar la respuesta definitiva por Telegram
    mensaje_final = (
        f"📊 *Reporte de Solicitud*\n\n"
        f"👤 *RUT:* {rut_alumno}\n"
        f"📚 *NRC:* {nrc_asignatura}\n"
        f"────────────────\n"
        f"📝 *Veredicto:* {resultado_veredicto}"
    )
    
    await update.message.reply_text(mensaje_final, parse_mode='Markdown')

# 4. Inicialización del Agente
if __name__ == '__main__':
    print("Iniciando Motor de Interfaz Hermes Analytics...")
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Rutas de comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("evaluar", comando_evaluar))
    
    print("🤖 Agente escuchando en Telegram. Presiona Ctrl+C para detener.")
    app.run_polling()