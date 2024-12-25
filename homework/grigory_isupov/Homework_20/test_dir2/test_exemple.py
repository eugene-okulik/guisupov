import allure


@allure.story("Basic assertion check")
@allure.feature("Simple tests")
def test_one():
    assert 1 == 1


@allure.story("Number comparison")
@allure.feature("Basic arithmetic operations")
@allure.story()
@allure.feature()
def test_two():
    a = 6
    b = 9
    assert a > b


@allure.story("Sum verification")
@allure.feature("Basic arithmetic operations")
def test_fife():
    assert 2 + 2


@allure.story("String equality")
@allure.feature("String operations")
def test_string_equality():
    assert "hello" == "hello"


@allure.story("Substring existence")
@allure.feature("String operations")
def test_substring():
    assert "world" in "hello world"


@allure.story("Check for empty list")
@allure.feature("List operations")
def test_empty_list():
    my_list = []
    assert len(my_list) == 0


@allure.story("List item existence")
@allure.feature("List operations")
def test_item_in_list():
    my_list = [1, 2, 3, 4]
    assert 3 in my_list


@allure.story("Check for empty dictionary")
@allure.feature("Dictionary operations")
def test_empty_dict():
    my_dict = {}
    assert len(my_dict) == 0


@allure.story("Dictionary key existence")
@allure.feature("Dictionary operations")
def test_key_in_dict():
    my_dict = {"name": "Alice", "age": 25}
    assert "name" in my_dict


@allure.story("Dictionary value check")
@allure.feature("Dictionary operations")
def test_value_in_dict():
    my_dict = {"name": "Alice", "age": 25}
    assert my_dict["age"] == 25


@allure.story("Tuple item existence")
@allure.feature("Tuple operations")
def test_item_in_tuple():
    my_tuple = (10, 20, 30)
    assert 20 in my_tuple


@allure.story("Check for set uniqueness")
@allure.feature("Set operations")
def test_set_uniqueness():
    my_set = {1, 2, 3, 3, 4}
    assert len(my_set) == 4


@allure.story("Set membership check")
@allure.feature("Set operations")
def test_set_membership():
    my_set = {1, 2, 3}
    assert 4 in my_set
