from io import BytesIO
import os
import discord

from dotenv import load_dotenv
import commands
import importlib
import discord.ext
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

tree = app_commands.CommandTree(bot)

load_dotenv()
TOKEN = os.getenv("TOKEN")

heroList = commands.heroList()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')






@tree.command(name = "hero",description="Returns information about a hero.")
async def hero(ctx:discord.Interaction, name:str):

  if(commands.checkConnection):
    endUrl = f"heroes/{name}"
    info = commands.heroData(name)
  else:
    endurl = open("error.png")
    info = "ERROR: There is a problem connecting to the API"
  commands.imageGrab(endUrl,'portrait')


  embed = discord.Embed( description=info[0])
  
  embed.set_thumbnail(url=f"{info[1]}")
  await ctx.response.send_message(embed=embed)

@hero.autocomplete("name")
async def hero_autocomplete(ctx: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
    options = heroList
    filtered_options = [option for option in options if current.lower() in option.lower()]
    choices = [app_commands.Choice(name=option, value=option) for option in filtered_options[:25]]
    #print(f"Autocomplete choices: {choices}")  # Debugging line
    return choices


@tree.command(name="reload",description="Syncs the commands with the discord server.")
async def reload(ctx:discord.Interaction):
  synced = await tree.sync()
  print(synced)
  await ctx.response.send_message("Commands reloaded")



@tree.command(name = "playersearch", description="Returns player stats.")
@app_commands.describe(username= "Your username with the # and numbers")
async def playersearch(ctx:discord.Interaction , username:str,platform:str):
  bites = commands.playerGrab(username,platform)#Had to look bites up
  bites.seek(0)
  await ctx.response.send_message("You're gonna have to click on the picture", file=discord.File(bites, filename="image.png"))#



@tree.command(description = "Returns whether or not the bot has connection to the API")
async def ping(interaction: discord.Interaction):
  if(commands.checkConnection()):
    response = "Connection found, everything should work."
  else:
    response = "It seems there is a connection issue with the API."
  await interaction.response(f"```{response}```")


@tree.command(name="getshop", description="Returns the current shop items.")
async def getShop(ctx: discord.Interaction):
    await ctx.response.defer()  # Defer the response to get more time to process
    images = commands.getShop()
    files = [discord.File(image, filename=f"image_{i}.png") for i, image in enumerate(images)]
    
    
    
    await ctx.followup.send(files=files)


"""
@bot.command(pass_context=True,description="Reloads all the functions associated with the commands. Only LizardWizard can run this")
async def reload(ctx):
  if(ctx.author.id == 266774102373564426):
    importlib.reload(commands)
    await ctx.respond("Functions at peak power!")
  else:
    await ctx.respond("No")

  """


@tree.command(name="herolist",description="Returns a list of all the heroes in Overwatch.")
async def herolist(ctx:discord.Interaction):

    heroList = commands.heroList()
    heroList = "\n".join(heroList)
    embed = discord.Embed(description=heroList)
    await ctx.response.send_message(embed=embed)


bot.run(TOKEN)  # Run the bot with the token


