import discord
import sys
import traceback
from datetime import datetime
from random import choice
from discord.ext import commands, tasks

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('The events cog has been loaded.')
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You don\'t have the permission to use this command.')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please enter all the necessary arguments.')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send('The bot doesn\'t have the permission for this. Give this bot admin permissions.')
        elif isinstance(error, commands.BotMissingRole):
            await ctx.send('The bot doesn\'t have the required role. Give this bot the appropriate role.')
        elif isinstance(error, commands.RoleNotFound):
            await ctx.send("Forbidden: missing permissions")
        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, (commands.CommandNotFound, commands.UserInputError)):
            await ctx.send('Incorrect command syntax or command not found.')
        if isinstance(error, commands.CheckFailure):
            await ctx.send('You don\'t have the permission to use this command.')
    
def setup(bot):
    bot.add_cog(Events(bot))