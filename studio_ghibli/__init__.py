# Client for Studio Ghibli
from typing import Dict, List, Sequence

from studio_ghibli.api import API, JSONResponse


class StudioGhibli(object):
    '''
    StudioGhibli give us the abstraction to interact with the
    real Studio Ghibli API service.
    '''
    def __init__(
            self,
            proto: str = 'https',
            base_url: str = 'ghibliapi.herokuapp.com',
            proxies: Dict[str, str] = {}) -> None:
        self.api_cli = API(proto, base_url, proxies)

    def films(self, fields: List[str] = []) -> Sequence[JSONResponse]:
        '''
        Get all the available films.
        '''
        endpoint = 'films'
        return self.api_cli.request_endpoint(endpoint, fields)

    def people(self, fields: List[str] = []) -> Sequence[JSONResponse]:
        '''
        Get all the available people.
        '''
        endpoint = 'people'
        return self.api_cli.request_endpoint(endpoint, fields)
