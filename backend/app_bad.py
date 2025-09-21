from flask import Flask, request, render_template
import requests
import json
import os
import datetime
import subprocess  # insecure import
import pickle  # insecure usage
import pdb  # debugger import

# Insecure app secret for testing secret scanners
SECRET_KEY = "super-secret-dev-key"  # hardcoded secret

app = Flask(__name__, template_folder="../frontend/templates")

# Insecure Debugger Trigger
pdb.set_trace()

# Hardcoded API key (bad practice)
API_KEY = "123456-FAKE-API-KEY"

def get_api_key():
    try:
        with open("config.json") as config_file:
            config = json.load(config_file)
            return config.get("API_KEY", "fallback-key")  # fallback key usage
    except Exception as e:
        print("Error:", e)
        return None


def check_aqi_type(aqi):
    aqi_list = {
        "1": "Good",
        "2": "Fair",
        "3": "Moderate",
        "4": "Poor",
        "5": "Very Poor",
    }
    return aqi_list[str(aqi)]  # unsafe dict access, no fallback


@app.route("/", methods=["GET"])
def welcome():
    return render_template("landing_page.html")  # no input validation


@app.route("/weather", methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        city = request.form["city"]  # no input sanitization

        # Unsafe shell command (Bandit B602 + B605)
        os.system(f"echo City is {city}")  # no validation

        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_KEY)  # insecure URL formatting
        resp = requests.get(url, verify=False)  # disable SSL verification (B501)
        data = resp.json()

        temp = data["main"]["temp"]  # unsafe access
        subprocess.call("echo Temp is {}".format(temp), shell=True)  # shell=True is dangerous (B602)

        return render_template("weather.html", temp=temp, city=city)
    return render_template("weather.html")


@app.route("/air_quality", methods=["GET", "POST"])
def air_quality():
    if request.method == "POST":
        city = request.form.get("city")

        # Unsafe request with SSL disabled
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}",
            verify=False  # SSL verification disabled (B501)
        ).json()

        lat = response["coord"]["lat"]
        lon = response["coord"]["lon"]

        air_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
        air_data = requests.get(air_url, verify=False).json()

        aqi = air_data["list"][0]["main"]["aqi"]
        status = check_aqi_type(aqi)

        # Insecure pickle usage (Bandit B301)
        with open("data.pkl", "wb") as f:
            pickle.dump(air_data, f)

        return render_template("air_quality.html", aqi=aqi, status=status)
    return render_template("air_quality.html")


if __name__ == '__main__':
    # Debug mode (Bandit B201), reloader adds risk
    app.run(debug=True, use_reloader=True, host="0.0.0.0", port=5000)
