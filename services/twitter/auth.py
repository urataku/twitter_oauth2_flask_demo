import requests
import os
from services.random_string_maker import RandomStringMaker
from services.twitter.api import TwitterApi
from requests.auth import HTTPBasicAuth
import hashlib
import base64


class TwitterOauth:

    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    OAUTH_URI = 'https://twitter.com/i/oauth2/authorize'
    REDIRECT_URI = 'http://127.0.0.1/callback'

    def get_url(self, token_code) -> str:
        param_str = self.__create_login_url_param_str(token_code)
        url = self.OAUTH_URI + '?' + param_str
        return url

    def fetch_token(self, code, code_verifier) -> list:
        endpoint = "oauth2/token"
        data = {
            'code': code,
            'client_id': self.CLIENT_ID,
            'grant_type': 'authorization_code',
            'redirect_uri': self.REDIRECT_URI,
            'code_verifier': code_verifier
        }
        auth = HTTPBasicAuth(self.CLIENT_ID, self.CLIENT_SECRET)
        url = TwitterApi.API_URL + endpoint
        response = requests.post(url, data=data,
                            headers={}, auth=auth)

        return response.json()

    def __create_login_url_param_str(self, token_code: str) -> str:
        encoded_token_code = base64.b64encode(hashlib.sha256(token_code.encode('utf-8')).digest()).decode()
        code_challenge = encoded_token_code.rstrip('=').replace('=', '').replace('+', '-').replace('/', '_')
        state = RandomStringMaker.exec(100)
        return f"response_type=code&client_id={self.CLIENT_ID}&redirect_uri={self.REDIRECT_URI}&scope=tweet.read users.read offline.access&state={state}&code_challenge={code_challenge}&code_challenge_method=s256"