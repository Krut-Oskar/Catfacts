import requests
import json


class ApiHandler:
    def __init__(self, url):
        self._url = url
    def getQuote(self):
        response = requests.get(self._url)
        response_to_json = response.json()
        quote = response_to_json['value']
        return quote
    def setPerson(self, person):
        if person == "Donald Trump":
            self._url = "https://www.tronalddump.io/random/quote"
        if person == "Chuck Norris":
            self._url = "https://api.chucknorris.io/jokes/random"
    
    
