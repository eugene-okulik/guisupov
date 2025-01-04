import requests
from test_api_guisupov.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    def delete_object(self, post_id):
        self.response = requests.delete(
            f'{self.host}/object/{post_id}',
            headers=self.headers
        )
        print(self.response.text)
        return self.response