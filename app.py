from flask import Flask,request,render_template
import requests
import datetime as dt

app = Flask(__name__)

#Your API Key
API_KEY = '5f1348e8f6aa675ecc09c5bafd5cf2d3'

@app.route('/',methods = ["POST","GET"])
def search_city():
    if request.method == "POST":
        city = request.form.get("city")
        if city == "":
            return render_template("error.html")
        units = 'Metric'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={units}'
        response = requests.get(url).json()

        
        new_city = city 
        temperature = response["main"]["temp"]
        description = response["weather"][0]["description"]
        icon = response["weather"][0]["icon"]
        humidity = response["main"]["humidity"]
        
        return render_template("weather_new.html",city = new_city,temperature = temperature,description = description,icon = icon,humidity=humidity)
    return render_template("weather_new.html")
if __name__ == '__main__':
    app.debug = True
    app.run()
