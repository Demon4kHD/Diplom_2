from data_endpoint.changing_user_data import ChangingUserData as CUD


class CreateOrderData(CUD):
    CREATE_ORDER_URL = ' https://stellarburgers.nomoreparties.site/api/orders'
    CREATE_ORDER_REQUEST_ADD_INGREDIENTS_BODY = {"ingredients": []}
    CREATE_ORDER_RESPONSE_ADD_INGREDIENTS_BODY = {"name": '',
                                                  "order": {"number": 0},
                                                  "success": True}
    CREATE_ORDER_REQUEST_ADD_INGREDIENTS_STATUS_CODE = 200
    CREATE_ORDER_ERROR_WITHOUT_AUTHORIZATION_STATUS_CODE = 400
    CREATE_ORDER_ERROR_NONE_INGREDIENTS_RESPONSE_BODY = {"success": False,
                                                         "message": "Ingredient ids must be provided"}
    CREATE_ORDER_ERROR_NONE_INGREDIENTS_STATUS_CODE = 400
    CREATE_ORDER_GET_INGREDIENTS_LIST_URL = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    CREATE_ORDER_ERROR_NOT_VALID_HASH_STATUS_CODE = 500
    CREATE_ORDER_TYPE_INGREDIENTS = ['bun', 'sauce', 'main']
    CREATE_ORDER_DATA_INGREDIENTS_LIST_PATTERN = {"bun": {"_id": [], 'name': []},
                                                  "sauce": {"_id": [], 'name': []},
                                                  "main": {"_id": [], 'name': []}}
