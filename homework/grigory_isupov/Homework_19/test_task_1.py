import requests
import pytest

host = 'http://167.172.172.115:52353/'
headers = {'Content-Type': 'application/json'}

# Вынес в переменные, что бы потом можно было сравнить
name = "Two object"
color = "Orange"
size = "Little"


def test_post(clean, hello, everytest):
    print("\nCоздание объекта метод POST")
    body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "min"}
            }
    response = requests.post(f'{host}/object', headers=headers, json=body)
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'


@pytest.mark.critical
def test_get(create_new_post, everytest):
    print("\nПолучение данных по объекту, метод GET")
    response = requests.get(f'{host}/object/{create_new_post}')
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['id'] == create_new_post, f"Ждал id: {create_new_post}, получил {data['id']}"


@pytest.mark.medium
def test_put(create_new_post, everytest):
    print("\nИзменение данных по объекту, метод PUT")
    body = {"name": f"{name}",
            "data": {
                "color": f"{color}",
                "size": f"{size}"}
            }
    response = requests.put(f'{host}/object/{create_new_post}', headers=headers, json=body)
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['name'] == name
    assert data['data']['color'] == color
    assert data['data']['size'] == size


def test_patch(create_new_post, everytest):
    print("\nИзменение данных по объекту, метод PATCH")
    body = {"name": f"{name}"
            }

    response = requests.patch(f'{host}/object/{create_new_post}', headers=headers, json=body)
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['name'] == name


def test_delete(create_post_for_delete, everytest):
    print("\nУдаление объекта, метод DELETE")
    response = requests.delete(f'{host}/object/{create_post_for_delete}')
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'


@pytest.mark.regress
@pytest.mark.parametrize(
    'body',
    [
        {"name": "One", "data": {"color": "Black", "size": "min"}},
        {"name": "Two", "data": {"color": "White", "size": "max"}},
        {"name": "Three", "data": {"color": "Blue", "size": "medium"}}
    ]
)
def test_post_parametrize(clean, everytest, body):
    print("\nCоздание объекта метод POST")
    response = requests.post(f'{host}/object', headers=headers, json=body)
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    data = response.json()
    clean.append(data['id'])  # Добавляю id в список для последующего удаления
