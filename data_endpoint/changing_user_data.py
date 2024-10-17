
from data_endpoint.authorization_data import AuthorizationData as AD

class ChangingUserData(AD):
    CHANGING_USER_ENDPOINT_URL = "https://stellarburgers.nomoreparties.site/api/auth/user"
    CHANGING_USER_SUCCESS_STATUS_CODE = 200
    CHANGING_USER_SUCCESS = {"success": True,
                             "user": {"email": "",
                                      "name": ""}}
    CHANGING_USER_WITHOUT_AUTHORIZATION_STATUS_CODE = 401
    CHANGING_USER_WITHOUT_AUTHORIZATION = {"success": False,
                                           "message": "You should be authorised"}
    CHANGING_USER_WITH_SAME_EMAIL_STATUS_CODE = 403
    CHANGING_USER_WITH_SAME_EMAIL = {"success": False,
                                     "message": "User with such email already exists"}

