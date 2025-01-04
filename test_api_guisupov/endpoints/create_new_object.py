import requests
from test_api_guisupov.endpoints.endpoint import Endpoint


class NewObject(Endpoint):
    post_id = None


    def create_new_object(self):


        self.response = requests.post(f'{self.host}/object', headers=self.headers, json=self.default_body)
        self.response_data = self.response.json()
        self.post_id = self.response_data['id']
        print(self.response.json())
        print(self.post_id)

        return self.response

    def check_validate_response_data(self):
        assert self.response_data['name'] == self.default_body['name']
        assert self.response_data['data']['color'] == self.default_body['data']['color']
        assert self.response_data['data']['size'] == self.default_body['data']['size']



