import os, discord
import discord
from discord.ext import commands

TOKEN = os.environ['token']
creatorid = os.environ['creatorid']

client = commands.Bot(command_prefix = ".")
client.remove_command("help")
bot_vesrion = ("Bot Version is 1.0.0 - Under Development.")
bot_version_credits = ("Bot Version is 1.0.0 (Under Development) by Joseph (DaSniKe)")

@client.event #Confirmation that the bot is running - Sent through the console
async def on_ready():
	await client.change_presence(game=discord.Game(name="with DaSniKe xD"))
	print("DaSniKe BOT is now running!")
	print(bot_version_credits)

@client.command() # .dasnike command
async def dasnike():
	await client.say("What you want bruh?")

@client.command(pass_context=True) #Bot Version with Owner permission
async def version(ctx):
    if ctx.message.author.id ==['creatorid']:
        await client.say (bot_vesrion)
    else:
        await client.say("This command can only be used by the bot creator.")

@client.command()
async def help():
	await client.say("The dude programming me is very slow, he didn't even make the help command -_-")

client.run(TOKEN)
