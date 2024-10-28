import requests
import allure

from endpoints.base_endpoint import BaseMethod
from data_endpoint.registration_data import RegistrationData as RD
from helper import create_data_for_test, create_request_json_for_test


class RegistrationMethod(BaseMethod):
    @allure.step('Создание пользователя')
    def post_create_user(self, not_created=None):
        name, password, email = create_data_for_test(), create_data_for_test(), create_data_for_test(type_obj='email')
        self.request_json = create_request_json_for_test(
            RD.REGISTRATION_BODY, [email, password, name], not_created)
        self.response = requests.post(url=RD.REGISTRATION_URL, json=self.request_json)
        if not_created == None:
            self.token = self.response.json()["accessToken"]
            self.refresh_token = self.response.json()["refreshToken"]

        return self.response

    @allure.step('Создание второго пользователя')
    def post_create_duplicate_user(self, json_for_repeat):
        self.response = requests.post(url=RD.REGISTRATION_URL, json=json_for_repeat)

        return self.response