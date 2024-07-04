import requests
import json
from writeToFile import get_unique_filename
from bs4 import BeautifulSoup

def fullName(fullname):
    lastname = fullname.split(" ")[1]
    firstname = fullname.split(" ")[0]
    url = f"https://www.118000.fr/search?who={firstname}+{lastname}"
    response = requests.get(url)
    
    soup = BeautifulSoup(response.content, "html.parser")
    allFoundUsers = soup.findAll("section", {"class": "card part lnk"})

    checkedFilename = get_unique_filename("result.txt")
    with open(checkedFilename, 'w') as file:

        for target in allFoundUsers:
            fetchedFullname = target.find(attrs={"data-title":True}).get("data-title").split()
            surname = fetchedFullname[0].capitalize()
            firstName = " ".join(fetchedFullname[1:]).capitalize()
            info = json.loads(target.find(attrs={"data-info":True}).get("data-info"))
            address = target.find(attrs={"data-address":True}).get("data-address")
            address = address.replace("<br>", " ").replace("<br/>", " ")

            print("First name: ",firstName)
            file.write(f"First name: {firstName}\n")

            print("Last name: ",surname)
            file.write(f"Last name: {surname}\n")

            if len(info["address"]) > 0:
                print("Address: ",info["address"])
                file.write(f"Address: {info["address"]}\n")

            print(info["cp"], info["city"])
            file.write(f"{info["cp"]} {info["city"]}\n")

            print("Number: ", info["mainLine"])
            file.write(f"Number: {info["mainLine"]}\n")
            print("-----------------------------------")
            file.write(f"-----------------------------------\n")
