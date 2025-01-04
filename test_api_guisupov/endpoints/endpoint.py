import allure


class Endpoint:
    host = 'http://167.172.172.115:52353/'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    post_id = None
    default_body = {"name": "Five",
                    "data": {"color": "Black", "size": "max"}
                    }

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, (
            f"Expected status code 200, but got {self.response.status_code}"
        )


    @allure.step('Check that name is the same as sent')
    @allure.step('Check that name, color, or size is the same as sent')
    def check_response_body_is_correct(self, name=None, color=None, size=None):
        if name is not None:
            assert self.json['name'] == name, (
                f"Expected name '{name}', but got '{self.json.get('name')}'"
            )
        if color is not None:
            assert self.json['data']['color'] == color, (
                f"Expected color '{color}', but got '{self.json['data'].get('color')}'"
            )
        if size is not None:
            assert self.json['data']['size'] == size, (
                f"Expected size '{size}', but got '{self.json['data'].get('size')}'"
            )
