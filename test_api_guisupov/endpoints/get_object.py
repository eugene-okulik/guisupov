import requests
from test_api_guisupov.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    def get_object(self, post_id):
        self.response = requests.get(
            f'{self.host}/object/{post_id}',
            headers=self.headers
        )
        print(self.response.text)
        self.json = self.response.json()
        return self.response

    def check_object_data(self, expected_body):
        assert self.json['name'] == expected_body['name'], (
            f"Expected name '{expected_body['name']}', but got '{self.json['name']}'"
        )
        assert self.json['data']['color'] == expected_body['data']['color'], (
            f"Expected color '{expected_body['data']['color']}', but got '{self.json['data']['color']}'"
        )
        assert self.json['data']['size'] == expected_body['data']['size'], (
            f"Expected size '{expected_body['data']['size']}', but got '{self.json['data']['size']}'"
        )