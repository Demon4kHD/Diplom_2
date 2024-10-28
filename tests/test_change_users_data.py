import allure
import pytest

from data_endpoint.changing_user_data import ChangingUserData as CUD
from helper import get_json_from_some_users_data


@allure.feature('Проверки смены данных пользователя')
class TestChangeUsersData:
    @allure.title('Смена данных пользователя без авторизации')
    def test_change_users_data_without_authorization(self, create_user_and_delete_after_test):
        user = create_user_and_delete_after_test
        user.changing_user_data()

        user.assert_status_code_and_json(CUD.CHANGING_USER_WITHOUT_AUTHORIZATION_STATUS_CODE,
                                        CUD.CHANGING_USER_WITHOUT_AUTHORIZATION)

    @allure.title('Смена данных пользователя')
    @pytest.mark.parametrize('is_witch_changed', [["name"], ["password"], ["email"],
                                                  ["name", "password"], ["password", "email"],
                                                  ["name", "email"], ["name", "password", "email"]])
    def test_change_users_data_with_authorization(self, create_user_and_delete_after_test, is_witch_changed):
        user = create_user_and_delete_after_test
        user.changing_user_data(selected_authorization=True,
                                    is_witch_changed=is_witch_changed)

        user.assert_status_code_and_json(CUD.CHANGING_USER_SUCCESS_STATUS_CODE,
                                             CUD.CHANGING_USER_SUCCESS)

    @allure.title('Смена пароля пользователя без изменения пароля')
    def test_change_user_data_with_same_email(self, create_user_and_delete_after_test,
                                              create_and_delete_duplicate_user):
        user = create_user_and_delete_after_test
        same_user = create_and_delete_duplicate_user
        existing_json = get_json_from_some_users_data(same_user.request_json)
        user.changing_user_data(existing_json=existing_json)

        user.assert_status_code_and_json(CUD.CHANGING_USER_WITH_SAME_EMAIL_STATUS_CODE,
                                             CUD.CHANGING_USER_WITH_SAME_EMAIL)
