import pytest
import requests
import allure

from data_endpoint.registration_data import RegistrationData as RD
from endpoints.changing_user_endpoint import ChangingUserMethod as CUM
from endpoints.get_current_user_orders_endpoint import CurrentUserOrdersEndpoint as CUOE
from endpoints.registration_endpoint import RegistrationMethod as RM


@pytest.fixture
def delete_user_after_test():
    with allure.step("Создание объекта user"):
        user = RM()

    yield user

    with allure.step("Удаление пользователя"):
        deleted = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{user.token}'})
    status_code = deleted.status_code
    if user.token != '':
        assert status_code == 202
    else:
        assert status_code == 401

@pytest.fixture
def create_user_and_delete_after_test():
    user = CUOE()
    with allure.step("Создание пользователя"):
        user.post_create_user()

    yield user

    with allure.step("Удаление пользователя"):
        deleted = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{user.token}'})
    status_code = deleted.status_code
    assert status_code == 202

@pytest.fixture
def create_and_delete_duplicate_user():
    user = CUM()
    with allure.step("Создание пользователя"):
        user.post_create_user()

    yield user

    with allure.step("Удаление пользователя"):
        deleted = requests.delete(url=RD.DELETE_URL, headers={"authorization": f'{user.token}'})
    status_code = deleted.status_code
    assert status_code == 202


@pytest.fixture
def create_burger():
    with allure.step("Создание объекта burger"):
        burger = CUOE()

    return burger
