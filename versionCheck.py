#This is going to monitor if the version in github is the same as the local version. If not download github version and run new version
import os
import requests
from urllib.request import urlopen

fileNames = [[["bot.py"],["https://raw.githubusercontent.com/LizardWizard5/Overwatch2-Discordbot/master/bot.py"]],
             [["commands.py"],["https://raw.githubusercontent.com/LizardWizard5/Overwatch2-Discordbot/master/commands.py"]]]

def runBot():
    import bot

file = fileNames[0][1]
print(file)
 
"""
versionTxt = open("version.txt","r")
version = versionTxt.readline()
versionTxt.close()
githubVersion = urlopen("https://raw.githubusercontent.com/LizardWizard5/Overwatch2-Discordbot/master/version.txt")
githubVersion = str(githubVersion.read())
githubVersion = githubVersion.split("'")[1]

versionTxt = open("version.txt","w")
version = versionTxt.write(githubVersion)
versionTxt.close()


if(version == githubVersion):
    runBot()
else:
    for x in range(len(fileNames)):
        print(fileNames[x][1])
        replacementFile = urlopen(fileNames[x][1])
        
        replacementFile=str(replacementFile.read())
        newFile = open(fileNames[x][1],"w")
        newFile.write(replacementFile)
        newFile.close()

"""


