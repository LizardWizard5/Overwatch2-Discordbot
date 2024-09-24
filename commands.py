import requests
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
import datetime
from dotenv import load_dotenv


def heroList():
    req = requests.get("https://overfast-api.tekrop.fr/heroes")
    data = req.text
    jdata = json.loads(data)
    heroList = []
    for x in jdata:
        heroList.append(x['key'])
    return heroList

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
        data = [f"**Name: {jdata['name']}\nRole: {jdata['role']}\nLocation: {jdata['location']}\nDescription: {jdata['description']}**", f"{jdata['portrait']}"]  
    except:
        return [f"There was an error grabbing the hero **\"{name}\"**. Make sure you entered the name correctly","https://github.com/LizardWizard5/Overwatch2-Discordbot/blob/master/ErrorPortrait.png?raw=true"]
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

    fontPath = os.path.join("Fonts","COOPERHEWITT-BOLD","CooperHewitt-Bold.otf")#Sets up the font path regardless of OS
    font = ImageFont.truetype(fontPath, 29)#Sets text font.

    if(data == '{"error":"Player not found"}'):
        return returnErrorImage("There was an error grabbing the player.\nMake sure you entered the name and platform correctly.")
    
    data = f"{jdata['username']}\n\n{jdata['title']}\n\nEndorsmentLVL: {jdata['endorsement']['level']}\n\n"
    roles = ['tank','damage','support']

    bgImg = Image.open(requests.get(jdata['namecard'], stream=True).raw)
    avatar = Image.open(requests.get(jdata['avatar'], stream=True).raw)#Gets the image from api and stores to variable
    finalImage = bgImg.copy()#Copies img data to another variable
    finalImage.paste(avatar, (50, 20))#pastes the avatar image to image 1 copy

    pos = [[140,160],[200,210],[350,160]]
    for x in range(0, len(roles)):#Massive shoutout to WuTeEf on Realm of the Mad God! This would have taken me several hours to figure out.
        if(jdata['competitive']['pc'][roles[x]] == None):
            imagePath = os.path.join("Resources","UnknownRank.png")
            roleImage=Image.open(imagePath).convert("RGBA").resize((40,45))
        else:
            roleImage=Image.open(requests.get(jdata['competitive'][platform][roles[x]]['rank_icon'], stream=True).raw).convert("RGBA").resize((40,45))
        alpha = roleImage.split()[-1]
        finalImage.paste(roleImage,(pos[x][0], pos[x][1]),mask=alpha)
    
    finalText = ImageDraw.Draw(finalImage)#Sets up image for adding text
    
    pos = [[50, 175],[50, 225], [200, 175]]
    finalText.text((200, 20), data, fill =(244, 244, 244),font=font)#Writes text

    for x in range(0, len(roles)):
        finalText.text((pos[x][0], pos[x][1]), roles[x].upper()+":", fill =(244, 244, 244),font=font)#Writes text
    bites = BytesIO()#had to look this one up
    
    #maxsize = (1500, 512)
    #finalImage.thumbnail(maxsize, Image.ANTIALIAS)
    finalImage.save(bites, format="PNG", box=None,reducing_gap=2)#
    return bites

def returnErrorImage(message):
    fontPath = os.path.join("Fonts","COOPERHEWITT-BOLD","CooperHewitt-Bold.otf")#Sets up the font path regardless of OS
    font = ImageFont.truetype(fontPath, 29)#Sets text font.
    errorImg = Image.open("ErrorPortrait.png")
    errorText = ImageDraw.Draw(errorImg)
    #Align text to center


    errorText.text((20, 20), "ERROR", fill =(255, 0, 0),font=font)
    errorText.text((20, errorImg.height-100), message, fill =(255, 0, 0),font=font)
    bites = BytesIO()
    errorImg.save(bites, format="PNG")
    return bites
   
def getShop():

    load_dotenv()
    url = os.getenv("shopURL")
    req = requests.get(url)
    data = req.text
    jdata = json.loads(data)

    dTime = datetime.datetime.now()
    print("getShop ran at "+dTime.strftime("%m/%d/%Y, %H:%M:%S"))

    currencyLocation = os.path.join("resources","OW2_VirtualCurrency.png")
    currency = Image.open(currencyLocation).convert("RGBA")
    currency = currency.resize((50,50))
    gradientFade = Image.open(os.path.join("resources","GradientFade.png"))#.convert("RGBA")

    alpha = currency.split()[-1]

    images = []#Used to store image with the text we add using PIL
    for item in jdata['mtxCollections'][0]['items']:
        bgImg = Image.open(requests.get("https:"+item['image']['url'], stream=True).raw).convert("RGBA")#Gets the image from api and stores to variable
         # Resize gradientFade to match the width of bgImg
        gradientFade = gradientFade.resize((bgImg.width, 200))
        
        # Create a new image to composite the gradient on
        gradientLayer = Image.new("RGBA", bgImg.size)
        gradientLayer.paste(gradientFade, (0, int(bgImg.height) - 235), mask=gradientFade.split()[-1])

        # Composite the gradient on top of the background image
        bgImg = Image.alpha_composite(bgImg, gradientLayer)
        
        finalText = ImageDraw.Draw(bgImg)#Sets up image for adding text
        
       
        
        fontPath = os.path.join("Fonts","COOPERHEWITT-BOLD","CooperHewitt-Bold.otf")#Sets up the font path regardless of OS
        font = ImageFont.truetype(fontPath, 50)
        finalText.text((50, int(item['image']['height']) - 210), item['title'], fill =(244, 244, 244),font=font)
        font = ImageFont.truetype(fontPath, 40)
        finalText.text((50, int(item['image']['height']) -150), item['description'], fill =(244, 244, 244),font=font)
        font = ImageFont.truetype(fontPath, 30)
        if(item['price']['discountAmount'] == None):
            finalText.text((110, int(item['image']['height']) - 100), item['price']['fullAmount'], fill =(244, 244, 244),font=font)
        else:
            finalText.text((110, int(item['image']['height']) - 100), item['price']['discountAmount'], fill =(244, 244, 244),font=font)
        
        bgImg.paste(currency, (50, int (item['image']['height']) - 110),mask=alpha)

        bites = BytesIO()
        bgImg.save(bites, format="PNG")
        bites.seek(0) 
        images.append(bites)
    return images




