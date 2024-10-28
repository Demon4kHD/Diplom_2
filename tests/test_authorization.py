import allure
import pytest

from data_endpoint.authorization_data import AuthorizationData as AD


@allure.feature('Проверки авторизации пользователя')
class TestAuthorization:
    @allure.title('Авторизация пользователя')
    def test_authorized_user(self, create_user_and_delete_after_test):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json)

        user.assert_status_code_and_json(AD.AUTHORIZATION_RESPONSE_STATUS_CODE,
                                             AD.AUTHORIZATION_BODY_RESPONSE)

    @allure.title('Авторизация пользователя без обязательного поля в body')
    @pytest.mark.parametrize('same_data', ['email', 'password'])
    def test_authorized_user_without_same_data(self, create_user_and_delete_after_test, same_data):
        user = create_user_and_delete_after_test
        user.post_authorized_user(user.request_json, same_data)

        user.assert_status_code_and_json(AD.AUTHORIZATION_ERROR_RESPONSE_STATUS_CODE,
                                             AD.AUTHORIZATION_BODY_INCORRECT_DATA)