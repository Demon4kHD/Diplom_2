class AuthorizationData:
    AUTHORIZATION_URL = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    AUTHORIZATION_BODY = {"email": "",
                          "password": ""}
    AUTHORIZATION_BODY_RESPONSE = {"success": True,
                                  "accessToken": "Bearer ...",
                                  "refreshToken": "",
                                  "user": {"email": "",
                                           "name": ""}}
    AUTHORIZATION_RESPONSE_STATUS_CODE = 200
    AUTHORIZATION_BODY_INCORRECT_DATA = {"success": False,
                                        "message": "email or password are incorrect"}
    AUTHORIZATION_ERROR_RESPONSE_STATUS_CODE = 401
