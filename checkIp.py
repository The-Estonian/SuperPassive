import requests

def checkIp(ip=None):
    if ip and ip != "127.0.0.1":
        url = f'http://ip-api.com/json/{ip}'
    else:
        url = 'http://ip-api.com/json'
    
    response = requests.get(url)
    data = response.json()
    return data
    
    # ip = data.get('query')
    # city = data.get('city')
    # region = data.get('regionName')
    # country = data.get('country')
    # latitude = data.get('lat')
    # longitude = data.get('lon')
    
    # return {
    #     'ip': ip,
    #     'city': city,
    #     'region': region,
    #     'country': country,
    #     'latitude': latitude,
    #     'longitude': longitude
    # }