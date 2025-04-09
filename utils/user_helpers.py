import requests
from config.endpoints import USERS

def get_users_list(page=2):
    response = requests.get(f"{USERS}?page={page}")
    return response

def post_create_user(data):
    response = requests.post(USERS, json=data)
    return response


def post_update_user(user_id, payload):
    response = requests.put(f"{USERS}/{user_id}", json=payload)
    return response


def delete_user(user_id):
    response = requests.delete(f"{USERS}/{user_id}")
    return response


def get_non_existing_user(user_id):
    response = requests.get(f"{USERS}/{user_id}")
    return response


def get_single_user(user_id):
    response = requests.get(f"{USERS}/{user_id}")
    return response

def post_create_user_with_headers(data, headers=None):
    response = requests.post(USERS, json=data, headers=headers)
    return response
