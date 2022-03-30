import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_message(message):
 
    if(message.author.name == "suskey"):
        if('!' in message.content):
            return
        await message.delete()
    
bot.run("OTQ4MDU3NzAzNTk3NjA0ODc0.Yjihtw.n_OlxnrZBHTdw_8njGBkRdYY_dk", bot=False)