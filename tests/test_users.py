import requests
import allure
from utils import user_helpers as users

@allure.story("Users API")
@allure.title("Get list of users (page 2)")
@allure.step("Test: GET /api/users?page=2")
def test_get_users_list():
    response = users.get_users_list()
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert isinstance(json_data["data"], list)


@allure.story("Users API")
@allure.title("Create user with name and job")
@allure.step("Test: POST /api/users")
def test_create_user():
    payload = {"name": "John", "job": "QA"}
    response = users.post_create_user(payload)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["name"] == payload["name"]
    assert json_data["job"] == payload["job"]
    assert "id" in json_data
    assert "createdAt" in json_data


@allure.story("Users API")
@allure.title("Update user")
@allure.step("Test: PUT /api/users/user_id")
def test_update_user():
    payload = {
        "name": "John Updated",
        "job": "Lead QA Engineer"
    }
    response = users.post_update_user(3, payload)
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["name"] == payload["name"]
    assert json_data["job"] == payload["job"]
    assert "updatedAt" in json_data


@allure.story("Users API")
@allure.title("Delete user")
@allure.step("Test: DELETE /api/users/user_id")
def test_delete_user():
    response = users.delete_user(2)
    assert response.status_code == 204
    assert response.text == "", "Expected empty response body"


@allure.story("Users API")
@allure.title("Single user not found")
@allure.step("Test: GET /api/users/user_id")
def test_get_non_existing_user():
    response = users.get_non_existing_user(23)
    assert response.status_code == 404


@allure.story("Users API")
@allure.title("Get single user by ID")
@allure.step("GET /api/users/2")
def test_get_single_user():
    response = users.get_single_user(6)
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    print(data)
    user = data["data"]
    assert user["id"] == 6
    assert "email" in user
    assert "first_name" in user