import requests
from test_api_guisupov.endpoints.endpoint import Endpoint


class UpdatePut(Endpoint):

    def update_put(self, post_id, body):
        self.response = requests.put(
            f'{self.host}/object/{post_id}',
            json=body,
            headers=self.headers
        )
        print(self.response.text)
        self.json = self.response.json()
        return self.response
