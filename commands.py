import requests
import json

def checkConnection():
    req = requests.get("https://overfast-api.tekrop.fr/heroes/")
    print(f"Status: {req.status_code}")
    if req.status_code == 200:
        return True
    else:
        return False


#Hero stuff
def heroData(name):
    req = requests.get(f"https://overfast-api.tekrop.fr/heroes/{name}")
    data = req.text
    jdata = json.loads(data)
    data = f"**Name: {jdata['name']}\nRole: {jdata['role']}\nLocation: {jdata['location']}\nDescription: {jdata['description']}**"
    return data

def imageGrab(endURL,command):
    req = requests.get(f"https://overfast-api.tekrop.fr/{endURL}")
    data = req.text
    jdata = json.loads(data)
    data = f"{jdata[command]}"
    return data

#Player stuff
def playerGrab(name,platform):#
    req = requests.get(f"https://overfast-api.tekrop.fr/players/{name}/summary")
    data = req.text
    jdata = json.loads(data)
    try:
    #There actually has to be a faster method to do this but it's too late for my brain to process the research
        data = f"**Name: {jdata['username']}\nTitle: {jdata['title']}\n\
         EndorsmentLVL: {jdata['endorsement']['level']}\n\
            RANKED\n\
            Tank:   {jdata['competitive'][platform]['tank']['division']}    {jdata['competitive'][platform]['tank']['tier']}\n\
            DPS:    {jdata['competitive'][platform]['damage']['division']}  {jdata['competitive'][platform]['damage']['tier']}\n\
            Support:{jdata['competitive'][platform]['support']['division']} {jdata['competitive'][platform]['support']['tier']}**"
    except:
        return "There was an error grabbing info, make sure you have the right name and the profile is set to public"
    return data
   