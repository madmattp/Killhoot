# Code by madmattp https://github.com/madmattp

import discord
from discord.ext import commands, tasks
from kahoot import client as account

token = "coloque o token aqui!" 
client = commands.Bot(command_prefix = ';')
client.remove_command('help')

bots = []

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="O CAOS 🔥🔥🔥"))
    print("=====================\n Running Killhoot...\n=====================")

@client.command(aliases=["h"])
async def help(ctx):
    embed = discord.Embed(
        title = "🧨🔥 KILLHOOT V3 🔥🧨",
        colour = discord.Colour.red()
    )
    embed.set_footer(text=f"Killhoot#0542")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/780874141585768458/780874204979527760/killhoot.png")
    embed.add_field(name="help / h", value="● Retorna a minha lista de Comandos.", inline=False)
    embed.add_field(name="ping", value="● Retorna a latência em milissegundos.", inline=True)
    embed.add_field(name="killhoot <pin> <nome> <n>", value="● Invade uma sala kahoot linkada ao <pin>.\n⠀⠀<nome> define o nome dos bots invasores. \n⠀⠀<n> define o número de bots.\n⠀⠀(Ex: ;killhoot 1234567 BOOM 1000)", inline=False)
    embed.add_field(name="leave", value="● Desconecta todos os bots", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000)}ms")

@client.command(aliases=["kill"])
async def killhoot(ctx, pin, name, n):
    await ctx.message.add_reaction("🔥")
    await ctx.send(f"Enviando {n} bots para {pin}...\nOrdem de:{ctx.message.author.mention}")

    n = int(n)
    index = 0
    while(index != n):
        bot = account()
        bot.join(pin, f"{name}{index + 1}")
        bots.append(bot)
        index += 1
        
    await ctx.send("Bots enviados com sucesso")
    
@client.command()
async def leave(ctx):
    await ctx.message.add_reaction("👋")
    await ctx.send("Batendo em retirada...")

    for bot in bots:
        bot.leave()

    bots.clear()

client.run(token)
