import allure
import requests

from data_endpoint.create_order_data import CreateOrderData as COD
from endpoints.changing_user_endpoint import ChangingUserMethod as CUM
from helper import get_ingredients_data_for_test, get_ingredients_list_for_create_burger, get_json_for_create_order


class CreateOrderEndpoint(CUM):
    @allure.step('Создание заказа')
    def post_create_order(self, without_ingredients: bool, with_not_valid_hash: bool):
        created_data_for_method = get_ingredients_data_for_test()
        data_for_method = get_ingredients_list_for_create_burger(created_data_for_method,
                                                                 without_ingredients,
                                                                 with_not_valid_hash)
        json_for_endpoint = get_json_for_create_order(data_for_method)

        self.response = requests.post(url=COD.CREATE_ORDER_URL,
                                      headers={"authorization": f'{self.token}'},
                                      json=json_for_endpoint)

        return self.response, data_for_method
