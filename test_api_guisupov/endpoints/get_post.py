import requests
from test_api_guisupov.endpoints.endpoint import Endpoint


class Post(Endpoint):

    def get_post(self):
        self.response = requests.get(f'{self.host}/object/1', headers=self.headers)
        self.json = self.response.json()

        return self.response

