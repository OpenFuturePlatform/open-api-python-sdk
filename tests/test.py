import urllib.parse
from unittest import TestCase
from unittest.mock import patch, Mock

import requests

from open_api import OpenPlatform
from openplatform.utils import validate_address, merge_headers
from tests.const import *


def base_url_mock(rest):
    predefined_url = urllib.parse.urljoin(test_base_url, 'api/')
    return urllib.parse.urljoin(predefined_url, rest)


class TestScaffoldGetters(TestCase):
    mock_requests_patcher = None
    requests_mock = None

    @classmethod
    def setUp(cls):
        cls.mock_requests_patcher = patch('openplatform.senders.requests.get')
        cls.requests_mock = cls.mock_requests_patcher.start()

    @classmethod
    def tearDown(cls):
        cls.mock_requests_patcher.stop()

    def test_getting_list(self):
        self.requests_mock.return_value = Mock(ok=True)
        self.requests_mock.return_value.json.return_value = list_of_scaffolds

        # Send a request to the API server and store the response.
        op = OpenPlatform(test_key)
        response = op.scaffold.get_all()

        # Confirm that the request-response cycle completed successfully.
        self.assertEqual(response, list_of_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds'), headers=authorization_header)

    def test_getting_single_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = scaffold
        response = op.scaffold.get_single(valid_address)
        self.assertEqual(response, scaffold)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_single_with_wrong_token(self):
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error
        self.requests_mock.return_value = mock_response

        invalid_key = 'some_invalid_open_key'
        self.requests_mock.return_value.json.return_value = {'status': 401,
                                                             'message': 'Open token is invalid or disabled'}
        op = OpenPlatform(invalid_key)
        with self.assertRaises(requests.HTTPError) as error:
            op.scaffold.get_single(valid_address)
        self.assertEqual(str(error.exception), 'Open token is invalid or disabled')
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address),
                                              headers={'Authorization': invalid_key})

    def test_getting_single_without_token(self):
        with self.assertRaises(AttributeError) as error:
            OpenPlatform()
        self.assertEqual(str(error.exception), 'open_key can not be empty')

    def test_getting_single_with_wrong_address(self):
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error
        self.requests_mock.return_value = mock_response
        self.requests_mock.return_value.json.return_value = {
            'timestamp': '2018-07-25T09:44:00.491+0000',
            'status': 404,
            'error': 'Not Found',
            'message': 'Not Found',
            'path': '/api/scaffolds/0x0000000000000000000000000000000000000000'}
        op = OpenPlatform(test_key)
        with self.assertRaises(requests.exceptions.HTTPError) as error:
            op.scaffold.get_single(valid_address)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=authorization_header)
        self.assertTrue(mock_response.raise_for_status.called)
        self.assertEqual('Not Found', str(error.exception))

    def test_getting_all_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = list_of_scaffolds
        response = op.scaffold.get_all()
        self.assertEqual(response, list_of_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds'), headers=authorization_header)

    def test_getting_summary_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = summary
        response = op.scaffold.get_summary(valid_address)
        self.assertEqual(response, summary)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/summary'),
                                              headers=authorization_header)

    def test_getting_transactions_successfully(self):
        op = OpenPlatform(test_key)
        self.requests_mock.return_value.json.return_value = transactions
        response = op.scaffold.get_transactions(valid_address)
        self.assertEqual(response, transactions)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/transactions'),
                                              headers=authorization_header)

    def test_getting_quota_successfully(self):
        op = OpenPlatform(test_key)
        result_qouta = {'limitCount': 10, 'currentCount': 4}
        self.requests_mock.return_value.json.return_value = result_qouta
        response = op.scaffold.get_quota()
        self.assertEqual(response, result_qouta)
        self.requests_mock.assert_called_with(base_url_mock('scaffolds/quota'),
                                              headers=authorization_header)


class TestScaffoldPosters(TestCase):

    @patch('openplatform.senders.requests.post')
    def test_deploying(self, post_mock):
        post_mock.return_value.json.return_value = scaffold

        op = OpenPlatform(test_key)
        response = op.scaffold.deploy(scaffold_data)

        self.assertEqual(response, scaffold)
        post_mock.assert_called_with(base_url_mock('scaffolds/doDeploy'), json=scaffold_data,
                                     headers=request_headers)


class TestScaffoldDeleters(TestCase):

    @patch('openplatform.senders.requests.delete')
    def test_deactivating(self, post_mock):
        post_mock.return_value.json.return_value = scaffold

        op = OpenPlatform(test_key)
        response = op.scaffold.deactivate(valid_address)

        self.assertEqual(response, scaffold)
        post_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), headers=request_headers)


class TestScaffoldPatchers(TestCase):

    @patch('openplatform.senders.requests.patch')
    def test_setting_web_hook(self, post_mock):
        post_mock.return_value.json.return_value = scaffold
        web_hook = {'webHook': 'https://zensoft.io'}
        op = OpenPlatform(test_key)
        response = op.scaffold.set_webhook(valid_address, web_hook)

        self.assertEqual(response, scaffold)
        post_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address), json=web_hook,
                                     headers=request_headers)


class TestShareholders(TestCase):

    @patch('openplatform.senders.requests.post')
    def test_creation(self, post_mock):
        post_mock.return_value.json.return_value = new_shareholders
        op = OpenPlatform(test_key)
        response = op.shareholder.create(valid_address, shareholder_to_be_added)

        self.assertEqual(response, new_shareholders)
        post_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/holders'),
                                     json=shareholder_to_be_added,
                                     headers=request_headers)

    @patch('openplatform.senders.requests.put')
    def test_updating(self, post_mock):
        post_mock.return_value.json.return_value = scaffold
        op = OpenPlatform(test_key)
        response = op.shareholder.update(valid_address, developer_address, shareholder_to_be_updated)

        self.assertEqual(response, scaffold)
        post_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/holders/' + developer_address),
                                     json=shareholder_to_be_updated,
                                     headers=request_headers)

    @patch('openplatform.senders.requests.delete')
    def test_removing(self, post_mock):
        post_mock.return_value.json.return_value = removing_shareholder
        op = OpenPlatform(test_key)
        response = op.shareholder.remove(valid_address, developer_address)

        self.assertEqual(response, removing_shareholder)
        post_mock.assert_called_with(base_url_mock('scaffolds/' + valid_address + '/holders/' + developer_address),
                                     headers=request_headers)


class TestHelpers(TestCase):
    def test_address_validation(self):
        address = 'address'
        # validation should raise AttributeError. Address should start with '0x'
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
        self.assertEqual(request_headers, merged_headers)
