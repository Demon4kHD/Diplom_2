import random

import requests

from data_endpoint.create_order_data import CreateOrderData as COD


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


def creating_changeable_object(request_json: dict, is_witch_changed: list):
    new_json = {}
    for key in request_json:
        if key in is_witch_changed:
            new_json[key] = create_data_for_test(type_obj=key, len_data=10)
        else:
            continue

    return new_json

def get_json_from_some_users_data(request_json):
    new_json: dict = {'email': request_json["email"]}

    return new_json


def get_ingredients_data_for_test():
    ingredients_data = COD.CREATE_ORDER_DATA_INGREDIENTS_LIST_PATTERN

    response_json = requests.get(url=COD.CREATE_ORDER_GET_INGREDIENTS_LIST_URL).json()

    for ingredient in response_json["data"]:
        new_name_list, new_id_list = [], []

        if ingredient["type"] == 'bun':
            param = "bun"

        elif ingredient["type"] == 'sauce':
            param = 'sauce'

        else:
            param = 'main'

        name_list, id_list = ingredients_data[param]["name"], ingredients_data[param]["_id"]
        name_str, id_str = ingredient["name"], ingredient["_id"]

        new_name_list.append(name_str), new_id_list.append(id_str)

        ingredients_data[param]["name"], ingredients_data[param]["_id"] = (name_list + new_name_list,
                                                                           id_list + new_id_list)

    return ingredients_data


def get_ingredients_list_for_create_burger(current_ingredients_dict: dict,
                                           without_ingredients: bool,
                                           with_not_valid_hash: bool):
    current_ingredients_data = {"_id": [], 'name': []}

    for type_ingredient in COD.CREATE_ORDER_TYPE_INGREDIENTS:
        new_name_list, new_id_list = [], []

        if without_ingredients == True:
            continue

        else:
            name_list, id_list = current_ingredients_data['name'], current_ingredients_data['_id']

            random_value_from_id_list = random.choice(current_ingredients_dict[type_ingredient]['_id'])
            index_in_id_list = current_ingredients_dict[type_ingredient]['_id'].index(random_value_from_id_list)
            name_value = current_ingredients_dict[type_ingredient]['name'][index_in_id_list]

            if with_not_valid_hash == True:
                new_name_list.append(name_value), new_id_list.append(random_value_from_id_list + '100500')
            else:
                new_name_list.append(name_value), new_id_list.append(random_value_from_id_list)

            current_ingredients_data['_id'], current_ingredients_data['name'] = (id_list + new_id_list,
                                                                                 name_list + new_name_list)

    return current_ingredients_data


def get_json_for_create_order(data_dict: dict):
    current_json = COD.CREATE_ORDER_REQUEST_ADD_INGREDIENTS_BODY
    ingredients_list = []
    for id_ingredient in data_dict['_id']:
        ingredients_list.append(id_ingredient)

    current_json["ingredients"] = ingredients_list

    return current_json
