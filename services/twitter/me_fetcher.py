class MeFetcher:

    ENDPOINT = "users/me"

    def __init__(self, api) -> None:
        self.api = api

    def exec(self):
        params = {
            "user.fields": "profile_image_url"
        }
        response = self.api.get(self.ENDPOINT, params)
        return response.json()['data']
