#Before using this script make sure to get the stormglass.io API authentication 
#token saved at the first line in a file caled "authtoken.txt" in the same 
#directory of this script.
#Thank you

import json
import requests
from geopy.geocoders import Nominatim

#Step 1: Get user coordinates based on user address
loc = Nominatim(user_agent="GetLoc")
address = str(input("Enter your address: "))
while (address == ""):
    address = str(input("Enter your address: "))
print(f'Your address is {address}')
getLoc = loc.geocode(address)
print(f'Your coordinates are lat:{getLoc.latitude} long:{getLoc.longitude}')

#Step 2: Get the windspeed and direction
#This step uses an API provided for free by stormglass.io
#If you haven't yet registered with them, please do so.
#They provide the authentication token for the API.
#Till the creation of this program the free plan of the API 
#allows for 10 requests per day

#Step 2a: Check the authentication token in a file
with open("authtoken.txt") as f:
    auth_token = f.readline().strip('\n')
print(auth_token)


if (auth_token == ""):
    print("Sorry you don't seem to have a valid token.\n Please register yourself at stormglass.io and get a API auth token.\n Then save it in a file called \"authtoken.txt\" on the first line.\nThe file should be saved within the same directory as the script")
    exit()

"""
#Step 2b: Making the request
response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat':getLoc.latitude,
        'lng':getLoc.longitude,
        'params':'windSpeed,windDirection',
    },
    headers={
        'Authorization':auth_token
    }
)

json_data = response.json()
print(json_data)
"""

with open("testdata.json") as f:
    json_data = json.load(f)
    print(json_data)
