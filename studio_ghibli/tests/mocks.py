from studio_ghibli.api import JSONResponse


class MockResponse:
    '''
    Mock the response requests.
    '''

    def __init__(self, json_data: JSONResponse, status_code: int) -> None:
        self.json_data = json_data
        self.status_code = status_code
        self.text = 'A valid HTTP text response.'

    def __bool__(self):
        return self.ok

    def __nonzero__(self):
        print(self.ok)
        return self.ok

    @property
    def ok(self):
        if self.status_code != 200:
            return False
        return True

    def json(self) -> JSONResponse:
        return self.json_data
