import requests
import json
def heroData(name):
    req = requests.get(f"https://overfast-api.tekrop.fr/heroes/{name}")
    data = req.text
    jdata = json.loads(data)
    data = f"Name: {jdata['name']}\nRole: {jdata['role']}\nLocation: {jdata['location']}\nDescription: {jdata['description']}"
    return data

def imageGrab(endURL):
    req = requests.get(f"https://overfast-api.tekrop.fr/{endURL}")
    data = req.text
    jdata = json.loads(data)
    data = f"{jdata['portrait']}"
    return data