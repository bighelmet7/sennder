from unittest import mock, TestCase

from studio_ghibli.api import API
from studio_ghibli.exceptions import ResponseError
from studio_ghibli.tests.mocks import MockResponse


class APITest(TestCase):
    '''
    API Studio Ghibli tests.
    '''

    def test_serialize_fields(self):
        # Having an api client created and a list of fields.
        api_client = API(
            proto='https',
            base_url='simple.test.com',
        )
        query_fields = ['id', 'name', 'thing']
        # When calling the _serialize_fields function should
        # return a formatted string with the fields that we are
        # going to request.
        fields = api_client._serialize_fields(query_fields)
        # Then the query_fields should be transformed to a valid
        # query URL string.
        expected = 'fields=id,name,thing'
        self.assertEqual(expected, fields)

    def test_request_endpoint_raise_response_error(self):
        # Having an api client created and an endpoint.
        api_client = API(
            proto='https',
            base_url='simple.test.com',
        )
        endpoint = 'fail'
        # When calling the request_endpoint function and the response
        # is different than 200 (HTTP_STATUS_OK) it should raise the
        # exception ResponseError.
        method_to_mock = 'studio_ghibli.api.requests.get'
        mock_response = MockResponse({'super': 'test'}, 400)
        with self.assertRaises(ResponseError):
            with mock.patch(method_to_mock, return_value=mock_response):
                api_client.request_endpoint(endpoint)

    def test_request_endpoint_status_ok(self):
        # Having an api client created and an endpoint.
        api_client = API(
            proto='https',
            base_url='simple.test.com',
        )
        endpoint = 'test'
        # When calling the request_endpoint function with a
        # 200 response, should return a valid json object.
        method_to_mock = 'studio_ghibli.api.requests.get'
        json_data = [{'id': '1', 'name': 'Naku Testu'}]
        mock_response = MockResponse(json_data, 200)
        with mock.patch(method_to_mock, return_value=mock_response):
            resp = api_client.request_endpoint(endpoint)
            expected = json_data
            self.assertEqual(expected, resp)

    def test_request_endpoint_filter_by_fields(self):
        # Having an api client created, an endpoint and a list of fields.
        api_client = API(
            proto='https',
            base_url='simple.test.com',
        )
        endpoint = 'test'
        fields = ['id']
        # When calling the request_endpoint function with a list of fields will
        # be appended to the URL of the api_client requesting this formatted
        # URL to the API.
        method_to_mock = 'studio_ghibli.api.requests.get'
        json_data = [{'id': '1'}]
        mock_response = MockResponse(json_data, 200)
        with mock.patch(method_to_mock, return_value=mock_response):
            resp = api_client.request_endpoint(endpoint, fields)
            expected = json_data
            self.assertEqual(expected, resp)
