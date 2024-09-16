import requests, json, colorama, datetime, time 
from colorama import Fore, init

init()

bio = False
pronouns = False
both = False

Reset = Fore.RESET
Magenta = Fore.MAGENTA
Black = Fore.LIGHTBLACK_EX
Green = Fore.GREEN
Red = Fore.RED

with open("config.json", "r") as file:   
    print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Magenta}[Info] Loading Config...{Reset}")
    config = json.load(file)
    token = config["Token"]
    bio_1 = config["Bio_1"]
    bio_2 = config["Bio_2"]
    prounoun_1 = config["Pronoun_1"]
    prounoun_2 = config["Pronoun_2"]
    delay = int(config["Delay"]) 
    print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Green}[Success] Done Loading Config{Reset}")
    pronouns_or_bio = input(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Magenta}[?] pronouns, bio or both?\n{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Magenta}[?] {Reset}")
    if pronouns_or_bio == "bio":
        bio = True
    elif pronouns_or_bio == "pronouns":
        pronouns = True   
    elif pronouns_or_bio == "both":
        both = True     
    else:
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Red}[Failed] Wrong input use 'pronouns', 'bio' or 'both'{Reset}")    
        time.sleep(2)
        exit(0)
    

def update_bio(bio):
    url = "https://discord.com/api/v9/users/@me/profile"
    payload = {
        "bio": bio
    }
    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Green}[Success] Updated Bio to {bio}{Reset}")
    else:        
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Red}[Failed] Failed updating bio to {bio} - {response.status_code}{Reset}")      

def update_pronouns(pronouns):
    url = "https://discord.com/api/v9/users/@me/profile"
    payload = {
        "pronouns": pronouns
    }

    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Green}[Success] Updated Pronouns to {pronouns}{Reset}")
    else:        
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Red}[Failed] Failed updating Pronouns to {pronouns} - {response.status_code}{Reset}")  
            
def update_both(bio, pronouns):
    url = "https://discord.com/api/v9/users/@me/profile"
    payload = {
        "bio": bio,
        "pronouns": pronouns
    }

    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Green}[Success] Updated Pronouns and Bio to {pronouns} and {bio}{Reset}")
    else:        
        print(f"{Black}{datetime.datetime.now().strftime('%H:%M:%S')} -> {Red}[Failed] Failed updating Pronouns and bio to {pronouns} and {bio} - {response.status_code}{Reset}")               

while True:
    if bio == True:
        update_bio(bio_1)
        time.sleep(delay)
        update_bio(bio_2)
        time.sleep(delay)
    elif pronouns == True:
        update_pronouns(prounoun_1)
        time.sleep(delay)
        update_pronouns(prounoun_2)
        time.sleep(delay)
    elif both == True:
        update_both(bio_1, prounoun_1)
        time.sleep(delay)
        update_both(bio_2, prounoun_2) 
        time.sleep(delay)   

