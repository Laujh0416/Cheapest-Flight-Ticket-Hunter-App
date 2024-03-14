import requests
from data_manager import DataManager

class FlightSearch:
    def __init__(self, fly_from, fly_to, date_from, date_to, adults, limit=3):
        object = DataManager()
        self.route_line = []
        self.header = {
            "apikey":"ENTER_TOKEN"
            }
        self.parameter = {
            "fly_from" : str(object.code_search(fly_from)),
            "fly_to" : str(object.code_search(fly_to)),
            "date_from" : str(date_from),
            "date_to" : str(date_to),
            "adults" : int(adults),
            "limit": int(limit)
           # "select_stop_airport_exclude": True
            #"price_from" : price_from
        }

        self.response = requests.get(url="https://api.tequila.kiwi.com/v2/search", params=self.parameter, headers=self.header)
        self.response.raise_for_status()
        self.data = self.response.json()
        self.route_line_attribute = self.route_lines()
        self.stop_over_attribute = self.stop_over()
        self.num_stop_over = len(self.stop_over_attribute)
    
    def stop_over(self):
        for dict in self.data["data"][0]["route"]:
            self.route_line.append(dict["cityFrom"])
            self.route_line.append(dict["cityTo"])
        self.stop_over_city = self.route_line.copy()
        self.stop_over_city.pop(0)
        self.stop_over_city.pop(-1)
        if len(self.stop_over_city) > 0:
            return set(self.stop_over_city)
        else:
            print("Sorry, there is no stop over for this flight :(")
    
    def route_lines(self):
        msg = "Route:\n"
        for i in range(0,len(self.data["data"][0]["route"])):
            msg += f"From {self.data['data'][0]['route'][i]['cityFrom']} To {self.data['data'][0]['route'][i]['cityTo']} (Departure time: {self.data['data'][0]['route'][i]['utc_departure']}, Arrival time: {self.data['data'][0]['route'][i]['utc_arrival']}\n"
        return msg





# DEPARTURE_LOCATION = "rome" #"kota kinabalu"
# DESTINATION = "kuala lumpur" #kuala lumpur"
# DURATION_START = "16/03/2024" #dd/mm/yyyy
# DURATION_END = "21/09/2024" #dd/mm/yyyy
# NUM_ADULT = 1
# LIMIT_DATA = 3 #in default will be 3

# test = FlightSearch(DEPARTURE_LOCATION, DESTINATION, DURATION_START, DURATION_END, NUM_ADULT, LIMIT_DATA)
# #print(test.route_lines())
# print(test.num_stop_over)