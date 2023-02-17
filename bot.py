import discord
import commands

bot = discord.Bot()

TOKEN = ""


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.command()
# pycord will figure out the types for you
async def hero(ctx, name: discord.Option(str)):
  # you can use them as they were actual integers
    endUrl = f"heroes/{name}"
    embed = discord.Embed(title="Portrait", description=f"{commands.heroData(name)}")
    embed.set_image(url=f"{commands.imageGrab(endUrl)}")
    await ctx.respond(embed=embed)

    
bot.run(TOKEN) # run the bot with the token

