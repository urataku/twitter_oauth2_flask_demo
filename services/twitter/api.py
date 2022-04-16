import requests

class TwitterApi:

    API_URL = "https://api.twitter.com/2/"

    def __init__(self, access_token) -> None:
        self.access_token = access_token

    def get(self, endpoint: str, params: dict):
        url = self.API_URL + endpoint
        headers = {
            "Authorization" : f"Bearer {self.access_token}"
        }
        return requests.get(url, headers=headers, params=params)

    def post(self, endpoint: str, payload: dict):
        url = self.API_URL + endpoint
        headers = {
            "Authorization" : f"Bearer {self.access_token}"
        }
        return requests.post(url, headers=headers, data=payload)
