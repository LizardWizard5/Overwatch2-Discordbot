#just a file for me to test run stuff

import requests
import json
from PIL import Image, ImageDraw, ImageFont
from imageio import imread
req = requests.get("https://overfast-api.tekrop.fr/players/TheRuler420-1318/summary")
data = req.text
platform = 'pc'
jdata = json.loads(data)
data = f"Name: {jdata['username']}\nTitle: {jdata['title']}\n\
EndorsmentLVL: {jdata['endorsement']['level']}\n"
roles = ['tank','support','damage']
for role in roles:
    data+=(f"{role}: {jdata['competitive'][platform][role]['division']} {jdata['competitive'][platform][role]['tier']}\n")
print(f"**{data}**")

print(jdata['avatar'])


size = (800,800)#Size of image variable
#img  = Image.new( mode = "RGB", size = size, color = (209, 123, 193) )#Creates image of size 500x500px and sets the background colour
img = Image.open("resources\Overwatch 2 Screenshot 2023.04.17 - 01.22.00.16.png")
img2 = Image.open(requests.get(jdata['avatar'], stream=True).raw)#Gets the image from api and stores to variable
back_im = img.copy()#Copies img data to another variable
back_im.paste(img2, (100, 50))#pastes the avatar image to image 1 copy


d1 = ImageDraw.Draw(back_im)#Sets up image for adding text
font = ImageFont.truetype("arial.ttf", 40)#Sets text font
#back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)
d1.text((65, 10), data, fill =(0, 0, 0),font=font)#Writes text
back_im.show()
