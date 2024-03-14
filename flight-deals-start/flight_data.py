from flight_search import FlightSearch

class FlightData(FlightSearch):
    def __init__(self, fly_from, fly_to, date_from, date_to, adults, limit=3):
        super().__init__(fly_from, fly_to, date_from, date_to, adults, limit)
        #object = FlightSearch("LON", "KUL", "12/03/2024", "21/09/2024", 1, 20) #this needs to amend
        self.flight_data_lst = []
        for data in self.data["data"]:
            self.flight_data = {
            "city_from": data["cityFrom"],
            "city_to": data["cityTo"],
            "price" : data["price"],
            "departure" : data["local_departure"],
            "available_seat" : data["availability"],
            "airlines" : data["airlines"]
            }
            self.flight_data_lst.append(self.flight_data)
        self.sort_function()

    def value_function(self, e):
        return e["price"]
    
    def sort_function(self):
        self.flight_data_lst.sort(key=self.value_function)
    
