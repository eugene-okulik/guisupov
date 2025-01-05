import pytest
import requests
from test_api_guisupov.endpoints.create_new_object import NewObject
from test_api_guisupov.endpoints.put_update_object import UpdatePut
from test_api_guisupov.endpoints.patch_uptate_object import UpdatePatch
from test_api_guisupov.endpoints.get_object import GetObject
from test_api_guisupov.endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_post_endpoint():
    return NewObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def update_put_endpoint():
    return UpdatePut()


@pytest.fixture()
def update_patch_endpoint():
    return UpdatePatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def post_id(create_post_endpoint):
    # Создаю объект
    create_post_endpoint.create_new_object()
    post_id = create_post_endpoint.post_id

    # Возвращаю id объекта
    yield post_id

    # Удаляю объект после завершения теста
    requests.delete(
        f'{create_post_endpoint.host}/object/{post_id}',
        headers=create_post_endpoint.headers
    )


@pytest.fixture()
def verify_object_deleted(create_post_endpoint):
    def verify(post_id):
        response = requests.get(
            f'{create_post_endpoint.host}/object/{post_id}',
            headers=create_post_endpoint.headers
        )
        assert response.status_code == 404, (
            f"Expected status code 404 for deleted object, but got {response.status_code}"
        )

    return verify


@pytest.fixture()
def deleting_object():
    def deleting_object(host, headers, post_id):
        response = requests.delete(
            f'{host}/object/{post_id}',
            headers=headers
        )
        assert response.status_code == 200, (
            f"Expected status code 200 for delete, but got {response.status_code}"
        )
        return response

    return deleting_object
