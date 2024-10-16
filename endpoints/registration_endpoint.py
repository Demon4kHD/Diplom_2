import requests

from endpoints.base_endpoint import BaseMethod
from data_endpoint.registration_data import RegistrationData as RD
from helper import create_data_for_test, create_request_json_for_test


class RegistrationMethod(BaseMethod):
    token = ''

    def post_create_user(self, repeat_request=False, json_for_repeat={}, not_created=None):
        if repeat_request == False:
            name, password, email = create_data_for_test(), create_data_for_test(), create_data_for_test(type_obj='email')
            request_json = create_request_json_for_test(RD.REGISTRATION_BODY, [email, password, name], not_created)
            self.response = requests.post(url=RD.REGISTRATION_URL, json =request_json)
            self.response_json = self.response.json()
            if not_created == None:
                self.token = self.response_json["accessToken"]
        else:
            self.response = requests.post(url=RD.REGISTRATION_URL, json=json_for_repeat)

        return self.response_json, self.token
