import asyncio
import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils import obtener_precios_actuales, analizar_token, generar_resumen_cartera
from alerts import revisar_alertas

# Configura el log
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carga el token desde variable de entorno
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

# Define tus tokens
CARTERA = {
    'SOLX': 187252,
    'TICS': 592.58
}
SEGUIMIENTO = ['BTC', 'FIL', 'TON', 'TRX', 'FET', 'TAO']

# Riesgos por defecto (pueden modificarse con /set_riesgo)
RIESGO = {
    'SOLX': 'agresivo',
    'TICS': 'agresivo',
    'BTC': 'moderado',
    'FIL': 'moderado',
    'TON': 'moderado',
    'TRX': 'moderado',
    'FET': 'agresivo',
    'TAO': 'agresivo'
}

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Estado", callback_data='estado')],
        [InlineKeyboardButton("🧠 Analiza", callback_data='analiza')],
        [InlineKeyboardButton("⚙️ Riesgo", callback_data='set_riesgo')],
        [InlineKeyboardButton("📰 Noticias", callback_data='noticias')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenido a FevalAlertsBot. Selecciona una opción:", reply_markup=reply_markup)

# Manejador de botones
async def botones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'estado':
        await estado(update, context)
    elif data == 'analiza':
        await analiza(update, context)
    elif data == 'set_riesgo':
        await set_riesgo(update, context)
    elif data == 'noticias':
        await noticias(update, context)

# /estado: Precios y estado cartera
async def estado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    precios = await obtener_precios_actuales(CARTERA.keys() | set(SEGUIMIENTO))
    mensaje = "\n".join([f"{k}: {v:.4f} USD" for k, v in precios.items()])
    await update.effective_chat.send_message(f"\U0001F4CA *Precios actuales:*
{mensaje}", parse_mode='Markdown')

# /resumen: resumen total
async def resumen(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = await generar_resumen_cartera(CARTERA)
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# /analiza: analiza cada token
async def analiza(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for token in CARTERA.keys() | set(SEGUIMIENTO):
        resultado = await analizar_token(token, RIESGO.get(token, 'moderado'))
        await update.message.reply_text(resultado, parse_mode='Markdown')

# /set_riesgo: cambia nivel de riesgo
async def set_riesgo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Uso: /set_riesgo TOKEN nivel (conservador, moderado, agresivo)")
        return
    token, nivel = context.args
    if nivel.lower() not in ['conservador', 'moderado', 'agresivo']:
        await update.message.reply_text("Nivel no válido. Usa: conservador, moderado o agresivo.")
        return
    RIESGO[token.upper()] = nivel.lower()
    await update.message.reply_text(f"Riesgo de {token.upper()} actualizado a {nivel.lower()}.")

# /noticias: resumen
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 *Noticias*\nAún no implementado, pero pronto recibirás alertas automáticas aquí.", parse_mode='Markdown')

# Informe automático
async def enviar_informe_horario():
    precios = await obtener_precios_actuales(CARTERA.keys() | set(SEGUIMIENTO))
    resumen = await generar_resumen_cartera(CARTERA)
    mensaje = "\u23f0 *Informe horario:*\n"
    mensaje += "\n".join([f"{k}: {v:.4f} USD" for k, v in precios.items()])
    mensaje += f"\n\n{resumen}"
    await app.bot.send_message(chat_id=USER_ID, text=mensaje, parse_mode='Markdown')

# Loop principal
async def main():
    global app
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("estado", estado))
    app.add_handler(CommandHandler("resumen", resumen))
    app.add_handler(CommandHandler("analiza", analiza))
    app.add_handler(CommandHandler("set_riesgo", set_riesgo))
    app.add_handler(CommandHandler("noticias", noticias))
    app.add_handler(CallbackQueryHandler(botones))

    scheduler = AsyncIOScheduler()
    scheduler.add_job(enviar_informe_horario, 'interval', hours=1)
    scheduler.add_job(lambda: revisar_alertas(app.bot, USER_ID, CARTERA, SEGUIMIENTO), 'interval', minutes=5)
    scheduler.start()

    print("\u2705 Bot FevalAlertsBot iniciado correctamente.")
    await app.run_polling()

if __name__ == '__main__':
    import nest_asyncio
    nest_asyncio.apply()
    asyncio.run(main())
