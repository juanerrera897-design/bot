import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

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
async def saludo(ctx):
   await ctx.send(f"Hola {ctx.author.mention} ,bienvenido a mi servidor")

@bot.command()
async def suma(ctx,a1:int, b2:int):
   await ctx.send(f"tu suma es {a1 + b2}    ")


bot.run("")
