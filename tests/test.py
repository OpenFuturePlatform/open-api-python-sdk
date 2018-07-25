import json
import urllib.parse
from unittest import TestCase
from unittest.mock import patch, Mock

from openplatform.main import OpenPlatform
from openplatform.utils import validate_address, merge_headers
from tests.const import *


def base_url_mock(rest):
    predefined_url = urllib.parse.urljoin(test_base_url, 'api/')
    return urllib.parse.urljoin(predefined_url, rest)


class TestGettingScaffold(TestCase):
    mock_requests_patcher = None
    requests_mock = None

    @classmethod
    def setUp(cls):
        cls.mock_requests_patcher = patch('openplatform.senders.requests.get')
        cls.requests_mock = cls.mock_requests_patcher.start()

    @classmethod
    def tearDown(cls):
        cls.mock_requests_patcher.stop()

    def test_connection(self):
        self.requests_mock.return_value = Mock(ok=True)
        self.requests_mock.return_value.json.return_value = list_of_scaffolds

        # Send a request to the API server and store the response.
        op = OpenPlatform(test_key)
        response = op.scaffold.get_all()

        # Confirm that the request-response cycle completed successfully.
        self.assertIsNotNone(response)
        print(json.dumps(response))
        self.assertEqual(response, list_of_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds'), headers=authorization_header)

    def test_getting_single_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = scaffold
        response = op.scaffold.get_single(valid_address)
        self.assertIsNotNone(response)
        self.assertEqual(response, scaffold)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_single_without_token(self):
        self.requests_mock.return_value.status_code = 401
        self.requests_mock.return_value.json.return_value = {"status": 401,
                                                             "message": "Open token is invalid or disabled"}
        op = OpenPlatform("some_invalid_open_key")
        response = op.scaffold.get_single(valid_address)
        self.assertEqual(response.get('status'), 401, "There should be an error in the API")
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_single_without_token(self):
        self.requests_mock.return_value.status_code = 401
        self.requests_mock.return_value.json.return_value = {"status": 401,
                                                             "message": "Open token is invalid or disabled"}
        op = OpenPlatform(test_key)
        response = op.scaffold.get_single(valid_address)
        self.assertEqual(response.get('status'), 401, "There should be an error in the API")
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_single_with_wrong_address(self):
        self.requests_mock.return_value.status_code = 404
        self.requests_mock.return_value.json.return_value = {
            "timestamp": "2018-07-25T09:44:00.491+0000",
            "status": 404,
            "error": "Not Found",
            "message": "Not Found",
            "path": "/api/scaffolds/0x0000000000000000000000000000000000000000"}
        op = OpenPlatform(test_key)
        response = op.scaffold.get_single(valid_address)
        self.assertEqual(response.get('status'), 404, "Should not be found")
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_all_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = list_of_scaffolds
        response = op.scaffold.get_all()
        self.assertIsNotNone(response)
        self.assertEqual(response, list_of_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds'), headers=authorization_header)

    def test_getting_summary_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = summary
        response = op.scaffold.get_summary(valid_address)
        self.assertIsNotNone(response)
        self.assertEqual(response, summary)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/summary'),
                                              headers=authorization_header)

    def test_getting_transactions_successfully(self):
        result_transactions = {'totalCount': 0, 'list': []}
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = result_transactions
        response = op.scaffold.get_transactions(valid_address)
        self.assertIsNotNone(response)
        self.assertEqual(response, result_transactions)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/transactions'),
                                              headers=authorization_header)

    def test_getting_quota_successfully(self):
        op = OpenPlatform(test_key)
        result_qouta = {'limitCount': 10, 'currentCount': 4}
        self.requests_mock.return_value.json.return_value = result_qouta
        response = op.scaffold.get_quota()
        self.assertIsNotNone(response)
        self.assertEqual(response, result_qouta)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/quota'),
                                              headers=authorization_header)


class TestHelpers(TestCase):
    def test_address_validation(self):
        address = 'address'
        # validation should raise AttributeError. Address should start with "0x"
        with self.assertRaises(AttributeError):
            validate_address(address)
        address = '0xNotEnoughLength'
        # validation should raise AttributeError. Address should be 42 characters long
        with self.assertRaises(AttributeError):
            validate_address(address)
        # valid address should pass
        validate_address(valid_address)

    def test_merge_headers(self):
        given_list_of_headers = [{'Authorization': test_key}, {'Content-Type': 'application/json'}]
        merged_headers = merge_headers(given_list_of_headers)
        self.assertEqual(headers, merged_headers)
