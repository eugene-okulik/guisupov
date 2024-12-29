import requests
from test_api_guisupov.endpoints.endpoint import Endpoint

class UpdatePost(Endpoint):


    def make_changes_in_post(self, post_id, payload):

        self.response = requests.put(
            f'{self.host}/{post_id}',
            json=payload,
            headers=self.headers
        )
        self.json = self.response.json()
        return self.response