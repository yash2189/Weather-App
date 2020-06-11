from flask import Flask,request,render_template
import requests
import datetime as dt

app = Flask(__name__)



@app.route('/')
def search_city():
    API_KEY = '5f1348e8f6aa675ecc09c5bafd5cf2d3'
    city = 'Seoul'
    units = 'Metric'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units={units}'
    response = requests.get(url).json()

    weather = {
        'city': city,
        'temperature': response["main"]["temp"],
        'description':response["weather"][0]["description"],
        'icon':response["weather"][0]["icon"],
        'humidity':response["main"]["humidity"],
    }


    return render_template("weather_new.html",weather=weather)
if __name__ == '__main__':
    app.debug = True
    app.run()
