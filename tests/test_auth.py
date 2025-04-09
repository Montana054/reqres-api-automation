import requests
import allure
from utils import auth_helpers as auth


@allure.story("Auth API")
@allure.title("Login with valid credentials")
@allure.step("Test: POST /api/login (valid)")
def test_login_valid():
    payload = \
    {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = auth.post_login_user(payload)
    assert response.status_code == 200, "Expected status code 200"
    json_data = response.json()
    assert "token" in json_data, "Expected token in response"


@allure.story("Auth API")
@allure.title("Login with missing password (negative)")
@allure.step("Test: POST /api/login (missing password)")
def test_login_missing_password():
    payload = \
    {
        "email": "eve.holt@reqres.in"
        # no password
    }
    response = auth.post_login_missing_password(payload)
    assert response.status_code == 400, "Expected status code 400"
    json_data = response.json()
    assert "error" in json_data
    assert json_data["error"] == "Missing password"

@allure.story("Auth API")
@allure.title("Register new user")
@allure.step("POST /api/register")
def test_register_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = auth.post_register_user(payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "id" in json_data
    assert "token" in json_data