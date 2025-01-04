import allure
import pytest


@pytest.mark.smoke
@allure.story("API Get Object")
@allure.feature("GET method")
@allure.title("Test: Get object by ID")
def test_get_object(get_object_endpoint, post_id, create_post_endpoint):
    get_object_endpoint.get_object(post_id)
    get_object_endpoint.check_that_status_is_200()
    expected_body = create_post_endpoint.default_body
    get_object_endpoint.check_object_data(expected_body)


@pytest.mark.smoke
@allure.story("API Create Object")
@allure.feature("POST method")
@allure.title("Test: Create new object")
def test_create_object(post_id, create_post_endpoint):
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_validate_response_data()


@pytest.mark.smoke
@allure.story("API Update Object (PUT)")
@allure.feature("PUT method")
@allure.title("Test: Update object data using PUT")
def test_put_a_post(update_put_endpoint, post_id):
    body = {"name": "Six",
            "data": {"color": "White", "size": "min"}}
    update_put_endpoint.update_put(post_id, body)
    update_put_endpoint.check_that_status_is_200()
    update_put_endpoint.check_response_body_is_correct(body['name'])
    update_put_endpoint.check_response_body_is_correct(body['name'], body['data']['color'], body['data']['size'])


@pytest.mark.smoke
@allure.story("API Update Object (PATCH)")
@allure.feature("PATCH method")
@allure.title("Test: Update object data using PATCH")
def test_patch(update_patch_endpoint, post_id):
    body = {"name": "Python",
            "data": {"color": "Blue"}}
    update_patch_endpoint.update_patch(post_id, body)
    update_patch_endpoint.check_that_status_is_200()
    update_patch_endpoint.check_response_body_is_correct(body['name'])
    update_patch_endpoint.check_response_body_is_correct(body['name'], body['data']['color'])


@pytest.mark.smoke
@allure.story("API Delete Object")
@allure.feature("DELETE method")
@allure.title("Test: Delete object by ID")
def test_delete_object(delete_object_endpoint, post_id, verify_object_deleted):
    delete_object_endpoint.delete_object(post_id)
    delete_object_endpoint.check_that_status_is_200()
    verify_object_deleted(post_id)


TEST_DATA = [
    {"name": "One", "data": {"color": "Black", "size": "min"}},
    {"name": "Two", "data": {"color": "White", "size": "max"}},
    {"name": "Three", "data": {"color": "Blue", "size": "medium"}}
]


@pytest.mark.smoke
@pytest.mark.parametrize('data', TEST_DATA)
@allure.story("API Create Object")
@allure.feature("POST method")
@allure.title("Test: Parameterized Create Object")
def test_parameterized_create_object(create_post_endpoint, deleting_object, data):
    create_post_endpoint.default_body = data
    create_post_endpoint.create_new_object()
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_validate_response_data()
    deleting_object(create_post_endpoint.host, create_post_endpoint.headers, create_post_endpoint.post_id)
