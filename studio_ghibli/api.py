import requests
from typing import Any, Dict, List, Sequence

from studio_ghibli.exceptions import ResponseError

# Code snippet:
# https://github.com/python/typing/issues/182#issuecomment-199532520
JSONResponse = Dict[str, Any]


class API(object):
    '''
    Base class which interacts with Studio Ghibli API.
    '''

    def __init__(
            self,
            proto: str,
            base_url: str,
            proxies: Dict[str, str] = {}) -> None:
        self.base_url = base_url
        self.proto = proto
        self.url = f'{proto}://{base_url}'
        self.proxies = proxies
        self.headers = {
            'Content-Type': 'application/json',
        }

    def _serialize_fields(self, fields: List[str]) -> str:
        '''
        Return a serialized Query for any URL with the given fields list.
        '''
        return f'fields={",".join(fields)}'

    def request_endpoint(
            self,
            endpoint: str,
            fields: List[str] = []) -> Sequence[JSONResponse]:
        '''
        Request to the given endpoint the JSON response.
        '''
        url = f'{self.url}/{endpoint}'
        if fields:
            url += f'?{self._serialize_fields(fields)}'
        resp = requests.get(url, headers=self.headers, proxies=self.proxies)
        if not resp:
            msg = f'Status: {resp.status_code}\n Body:{resp.text}'
            raise ResponseError(msg)
        return resp.json()
