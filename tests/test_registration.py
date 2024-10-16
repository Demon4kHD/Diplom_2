import pytest
from data_endpoint.registration_data import RegistrationData as RD
from endpoints.registration_endpoint import RegistrationMethod as RM


class TestRegistration:

    def test_create_user(self, delete_user_after_test):
        response = delete_user_after_test
        response.post_create_user()
        response.assert_length_json_file(RD.REGISTRATION_BODY_RESPONSE)
        response.assert_structure_response_json(RD.REGISTRATION_BODY_RESPONSE)
        response.assert_status_code(RD.REGISTRATION_RESPONSE_STATUS_CODE)

    def test_creating_user_with_same_data(self, delete_user_after_test):
        response = delete_user_after_test
        response.post_create_user()
        response.post_create_user(repeat_request=True)
        # response.assert_length_json_file(RD.REGISTRATION_BODY_SAME_DATA)
        # response.assert_structure_response_json(RD.REGISTRATION_BODY_SAME_DATA)
        response.assert_status_code(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE)

    @pytest.mark.parametrize('same_data', ['email', 'password', 'name'])
    def test_creating_user_without_same_data(self, delete_user_after_test, same_data):
        response = delete_user_after_test
        response.post_create_user(not_created=same_data)
        response.assert_length_json_file(RD.REGISTRATION_BODY_WITHOUT_SAME_DATA)
        response.assert_structure_response_json(RD.REGISTRATION_BODY_WITHOUT_SAME_DATA)
        response.assert_status_code(RD.REGISTRATION_ERROR_RESPONSE_STATUS_CODE)
