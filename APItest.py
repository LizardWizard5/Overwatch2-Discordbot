#just a file for me to test run stuff
import requests
import json
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

