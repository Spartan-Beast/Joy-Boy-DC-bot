import discord
import sys
import json
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
            print(f'Ignoring exception in command {ctx.command}:', file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, (commands.CommandNotFound, commands.UserInputError)):
            await ctx.send('Incorrect command syntax or command not found.')
        if isinstance(error, commands.CheckFailure):
            await ctx.send('You don\'t have the permission to use this command.')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        fights = open('fights.json')
        fight = json.load(fights)
        if message.content.lower().startswith('kuro'):
            await message.channel.send(fight["Kuro"])
        if message.content.lower().startswith('don krieg'):
            await message.channel.send(fight["Don Krieg"])
        if message.content.lower().startswith('arlong'):
            await message.channel.send(fight["Arlong"])
        if message.content.lower().startswith('crocodile'):
            await message.channel.send(fight["Crocodile"])
        if message.content.lower().startswith('enel'):
            await message.channel.send(fight["Enel"])
        if message.content.lower().startswith('luffy vs blueno'):
            await message.channel.send(fight["Luffy vs Blueno"])
        if message.content.lower().startswith('rob lucci') or message.content.lower().startswith('lucci'):
            await message.channel.send(fight["Rob Lucci"])
        if message.content.lower().startswith('gecko moria') or message.content.lower().startswith('moria'):
            await message.channel.send(fight["Gecko Moria"])
        if message.content.lower().startswith('magellan'):
            await message.channel.send(fight["Magellan"])
        if message.content.lower().startswith('hody jones'):
            await message.channel.send(fight["Hody Jones"])
        if message.content.lower().startswith('sentomaru'):
            await message.channel.send(fight["Sentomaru"])
        if message.content.lower().startswith('pacifista'):
            await message.channel.send(fight["Pacifista"])
        if message.content.lower().startswith('caesar'):
            await message.channel.send(fight["Caesar"])
        if message.content.lower().startswith('doflamingo') or message.content.lower().startswith('doffy'):
            await message.channel.send(fight["Doflamingo"])
        if message.content.lower().startswith('katakuri'):
            await message.channel.send(fight["Katakuri"])
        if message.content.lower().startswith('cracker'):
            await message.channel.send(fight["Cracker"])
        if message.content.lower().startswith('kaido'):
            await message.channel.send(fight["Kaido"])
        
        if message.content.lower().startswith('morgan'):
            await message.channel.send(fight["Morgan"])
        if message.content.lower().startswith('cabaji'):
            await message.channel.send(fight["Cabaji"])
        if message.content.lower().startswith('nyaban'):
            await message.channel.send(fight["Nyaban Brothers"])
        if message.content.lower().startswith('mihawk'):
            await message.channel.send(fight["Mihawk"])
        if message.content.lower().startswith('hachi'):
            await message.channel.send(fight["Hachi"])
        if message.content.lower().startswith('tashigi'):
            await message.channel.send(fight["Tashigi"])
        if message.content.lower().startswith('daz bones'):
            await message.channel.send(fight["Daz Bones"])
        if message.content.lower().startswith('braham'):
            await message.channel.send(fight["Braham"])
        if message.content.lower().startswith('groggy monsters'):
            await message.channel.send(fight["Groggy monsters"])
        if message.content.lower().startswith('franky family'):
            await message.channel.send(fight["Franky Family"])
        if message.content.lower().startswith('t bone'):
            await message.channel.send(fight["T Bone"])
        if message.content.lower().startswith('ohm'):
            await message.channel.send(fight["Ohm"])
        if message.content.lower().startswith('kaku'):
            await message.channel.send(fight["Kaku"])
        if message.content.lower().startswith('shu'):
            await message.channel.send(fight["Shu"])
        if message.content.lower().startswith('ryuma'):
            await message.channel.send(fight["Ryuma"])
        if message.content.lower().startswith('kuma'):
            await message.channel.send(fight["Kuma"])
        if message.content.lower().startswith('humandrills'):
            await message.channel.send(fight["Humandrills"])
        if message.content.lower().startswith('zoro vs hody'):
            await message.channel.send(fight["Zoro vs Hody"])
        if message.content.lower().startswith('pica'):
            await message.channel.send(fight["Pica"])
        if message.content.lower().startswith('kamazou'):
            await message.channel.send(fight["Kamazou"])
        if message.content.lower().startswith('killer'):
            await message.channel.send(fight["Killer"])
        if message.content.lower().startswith('hyouzou'):
            await message.channel.send(fight["Hyouzou"])
        if message.content.lower().startswith('monet'):
            await message.channel.send(fight["Monet"])
        if message.content.lower().startswith('fujitora'):
            await message.channel.send(fight["Fujitora"])
        if message.content.lower().startswith('carrot'):
            await message.channel.send(fight["Carrot"])
        if message.content.lower().startswith('samurais'):
            await message.channel.send(fight["Samurais"])
        if message.content.lower().startswith('denjiro'):
            await message.channel.send(fight["Denjiro"])
        if message.content.lower().startswith('hawkins'):
            await message.channel.send(fight["Hawkins"])
        if message.content.lower().startswith('oniwabanshu'):
            await message.channel.send(fight["Oniwabanshu"])
            
        if message.content.lower().startswith('gin and pearl'):
            await message.channel.send(fight["Gin and Pearl"])
        if message.content.lower().startswith('kurobi'):
            await message.channel.send(fight["Kurobi"])
        if message.content.lower().startswith('unluckies'):
            await message.channel.send(fight["Unluckies"])
        if message.content.lower().startswith('bon clay'):
            await message.channel.send(fight["Bon Clay"])
        if message.content.lower().startswith('satori'):
            await message.channel.send(fight["Satori"])
        if message.content.lower().startswith('enel'):
            await message.channel.send(fight["Enel"])
        if message.content.lower().startswith('aokiji'):
            await message.channel.send(fight["Aokiji"])
        if message.content.lower().startswith('franky'):
            await message.channel.send(fight["Franky"])
        if message.content.lower().startswith('sanji vs blueno'):
            await message.channel.send(fight["Sanji vs Blueno"])
        if message.content.lower().startswith('kalifa'):
            await message.channel.send(fight["Kalifa"])
        if message.content.lower().startswith('jabura'):
            await message.channel.send(fight["Jabura"])
        if message.content.lower().startswith('absalom'):
            await message.channel.send(fight["Absalom"])
        if message.content.lower().startswith('kuma'):
            await message.channel.send(fight["Kuma"])
        if message.content.lower().startswith('kizaru'):
            await message.channel.send(fight["Kizaru"])
        if message.content.lower().startswith('ivankov'):
            await message.channel.send(fight["Ivankov"])
        if message.content.lower().startswith('wadatsumi'):
            await message.channel.send(fight["Wadatsumi"])
        if message.content.lower().startswith('vergo'):
            await message.channel.send(fight["Vergo"])
        if message.content.lower().startswith('sanji vs doflamingo'):
            await message.channel.send(fight["Sanji vs Doflamingo"])
        if message.content.lower().startswith('judge'):
            await message.channel.send(fight["Judge"])
        if message.content.lower().startswith('oven'):
            await message.channel.send(fight["Oven"])
        if message.content.lower().startswith('big mom pirates'):
            await message.channel.send(fight["Big Mom Pirates"])
        if message.content.lower().startswith('daifuku'):
            await message.channel.send(fight["Daifuku"])
        if message.content.lower().startswith('kyoshiro family'):
            await message.channel.send(fight["Kyoshiro Family"])
        if message.content.lower().startswith('x-drake'):
            await message.channel.send(fight["X-Drake"])
        if message.content.lower().startswith('page one'):
            await message.channel.send(fight["Page One"])
            
        if message.content.lower().startswith('miss doublefinger'):
            await message.channel.send(fight["Miss Doublefinger"])
        if message.content.lower().startswith('Hotori and Kotori'):
            await message.channel.send(fight["Hotori and Kotori"])
        if message.content.lower().startswith('nami vs kalifa'):
            await message.channel.send(fight["Nami vs Kalifa"])
        if message.content.lower().startswith('cracker'):
            await message.channel.send(fight["Cracker"])
        if message.content.lower().startswith('kumadori'):
            await message.channel.send(fight["Kumadori"])
        if message.content.lower().startswith('miss valentine'):
            await message.channel.send(fight["Miss Valentine"])
        if message.content.lower().startswith('nami vs big mom'):
            await message.channel.send(fight["Nami vs Big Mom"])
        if message.content.lower().startswith('ulti'):
            await message.channel.send(fight["Ulti"])
            
        if message.content.lower().startswith('chew'):
            await message.channel.send(fight["Chew"])
        if message.content.lower().startswith('daddy masterson') or message.content.lower().startswith('daddy'):
            await message.channel.send(fight["Daddy"])
        if message.content.lower().startswith('mr 4 and miss merry christmas') or message.content.lower().startswith('mr 4'):
            await message.channel.send(fight["Mr 4"])
        if message.content.lower().startswith('satori'):
            await message.channel.send(fight["Satori"])
        if message.content.lower().startswith('perona'):
            await message.channel.send(fight["Perona"])
        if message.content.lower().startswith('onigashima guards'):
            await message.channel.send(fight["Onigashima guards"])
        if message.content.lower().startswith('sugar'):
            await message.channel.send(fight["Sugar"])
        if message.content.lower().startswith('trebol and sugar'):
            await message.channel.send(fight["Trebol and Sugar"])
        
        if message.content.lower().startswith('marines'):
            await message.channel.send(fight["Marines"])
        if message.content.lower().startswith('sogeking vs kumacy'):
            await message.channel.send(fight["Sogeking vs Kumacy"])
            
        if message.content.lower().startswith('pell'):
            await message.channel.send(fight["Pell"])
        if message.content.lower().startswith('robin vs crocodile'):
            await message.channel.send(fight["Robin vs Crocodile"])
        if message.content.lower().startswith('yama'):
            await message.channel.send(fight["Yama"])
        if message.content.lower().startswith('tashigi'):
            await message.channel.send(fight["Tashigi"])
        if message.content.lower().startswith('robin vs enel'):
            await message.channel.send(fight["Robin vs Enel"])
        if message.content.lower().startswith('spandam'):
            await message.channel.send(fight["Spandam"])
        if message.content.lower().startswith('tararan'):
            await message.channel.send(fight["Tararan"])
        if message.content.lower().startswith('hogback') or message.content.lower().startswith('dr hogback'):
            await message.channel.send(fight["Hogback"])
        
        if message.content.lower().startswith('sabaody'):
            await message.channel.send(fight["Sabaody"])
        if message.content.lower().startswith('oars'):
            await message.channel.send(fight["Oars"])
        if message.content.lower().startswith('baka song') or message.content.lower().startswith('luffy\'s baka song'):
            await message.channel.send(fight["Baka song"])
        if message.content.lower().startswith('sogeking theme song'):
            await message.channel.send(fight["Sogeking theme song"])
        if message.content.lower().startswith('bink\'s sake'):
            await message.channel.send(fight["Binks sake"])
        if message.content.lower().startswith('oden song'):
            await message.channel.send(fight["Oden song"])
    
def setup(bot):
    bot.add_cog(Events(bot))
