import pytest

from data_endpoint.registration_data import RegistrationData as RD


class TestRegistration:

    def test_create_user(self, delete_user_after_test):
        response = delete_user_after_test
        response.post_create_user()

        response.assert_status_code_and_json(RD.REGISTRATION_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_RESPONSE)


    def test_creating_user_with_same_data(self, delete_user_after_test):
        response = delete_user_after_test
        response.post_create_user()
        response.post_create_duplicate_user(response.request_json)

        response.assert_status_code_and_json(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_SAME_DATA)


    @pytest.mark.parametrize('same_data', ['email', 'password', 'name'])
    def test_creating_user_without_same_data(self, delete_user_after_test, same_data):
        response = delete_user_after_test
        response.post_create_user(not_created=same_data)

        response.assert_status_code_and_json(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE,
                                             RD.REGISTRATION_BODY_WITHOUT_SAME_DATA)
