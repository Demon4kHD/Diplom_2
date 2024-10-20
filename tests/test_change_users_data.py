import pytest

from data_endpoint.changing_user_data import ChangingUserData as CUD
from helper import get_json_from_some_users_data


class TestChangeUsersData:

    def test_change_users_data_without_authorization(self, create_and_delete_user_for_changing_test):
        response = create_and_delete_user_for_changing_test
        response.changing_user_data()
        response.assert_status_code_and_json(CUD.CHANGING_USER_WITHOUT_AUTHORIZATION_STATUS_CODE,
                                        CUD.CHANGING_USER_WITHOUT_AUTHORIZATION)

    @pytest.mark.parametrize('is_witch_changed', [["name"], ["password"], ["email"],
                                                  ["name", "password"], ["password", "email"],
                                                  ["name", "email"], ["name", "password", "email"]])
    def test_change_users_data_with_authorization(self, create_and_delete_user_for_changing_test, is_witch_changed):
        response = create_and_delete_user_for_changing_test
        response.changing_user_data(selected_authorization=True,
                                    is_witch_changed=is_witch_changed)
        response.assert_status_code_and_json(CUD.CHANGING_USER_SUCCESS_STATUS_CODE,
                                             CUD.CHANGING_USER_SUCCESS)

    def test_change_user_data_with_same_email(self,create_and_delete_user_for_changing_test, create_user_and_delete_after_test):
        response = create_and_delete_user_for_changing_test
        same_response = create_user_and_delete_after_test
        existing_json = get_json_from_some_users_data(same_response.request_json)
        response.changing_user_data(existing_json=existing_json)
        response.assert_status_code_and_json(CUD.CHANGING_USER_WITH_SAME_EMAIL_STATUS_CODE,
                                             CUD.CHANGING_USER_WITH_SAME_EMAIL)
