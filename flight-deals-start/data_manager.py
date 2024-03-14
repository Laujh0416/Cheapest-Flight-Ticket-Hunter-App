import requests


BEARER_HEADERS = {
    "Authorization":"Bearer ENTER_TOKEN",
    "ContentType":"application/json"
    }

API_KEY = {"apikey":"ENTER_TOKEN"}

class DataManager():
    def __init__(self):
        self.destination_data = {}
    
    def code_search(self, city_name):
        city_params = {
            "term": city_name
        }
        city_response = requests.get(url="https://api.tequila.kiwi.com/locations/query", params=city_params, headers=API_KEY)
        city_response.raise_for_status()
        city_data = city_response.json()
        city_code = city_data["locations"][0]["code"]
        return city_code
    
    def retrieve_data(self):
        sheet_response = requests.get(url="https://api.sheety.co/.../.../prices", headers=BEARER_HEADERS)
        sheet_response.raise_for_status()
        self.destination_data = sheet_response.json()
        return self.destination_data["prices"]

    def code_saving(self):
        sheet_response = requests.get(url="https://api.sheety.co/.../.../prices", headers=BEARER_HEADERS)
        sheet_response.raise_for_status()
        self.destination_data = sheet_response.json()
        for city in self.destination_data["prices"]:
            city["iataCode"] = self.code_search(city["city"])
        return self.destination_data["prices"]

    def update_code(self):
        self.code_saving()
        for city in self.destination_data["prices"]:
            new_data = {
                "price":{
                    "iataCode":city["iataCode"]
                }
            }
            adding_response = requests.put(url=f"https://api.sheety.co/.../.../prices/{city['id']}", 
                                           json=new_data,
                                           headers=BEARER_HEADERS)
            print(adding_response.text)

