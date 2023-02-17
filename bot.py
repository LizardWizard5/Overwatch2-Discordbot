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

@bot.command()

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

@bot.command()

async def player(ctx, namedashnumber:discord.Option(str),pcorconsole: discord.Option(str)):
  endUrl = f"players/{namedashnumber}/summary"
  embed = discord.Embed(description=f"{commands.playerGrab(namedashnumber,pcorconsole)}")
  embed.set_thumbnail(url=f"{commands.imageGrab(endUrl,'avatar')}")
  await ctx.respond(embed=embed)

bot.run(TOKEN) # run the bot with the token

