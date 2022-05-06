import discord
from discord.ext import commands
from pathlib import Path
from cogs.jsonload import *
import random
import os

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    @commands.Cog.listener()
    async def on_ready(self):
        print("The commands cog has been loaded.")

    @commands.group(invoke_wihtout_command=True)
    async def help(self, ctx):
        embed = discord.Embed(title='Help', description='Here is the list of commands for this bot:\nUse #help <cmd> for extended information on that command.', color=ctx.author.color)
        embed.add_field(name='Joy Boy commands', value='joke, opjoke, bmjoke, meme', inline=False)
        embed.add_field(name='Miscellaneous', value='clear', inline=False)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
            
    @help.command()
    async def clear(self, ctx):
        embed = discord.Embed(title='Clear', description='Clears the most recent message, or, if specified, the last <n> messages.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value='%clear <number>')
        embed.add_field(name='Command shortcuts', value='%clr  %c')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)

    @help.command()
    async def bmjoke(self, ctx):
        embed = discord.Embed(title='Big Mom joke', description='Sends a random Big Mom ~~joke~~ fact.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value='%bmjoke')
        embed.add_field(name='Command shortcuts', value='%bm')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def opjoke(self, ctx):
        embed = discord.Embed(title='One Piece joke', description='Sends a random One Piece ~~joke~~ fact.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value='%opjoke')
        embed.add_field(name='Command shortcuts', value='%op')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def joke(self, ctx):
        embed = discord.Embed(title='Message', description='Sends a random joke.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value='%joke')
        embed.add_field(name='Command shortcut', value='%j')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
    @help.command()
    async def meme(self, ctx):
        embed = discord.Embed(title='Message', description='Sends a random One Piece meme.', color=ctx.author.color)
        embed.add_field(name='**Syntax**', value='%meme')
        embed.add_field(name='Command shortcut', value='%m')
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Commands(bot))