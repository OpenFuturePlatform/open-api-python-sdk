import requests

from open_py.urls import base
from open_py.utils import validate_address, merge_headers, CONTENT_JSON


class EthereumScaffold:
    def __init__(self, headers=None):
        self.headers = headers

    def get_all(self):
        res = requests.get(base('ethereum-scaffolds'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_single(self, address):
        validate_address(address)
        res = requests.get(base('ethereum-scaffolds/' + address), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_summary(self, address):
        validate_address(address)
        res = requests.get(base('ethereum-scaffolds/' + address + '/summary'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_transactions(self, address):
        validate_address(address)
        res = requests.get(base('ethereum-scaffolds/' + address + '/transactions'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_quota(self):
        res = requests.get(base('ethereum-scaffolds/quota'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def deploy(self, data):
        res = requests.post(base('ethereum-scaffolds/doDeploy'), json=data, headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def deactivate(self, address):
        validate_address(address)
        res = requests.delete(base('ethereum-scaffolds/' + address), headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def set_webhook(self, address, data):
        validate_address(address)
        res = requests.patch(base('ethereum-scaffolds/' + address), json=data,
                             headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()


class EthereumShareholder:
    def __init__(self, headers=None):
        self.headers = headers

    def create(self, address, data):
        validate_address(address)
        res = requests.post(base('ethereum-scaffolds/' + address + '/holders'), json=data,
                            headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def update(self, address, holder_address, data):
        validate_address(address)
        res = requests.put(base('ethereum-scaffolds/' + address + '/holders/' + holder_address), json=data,
                           headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def remove(self, address, holder_address):
        validate_address(address)
        res = requests.delete(base('ethereum-scaffolds/' + address + '/holders/' + holder_address),
                              headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()


def raise_for_error(res):
    try:
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if hasattr(res, 'json'):
            raise requests.exceptions.HTTPError(res.json().get('message'))
        else:
            raise e
