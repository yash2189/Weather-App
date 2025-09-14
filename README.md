# Weather-App

- An application that gives the weather and Air Quality Index (AQI) by the city name


## Tech Stack

- Python (Flask)
- OpenWeatherMap API
- Docker
- Kubernetes & OpenShift
- GitHub Actions for CI
- Kyverno for policy enforcement

## Run the flask app directly:
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

## Use the docker image follow the steps:

- Pull the image : `docker pull yash301998/flask-weather-app:latest`
- Spin up a container from the image: `docker run -d -p 5000:5000 -e API_KEY=<KEY> yash301998/flask-weather-app:latest`
- Open a browser to validate if the app is running on localhost: `http://localhost:5000/`


## Deploying to OpenShift

1. Login to your OpenShift Cluster
`oc login --token=YOUR_TOKEN --server=https://your.ocp.cluster:port`

2. Create a New Project (Optional)
`oc new-project flask-weather`

3. Create Kubernetes Secret for API Key
`oc create secret generic weather-api-key \
  --from-literal=API_KEY=your_openweather_api_key -n flask-weather`

4. Create Docker Hub Secret (for image pulling)
`oc create secret docker-registry docker-hub-secret \
  --docker-server=docker.io \
  --docker-username=YOUR_DOCKERHUB_USERNAME \
  --docker-password=YOUR_DOCKERHUB_PASSWORD \
  --docker-email=YOUR_EMAIL -n flask-weather`

5. Apply Manifests
`oc apply -f k8s/`

6. Access the App
Get the route URL:
`oc get route flask-weather-app`
Then open `http://<route-url>`


## Linting & Security Checks
**KubeLinter** runs in GitHub Actions to flag:

- runAsUser: 0, privileged: true, missing probes, resource limits, latest image tags, and hardcoded secrets.

**Kyverno policies** (under `k8s/cluster_policy/`) enforce these checks on the cluster:

- Block root user and privilege escalation

- Require labels (app)

- Disallow latest image tags

- Require secrets from valueFrom.secretKeyRef

## Install Kyverno on cluster

Install helm utility
And then install Kyverno:
- `helm repo add kyverno https://kyverno.github.io/kyverno/`
- `helm repo update`
- `oc new-project kyverno`
- `helm install kyverno kyverno/kyverno -n kyverno`

## Apply Cluster policies
`oc apply -f k8s/cluster_policy/`
