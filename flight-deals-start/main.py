from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from airline_codes import Airline_Codes


#flight details
DEPARTURE_LOCATION =  #"kota kinabalu"
DESTINATION = #kuala lumpur"
DURATION_START =  #dd/mm/yyyy
DURATION_END = #dd/mm/yyyy
NUM_ADULT = 1
LIMIT_DATA = 3 #in default will be 3

#notification details
SENDER_EMAIL = 
PASSWORD = 
RECEIVER_EMAIL = 
MESSAGE = 

data = DataManager()
destination_data = data.retrieve_data()
flight = FlightData(DEPARTURE_LOCATION, DESTINATION, DURATION_START, DURATION_END, NUM_ADULT)

def lowestprice(destination):
    for dict in destination_data:
        if dict["city"].lower() == destination:
            return dict["lowestPrice"]
if len(flight.flight_data_lst)==0:
    print("Please provide a valid city with airport :)")
else:
    #test = False
    msg = "Hello! We have found the most cheapest prices for your flight ticket(s)! Please take a moment to review:\n"
    remind = "*Friendly Reminder: Although we couldn't detect the destination in your sheet, we managed to find these options for you. Kindly update your sheet accordingly. Thank you!\n"
    for dict in flight.flight_data_lst:
        if lowestprice(DESTINATION):
            if dict["city_to"].lower() == DESTINATION and int(dict["price"]) < lowestprice(DESTINATION):
                airline_code = Airline_Codes(dict['airlines'])
                airline_code_lst = airline_code.airlines_data_lst
                msg += f"\nFrom: {dict['city_from']}\nTo: {dict['city_to']}\nPrice: {dict['price']}USD\nDeparture Time: {dict['departure']}\nAvailable Airline(s): {airline_code_lst}\n"
                msg += f"**There is {flight.num_stop_over} stop over(s): {flight.stop_over_attribute}."
        else:
            #msg +="ERROR: Apologies, but our system is currently unable to compare ticker prices. Could you kindly provide your ticket price in the spreadsheet? This will enable us to conduct a search for the most economical flight ticket for you. Thank you for your understanding and cooperation."
            #REMOVE THESE COMMENTS IF
            airline_code = Airline_Codes(dict['airlines'])
            airline_code_lst = airline_code.airlines_data_lst
            msg += f"\nPrice: {dict['price']}USD\nFrom: {dict['city_from']}\nTo: {dict['city_to']}\nDeparture Time: {dict['departure']}\nAvailable Airline(s): {airline_code_lst}\n"
            msg += f"**There is {flight.num_stop_over} stop over(s): {flight.stop_over_attribute}.\n"

    NotificationManager(
        sender_email=SENDER_EMAIL, 
        password=PASSWORD, 
        receiver_email=RECEIVER_EMAIL, 
        msg=msg)
