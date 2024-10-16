class RegistrationData:
    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    DELETE_URL = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    REGISTRATION_BODY = {"email": str,
                         "password": str,
                         "name": str}
    REGISTRATION_BODY_RESPONSE = {"success": True,
                                  "user": {"email": "",
                                           "name": ""},
                                  "accessToken": "Bearer ...",
                                  "refreshToken": ""}
    REGISTRATION_RESPONSE_STATUS_CODE = 200
    REGISTRATION_BODY_SAME_DATA = {"success": False,
                                   "message": "User already exists"}
    REGISTRATION_BODY_WITHOUT_SAME_DATA = {"success": False,
                                           "message": "Email, password and name are required fields"}
    REGISTRATION_ERROR_RESPONSE_STATUS_CODE = 403
