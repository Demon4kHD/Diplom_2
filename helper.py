import random

import requests

from data_endpoint.authorization_data import AuthorizationData
from data_endpoint.changing_user_data import ChangingUserData
from data_endpoint.registration_data import RegistrationData


def create_request_json_for_test(body=dict, params=list, not_created=None):
    keys_body = list(body.keys())

    created_object = {}
    for position in range(len(keys_body)):
        if keys_body[position] != not_created:
            created_object[keys_body[position]] = params[position]
        else:
            continue

    return created_object


def create_data_for_test(type_obj=None, len_data=8, special_symbol=None):
    symbols_for_created_object = 'abcdefghijklmnopqrstuvwxyz0123456789'
    created_object = ''
    if type_obj == 'special_symbol':
        symbol_with_special_symbol = symbols_for_created_object + special_symbol
        for step in range(len_data):
            created_object += random.choice(symbol_with_special_symbol)

    elif type_obj == 'email':
        for step in range(len_data):
            created_object += random.choice(symbols_for_created_object)
        created_object += '@yandex.ru'

    else:
        for step in range(len_data):
            created_object += random.choice(symbols_for_created_object)

    return created_object


def create_new_json_from_json(json_data: dict, not_crated: str = ''):
    new_json = {}
    for key in json_data:
        if key == not_crated or key == 'name':
            continue
        else:
            new_json[key] = json_data[key]

    return new_json

def creating_changeable_object(request_json: dict, is_witch_changed: list=[]):
    new_json = {}
    for key in request_json:
        if key in is_witch_changed:
            new_json[key] = create_data_for_test(type_obj=key, len_data=10)
        else:
            continue

    return new_json

def get_json_from_some_users_data(request_json):
    new_json = {}
    new_json['email'] = request_json["email"]

    return new_json

requests.post(url=RegistrationData.REGISTRATION_URL,
              json={"email": "e2rtyyu@mail.ru",
                    "password": "k262ewjwr12",
                    "name": "Victor"})
some_method = requests.post(url=AuthorizationData.AUTHORIZATION_URL,
                            json={"email": "e2rtyyu@mail.ru",
                                  'password': 'k262ewjwr12'})
some_method_json = some_method.json()
token = some_method_json["accessToken"]
print(some_method.status_code)
# print(token)
some_method = requests.patch(url=ChangingUserData.CHANGING_USER_ENDPOINT_URL,
                             headers={"Authorization": f'{token}'},
                             json={"email": "e2rtyyu@mail.ru"})
print(some_method.status_code)
method = requests.delete(url=RegistrationData.DELETE_URL,
                         headers={"authorization": f'{token}'})
print(method.status_code)
