import requests
from endpoints.authorization_endpoint import AuthorizationMethod as AM
from data_endpoint.changing_user_data import ChangingUserData as CUD

class ChangingUserEndpoint(AM):

    def changing_user_data(self, changing_json):
        self.response = requests.patch(url=CUD.CHANGING_USER_ENDPOINT_URL,
                                       headers={"Authorization": f'{AM.token}'},
                                       json=changing_json)
        return self.response
