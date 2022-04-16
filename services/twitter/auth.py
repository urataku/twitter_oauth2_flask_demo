import requests
import os
from services.twitter.api import TwitterApi
from requests.auth import HTTPBasicAuth


class TwitterOauth:

    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    OAUTH_URI = "https://twitter.com/i/oauth2/authorize"
    REDIRECT_URI = "http://127.0.0.1:3000/callback"

    def get_url(self):
        param_str = f"response_type=code&client_id={self.CLIENT_ID}&redirect_uri={self.REDIRECT_URI}&scope=tweet.read users.read offline.access&state=state&code_challenge=code_challenge&code_challenge_method=plain"
        url = self.OAUTH_URI + "?" + param_str
        return url

    def fetch_token(self, code):
        endpoint = "oauth2/token"
        data = {
            "code": code,
            "client_id": self.CLIENT_ID,
            "grant_type": "authorization_code",
            "redirect_uri": self.REDIRECT_URI,
            "code_verifier": "code_challenge"

        }
        auth = HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET)
        url = TwitterApi.API_URL + endpoint
        response = requests.post(url, data=data,
                            headers={}, auth=auth)

        return response.json()
