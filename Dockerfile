FROM python:3.8.16-slim-buster

WORKDIR /python-docker

COPY backend/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask" , "run" , "--host=0.0.0.0" ]
