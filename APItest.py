#just a file for me to test run stuff
import requests
import json
req = requests.get("https://overfast-api.tekrop.fr/players/TheRuler420-1318/summary")
data = req.text
platform = 'pc'
jdata = json.loads(data)
data = f"**Name: {jdata['username']}\nTitle: {jdata['title']}\n\
         EndorsmentLVL: {jdata['endorsement']['level']}\n\
            RANKED\n\
            Tank:   {jdata['competitive'][platform]['tank']['tier']}\n\**"
print(data)

#data = f"Name: {jdata['name']}\nRole: {jdata['role']}\nDescription: {jdata['description']}"