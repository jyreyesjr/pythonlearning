import requests

#GET request
response = requests.get('http://api.open-notify.org/astros.json')
#print(response) check if API is good

#convert response into json format
json = response.json()
#print(json) this is to check the data inside the response

print("These people are in space right now: \n")
for person in json["people"]:
    print(person["name"])
