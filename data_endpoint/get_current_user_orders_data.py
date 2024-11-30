from data_endpoint.create_order_data import CreateOrderData as COD


class GetCurrentUserOrdersData(COD):
    GET_CURRENT_USER_ORDERS_URL = 'https://stellarburgers.nomoreparties.site/api/orders'
    GET_CURRENT_USER_ORDERS_SUCCESS_BODY = {"success": True,
                                            "orders": [{"ingredients": ["60d3463f7034a000269f45e9",
                                                                        "60d3463f7034a000269f45e7"],
                                                        "_id": "",
                                                        "status": "done",
                                                        "number": 1,
                                                        "createdAt": "2021-06-23T20:11:01.403Z",
                                                        "updatedAt": "2021-06-23T20:11:01.406Z", }],
                                            "total": 2,
                                            "totalToday": 2}
    GET_CURRENT_USER_ORDERS_SUCCESS_STATUS_CODE = 200
    GET_CURRENT_USER_ORDERS_ERROR_AUTHORIZATION_BODY = {"success": False,
                                                        "message": "You should be authorised"}
    GET_CURRENT_USER_ORDERS_ERROR_AUTHORIZATION_STATUS_CODE = 401
