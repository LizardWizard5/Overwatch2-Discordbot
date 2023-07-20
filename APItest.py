import requests
import json


name = "TheRuler420-1318"
platform = "PC"


req = requests.get(f"https://overfast-api.tekrop.fr/players/{name}/summary")
data = req.text
jdata = json.loads(data)
    
data = f"{jdata['username']}\n\n{jdata['title']}\n\nEndorsmentLVL: {jdata['endorsement']['level']}\n\n"
print(data)