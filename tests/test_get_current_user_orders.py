import allure
import pytest

from data_endpoint.get_current_user_orders_data import GetCurrentUserOrdersData as QCUOD

@allure.feature('Проверки полученя заказов конкретного пользователя')
class TestGetCurrentUserOrders:
    @allure.title('Получение списка с одним заказом у конкретоного пользователя')
    @allure.description("Тест падает, хотя должен проходить")
    def test_get_current_user_with_one_order(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)
        user.assert_status_code_and_json(QCUOD.AUTHORIZATION_RESPONSE_STATUS_CODE,
                                         QCUOD.AUTHORIZATION_BODY_RESPONSE)

        burger = create_burger
        burger.get_current_user_orders_endpoint()
        burger.assert_status_code_and_json_for_get_orders_endpoint(QCUOD.GET_CURRENT_USER_ORDERS_SUCCESS_STATUS_CODE,
                                                                   QCUOD.GET_CURRENT_USER_ORDERS_SUCCESS_BODY,)

    @allure.title('Получение списка с несколькими заказами у конкретоного пользователя')
    @allure.description("Тест падает, хотя должен проходить")
    @pytest.mark.parametrize('number_of_orders', (1, 2, 25, 49, 50))
    def test_get_current_user_with_same_orders(self, create_user_and_delete_after_test, create_burger, number_of_orders):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)
        user.assert_status_code_and_json(QCUOD.AUTHORIZATION_RESPONSE_STATUS_CODE,
                                         QCUOD.AUTHORIZATION_BODY_RESPONSE)

        burger = create_burger
        burger.get_current_user_orders_endpoint(number_of_orders)
        burger.assert_status_code_and_json_for_get_orders_endpoint(QCUOD.GET_CURRENT_USER_ORDERS_SUCCESS_STATUS_CODE,
                                                                   QCUOD.GET_CURRENT_USER_ORDERS_SUCCESS_BODY)

    @allure.title('Получение списка с одним заказом у неавторизованного пользователя')
    def test_get_current_user_orders_without_authorization(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test
        user.assert_status_code_and_json(QCUOD.REGISTRATION_RESPONSE_STATUS_CODE,
                                         QCUOD.REGISTRATION_BODY_RESPONSE)

        burger = create_burger
        burger.get_current_user_orders_endpoint()
        burger.assert_status_code_and_json(QCUOD.GET_CURRENT_USER_ORDERS_ERROR_AUTHORIZATION_STATUS_CODE,
                                           QCUOD.GET_CURRENT_USER_ORDERS_ERROR_AUTHORIZATION_BODY)
