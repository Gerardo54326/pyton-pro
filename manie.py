import discord
from discord.ext import commands
from settings import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()

async def add(ctx, left: int, right: int):

    """Adds two numbers together."""

    await ctx.send(f"La suma de {left} con {right} es {left + right}")

@bot.command()
async def Baki(ctx):
    await ctx.send(f"""
    Hola, soy un bot {bot.user}!
    """)# esta linea saluda
    await ctx.send("Quieres hablar de baki? responde si o no")
    # Esperar la respuesta del usuario
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response = await bot.wait_for('message', check=check)
    if response:
        if response.content == 'si':
            await ctx.send("""
                    Baki Hanma es el hijo de Yujiro Hanma la criatura mas fuerte del mundo,Mide 168cm y pesa 70k
                    Actualmente es el campeon de la arena korakuen.Lo gano a la edad de 17,derrotando a su medio hermano
                    es un luchador rapido y explocivo.capaz de noquear a sukune en 9,1 segundos siendo la pelea mas corta
                    Su meta es derrotar a su padre para vengar la valentia de su madre que se sacrifico por el
                    pero ahorasu meta es hacerse fuerte para disfrutar sus luchas. 
                            """)   
        else:
            await ctx.send("Está bien, si alguna vez necesitas saber sobre baki.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
 
    await ctx.send("Quieres saber qué habilidades tiene baki?, responde 'si' o 'no'.")
    def check1(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response1 = await bot.wait_for('message', check=check1)
    if response1:
        if response1.content == "si":
            await ctx.send("""
                        1. La espalda demon,esta habilidade e sunica de los hanma,aumenta la fuerza del usuario
                        por las endorfinas y la adrenalina  
                        2. El arranque de la cucaracha,esta es una habilida que baki aprendio por ver a las cucarachas
                        no tienen aceleracion solo inicia a su maxima velocidad,siendo tan rapido que puede noquear
                        en menos de 0.015 milisegundos,un tiempo que ni el cerebro humano puede reaccionar.
                        3 El cerebro de demoniaco,es un organo que solo baki tienen nisiquiera su padre o su abuelo
                        lo tienen,le ayuda a experimentar la adrenalina y las endorfinas con mayor produccion
                        le ayuda a crear enemigos imajinarios que le puede hacer daño o ayudarle a sus tecnicas
                        como el arranque de la cucaracha imajinandose un liquido o imajinando que el es un dinosaurio.
                        4 el latigaso,es una tecnica que se cree que solo son para niños o mujeres,pero baki
                        la aprendio por su padre,trata de hacer el cuerpoflexible y acelera como un latigo
                        Esas son las mas reconocidas de baki hanma 
                            """) 
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre juegos, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
    await ctx.send("Quieres ver una imagen de baki?, responde 'si' o 'no'.")
    def check2(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content in ['si', 'no']
    response2 = await bot.wait_for('message', check=check2)
    if response2:
        if response2.content == "si":
            with open('baki2.jpeg', 'rb') as f:

        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!

                picture = discord.File(f)

    # A continuación, podemos enviar este archivo como parámetro.

            await ctx.send(file=picture)
                        
        else:
            await ctx.send("Está bien, si alguna vez necesitas hablar sobre juegos, estaremos en contacto.")
    else:
        await ctx.send("Lo siento, no pude entender tu respuesta. Inténtalo de nuevo.")
bot.run(token)
