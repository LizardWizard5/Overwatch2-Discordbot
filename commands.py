import requests
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import datetime

def checkConnection():
    dTime = datetime.datetime.now()
    print("checkConnection ran at "+dTime.strftime("%m/%d/%Y, %H:%M:%S"))
    req = requests.get("https://overfast-api.tekrop.fr/heroes/")
    print(f"Status: {req.status_code}")
    if req.status_code == 200:
        return True
    else:
        return False

#Hero stuff
def heroData(name):
    dTime = datetime.datetime.now()
    print("heroData ran at "+dTime.strftime("%m/%d/%Y, %H:%M:%S"))
    req = requests.get(f"https://overfast-api.tekrop.fr/heroes/{name.lower()}")
    data = req.text
    jdata = json.loads(data)
    
    try:
        data = f"**Name: {jdata['name']}\nRole: {jdata['role']}\nLocation: {jdata['location']}\nDescription: {jdata['description']}**"
    except:
        return f"There was an error grabbing the hero **\"{name}\"**. Make sure you entered the name correctly"
    return data

def imageGrab(endURL,command):
    req = requests.get(f"https://overfast-api.tekrop.fr/{endURL}")
    data = req.text
    jdata = json.loads(data)
    try:
        data = f"{jdata[command]}"
    except:
        return 'https://github.com/LizardWizard5/Overwatch2-Discordbot/blob/master/ErrorPortrait.png?raw=true'
    return data

#Player stuff
def playerGrab(name,platform):#
    dTime = datetime.datetime.now()
    print("playerGrab ran at "+dTime.strftime("%m/%d/%Y, %H:%M:%S"))
    name = name.replace("#","-")
    platform = platform.lower()
    
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
    font = ImageFont.truetype("Fonts/COOPERHEWITT-BOLD/CooperHewitt-Bold.otf", 29)#Sets text font. If you are using a linux system keep the slashes as they are but if you are running on windows, use backslash(\)
    pos = [[50, 175],[50, 225], [200, 175]]
    finalText.text((200, 20), data, fill =(244, 244, 244),font=font)#Writes text

    for x in range(0, len(roles)):
        finalText.text((pos[x][0], pos[x][1]), roles[x].upper()+":", fill =(244, 244, 244),font=font)#Writes text
    bites = BytesIO()#had to look this one up
    
    #maxsize = (1500, 512)
    #finalImage.thumbnail(maxsize, Image.ANTIALIAS)
    finalImage.save(bites, format="PNG", box=None,reducing_gap=2)#
    return bites
   