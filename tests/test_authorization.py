import pytest

from data_endpoint.authorization_data import AuthorizationData as AD


class TestAuthorization:

    def test_authorized_user(self, create_user_and_delete_after_test):
        response = create_user_and_delete_after_test

        response.post_authorized_user(response.request_json)

        response.assert_length_json_file(AD.AUTHORIZATION_BODY_RESPONSE)
        response.assert_structure_response_json(AD.AUTHORIZATION_BODY_RESPONSE)
        response.assert_status_code(AD.AUTHORIZATION_RESPONSE_STATUS_CODE)

    @pytest.mark.parametrize('same_data', ['email', 'password'])
    def test_authorized_user_without_same_data(self, create_user_and_delete_after_test, same_data):
        response = create_user_and_delete_after_test

        response.post_authorized_user(response.request_json, same_data)

        response.assert_length_json_file(AD.AUTHORIZATION_BODY_INCORRECT_DATA)
        response.assert_structure_response_json(AD.AUTHORIZATION_BODY_INCORRECT_DATA)
        response.assert_status_code(AD.AUTHORIZATION_ERROR_RESPONSE_STATUS_CODE)
