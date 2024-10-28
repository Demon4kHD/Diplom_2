import allure

from data_endpoint.create_order_data import CreateOrderData as COD
from conftest import create_burger


@allure.feature('Проверки создания заказов')
class TestCreateOrder:
    @allure.title('Создание заказа неавторизованным пользователем')
    @allure.description("Тест падает, хотя должен проходить")
    def test_create_order_without_authorization(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test

        burger = create_burger
        burger.post_create_order(False, False)

        burger.assert_status_code(COD.CREATE_ORDER_ERROR_WITHOUT_AUTHORIZATION_STATUS_CODE)
        # Этот тест падает, а должен проходить

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_with_authorization(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)

        burger = create_burger
        burger.post_create_order(False, False)

        burger.assert_status_code_and_json(COD.CREATE_ORDER_REQUEST_ADD_INGREDIENTS_STATUS_CODE,
                                           COD.CREATE_ORDER_RESPONSE_ADD_INGREDIENTS_BODY)

    @allure.title('Создание заказа авторизованным пользователем без ингредиентов')
    def test_create_order_without_ingredients(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)

        burger = create_burger
        burger.post_create_order(True, False)

        burger.assert_status_code_and_json(COD.CREATE_ORDER_ERROR_NONE_INGREDIENTS_STATUS_CODE,
                                           COD.CREATE_ORDER_ERROR_NONE_INGREDIENTS_RESPONSE_BODY)

    @allure.title('Создание заказа авторизованным пользователем с невалидным хешем ингредиентов')
    def test_create_order_without_valid_hash(self, create_user_and_delete_after_test, create_burger):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)

        burger = create_burger
        burger.post_create_order(False, True)

        burger.assert_status_code(COD.CREATE_ORDER_ERROR_NOT_VALID_HASH_STATUS_CODE)
