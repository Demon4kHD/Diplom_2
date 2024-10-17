import pytest

from data_endpoint.authorization_data import AuthorizationData as AD


class TestAuthorization:

    def test_authorized_user(self, create_user_and_delete_after_test):
        response = create_user_and_delete_after_test
        response.post_authorized_user(response.request_json)

        response.assert_status_code_and_json(AD.AUTHORIZATION_RESPONSE_STATUS_CODE,
                                             AD.AUTHORIZATION_BODY_RESPONSE)

    @pytest.mark.parametrize('same_data', ['email', 'password'])
    def test_authorized_user_without_same_data(self, create_user_and_delete_after_test, same_data):
        response = create_user_and_delete_after_test
        response.post_authorized_user(response.request_json, same_data)

        response.assert_status_code_and_json(AD.AUTHORIZATION_ERROR_RESPONSE_STATUS_CODE,
                                             AD.AUTHORIZATION_BODY_INCORRECT_DATA)