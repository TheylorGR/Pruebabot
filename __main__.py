import discord

# Define los intents que tu bot utilizará
intento = discord.Intents(34315)

# Token de autenticación del bot
llave = 'MTIzMjQxMjQ4OTE5OTc4Mzk1Nw.GpZCP2.fpkvoBiqqxt1oGy-ebkIO-rJ37X7icT6zmNMR8'

cliente = discord.Client(intents=intento)

@cliente.event
async def on_message(mensaje):
    if mensaje.content.find("!Hola, Bot") != -1:
        await mensaje.channel.send("Hola! Soy happy un bot de discord")
    elif mensaje.content.find("!Cómo estás bot?") != -1:
        await mensaje.channel.send("Bien, gracias,\nY cómo te encuentras tú?")
cliente.run(llave)
