import requests
import pytest

from endpoints.registration_endpoint import RegistrationMethod as RM
from data_endpoint.registration_data import RegistrationData as RD
from endpoints.authorization_endpoint import AuthorizationMethod as AM


@pytest.fixture
def delete_user_after_test():
    response = RM()
    yield response
    deleted = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{response.token}'})
    status_code = deleted.status_code
    if response.token != '':
        assert status_code == 202
    else:
        assert status_code == 401

@pytest.fixture
def create_user_and_delete_after_test():
    response = AM()
    response.post_create_user()
    yield response
    deleted = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{response.token}'})
    status_code = deleted.status_code
    assert status_code == 202

def create_and_auth_user_and_delete_after_test(create_user_and_delete_after_test):
    response = create_user_and_delete_after_test
    response.post_authorized_user(response.request_json)

