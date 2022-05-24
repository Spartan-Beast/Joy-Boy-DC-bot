import discord
from discord.ext import commands
from cogs.jsonload import *
import random
import json
import os
from dotenv import load_dotenv, find_dotenv

if os.path.exists(fr"{get_path()}/config.json"):
    with open('./config.json') as file:
        configData = json.load(file)
else:
    configTemplate = {"Prefix": ""}
    with open(fr"{get_path()}/config.json", 'w+') as file:
        json.dump(configTemplate, file)

load_dotenv(find_dotenv())        
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=configData["Prefix"], intents=intents)
token = os.getenv("Token")

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
        await message.channel.send(f'Use {configData["Prefix"]}help to access the help menu.')
    await bot.process_commands(message)

@bot.command(aliases=['l'])
@commands.has_permissions(send_messages=True)
async def luffy(ctx):
    embed = discord.Embed(title="Luffy's epic fights", description="Please select one of the following\n(type the command without the prefix):\nKuro\nDon Krieg\nArlong\nCrocodile\nEnel\nLuffy vs Blueno\nRob Lucci\nGecko Moria\nMagellan\nHody Jones\nSentomaru\nPacifista\nCaesar\n||Doflamingo||\n||Cracker||\n||Katakuri||\n||Kaido||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['z'])
@commands.has_permissions(send_messages=True)
async def zoro(ctx):
    embed = discord.Embed(title="Zoro's epic fights", description="Please select one of the following\n(type the command without the prefix):\nMorgan\nCabaji\nNyaban Brothers\nMihawk\nHachi\nTashigi\nDaz Bones\nBraham\nGroggy monsters\nFranky Family\nT Bone\nOhm\nKaku\nShu\nRyuma\nKuma\nHumandrills\nZoro vs Hody\nHyouzou\nMonet\nFujitora\n||Pica||\n||Carrot||\n||Samurais||\n||Denjiro||\n||Hawkins||\n||Kamazou||\n||Oniwabanshu||\n||Killer||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['s'])
@commands.has_permissions(send_messages=True)
async def sanji(ctx):
    embed = discord.Embed(title="Sanji's epic fights", description="Please select one of the following\n(type the command without the prefix):\nGin and Pearl\nKurobi\nUnluckies\nBon Clay\nEnel\nSatori\nGroggy monsters\nAokiji\nFranky\nSanji vs Blueno\nKalifa\nJabura\nAbsalom\nKuma\nKizaru\nIvankov\nWadatsumi\nVergo\nSanji vs Doflamingo\n||Judge||\n||Oven||\n||Big Mom Pirates||\n||Daifuku||\n||Kyoshiro Family||\n||X-Drake||\n||Page One||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['n'])
@commands.has_permissions(send_messages=True)
async def nami(ctx):
    embed = discord.Embed(title="Nami's epic fights", description="Please select one of the following\n(type the command without the prefix):\nMiss Valentine\nMiss Doublefinger\nHotori and Kotori\nKumadori\nNami vs Kalifa\n||Cracker||\n||Big Mom||\n||Ulti||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['u'])
@commands.has_permissions(send_messages=True)
async def usopp(ctx):
    embed = discord.Embed(title="Usopp's epic fights", description="Please select one of the following\n(type the command without the prefix):\nChew\nDaddy Masterson\nMr 4 and Miss Merry Christmas\nSatori\nPerona\nTrebol and Sugar\nSugar\n||Onigashima guards||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['r'])
@commands.has_permissions(send_messages=True)
async def robin(ctx):
    embed = discord.Embed(title="Robin's epic fights", description="Please select one of the following\n(type the command without the prefix):\nPell\nTashigi\nRobin vs Crocodile\nYama\nSpandam\nTararan\nDr Hogback", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['sk'])
@commands.has_permissions(send_messages=True)
async def sogeking(ctx):
    embed = discord.Embed(title="Sogeking's epic fights", description="Please select one of the following\n(type the command without the prefix):\nMarines\nSogeking vs Kumacy", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['songs'])
@commands.has_permissions(send_messages=True)
async def opsongs(ctx):
    embed = discord.Embed(title="One Piece songs", description="Please select one of the following\n(type the command without the prefix):\nLuffy's baka song\nSogeking theme song\nBink's sake\n||Oden song||", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    
@bot.command(aliases=['sh'])
@commands.has_permissions(send_messages=True)
async def strawhats(ctx):
    embed = discord.Embed(title="Straw Hats' epic fights", description="Please select one of the following\n(type the command without the prefix):\nSabaody\nOars", color=ctx.author.color)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    
@bot.command(aliases=['m'])
@commands.has_permissions(send_messages=True)
async def meme(ctx):
    urls = open('memes.json',)
    memes = json.load(urls)
    embed = discord.Embed(title="One Piece meme", description="Funny One Piece meme", color=random.choice(bot.color_list))
    embed.set_image(url=random.choice(memes))
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['tm'])
@commands.has_permissions(send_messages=True)
async def tmeme(ctx):
    urls = open('texas_memes.json',)
    tmemes = json.load(urls)
    embed = discord.Embed(title="~~Texas~~ Teexus meme", description="~~Funny~~ True Texas meme", color=random.choice(bot.color_list))
    embed.set_image(url=random.choice(tmemes))
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command(aliases=['btm'])
@commands.has_permissions(send_messages=True)
async def bmeme(ctx):
    urls = open('brit_memes.json',)
    bmemes = json.load(urls)
    embed = discord.Embed(title="~~British~~ Bri'ish meme", description="~~Funny~~ True Bri'ish meme", color=random.choice(bot.color_list))
    embed.set_image(url=random.choice(bmemes))
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    
@bot.command(aliases=['am'])
@commands.has_permissions(send_messages=True)
async def ameme(ctx):
    urls = open('anime_memes.json',)
    amemes = json.load(urls)
    embed = discord.Embed(title="Anime meme", description="Funny anime meme", color=random.choice(bot.color_list))
    embed.set_image(url=random.choice(amemes))
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
