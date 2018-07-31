import requests

from openplatform.urls import base
from openplatform.utils import validate_address, merge_headers, CONTENT_JSON


class Scaffold:
    def __init__(self, headers=None):
        self.headers = headers

    def get_all(self):
        res = requests.get(base('scaffolds'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_single(self, address):
        validate_address(address)
        res = requests.get(base('scaffolds/' + address), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_summary(self, address):
        validate_address(address)
        res = requests.get(base('scaffolds/' + address + '/summary'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_transactions(self, address):
        validate_address(address)
        res = requests.get(base('scaffolds/' + address + '/transactions'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def get_quota(self):
        res = requests.get(base('scaffolds/quota'), headers=self.headers)
        raise_for_error(res)
        return res.json()

    def deploy(self, data):
        res = requests.post(base('scaffolds/doDeploy'), json=data, headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def deactivate(self, address):
        validate_address(address)
        res = requests.delete(base('scaffolds/' + address), headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def set_webhook(self, address, data):
        validate_address(address)
        res = requests.patch(base('scaffolds/' + address), json=data,
                             headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()


class Shareholder:
    def __init__(self, headers=None):
        self.headers = headers

    def create(self, address, data):
        validate_address(address)
        res = requests.post(base('scaffolds/' + address + '/holders'), json=data,
                            headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def update(self, address, holder_address, data):
        validate_address(address)
        res = requests.put(base('scaffolds/' + address + '/holders/' + holder_address), json=data,
                           headers=merge_headers([CONTENT_JSON, self.headers]))
        raise_for_error(res)
        return res.json()

    def remove(self, address, holder_address):
        validate_address(address)
        res = requests.delete(base('scaffolds/' + address + '/holders/' + holder_address),
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
