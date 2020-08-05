# Generic exceptions for Studio Ghibli API.

class APIError(Exception):
    '''
    Base API Error class.
    '''
    pass


class ResponseError(APIError):
    '''
    Response error when the status code it's different than 200.
    '''
    pass
