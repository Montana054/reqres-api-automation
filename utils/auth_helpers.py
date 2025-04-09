import requests
from config.endpoints import LOGIN, REGISTER


def post_login_user(payload):
    response = requests.post(LOGIN, json=payload)
    return response


def post_login_missing_password(payload):
    response = requests.post(LOGIN, json=payload)
    return response

def post_register_user(payload):
    response = requests.post(REGISTER, json=payload)
    return response

