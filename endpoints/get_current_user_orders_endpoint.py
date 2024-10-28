import time

import allure
import requests

from data_endpoint.get_current_user_orders_data import GetCurrentUserOrdersData as GCUOD
from endpoints.create_order_endpoint import CreateOrderEndpoint as COE
from helper import get_ingredients_list_for_create_burger, get_ingredients_data_for_test, get_json_for_create_order


class CurrentUserOrdersEndpoint(COE):
    @allure.step('Получение списка заказов конкретного пользователя')
    def get_current_user_orders_endpoint(self, repeat_create_order: int = 1):
        for repeat in range(repeat_create_order):
            created_data_for_method = get_ingredients_data_for_test()
            data_for_method = get_ingredients_list_for_create_burger(created_data_for_method,
                                                                     False,
                                                                     False)
            json_for_endpoint = get_json_for_create_order(data_for_method)

            self.response = requests.post(url=GCUOD.CREATE_ORDER_URL,
                                          headers={"authorization": f'{self.token}'},
                                          json=json_for_endpoint)

        self.response = requests.get(url=GCUOD.GET_CURRENT_USER_ORDERS_URL,
                                     headers={"Authorization": f'{self.token}'})

        return self.response
