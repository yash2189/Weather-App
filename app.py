from flask import Flask, request, render_template
from decimal import Decimal, ROUND_HALF_UP
import requests
import datetime as dt

app = Flask(__name__)

# Your API Key
API_KEY = '5f1348e8f6aa675ecc09c5bafd5cf2d3'

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = Decimal(kelvin * 1.8 - 459.67)
    return fahrenheit.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def kelvin_to_celsius(kelvin):
    celsius = Decimal(kelvin - 273.15)
    return celsius.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

@app.route('/', methods=["POST", "GET"])
def search_city():
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return render_template("error.html")
        if len(city) <= 1:
            return render_template("error.html")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
        response = requests.get(url).json()

        country = response["sys"]["country"]
        current_date = response["dt"]
        m = dt.datetime.fromtimestamp(int(current_date)).strftime('%d-%m-%Y %H:%M:%S ')
        new_city = city
        temperature = kelvin_to_fahrenheit(response["main"]["temp"])
        tempcelsius = kelvin_to_celsius(response["main"]["temp"])
        description = response["weather"][0]["description"]
        icon = response["weather"][0]["icon"]
        humidity = response["main"]["humidity"]

        return render_template("weather_new.html", city=new_city, temperature=temperature, tempcelsius=tempcelsius, description=description,
                               icon=icon, humidity=humidity, country=country, m=m)
    return render_template("weather_new.html")


if __name__ == '__main__':
    app.run()
