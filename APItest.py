import requests
import json
from PIL import Image, ImageDraw, ImageFont

def playerGrab(name,platform):#
    #Kinda unoptimised, takes about a second or two
    req = requests.get(f"https://overfast-api.tekrop.fr/players/{name}/summary")
    data = req.text
    jdata = json.loads(data)
    data = f"{jdata['username']}\n\n{jdata['title']}\n\nEndorsmentLVL: {jdata['endorsement']['level']}\n\n"
    roles = ['tank','damage','support']

    bgImg = Image.open(requests.get(jdata['namecard'], stream=True).raw)
    avatar = Image.open(requests.get(jdata['avatar'], stream=True).raw)#Gets the image from api and stores to variable
    finalImage = bgImg.copy()#Copies img data to another variable
    finalImage.paste(avatar, (50, 20))#pastes the avatar image to image 1 copy

    pos = [[140,160],[200,210],[350,160]]
    for x in range(0, len(roles)):#Massive shoutout to WuTeEf on Realm of the Mad God! This would have taken me several hours to figure out.
        roleImage=Image.open(requests.get(jdata['competitive'][platform][roles[x]]['rank_icon'], stream=True).raw).convert("RGBA").resize((40,45))
        alpha = roleImage.split()[-1]
        finalImage.paste(roleImage,(pos[x][0], pos[x][1]),mask=alpha)
    finalText = ImageDraw.Draw(finalImage)#Sets up image for adding text
    font = ImageFont.truetype("Fonts\COOPERHEWITT-BOLD\CooperHewitt-Bold.otf", 29)#Sets text font
    pos = [[50, 175],[50, 225], [200, 175]]
    finalText.text((200, 20), data, fill =(244, 244, 244),font=font)#Writes text

    for x in range(0, len(roles)):
        finalText.text((pos[x][0], pos[x][1]), roles[x].upper()+":", fill =(244, 244, 244),font=font)#Writes text
    return finalImage

image = Image.open(playerGrab("TheRuler420-1318","pc"))#
image.show()
#bites = BytesIO()
#image.save(bites, format="PNG")
#bites.seek(0)
#dfile = discord.File(bites, filename="image.png")
"""
#Player stuff
def playerGrab(name,platform):#
    req = requests.get(f"https://overfast-api.tekrop.fr/players/{name}/summary")
    data = req.text
    jdata = json.loads(data)
    try:
    #There actually has to be a faster method to do this but it's too late for my brain to process the research
        data = f"Name: {jdata['username']}\nTitle: {jdata['title']}\nEndorsmentLVL: {jdata['endorsement']['level']}\n"
        roles = ['tank','support','damage']
        for role in roles:
            data+=(f"{role}: {jdata['competitive'][platform][role]['division']} {jdata['competitive'][platform][role]['tier']}\n")
    except:
        return "There was an error grabbing info, make sure you typed all the fields correctly and the profile is set to public"
        raise
    return data
"""