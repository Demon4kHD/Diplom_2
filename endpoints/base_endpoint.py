import allure


class BaseMethod:
    response = None
    token = ''
    request_json = {}
    refresh_token = ''

    @allure.step('Проверка статус кода и структуры ответа')
    def assert_status_code_and_json(self, checked_status_code, standard_json):

        assert self.response.status_code == checked_status_code
        assert len(self.response.json()) == len(standard_json)
        for element in standard_json:
            assert type(standard_json[element]) == type(self.response.json()[element])

    @allure.step('Проверка статус кода для ответов без тела')
    def assert_status_code(self, checked_status_code):

        assert self.response.status_code == checked_status_code

    @allure.step('Проверка статус кода и структуры ответа при получении списка заказов')
    def assert_status_code_and_json_for_get_orders_endpoint(self, checked_status_code,
                                                            standard_json,
                                                            created_orders_num=1):

        assert len(self.response.json()["orders"]) == created_orders_num
        assert len(self.response.json()["orders"]) == self.response.json()["total"]
        assert self.response.status_code == checked_status_code
        assert len(self.response.json()) == len(standard_json)
        for element in standard_json:
            assert type(standard_json[element]) == type(self.response.json()[element])
