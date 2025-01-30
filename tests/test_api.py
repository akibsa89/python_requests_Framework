import pytest
import json
import requests
from utils.api_client import APIClient
import random




@pytest.fixture(scope="module")
def api_client():
    """Fixture to initialize API client"""
    return APIClient()

def test_get_api(api_client):
    response = api_client.get("/api/users/2")
    # response = test_get_class.get("/api/users/2")
    print(response.json())
    assert response.status_code == 200, "status_code is not 200"
    assert len(response.json()) > 0, "Response_body is empty"


def test_post_api(api_client, load_user_data):

    user_data = load_user_data   # Call the dict to get JSON data
    # user_name = user_data["name"]
    # user_job = user_data["job"]
    #
    # payload = {
    #     "name": user_name,
    #     "job": user_job
    # }
    response = api_client.post("/api/users", user_data)
    print(response.json())
    assert response.status_code ==201
    assert response.json()["name"] == user_data["name"]
    assert response.json()["job"] == user_data["job"]


def test_put_api(api_client, load_user_data):
    user_data = load_user_data
    name = user_data["name"]
    job = user_data["job"]

    val = random.randint(1, 100)
    # print(val)

    user_name = f"{name}{val}"
    user_job = f"{job}{val}"
    payload = {
        "name": user_name,
        "job": user_job
    }
    response = api_client.put("/api/users/2", payload)
    print(response.json())
    assert response.status_code ==200
    assert response.json()["name"] == payload["name"]
    assert response.json()["job"] == payload["job"]



