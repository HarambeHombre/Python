import os
import requests
from twilio.rest import Client

# TWILIO INFO----------------------------------------
ACCOUNT_SID = "ACCOUNT_SID"
ACCOUNT_PASSWORD = ACCOUNT_PASSWORD

# OPENWEATHER INFO-----------------------------------
API_KEY = os.environ['OWM_API_KEY']
LAT = 32.722310
LON = -114.620880
weather_params = {
    "lat":LAT,
    "lon":LON,
    "appid": API_KEY,
    "cnt": 4,
}
URL = f"https://api.openweathermap.org/data/2.5/forecast"

# OPENWEATHER CALL AND PRINT ------------------------
with requests.get(URL, params=weather_params) as response:
    response.raise_for_status()
    data = response.json()
will_rain = False
for hour_data in data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
    # OPEN TWILIO CLIENT --------------------------------
    # client = Client(ACCOUNT_SID, ACCOUNT_PASSWORD)
    # message = client.messages \
    #     .create(
    #     to="+11234567",
    #     body="It's going to rain today. Remember to bring an umbrella!",
    #     from_="SMS NUMBER GOES HERE"
    #     )
    # print(message.status)