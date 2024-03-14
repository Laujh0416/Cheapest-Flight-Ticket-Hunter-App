import requests


bearer_headers = {
    "Authorization":"Bearer klmvckewmvc32483290dscag3412sdqcxa",
    "Content-Type": "application/json"
    }
city_code = {"prices":{"city": "ttt"}}
            #print(city_code)
adding_response = requests.post(url="https://api.sheety.co/49e98dae4f75bd1270cac2df53f1933a/copyOfFlightDeals/prices", json=city_code, headers=bearer_headers)
adding_response.raise_for_status()