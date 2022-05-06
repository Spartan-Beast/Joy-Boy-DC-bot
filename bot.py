import discord
from discord.ext import commands
from cogs.jsonload import *
import random
import json
import os

if os.path.exists(fr"{get_path()}/config.json"):
    with open('./config.json') as file:
        configData = json.load(file)
else:
    configTemplate = {"Token": ""}
    with open(fr"{get_path()}/config.json", 'w+') as file:
        json.dump(configTemplate, file)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="%", intents=intents)
token = configData["Token"]

bot.colors = {
    "WHITE": 0xFFFFFF,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992022,
    "DARK_NAVY": 0x2C3E50
}
bot.color_list = [color for color in bot.colors.values()]

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Kaizoku ou ni ore wa naru!'))
    print("Ready")

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if message.content.lower().startswith('help'):
        await message.channel.send('Use %help to access the help menu.')
    await bot.process_commands(message)

@bot.command(aliases=['m'])
@commands.has_permissions(send_messages=True)
async def meme(ctx):
    urls = open('memes.json',)
    memes = json.load(urls)
    embed = discord.Embed(title="One Piece meme", description="Funny One Piece meme", color=random.choice(bot.color_list))
    embed.set_image(url=random.choice(memes))
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['j'])
@commands.has_permissions(send_messages=True)
async def joke(ctx):
    jokes = open('bot_jokes.json',)
    messages = json.load(jokes)
    message = random.choice(messages)
    embed = discord.Embed(title='Bot Joke!!', description='Amazing ~~joke~~ fact from the best bot on this planet!', color=random.choice(bot.color_list))
    embed.add_field(name='Joy Boy says:', value=message)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['bm'])
@commands.has_permissions(send_messages=True)
async def bmjoke(ctx):
    bm_jokes = open('bigmom_jokes.json',)
    messages = json.load(bm_jokes)
    message = random.choice(messages)
    embed = discord.Embed(title='Bot Joke!!', description='Big Mom ~~joke~~ fact from the best bot on this planet!', color=random.choice(bot.color_list))
    embed.add_field(name='Joy Boy says:', value=message)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['op'])
@commands.has_permissions(send_messages=True)
async def opjoke(ctx):
    op_jokes = open('onepiece_jokes.json',)
    messages = json.load(op_jokes)
    message = random.choice(messages)
    embed = discord.Embed(title='Bot Joke!!', description='One Piece ~~joke~~ fact from the best bot on this planet!', color=random.choice(bot.color_list))
    embed.add_field(name='Joy Boy says:', value=message)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['clr', 'c'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

if __name__ == '__main__':
    for file in os.listdir("./cogs"):
        if file.endswith('.py'):
            if file == 'jsonload.py':
                pass
            else:
                bot.load_extension(f"cogs.{file[:-3]}")

bot.run(token)
