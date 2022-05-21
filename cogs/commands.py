import discord
from discord.ext import commands
from pathlib import Path
from cogs.jsonload import *
import random
import os

if os.path.exists(fr"{get_path()}/config.json"):
    with open('./config.json') as file:
        configData = json.load(file)
else:
    configTemplate = {"Token": "", "Prefix": ""}
    with open(fr"{get_path()}/config.json", 'w+') as file:
        json.dump(configTemplate, file)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print("The commands cog has been loaded.")

    @commands.group(invoke_wihtout_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Help', description=f'Here is the list of commands for this bot:\nUse {configData["Prefix"]}help <cmd> for extended information on that command.', color=ctx.author.color)
        embed.add_field(name='Joy Boy commands', value='joke, opjoke, bmjoke, meme', inline=False)
        embed.add_field(name='Fights', value='straw hats, luffy, zoro, sanji, nami, robin, usopp, sogeking', inline=False)
        embed.add_field(name='Miscellaneous', value='clear', inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
            
    @help.command()
    async def clear(self, ctx):
        embed = discord.Embed(title='Clear', description='Clears the most recent message, or, if specified, the last <n> messages.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}clear <number>')
        embed.add_field(name='Command shortcuts', value=f'{configData["Prefix"]}clr | {configData["Prefix"]}c')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @help.command()
    async def bmjoke(self, ctx):
        embed = discord.Embed(title='Big Mom joke', description='Sends a random Big Mom ~~joke~~ fact.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}bmjoke')
        embed.add_field(name='Command shortcuts', value=f'{configData["Prefix"]}bm')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def opjoke(self, ctx):
        embed = discord.Embed(title='One Piece joke', description='Sends a random One Piece ~~joke~~ fact.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}opjoke')
        embed.add_field(name='Command shortcuts', value=f'{configData["Prefix"]}op')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def joke(self, ctx):
        embed = discord.Embed(title='Message', description='Sends a random joke.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}joke')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}j')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(title='Message', description='Sends a random One Piece meme.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}meme')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}m')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def strawhats(self, ctx):
        embed = discord.Embed(title='The Straw Hats\' fights', description='Collection of the Straw Hats\' fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{str(configData["Prefix"])}strawhats')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}sh')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def luffy(self, ctx):
        embed = discord.Embed(title='Luffy\'s fights', description='Collection of Luffy\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{str(configData["Prefix"])}luffy')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}l')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def zoro(self, ctx):
        embed = discord.Embed(title='Zoro\'s fights', description='Collection of Zoro\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}zoro')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}z')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def sanji(self, ctx):
        embed = discord.Embed(title='Sanji\'s fights', description='Collection of Sanji\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}sanji')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}s')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        
    @help.command()
    async def nami(self, ctx):
        embed = discord.Embed(title='Nami\'s fights', description='Collection of Nami\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}nami')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}n')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
      
    @help.command()
    async def usopp(self, ctx):
        embed = discord.Embed(title='Usopp\'s fights', description='Collection of Usopp\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}usopp')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}u')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    @help.command()
    async def sogeking(self, ctx):
        embed = discord.Embed(title='Sogeking\'s fights', description='Collection of Sogeking\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}sogeking')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}sk')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
        
    @help.command()
    async def robin(self, ctx):
        embed = discord.Embed(title='Robin\'s fights', description='Collection of Robin\'s fight scenes.\nSends a fight scene video based on the command written\nfrom the list of available fight commands in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}robin')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}r')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def opsongs(self, ctx):
        embed = discord.Embed(title='One Piece songs', description='One Piece original songs.\nSends a video of the song based on the command written\nfrom the list of available songs in the menu.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value=f'{configData["Prefix"]}opsongs')
        embed.add_field(name='Command shortcut', value=f'{configData["Prefix"]}songs')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Commands(bot))
