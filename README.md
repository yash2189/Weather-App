# Weather-App

* Flask Weather App
- An application that gives the weather and Air Quality Index (AQI) by the city name
- API Used OpenWeatherMap - https://openweathermap.org/current
- Docker image is available for this app


To run the flask app directly:
- Create your virtual environment : `virtualenv venv`
- Activate the virtual environement : `source venv/bin/activate`
- create a `config.json` in project's root directory

Example:
`{
    "API_KEY": ""
}`

- Run : `python app.py`

To use the docker image follow the steps:

- Pull the image : `docker pull yash301998/flask-weather-app:latest`
- Spin up a container from the image: `docker run -d -p 5000:5000 yash301998/flask-weather-app`
- Open a browser to validate if the app is running on localhost: `http://localhost:5000/`
