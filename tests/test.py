import urllib.parse
from unittest import TestCase
from unittest.mock import patch, Mock

import requests

from open_py.config import base_url
from open_py.open_py import OpenPy
from open_py.utils import validate_address, merge_headers
from tests.const import *


def base_url_mock(rest):
    predefined_url = urllib.parse.urljoin(base_url, 'api/')
    return urllib.parse.urljoin(predefined_url, rest)


class TestEthereumScaffoldGetters(TestCase):
    mock_requests_patcher = None
    requests_mock = None

    @classmethod
    def setUp(cls):
        cls.mock_requests_patcher = patch('open_py.senders.requests.get')
        cls.requests_mock = cls.mock_requests_patcher.start()

    @classmethod
    def tearDown(cls):
        cls.mock_requests_patcher.stop()

    def test_getting_list(self):
        self.requests_mock.return_value = Mock(ok=True)
        self.requests_mock.return_value.json.return_value = list_of_ethereum_scaffolds

        # Send a request to the API server and store the response.
        op = OpenPy(test_key)
        response = op.ethereum_scaffold.get_all()

        # Confirm that the request-response cycle completed successfully.
        self.assertEqual(response, list_of_ethereum_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds'), headers=authorization_header)

    def test_getting_single_successfully(self):
        op = OpenPy(test_key)
        self.requests_mock.return_value.json.return_value = ethereum_scaffold
        response = op.ethereum_scaffold.get_single(valid_address)
        self.assertEqual(response, ethereum_scaffold)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address), headers=authorization_header)

    def test_getting_single_with_wrong_token(self):
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        mock_response.raise_for_status.side_effect = http_error
        self.requests_mock.return_value = mock_response

        invalid_key = 'some_invalid_open_key'
        self.requests_mock.return_value.json.return_value = {'status': 401,
                                                             'message': 'Open token is invalid or disabled'}
        op = OpenPy(invalid_key)
        with self.assertRaises(requests.HTTPError) as error:
            op.ethereum_scaffold.get_single(valid_address)
        self.assertEqual(str(error.exception), 'Open token is invalid or disabled')
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address),
                                              headers={'Authorization': invalid_key})

    def test_getting_single_without_token(self):
        with self.assertRaises(AttributeError) as error:
            OpenPy()
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
            'path': '/api/ethereum_scaffolds/0x0000000000000000000000000000000000000000'}
        op = OpenPy(test_key)
        with self.assertRaises(requests.exceptions.HTTPError) as error:
            op.ethereum_scaffold.get_single(valid_address)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address), headers=authorization_header)
        self.assertTrue(mock_response.raise_for_status.called)
        self.assertEqual('Not Found', str(error.exception))

    def test_getting_all_successfully(self):
        op = OpenPy(test_key)
        self.requests_mock.return_value.json.return_value = list_of_ethereum_scaffolds
        response = op.ethereum_scaffold.get_all()
        self.assertEqual(response, list_of_ethereum_scaffolds)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds'), headers=authorization_header)

    def test_getting_summary_successfully(self):
        op = OpenPy(test_key)
        self.requests_mock.return_value.json.return_value = summary
        response = op.ethereum_scaffold.get_summary(valid_address)
        self.assertEqual(response, summary)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address + '/summary'),
                                              headers=authorization_header)

    def test_getting_transactions_successfully(self):
        op = OpenPy(test_key)
        self.requests_mock.return_value.json.return_value = transactions
        response = op.ethereum_scaffold.get_transactions(valid_address)
        self.assertEqual(response, transactions)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address + '/transactions'),
                                              headers=authorization_header)

    def test_getting_quota_successfully(self):
        op = OpenPy(test_key)
        result_qouta = {'limitCount': 10, 'currentCount': 4}
        self.requests_mock.return_value.json.return_value = result_qouta
        response = op.ethereum_scaffold.get_quota()
        self.assertEqual(response, result_qouta)
        self.requests_mock.assert_called_with(base_url_mock('ethereum-scaffolds/quota'),
                                              headers=authorization_header)


class TestScaffoldPosters(TestCase):

    @patch('open_py.senders.requests.post')
    def test_deploying(self, post_mock):
        post_mock.return_value.json.return_value = ethereum_scaffold

        op = OpenPy(test_key)
        response = op.ethereum_scaffold.deploy(ethereum_scaffold_data)

        self.assertEqual(response, ethereum_scaffold)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/doDeploy'), json=ethereum_scaffold_data,
                                     headers=request_headers)


class TestEthereumScaffoldDeleters(TestCase):

    @patch('open_py.senders.requests.delete')
    def test_deactivating(self, post_mock):
        post_mock.return_value.json.return_value = ethereum_scaffold

        op = OpenPy(test_key)
        response = op.ethereum_scaffold.deactivate(valid_address)

        self.assertEqual(response, ethereum_scaffold)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address), headers=request_headers)


class TestEthereumScaffoldPatchers(TestCase):

    @patch('open_py.senders.requests.patch')
    def test_setting_web_hook(self, post_mock):
        post_mock.return_value.json.return_value = ethereum_scaffold
        web_hook = {'webHook': 'https://zensoft.io'}
        op = OpenPy(test_key)
        response = op.ethereum_scaffold.set_webhook(valid_address, web_hook)

        self.assertEqual(response, ethereum_scaffold)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address), json=web_hook,
                                     headers=request_headers)


class TestEthereumShareholders(TestCase):

    @patch('open_py.senders.requests.post')
    def test_creation(self, post_mock):
        post_mock.return_value.json.return_value = new_shareholders
        op = OpenPy(test_key)
        response = op.ethereum_shareholder.create(valid_address, ethereum_shareholder_to_be_added)

        self.assertEqual(response, new_shareholders)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address + '/holders'),
                                     json=ethereum_shareholder_to_be_added,
                                     headers=request_headers)

    @patch('open_py.senders.requests.put')
    def test_updating(self, post_mock):
        post_mock.return_value.json.return_value = ethereum_scaffold
        op = OpenPy(test_key)
        response = op.ethereum_shareholder.update(valid_address, developer_address, ethereum_shareholder_to_be_updated)

        self.assertEqual(response, ethereum_scaffold)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address + '/holders/' + developer_address),
                                     json=ethereum_shareholder_to_be_updated,
                                     headers=request_headers)

    @patch('open_py.senders.requests.delete')
    def test_removing(self, post_mock):
        post_mock.return_value.json.return_value = removing_shareholder
        op = OpenPy(test_key)
        response = op.ethereum_shareholder.remove(valid_address, developer_address)

        self.assertEqual(response, removing_shareholder)
        post_mock.assert_called_with(base_url_mock('ethereum-scaffolds/' + valid_address + '/holders/' + developer_address),
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
