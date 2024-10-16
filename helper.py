import random

import requests

from data_endpoint.authorization_data import AuthorizationData
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

def create_new_json_from_json(json_data: dict, not_crated: str=''):
    new_json = {}
    for key in json_data:
        if key == not_crated or key == 'name':
            continue
        else:
            new_json[key] = json_data[key]

    return new_json
some_method = requests.post(url=RegistrationData.REGISTRATION_URL,
                            json={"email": "ertyyu@mail.ru", 'password': 'k62ewjwr12', "name": 'Victor'})
some_method_json = some_method.json()
token = some_method_json["accessToken"]
some_method = requests.post(url=RegistrationData.REGISTRATION_URL,
                            json={"email": "ertyyu@mail.ru", 'password': 'k62ewjwr12', "name": 'Victor'})
method = requests.delete(url=RegistrationData.DELETE_URL,
                         headers={"authorization": f'{token}'})
print(method.status_code)