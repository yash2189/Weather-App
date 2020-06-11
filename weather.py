import requests
import json
import datetime as dt

api_key = '5f1348e8f6aa675ecc09c5bafd5cf2d3'

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input('Enter city name:')

units = 'Metric'

complete_url = base_url + "appid=" + api_key + \
"&q=" + city_name + "&units=" + units

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    country = x["sys"]

    climate = x["weather"]

    current_weather = climate[0]["description"]

    y = x["main"]

    current_humidity = y["humidity"]

    current_pressure = y["pressure"]

    current_temperature = y["temp"]

    current_date = x["dt"]

    m = dt.datetime.fromtimestamp(
        int(current_date)).strftime('%Y-%m-%d %H:%M:%S')

    print(m)

    print("Country "+country['country'] +
          "\nThe weather in " + city_name + " is " + current_weather +
          "\nTemperature in Celsius " + str(current_temperature) +
          "\nAtmospheric pressure(in hPa Unit) " + str(current_pressure) +
          "\nHumidity(in Percentage)" + str(current_humidity))
else:
    print("City not Found")
