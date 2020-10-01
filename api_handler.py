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
    
    
    
