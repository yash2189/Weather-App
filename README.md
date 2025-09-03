# Weather-App

* Flask Weather App
- An application that gives the weather and Air Quality Index (AQI) by the city name
- API Used OpenWeatherMap - https://openweathermap.org/current
- Docker image is available for this app


To run the flask app directly:
- Create your virtual environment : `virtualenv venv`
- Activate the virtual environement : `source venv/bin/activate`
- create a `config.json` in project's root directory or export env variable for `API_KEY`

Example:
`{
    "API_KEY": ""
}`

or

`export API_KEY = 'YOUR_KEY'`

- Run : `python app.py`

To use the docker image follow the steps:

- Pull the image : `docker pull yash301998/flask-weather-app:latest`
- Spin up a container from the image: `docker run -d -p 5000:5000 -e API_KEY=<KEY> yash301998/flask-weather-app:latest`
- Open a browser to validate if the app is running on localhost: `http://localhost:5000/`


Deploying to OpenShift

1. Login to your OpenShift Cluster
`oc login --token=YOUR_TOKEN --server=https://your.ocp.cluster:port`

2. Create a New Project (Optional)
`oc new-project flask-weather`

3. Create Kubernetes Secret for API Key
`oc create secret generic weather-api-key \
  --from-literal=API_KEY=your_openweather_api_key`

4. Apply Manifests
`oc apply -f k8s/`

5. Access the App
Get the route URL:
`oc get route flask-weather-app`
Then open `http://<route-url>`
