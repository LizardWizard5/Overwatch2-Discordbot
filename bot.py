import discord
import commands

bot = discord.Bot()
#This is so I can push without worrying about removing my token because password is in my gitignore
file = open('password', 'r')
text = file.readline()
TOKEN = text
file.close()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command(description = "Returns information about any given hero.")
async def hero(ctx, name: discord.Option(str)):
  '''
  :param name: Hero name. some heroes have weird formatting like soldier76 -> soldier-76
  '''
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

async def player(ctx, name:discord.Option(str),platform: discord.Option(str)):
  '''
  :param name (str): Replace # with a - EX. TheRuler420-1318
  :param platform: PC or CONSOLE
  '''
  endUrl = f"players/{name}/summary"
  embed = discord.Embed(description=f"{commands.playerGrab(name,platform)}")
  embed.set_thumbnail(url=f"{commands.imageGrab(endUrl,'avatar')}")
  await ctx.respond(embed=embed)

@bot.command(description = "Returns whether or not the bot has connection to the API")

async def ping(ctx):
  if(commands.checkConnection):
    response = "Connection found, everything should work."
  else:
    response = "It seems there is a connection issue with the API."
  await ctx.respond(f"```{response}```")

bot.run(TOKEN) # run the bot with the token

