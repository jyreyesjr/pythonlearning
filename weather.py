import requests

api_key = ""
lat = ""
lon = ""
url = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key+"&units=imperial"

#GET request
response = requests.get(url)
#print(response) check if API is good

#convert response into json format
json = response.json()

#check what's inside the json
#print(json) 

#parsing the json file and assigning them to variables
description = json.get("weather")[0].get("description")
current_temp = json.get("main").get("temp")

print("Current Temperature in ", lat , " " , lon , " is:" , current_temp, "F")
print("Forcast is", description)

