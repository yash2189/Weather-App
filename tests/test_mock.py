import pytest
from backend.app import app
from unittest.mock import patch


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_weather_endpoint(client):
    with (
        patch("backend.app.load_api_key", return_value="test_api_key"),
        patch("requests.get") as mock_get,
    ):
        mock_get.return_value.status_code = 200
        response = client.post("/weather", data={"city": "London"})
        assert response.status_code == 200


def test_aq_endpoint(client):
    with (
        patch("backend.app.load_api_key", return_value="test_api_key"),
        patch("requests.get") as mock_get,
    ):
        mock_get.return_value.status_code = 200
        response = client.post("/air_quality", data={"city": "Mumbai"})
        assert response.status_code == 200
