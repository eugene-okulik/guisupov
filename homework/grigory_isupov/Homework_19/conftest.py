import pytest
import requests

host = 'http://167.172.172.115:52353/'
headers = {'Content-Type': 'application/json'}


# Фиктура выводит на печать фразу в начале тестов и после завершения последнего
@pytest.fixture(scope='session')
def hello():
    print('Start testing')
    yield
    print('Testing completed')


# Фикстура выводит на печть фразу перед, и после завершения теста
@pytest.fixture()
def everytest():
    print('before test')
    yield
    print('after test')


# Фиктура создает объект и удаляет его после теста
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


# Фикстура собирает список id созданых объектов и после завершения(для параметризированого теста, и теста на POST)
@pytest.fixture()
def clean():
    """Фикстура для удаления созданных объектов после теста."""
    ids_to_delete = []

    yield ids_to_delete

    # удаляю объекты
    for post_id in ids_to_delete:
        response = requests.delete(f'{host}/object/{post_id}')
        if response.status_code == 200:
            print(f'Объект с id: {post_id} успешно удален')
        else:
            print(f'Что-то пошло не так, объект с id: {post_id} не удален')


# Фикстура создания нового объекта(для теста на DELETE)
@pytest.fixture()
def create_post_for_delete():
    print("\nCоздание объекта метод POST")
    body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "min"}
            }
    response = requests.post(f'{host}/object', headers=headers, json=body)
    data = response.json()
    post_id = data['id']
    return post_id
