import requests

class Airline_Codes:
    def __init__(self, code):
        self.airlines_data_lst = []
        post_header = {
            "Content-Type": "application/x-www-form-urlencoded"
            } 
        post_data ={"grant_type":"client_credentials",
                  "client_id":"ENTER_TOKEN",
                  "client_secret":"ENTER_TOKEN"}
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", 
                                      data=post_data, 
                                      headers=post_header)
        response.raise_for_status()
        self.token_data = response.json()
        self.access_token = self.token_data["access_token"]

        for airline_code in code:
            airlines_parameter ={
            "airlineCodes": airline_code
            }

            airlines_header = {
                "authorization": f"Bearer {self.access_token}"
                }
            airline_code_response = requests.get(url="https://test.api.amadeus.com/v1/reference-data/airlines",params=airlines_parameter,headers=airlines_header)
            airline_code_response.raise_for_status()
            self.airlines_data = airline_code_response.json()
            self.businessname = self.airlines_data["data"][0]["businessName"]
            self.icacode = self.airlines_data["data"][0]["icaoCode"]
            arrangement = f"{self.businessname}({self.icacode})"
            self.airlines_data_lst.append(arrangement)

