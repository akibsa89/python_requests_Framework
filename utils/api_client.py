import pytest
import requests


class APIClient:
    BASE_URL = "https://reqres.in"

    def __init__(self):
        self.header = {
            "Content-Type": "application/json"
        }

    def get(self, end_point):
        url = f"{self.BASE_URL}{end_point}"
        response = requests.get(url, headers=self.header)
        return response

    def post(self, end_point, payload):
        url = f"{self.BASE_URL}{end_point}"
        response = requests.post(url, headers=self.header, json=payload)
        return response

    def put(self, end_point, payload):
        url = f"{self.BASE_URL}{end_point}"
        response = requests.put(url, headers=self.header, json=payload)
        return response