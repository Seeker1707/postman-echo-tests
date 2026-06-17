import requests

BASE_URL = "https://postman-echo.com"


def test_get_no_params():
    """GET без параметров: статус 200, args пуст, url совпадает."""
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == {}
    assert data["url"] == f"{BASE_URL}/get"


def test_get_with_params():
    """GET с query-параметрами: args совпадают с переданными."""
    params = {"foo": "bar", "baz": "123"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["args"] == {"wrong": "value"}


def test_post_form_data():
    """POST с данными формы: поле form содержит отправленные данные."""
    form_data = {"username": "testuser", "password": "secret"}
    response = requests.post(f"{BASE_URL}/post", data=form_data)
    assert response.status_code == 200
    data = response.json()
    assert data["form"] == form_data


def test_post_json():
    """POST с JSON: поле json содержит именно отправленный объект."""
    json_body = {"key": "value", "list": [1, 2, 3]}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/post", json=json_body, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == json_body


def test_custom_header():
    """Передача кастомного заголовка: он возвращается в headers ответа."""
    custom_header_name = "X-Custom-Header"
    custom_header_value = "TestValue"
    headers = {custom_header_name: custom_header_value}
    response = requests.get(f"{BASE_URL}/get", headers=headers)
    assert response.status_code == 200
    data = response.json()
    # Postman Echo приводит имена заголовков к нижнему регистру
    assert data["headers"]["x-custom-header"] == custom_header_value