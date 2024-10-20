import requests
from endpoints.authorization_endpoint import AuthorizationMethod as AM
from data_endpoint.authorization_data import AuthorizationData as AD
from data_endpoint.changing_user_data import ChangingUserData as CUD
from helper import creating_changeable_object, create_new_json_from_json


class ChangingUserMethod(AM):


    def changing_user_data(self, selected_authorization=False, is_witch_changed=[], existing_json={}):
        token = AM.token
        if selected_authorization == True:
            new_changing_json = create_new_json_from_json(self.request_json, '')
            self.response = requests.post(url=AD.AUTHORIZATION_URL, json=new_changing_json)
            token = self.response.json()["accessToken"]
            self.response = requests.patch(url=CUD.CHANGING_USER_ENDPOINT_URL,
                                           headers={"Authorization": f'{token}'},
                                           json=new_changing_json)

        elif existing_json != {}:
            new_changing_json = create_new_json_from_json(self.request_json, '')
            self.response = requests.post(url=AD.AUTHORIZATION_URL, json=new_changing_json)
            token = self.response.json()["accessToken"]
            self.response = requests.patch(url=CUD.CHANGING_USER_ENDPOINT_URL,
                                           headers={"Authorization": f'{token}'},
                                           json=existing_json)

        else:
            new_changing_json = creating_changeable_object(self.request_json, is_witch_changed)
            self.response = requests.patch(url=CUD.CHANGING_USER_ENDPOINT_URL,
                                           headers={"Authorization": f'{token}'},
                                           json=new_changing_json)

        return self.response

