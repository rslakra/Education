#
# Author: Rohtash Lakra
#
from urllib import request
import json
from typing import Any

_STAR_WAR_API_URL = 'https://swapi.dev/api/starships/9/'


class HttpRequest(request.Request):

    def __init__(self, url: str, method: str, body: dict = None):
        self.url = url
        self.method = method
        self.request = None
        # handle method and request's data
        match method:
            case 'POST':
                encode_data = json.dumps(body).encode()
                self.request = request.Request(self.url, data=encode_data)
            case _:
                self.request = request.Request(self.url)

    def execute(self):
        if self.method == 'POST':
            self.request.add_header('Content-Type', 'application/json')

        response = request.urlopen(self.request)
        data = response.read()
        return data


class HttpResponse:

    def __init__(self, url: str, status: int, data: Any):
        self.url = url
        self.status = status
        self.body = self._json_deserialize(data)

    def _json_deserialize(self, text: str):
        """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python
        object.

        Parameters:
            text: json text string
        """
        return json.loads(text.decode('utf-8'))


class Cooky:
    pass


class Header:
    pass


class HttpClient:

    def __init__(self):
        self.request: HttpRequest = None
        self.response: HttpResponse

    def _execute(self, url: str, method: str, body: dict = None) -> HttpResponse:
        http_request = HttpRequest(url, method, body)
        data = http_request.execute()
        http_response = HttpResponse(url, 200, data)
        return http_response

    def _json_deserialize(self, text: str):
        """Deserialize ``s`` (a ``str``, ``bytes`` or ``bytearray`` instance containing a JSON document) to a Python
        object.

        Parameters:
            text: json text string
        """
        return json.loads(text.decode('utf-8'))

    def get(self, url: str):
        return self._execute(url, 'GET').body

    def post(self, url: str, body: dict = None):
        return self._execute(url, 'POST', body).body

    def put(self, url: str):
        return self._execute(url, 'PUT').body

    def delete(self, url: str):
        return self._execute(url, 'DELETE').body
