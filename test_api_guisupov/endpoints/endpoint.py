import allure

class Endpoint:
    host = 'http://167.172.172.115:52353/'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    default_body = {"name": "Five",
                "data": {"color": "Black", "size": "max"}
                }
    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, (
            f"Expected status code 200, but got {self.response.status_code}"
        )

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, (
            f"Expected status code 400, but got {self.response.status_code}"
        )

    @allure.step('Check that title is the same as sent')
    def check_response_title_is_correct(self, title):
        assert self.json['title'] == title, (
            f"Expected title '{title}', but got '{self.json.get('title')}'"
        )

