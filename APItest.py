#just a file for me to test run stuff
import requests
import json
req = requests.get("https://overfast-api.tekrop.fr/heroes/cassidy")
data = req.text
jdata = json.loads(data)
print(f"Story: {jdata['story']}")
#data = f"Name: {jdata['name']}\nRole: {jdata['role']}\nDescription: {jdata['description']}"