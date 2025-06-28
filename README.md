# Feval Alerts Bot

Un bot avanzado de Telegram para seguimiento de criptomonedas, gestión de cartera y alertas automáticas personalizadas. Desarrollado para el usuario `feval8`, permite supervisar tanto tokens en cartera como en seguimiento, enviar informes periódicos y usar botones interactivos para una experiencia más intuitiva.

---

## 🚀 Funcionalidades principales

- 📊 **/estado**: Muestra los precios actuales de todas las criptomonedas en cartera y seguimiento.
- 🧐 **/analiza**: Analiza todos los tokens según tu nivel de riesgo y muestra señales con SL, TP y probabilidad.
- 📉 **/set_riesgo TOKEN nivel**: Cambia el riesgo asociado a cada token (conservador, moderado, agresivo).
- 💼 **/resumen**: Resumen total de tu cartera con valor actual.
- 📰 **/noticias**: Acceso a noticias relevantes del mercado (en desarrollo).
- ⏱️ **Informe automático cada hora**: Precios + resumen de cartera.
- 🔔 **Alertas automáticas**: Se envían cuando se detectan condiciones técnicas (breakout, RSI, volumen, etc.)

---

## 📦 Estructura del proyecto

```bash
fevalalertsbot/
├── main.py               # Código principal del bot
├── utils.py              # Funciones de soporte (precios, análisis, resumen)
├── alerts.py             # Sistema de alertas técnicas automáticas
├── server.py             # Servidor Flask para mantener el bot activo en Render
├── requirements.txt      # Dependencias
└── .env                  # Variables de entorno (no subir)
```

---

## ⚙️ Variables de entorno (.env)

```env
BOT_TOKEN=tu_token_aqui
USER_ID=tu_telegram_id
```

Estas variables deben configurarse en **Render** dentro de la sección Environment.

---

## 🧪 Instrucciones para desplegar en Render

1. Crea una cuenta en [https://render.com](https://render.com) con GitHub.
2. Crea un nuevo **Web Service** gratuito.
3. Configura:
   - **Runtime**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Root Directory**: `/`
4. En "Environment", pon tus variables `BOT_TOKEN` y `USER_ID`
5. Render lo desplegará automáticamente.

---

## 📌 Tokens soportados

Actualmente integrados:
- Cartera: `SOLX`, `TICS`
- Seguimiento: `BTC`, `FIL`, `TON`, `TRX`, `FET`, `TAO`

---

## 🧠 Objetivos

- Convertir este bot en una herramienta tipo "Forex Algo".
- Recomendaciones inteligentes con indicadores técnicos.
- Integración con Uniswap y APIs oficiales para precios exactos.
- Interfaz con botones, comandos intuitivos y alertas interactivas.

---

**Desarrollado junto a ChatGPT como asesor e ingeniero de automatización.**


