import requests
import allure
import pytest

host = 'http://167.172.172.115:52353/'
headers = {'Content-Type': 'application/json'}

# Вынес в переменные, что бы потом можно было сравнить
name = "Two object"
color = "Orange"
size = "Little"


@allure.story("Create a new object")
@allure.feature("POST Operations")
@allure.title("Create object using POST method")
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
@allure.story("Retrieve an object by ID")
@allure.feature("GET Operations")
@allure.title("Retrieve object using GET method")
def test_get(create_new_post, everytest):
    print("\nПолучение данных по объекту, метод GET")
    response = requests.get(f'{host}/object/{create_new_post}')
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['id'] == create_new_post, f"Ждал id: {create_new_post}, получил {data['id']}"


@pytest.mark.medium
@allure.story("Update an object")
@allure.feature("PUT Operations")
@allure.title("Update object using PUT method")
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


@allure.story("Partially update an object")
@allure.feature("PATCH Operations")
@allure.title("Update object using PATCH method")
def test_patch(create_new_post, everytest):
    print("\nИзменение данных по объекту, метод PATCH")
    body = {"name": f"{name}"
            }

    response = requests.patch(f'{host}/object/{create_new_post}', headers=headers, json=body)
    data = response.json()
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'
    assert data['name'] == name


@allure.story("Delete an object")
@allure.feature("DELETE Operations")
@allure.title("Delete object using DELETE method")
def test_delete(create_post_for_delete, everytest):
    print("\nУдаление объекта, метод DELETE")
    response = requests.delete(f'{host}/object/{create_post_for_delete}')
    assert response.status_code == 200, f'Ждал статус код 200, но получил {response.status_code}'


@pytest.mark.regress
@allure.story("Create objects with different parameters")
@allure.feature("POST Operations")
@allure.title("Create objects using parameterized POST requests")
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


@allure.feature("Object Management")
@allure.story("Create and validate an object")
@allure.title("Создю объект и проверяю его поля")
def test_create_and_validate_object():
    body = {"name": "TestObject", "data": {"color": "Green", "size": "Medium"}}

    with allure.step("Send a POST request to create a new object"):
        response = requests.post(f"{host}/object", headers=headers, json=body)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        data = response.json()
        object_id = data.get("id")
        assert object_id, "Object ID was not returned in the response"

    with allure.step("Send a GET request to retrieve the created object"):
        response = requests.get(f"{host}/object/{object_id}", headers=headers)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        retriev_data = response.json()

    with allure.step("Verify the retrieved object properties"):
        assert retriev_data["name"] == body["name"], f"Expected name {body['name']}, but got {retriev_data['name']}"
        assert retriev_data["data"]["color"] == body["data"][
            "color"], f"Expected color {body['data']['color']}, but got {retriev_data['data']['color']}"
        assert retriev_data["data"]["size"] == body["data"][
            "size"], f"Expected size {body['data']['size']}, but got {retriev_data['data']['size']}"

    with allure.step("Send a DELETE request to remove the created object"):
        response = requests.delete(f"{host}/object/{object_id}", headers=headers)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
