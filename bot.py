from io import BytesIO
import os
import discord
from discord import option
import commands
from dotenv import load_dotenv
import importlib

bot = discord.Bot()
load_dotenv()
TOKEN = os.getenv("TOKEN")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command(description = "Returns information about any given hero.")
async def hero(ctx, name: discord.Option(str)):

  if(commands.checkConnection):
    endUrl = f"heroes/{name}"
    info = f"{commands.heroData(name)}"
  else:
    endurl = open("error.png")
    info = "ERROR: There is a problem connecting to the API"
    
  embed = discord.Embed( description=info)
  embed.set_thumbnail(url=f"{commands.imageGrab(endUrl,'portrait')}")
  await ctx.respond(embed=embed)

@bot.command(description="Returns player stats.")
@option("name", description="Blizzard name and tag EX. TheRuler420-1318")
@option("platform", choices=["pc","console"])
async def player(ctx, name:str,platform:str):
  bites = commands.playerGrab(name,platform)#Had to look bites up
  bites.seek(0)
  await ctx.respond("You're gonna have to click on the picture", file=discord.File(bites, filename="image.png"))

@bot.command(description = "Returns whether or not the bot has connection to the API")
async def ping(ctx):
  if(commands.checkConnection()):
    response = "Connection found, everything should work."
  else:
    response = "It seems there is a connection issue with the API."
  await ctx.respond(f"```{response}```")
@bot.command(pass_context=True,description="Reloads all the functions associated with the commands. Only LizardWizard can run this")
async def reload(ctx):
  if(ctx.author.id == 266774102373564426):
    importlib.reload(commands)
    await ctx.respond("Functions at peak power!")
  else:
    await ctx.respond("No")

bot.run(TOKEN) # run the bot with the token