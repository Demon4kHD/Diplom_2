from http.client import responses


class BaseMethod:
    response = None
    token = ''
    request_json = {}
    refresh_token = ''

    def assert_status_code_and_json(self, checked_status_code, standart_json):
        assert self.response.status_code == checked_status_code
        assert len(self.response.json()) == len(standart_json)
        for element in standart_json:
            assert type(standart_json[element]) == type(self.response.json()[element])
