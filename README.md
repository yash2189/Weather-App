# Weather-App

* Flask Weather App
- An application that gives the weather by the city name
- API Used OpenWeatherMap - https://openweathermap.org/current
- Docker image is available for this app


To run the flask app directly:
- Run : `python app.py`

To use the docker image follow the steps:

- Pull the image : `docker pull yash301998/flask-weather-app:latest`
- Spawn a container : `docker run -d -p 5000:5000 flask-weather-app`
