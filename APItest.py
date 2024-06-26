import requests
import json
import commands
import os
from PIL import Image, ImageDraw, ImageFont

from dotenv import load_dotenv




load_dotenv()
url = os.getenv("shopURL")
req = requests.get(url)
data = req.text
jdata = json.loads(data)

images = []#Used to store image with the text we add using PIL
for item in jdata['mtxCollections'][0]['items']:
    i=0
    bgImg = Image.open(requests.get("https:"+item['image']['url'], stream=True).raw).convert("RGBA")#Gets the image from api and stores to variable
    finalText = ImageDraw.Draw(bgImg)#Sets up image for adding text
        

    fontPath = os.path.join("Fonts","COOPERHEWITT-BOLD","CooperHewitt-Bold.otf")#Sets up the font path regardless of OS
    font = ImageFont.truetype(fontPath, 50)
    finalText.text((50, 50), item['title'], fill =(244, 244, 244),font=font)
    font = ImageFont.truetype(fontPath, 40)
    finalText.text((50, 100), item['description'], fill =(244, 244, 244),font=font)
    font = ImageFont.truetype(fontPath, 30)
    if(item['price']['discountAmount'] == None):
        finalText.text((50, 150), item['price']['fullAmount'], fill =(244, 244, 244),font=font)
    else:
        finalText.text((50, 150), item['price']['discountAmount'], fill =(244, 244, 244),font=font)
    bgImg.show()
    #bgImg.save(f"test{item['order']}.png", format="PNG", box=None,reducing_gap=2)
    

"""


response = requests.get("https://overfast-api.tekrop.fr/players/TheRuler420-1318/summary")
data = response.text
jdata = json.loads(data)

print("Comp stat")
print(jdata['competitive']['pc']['support'])
if jdata['competitive']['pc']['support'] == None:
    print("None support")

req = requests.get('https://us.shop.battle.net/api/itemshop/pages/blt01ee8af4f4da5e5f?userId=0&locale=en-US')
data = req.text
jdata = json.loads(data)

#print(f"{jdata['mtxCollections'][0]['items'][0]}")
for x in range(0,len(jdata['mtxCollections'][0]['items'])):
    print(jdata['mtxCollections'][0]['items'][x]['title'])


"""
"""
 {
	'cmsId': None,
	'order': 0,
	'slug': 'overwatch-mythos-mega-bundle',
	'productIds': [1585302, 1584572],
	'subscriptionIds': [],
	'title': 'Mythos Mega Bundle',
	'destination': '/family/overwatch/items/1591985/mythos-mega-bundle',
	'franchiseIcon': {
		'name': 'Overwatch 2',
		'iconUrl': 'https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blt7e22237aad327854/63db19a1592f74643d1a389a/Overwatch2_(1).svg', 
		'slug': None, 
		'anchorText': None
	}, 
	'cardLogoUrl': None, 
	'categoryId': None, 
	'description': 'Legendary | Bundle (2 items)', 
	'marketingText': None, 
	'marketingBadge': None, 
	'price': {
		'currency': 'XWC',
		'fullAmount': '3,800\xa0Coins',
		'discountAmount': '2,800\xa0Coins',
		'labelFormat': None,
		'iconUrl': 'https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blta0dcc11657537871/OW2_VirtualCurrency.svg',
		'raw': 2800.0,
		'discountPercentage': 26.31
	}, 
	'eligibility': None, 
	'panelButtonSection': None, 
	'expiresAtMs': None, 
	'image': {
		'width': 1920.0,
		'height': 1080.0,
		'url': '//bnetproduct-a.akamaihd.net//f8f/61e317cf8dae674a0c4cb7bb70d17a88-S8_Mythos_Web_1920x1080_ux.png',
		'description': None
	}, 
	'ecommerceAnalytics': {
		'products': {
			'1591985': {
				'name': 'S08 - SHOP - BUNDLE - Mythos Mega Bundle',
				'brand': 'OVERWATCH',
				'category': 'Game Add-on'
			}
		},
		'brand': 'OVERWATCH',
		'category': 'Game Add-on'
	}
}
"""
