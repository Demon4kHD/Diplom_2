import requests
import pytest

from endpoints.registration_endpoint import RegistrationMethod as RM
from data_endpoint.registration_data import RegistrationData as RD
from endpoints.authorization_endpoint import AuthorizationMethod as AM


@pytest.fixture
def delete_user_after_test():
    response = RM()
    yield response
    is_created = False
    try:
        response = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{RM.token}'})
        status_code = response.status_code

    except IndexError:
        print('Пользователь не создан, удалять нечего!')
    if is_created == True:
        assert status_code == 202

@pytest.fixture
def create_user_and_delete_after_test():
    response = AM()
    response_json, request_json, token = response.post_create_user()
    response.assert_status_code(RD.REGISTRATION_RESPONSE_STATUS_CODE)
    yield response, request_json
    response = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{RM.token}'})
    status_code = response.status_code

    assert status_code == 202
