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
    req = requests.get(f"https://overfast-api.tekrop.fr/heroes/{name.lower()}")
    data = req.text
    jdata = json.loads(data)
    try:
        data = f"**Name: {jdata['name']}\nRole: {jdata['role']}\nLocation: {jdata['location']}\nDescription: {jdata['description']}**"
    except:
        return f"There was an error grabbing the hero **\"{name}\"**. Make sure you entered the name correctly"
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
    req = requests.get(f"https://overfast-api.tekrop.fr/players/{name}/summary")
    data = req.text
    jdata = json.loads(data)
    try:
    #There actually has to be a faster method to do this but it's too late for my brain to process the research
        data = f"Name: {jdata['username']}\nTitle: {jdata['title']}\nEndorsmentLVL: {jdata['endorsement']['level']}\n"
        roles = ['tank','support','damage']
        for role in roles:
            data+=(f"{role}: {jdata['competitive'][platform][role]['division']} {jdata['competitive'][platform][role]['tier']}\n")
    except:
        return "There was an error grabbing info, make sure you typed all the fields correctly and the profile is set to public"
    return data
   