import requests
import json

def api_fuct(word):
    w = word
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + w
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]["meanings"][0]["definitions"]
        # return data
    else:
        print("This word does not exist")

o = input("Enter any Word You Like :- ")
for i in api_fuct(o):
    print(i["definition"])
