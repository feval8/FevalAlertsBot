import httpx

async def obtener_precios_actuales(tokens):
    precios = {}
    for token in tokens:
        if token == "SOLX":
            precios[token] = await obtener_precio_solx()
        elif token == "TICS":
            precios[token] = await obtener_precio_tics()
        else:
            try:
                url = f"https://api.coingecko.com/api/v3/simple/price?ids={token.lower()}&vs_currencies=usd"
                r = httpx.get(url)
                data = r.json()
                precios[token] = data.get(token.lower(), {}).get("usd", 0)
            except:
                precios[token] = 0
    return precios

async def obtener_precio_solx():
    return 0.00012  # Simulación: integrar con Uniswap real si lo deseas

async def obtener_precio_tics():
    return 0.0734  # Simulación: integrar scraping desde su web oficial

async def generar_resumen_cartera(cartera):
    precios = await obtener_precios_actuales(cartera.keys())
    total = 0
    resumen = "*Resumen cartera:*\n"
    for token, cantidad in cartera.items():
        precio = precios.get(token, 0)
        valor = cantidad * precio
        total += valor
        resumen += f"{token}: {cantidad} × {precio:.4f}$ = {valor:.2f}$\n"
    resumen += f"\n*Valor total:* {total:.2f} USD"
    return resumen
