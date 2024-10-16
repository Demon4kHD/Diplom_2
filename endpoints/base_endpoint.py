
class BaseMethod:
    response = None
    response_json = None

    def get_json(self):
        return self.response.json()

    def get_status_code(self):
        return self.response.status_code

    def assert_status_code(self, checked_status_code):
        assert self.response.status_code == checked_status_code

    def assert_structure_response_json(self, standard_json):
        for element in standard_json:
            assert type(standard_json[element]) == type(self.response.json()[element])

    def assert_length_json_file(self, standard_json):
        assert len(self.response.json()) == len(standard_json)
