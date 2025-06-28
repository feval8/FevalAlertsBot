# 🤖 Feval Alerts Bot

FevalAlertsBot es un bot personalizado de Telegram que actúa como **asesor de trading en criptomonedas**, diseñado para ofrecer:

- 📈 Seguimiento en tiempo real de tu cartera.
- 🔔 Alertas automáticas de precio configurables.
- 📊 Análisis técnico adaptado a tu perfil de riesgo.
- 🗞️ Informes automáticos e integración futura de noticias.
- 📲 Interfaz intuitiva con botones interactivos.
- ☑️ Comandos fáciles y rápidos para tener el control total.

---

## 🚀 ¿Qué puede hacer este bot?

### 🔧 Comandos principales

| Comando        | Descripción |
|----------------|-------------|
| `/start`       | Muestra el menú con botones interactivos. |
| `/estado`      | Muestra el precio actual de todos los tokens. |
| `/resumen`     | Muestra el resumen completo y valor total de tu cartera. |
| `/analiza`     | Muestra análisis técnico individual de cada token con sugerencias. |
| `/set_riesgo`  | Cambia tu perfil de riesgo por token (`conservador`, `moderado`, `agresivo`). |
| `/noticias`    | Recibirá noticias relevantes (implementación en desarrollo). |

---

## 🛠️ Tecnologías usadas

- [Python](https://www.python.org/)
- [python-telegram-bot](https://docs.python-telegram-bot.org/)
- [httpx](https://www.python-httpx.org/)
- [APScheduler](https://apscheduler.readthedocs.io/)
- CoinGecko API (para precios en tiempo real)
- Uniswap + scraping (para tokens especiales como SOLX y TICS)

---

## 🧪 Alertas automáticas y análisis

El bot detecta:

- 🔺 Subidas por encima del umbral establecido.
- 🔻 Caídas por debajo del nivel crítico.
- 🧠 Recomendaciones de entrada/salida, SL y TP en base a indicadores como RSI, soportes y volumen (implementado parcialmente).
- 🕐 Envío automático de informe horario cada 60 minutos.
- 🔁 Revisión cada 5 minutos de todos los precios monitoreados.

---

## ⚙️ Instalación en Railway

1. Crea una cuenta en [Railway](https://railway.app)
2. Conecta este repositorio desde GitHub.
3. En la pestaña `Variables`, añade:
    - `BOT_TOKEN`: Tu token de Telegram Bot
    - `USER_ID`: Tu ID personal de Telegram (número)
4. Espera a que el proyecto se despliegue y... ¡listo! 🎉

---

## 🧠 A tener en cuenta

- **Tokens monitorizados por defecto**: SOLX, TICS, BTC, FIL, TON, TRX, FET, TAO
- Puedes modificar los tokens directamente en `main.py`, `utils.py` y `alerts.py` si deseas personalizar tu cartera o seguir nuevos proyectos.
- El bot está pensado para ser un *asistente de trading de alta utilidad para inversores activos*.

---

## 📍 Autor

Este proyecto ha sido creado junto con [ChatGPT] como asesor financiero personal de [@feval8](https://github.com/feval8) para gestión avanzada de inversiones en criptomonedas. 🚀

---

## 🛡️ Advertencia

> Este bot no realiza operaciones ni gestiona fondos. Las recomendaciones son basadas en lógica de análisis técnico, pero **no constituyen asesoramiento financiero real**.

---

## 🧩 En desarrollo

- 🔄 Mejora de scraping y precios para SOLX/TICS.
- 📥 Sistema de gestión de alertas personalizables por comando.
- 📰 Noticias cripto automáticas.
- 📊 Gráficas y análisis visual.
- ⚡ Panel web o escritorio futuro para mejor interacción.

---

## ✅ ¡Listo para usar!

Una vez desplegado, simplemente inicia conversación con tu bot en Telegram, escribe `/start`, y comienza a recibir información, alertas y recomendaciones.

