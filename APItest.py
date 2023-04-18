#just a file for me to test run stuff

import requests
import json
from PIL import Image, ImageDraw, ImageFont
from imageio import imread
req = requests.get("https://overfast-api.tekrop.fr/players/TheRuler420-1318/summary")
data = req.text
platform = 'pc'
jdata = json.loads(data)
data = f"{jdata['username']}\n\n{jdata['title']}\n\nEndorsmentLVL: {jdata['endorsement']['level']}\n\n"
roles = ['tank','support','damage']
for role in roles:
    data+=(f"{role.upper()}:\n\n")
print(f"**{data}**")

print(jdata['avatar'])


size = (800,800)#Size of image variable
#img  = Image.new( mode = "RGB", size = size, color = (209, 123, 193) )#Creates image of size 500x500px and sets the background colour
bgImg = Image.open(requests.get(jdata['namecard'], stream=True).raw)
avatar = Image.open(requests.get(jdata['avatar'], stream=True).raw)#Gets the image from api and stores to variable
#avatarOutline = Image.new( mode = "RGB", size = size, color = (209, 123, 193) )
#endorseLvl = Image.open(requests.get(jdata['endorsement']['frame'], stream=True).raw)

roleImages=[]


back_im = bgImg.copy()#Copies img data to another variable

back_im.paste(avatar, (200, 50))#pastes the avatar image to image 1 copy
yPos= 100
for x in range(0, len(roles)):
    back_im.paste(Image.open(requests.get(jdata['competitive'][platform][roles[x]]['rank_icon'], stream=True).raw).convert('RGBA').resize((50,50)), (200, yPos))
    yPos +=100



d1 = ImageDraw.Draw(back_im)#Sets up image for adding text
font = ImageFont.truetype("Fonts\COOPERHEWITT-BOLD\CooperHewitt-Bold.otf", 28)#Sets text font
#back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)
d1.text((500, 10), data, fill =(244, 244, 244),font=font)#Writes text
back_im.show()
