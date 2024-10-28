import requests
import allure

from data_endpoint.authorization_data import AuthorizationData as AD
from endpoints.registration_endpoint import RegistrationMethod as RM
from helper import create_new_json_from_json


class AuthorizationMethod(RM):
    @allure.step('САвторизация пользователя')
    def post_authorized_user(self, json_data, not_created=None):
        new_json = create_new_json_from_json(json_data=json_data, not_crated=not_created)
        self.response = requests.post(url=AD.AUTHORIZATION_URL, json=new_json)

        return self.response
