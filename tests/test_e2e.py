import allure
import requests
from utils import auth_helpers as auth
from utils import user_helpers as users


@allure.story("E2E Scenario")
@allure.title("Register → Login → Create User")
@allure.step("Full user flow from registration to creation")
def test_e2e_register_login_create_user():
    register_payload ={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    register_response = auth.post_register_user(register_payload)
    assert register_response.status_code == 200
    token = register_response.json().get("token")
    assert token is not None
    login_payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_response = auth.post_login_user(login_payload)
    assert login_response.status_code == 200
    create_payload = {"name": "NewUser", "job": "QA"}
    headers = {"Authorization": f"Bearer {token}"}
    create_response = users.post_create_user_with_headers(create_payload, headers=headers)
    assert  create_response.status_code == 201
    created_user = create_response.json()
    assert created_user["name"] == create_payload["name"]
    assert created_user["job"] == create_payload["job"]
