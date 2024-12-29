import pytest
import requests
from test_api_guisupov.endpoints.endpoint import Endpoint
host = 'http://167.172.172.115:52353/'
headers = {'Content-Type': 'application/json'}


from test_api_guisupov.endpoints.endpoint import Endpoint

@pytest.fixture
def cleanup_object():
    """
    Фикстура для удаления объекта после теста.
    Тест передает идентификатор объекта (post_id), который будет удален.
    """
    objects_to_delete = []

    yield objects_to_delete

    # Удаляем все объекты, добавленные в список
    for post_id in objects_to_delete:
        response = requests.delete(f'{Endpoint.host}/object/{post_id}')
        if response.status_code == 200:
            print(f'Объект с id: {post_id} успешно удален')
        else:
            print(f'Ошибка при удалении объекта с id: {post_id}, статус: {response.status_code}')
@pytest.fixture()
def create_new_post():
    body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "max"}
            }
    response = requests.post(f'{host}/object', headers=headers, json=body)
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    data = response.json()
    post_id = data['id']
    yield post_id
    response = requests.delete(f'{host}/object/{post_id}')
    if response.status_code == 200:
        print(f'Объекст с id: {post_id} успешно удален')
    else:
        print(f'Что то пошло не так, {post_id} не удален')


@pytest.fixture()

def clean(post_id):
    response = requests.delete(f'{host}/object/{post_id}')
    if response.status_code == 200:
        print(f'Объект с id: {post_id} успешно удален')
    else:
        print(f'Что-то пошло не так, объект с id: {post_id} не удален')