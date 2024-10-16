import requests

from data_endpoint.authorization_data import AuthorizationData as AD
from endpoints.registration_endpoint import RegistrationMethod as RM
from helper import create_data_for_test, create_request_json_for_test, create_new_json_from_json


class AuthorizationMethod(RM):

    def post_authorized_user(self, json_data, not_created=None):
        new_json = create_new_json_from_json(json_data=json_data, not_crated=not_created)
        self.response = requests.post(url=AD.AUTHORIZATION_URL, json=new_json)
        response_json = self.response.json()
        try:
            RM.token = response_json["accessToken"]
        except KeyError:
            return RM.token, response_json
        return response_json
