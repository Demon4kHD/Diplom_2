import allure
import pytest

from data_endpoint.registration_data import RegistrationData as RD


@allure.feature('Проверки регистрации пользователя')
class TestRegistration:
    @allure.title('Регистрация нового пользователя')
    def test_create_user(self, delete_user_after_test):
        user = delete_user_after_test
        user.post_create_user()

        user.assert_status_code_and_json(RD.REGISTRATION_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_RESPONSE)

    @allure.title('Регистрация пользователя, который уже зарегистрирован')
    def test_creating_user_with_same_data(self, delete_user_after_test):
        user = delete_user_after_test
        user.post_create_user()
        user.post_create_duplicate_user(user.request_json)

        user.assert_status_code_and_json(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_SAME_DATA)

    @allure.title('Регистрация пользователя без заполнения одного из обязательных полей')
    @pytest.mark.parametrize('same_data', ['email', 'password', 'name'])
    def test_creating_user_without_same_data(self, delete_user_after_test, same_data):
        user = delete_user_after_test
        user.post_create_user(not_created=same_data)

        user.assert_status_code_and_json(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_WITHOUT_SAME_DATA)
