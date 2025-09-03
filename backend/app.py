from flask import Flask, request, render_template
import requests
import json
import os
import datetime as dt

app = Flask(__name__, template_folder="../frontend/templates")


def load_api_key():
    """Get API key from env variable, fallback to config.json"""
    api_key = os.environ.get("API_KEY")
    if api_key:
        return api_key

    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
            return config.get("API_KEY")
    except FileNotFoundError:
        return None  # or raise an error if it's required


API_KEY = load_api_key()

if not API_KEY:
    raise RuntimeError("API_KEY not found in environment variables or config.json")


def check_aqi_type(aqi):
    """AQI List"""
    aqi_list = {
        "1": "Good",
        "2": "Fair",
        "3": "Moderate",
        "4": "Poor",
        "5": "Very Poor",
    }
    return aqi_list.get(str(aqi))


@app.route("/", methods=["GET"])
def welcome():
    """Render Home Page"""
    return render_template("landing_page.html")


@app.route("/weather", methods=["POST", "GET"])
def weather():
    """Fetch Weather for a city"""
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return render_template("error.html")
        if len(city) <= 1:
            return render_template("error.html")
        units = "Metric"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={units}"
        response = requests.get(url).json()

        country = response["sys"]["country"]
        current_date = response["dt"]
        m = dt.datetime.fromtimestamp(int(current_date)).strftime("%d-%m-%Y %H:%M:%S ")
        new_city = city
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        icon = response["weather"][0]["icon"]
        humidity = response["main"]["humidity"]

        return render_template(
            "weather.html",
            city=new_city,
            temperature=temperature,
            description=description,
            icon=icon,
            humidity=humidity,
            country=country,
            m=m,
        )
    return render_template("weather.html")


@app.route("/air_quality", methods=["POST", "GET"])
def air_quality():
    """Fetch AQI Data of a city"""
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return render_template("error.html")
        if len(city) <= 1:
            return render_template("error.html")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url).json()

        lat = response["coord"]["lat"]
        lon = response["coord"]["lon"]

        air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        air_response = requests.get(air_url).json()
        aqi = air_response["list"][0]["main"]["aqi"]
        aqi_status = check_aqi_type(aqi)
        return render_template(
            "air_quality.html", city=city, aqi=aqi, aqi_status=aqi_status
        )
    return render_template("air_quality.html")


if __name__ == "__main__":
    app.run()
