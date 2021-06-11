import webbrowser
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import xml.etree.ElementTree as ET
import requests, json
import media_player
import old_modules
import vlc
import wikipedia
import old_modules


tree=ET.parse('registry.xml')
root=tree.getroot()

###DISTRIBUTOR###
def main(c,w):
    
    

    if(c=="004"):

        print(".../search sector\...")
        browser(w)


    if(c=="002"):
        print("../execution sector\...")
        executor(w)
    
        
    if(c=="003"):
        print("../Player Sector\..")
        player(w)

    if(c=="005"):
        print("File addition Sector")
        add_files()
    if(c=="006"):
        print("program addition Sector")
        add_app()

### GOOGLE SEARCH ###

def browser(w):
    s="https://www.google.com/search?q="
    x=len(w)
    
    s=s+" + "+w
    webbrowser.open(s)

###LOCAL-SOFTWARE-FIRE-UP###

def executor(w):
   print("In the Execution Sector")
   w=old_modules.chatterbot(w)
   i=int(root[1].text)
   flag=0
   for i in range(0,i):
       print(root[2][i][0].text)
       if(w==str(root[2][i][0].text)):
           print("File found "+str(root[2][i][0].text))
           print("Registered path: "+str(root[2][i][1].text))
           os.startfile(str(root[2][i][1].text))
           flag=1
           break
   if(flag==0):
        print("Application not found")
###LOCAL-VIDEO-PLAYER###

def player(w):
    w=old_modules.chatterbot(w)
    i=int(root[0].text)
    flag=0
    print(w)
    for x in range(0,i):
        print(str(x)+"- "+str(root[3][x].attrib['name']))
        if w==root[3][x].attrib['name']:
            print("files found")
            flag=1
            print("file_path_Found "+str(root[3][x].text))
            print("Now Playing: "+str(root[3][x].attrib['name']))
            os.startfile(root[3][x].text)
            break
    if(flag==0):
        print("File not found")


###REGISTRY-APP-UPDATER####


def add_app():
    print("app adding module")
    total_apps=int(root[1].text)
    app_id=str(total_apps+1)
    ET.SubElement(root[2],"app")
    root[2][total_apps+1].tag="app"
    root[2][total_apps+1].set("id",app_id)
    print("Give this app a name")
    app_name=input()
    print("url:")
    url=input()
    ET.SubElement(root[2][total_apps+1],"name")
    root[2][total_apps+1][0].text=app_name
    ET.SubElement(root[2][total_apps+1],"url")
    root[2][total_apps+1][1].text=url
    root[0].text=str(int(root[0].text)+1)
    tree.write("registry.xml")
    f=open("C:/Users/LENOVO/programs/Anaconda3/Lib/site-packages/chatterbot_corpus/data/english/registry.yml","a")
    q=app_name
    a=app_name
    s="\n- - "+q+"\n  - "+a
    f.write(s)
    f.close()

###REGISTRY-VIDEO-UPDATER###

def add_files():
    print("file adding module")
    total_files=int(root[0].text)
    
    file_name=input("Give the name of the file: ")
    file_loc=input("Give the location of the file: ")

    ET.SubElement(root[3],"url")
    root[3][total_files].text=file_loc
    root[3][total_files].set("name",file_name)
    root[0].text=str(int(root[0].text)+1)
    tree.write("registry.xml")
    f=open("C:/Users/LENOVO/programs/Anaconda3/Lib/site-packages/chatterbot_corpus/data/english/registry.yml","a")
    q=file_name
    a=q
    s="\n- - "+q+"\n  - "+a  
    f.write(s)
    f.close()

###WEATHER-API###

def get_weather(city_name):


   
    api_key='<api-key>'
    url="https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key


    response=requests.get(url).json()
    
    
    if response["cod"] != "404":


        data=response["main"]
        tempreture=data["temp"]-273.15
        pressure=data["pressure"]
        humidity=data["humidity"]

        
        _string=("It is currently "+str(round(tempreture))+" degree at the place with humidity at "+str(humidity)+" percentage and atmospheric pressure at "+str(pressure)+" hPa at "+city_name+". ")
        _string=_string+("Visibility lies at "+str(response['visibility'])+" meters and wind speed is at "+str(response['wind']['speed'])+" Meters per second. ")
        _string=_string+("Wind gust at "+str(response['wind']['gust'])+". ")
        try: 
            _string=_string+("Rate of precipitation at "+str(response['rain']['1h'])+" per hour")
        except:
            _string=_string+("No precipitation in this area. ")
        _string=_string+(" Weather description says "+response["weather"][0]["description"])
    else:
        _string=("could not find the city.")

    return _string

###YOUTUBE UTILS####
def youtube(keywords):
    url=media_player.Player.get_local_url(keywords)
    media=vlc.MediaPlayer(url)
    media.play()
    while(1):
        command=old_modules.user_input()
        if(command=="play"):
            media.play()
        elif(command=="pause"):
            media.pause()
        elif(command=="stop"):
            media.stop()
            break
        else:
            print("illegal command")
    media.release()

#youtube(old_modules.user_input())

##Wikipedia Module##

def wiki(keywords):
    try:
        arr=wikipedia.search(keywords)
        info=wikipedia.summary(arr[0])
        return info
    except Exception as e:

        return "wikipedia has no info on "+keywords

