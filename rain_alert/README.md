# Rain Alert Bot - ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**Rain Alert Bot** is a Python script that integrates OpenWeather's API and Twilio's SMS service to notify users when it is expected to rain. This script checks the weather forecast for a specific location and sends a text message alert if rain is predicted.

---

## Features

- Fetches weather forecasts using OpenWeather's API.
- Analyzes weather data to determine if rain is expected.
- Sends SMS notifications using Twilio's API.
- Easily customizable for different locations and users.

---

## Requirements

### Python Libraries
- `os`: For accessing environment variables.
- `requests`: For API calls.
- `twilio`: For SMS functionality.

Install the required libraries using:
```bash
pip install requests twilio
```

---

## External APIs
1. **OpenWeather API**:
  - Sign up at `OpenWeather` and generate your API key.
  - Set the API key as an environment variable (`OWM_API_KEY`).

2. **Twilio API**:- Create a Twilio account at `Twilio`.
- Get your Account SID, Auth Token, and SMS number.

---

## Setup
1. Clone the repository or download the script file.
2. Install the required Python libraries:
```bash
pip install requests twilio
```
3. Set up environment variables:
  - OpenWeather API key: `OWM_API_KEY`
  - Twilio Account SID and Auth Token: Replace placeholders in the script (`ACCOUNT_SID` and `ACCOUNT_PASSWORD`) with your Twilio credentials.

---

## Usage
**Step 1**: Customize the Location
Update the `LAT` and `LON` variables in the script with the latitude and longitude of your preferred location.
**Step 2**: Run the Script
Execute the script:
```bash
python main.py
```
**Step 3**: Receive SMS Alerts
If rain is expected, you'll receive an SMS with the message:
```bash
It's going to rain today. Remember to bring an umbrella!
```

---

## Code Breakdown
### Import Libraries
The script begins by importing necessary libraries:
```Python
import os
import requests
from twilio.rest import Client
```

### Weather Data Retrieval
It fetches weather data for the specified location using the OpenWeather API:
```Python
weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4,
}
URL = f"https://api.openweathermap.org/data/2.5/forecast"
with requests.get(URL, params=weather_params) as response:
    response.raise_for_status()
    data = response.json()
```

### Rain Alert Logic
Analyzes the forecast to check for rain based on weather condition codes:
```Python
will_rain = False
for hour_data in data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
```

### SMS Notification
If rain is expected, sends an SMS alert using Twilio:
```Python
if will_rain:
    client = Client(ACCOUNT_SID, ACCOUNT_PASSWORD)
    message = client.messages.create(
        to="+11234567",
        body="It's going to rain today. Remember to bring an umbrella!",
        from_="SMS NUMBER GOES HERE"
    )
```

---

## Notes
- **Weather API Limitations**: Ensure the API key has sufficient privileges and the query count (`cnt`) matches your forecast needs.
- **Twilio Setup**: Verify that your Twilio account is configured for sending SMS to the desired recipient.
- **Customization**: You can modify the message content and recipient number for personalized alerts.



