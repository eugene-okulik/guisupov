from test_api_guisupov.endpoints.get_post import Post
from test_api_guisupov.endpoints.create_new_object import NewObject
import allure


@allure.story("Create a new object")
@allure.feature("POST Operations")
@allure.title("Create object using POST method")
def test_get_post():
    endpoint = Post()
    endpoint.get_post()
    endpoint.check_that_status_is_200()


def test_create_object(cleanup_object):
    new_post = NewObject()
    new_post.create_new_object()
    new_post.check_that_status_is_200()
    new_post.check_validate_response_data()
    cleanup_object.append(new_post.post_id)


def test_put():

def atest_put_a_post(update_post_endpoint, post_id):
    payload = {
        "title": "Hello",
        "body": "My Friend",
        "userId": 2
    }
    update_post_endpoint.make_changes_in_post(post_id, payload)
    update_post_endpoint.check_that_status_is_200()
    update_post_endpoint.check_response_title_is_correct(payload['title'])

