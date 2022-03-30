import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_message(message):
 
    if(message.author.name == "suskey"):
        if('!' in message.content):
            return
        await message.delete()
    
bot.run("", bot=False)
