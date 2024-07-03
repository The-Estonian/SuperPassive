import requests
from bs4 import BeautifulSoup

def check_facebook(username):
    url = f"https://www.facebook.com/{username}"
    response = requests.get(url)
    if response.status_code != 200:
        return False
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: check for the presence of a profile name element
    pageTitle = soup.find('title')
    print(pageTitle)
# print(check_facebook("kristi.toom.75"))

def check_twitter(username):
    url = f"https://twitter.com/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_name = soup.find('a', {'class': 'ProfileHeaderCard-nameLink'})
        
        if profile_name:
            return True
        else:
            return False
    else:
        print(f"Error fetching URL: {url}. Status code: {response.status_code}")
        return False

check_facebook("qqwweerr")