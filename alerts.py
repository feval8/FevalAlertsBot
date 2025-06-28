import asyncio
import httpx

# Umbrales de ejemplo por token
ALERTAS = {
    'BTC': {'max': 70000, 'min': 58000},
    'FIL': {'max': 8, 'min': 5},
    'TON': {'max': 8, 'min': 5},
    'TRX': {'max': 0.13, 'min': 0.09},
    'FET': {'max': 2.0, 'min': 1.4},
    'TAO': {'max': 430, 'min': 350},
    'SOLX': {'max': 0.0002, 'min': 0.00009},
    'TICS': {'max': 0.09, 'min': 0.06}
}

async def obtener_precio(token):
    if token == "SOLX":
        return 0.00012
    elif token == "TICS":
        return 0.0734
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token.lower()}&vs_currencies=usd"
    try:
        r = httpx.get(url)
        data = r.json()
        return data.get(token.lower(), {}).get("usd", 0)
    except:
        return 0

async def revisar_alertas(bot, user_id, cartera, seguimiento):
    for token in set(cartera.keys()) | set(seguimiento):
        umbrales = ALERTAS.get(token)
        if not umbrales:
            continue
        precio = await obtener_precio(token)
        if precio == 0:
            continue
        if precio >= umbrales['max']:
            await bot.send_message(chat_id=user_id, text=f"🚨 *{token} ha superado el máximo!* {precio}$", parse_mode='Markdown')
        elif precio <= umbrales['min']:
            await bot.send_message(chat_id=user_id, text=f"⚠️ *{token} ha caído por debajo del mínimo!* {precio}$", parse_mode='Markdown')
