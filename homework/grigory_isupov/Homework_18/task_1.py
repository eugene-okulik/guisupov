import requests

host = 'http://167.172.172.115:52353/'
headers = {'Content-Type': 'application/json'}

# Вынес в переменные, что бы потом можно было сравнить
name = "Two object"
color = "Orange"
size = "Little"


def clear(post_id):
    response = requests.delete(f'{host}/object/{post_id}')
    if response.status_code == 200:
        print(f'Объекст с id: {post_id} успешно удален')
    else:
        print(f'Что то пошло не так, {post_id} не удален')


def create_new_post():
    body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "max"}
            }
    response = requests.post(f'{host}/object', headers=headers, json=body)
    print(f'Создание объекта, код ответа: {response.status_code}')
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    data = response.json()
    print(f'Создан объект: {data}')
    return response.json()['id']


def post():
    print("\nCоздание объекта метод POST")
    body = {"name": "Five",
            "data": {
                "color": "Black",
                "size": "min"}
            }
    response = requests.post(f'{host}/object', headers=headers, json=body)
    print(f"Статус код: {response.status_code}")
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    data = response.json()
    print(data)

    clear(data['id'])


def get():
    print("\nПолучение данных по объекту, метод GET")
    post_id = create_new_post()
    response = requests.get(f'{host}/object/{post_id}')
    print(f"Статус код: {response.status_code}")
    data = response.json()
    print(f'Данные по объекту: {data}')
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['id'] == post_id, f"Ждал id: {post_id}, получил {data['id']}"

    clear(post_id)


def put():
    print("\nИзменение данных по объекту, метод PUT")
    post_id = create_new_post()
    body = {"name": f"{name}",
            "data": {
                "color": f"{color}",
                "size": f"{size}"}
            }
    response = requests.put(f'{host}/object/{post_id}', headers=headers, json=body)
    print(f"Статус код: {response.status_code}")
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['name'] == name
    assert data['data']['color'] == color
    assert data['data']['size'] == size
    print(data)

    clear(post_id)


def patch():
    print("\nИзменение данных по объекту, метод PATCH")
    post_id = create_new_post()
    body = {"name": f"{name}"
            }

    response = requests.patch(f'{host}/object/{post_id}', headers=headers, json=body)
    data = response.json()
    print(f"Статус код: {response.status_code}")
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['name'] == name
    print(data)

    clear(post_id)


def delete():
    print("\nУдаление объекта, метод DELETE")
    post_id = create_new_post()
    response = requests.delete(f'{host}/object/{post_id}')
    if response.status_code == 200:
        print(f'Объект с id: {post_id} успешно удален')
    else:
        print(f'Что то пошло не так, объект с id: {post_id} не удален')


get()
post()
put()
patch()
delete()
