import requests

from openplatform.helpers.utils import validate_address, merge_headers, CONTENT_JSON
from openplatform.urls import base


class Scaffold:
    def __init__(self, open_key, headers=None):
        self.open_key = open_key
        self.headers = headers

    def get_all(self):
        try:
            res = requests.get(base('/scaffolds'), headers=self.headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as err:
            print(err)

    def get_single(self, address):
        validate_address(address)
        res = requests.get(base('/scaffolds/' + address), headers=self.headers)
        res.raise_for_status()
        return res

    def get_summary(self, address):
        validate_address(address)
        res = requests.get(base('/scaffolds/' + address + '/summary'), headers=self.headers)
        res.raise_for_status()
        return res

    def get_transactions(self, address):
        validate_address(address)
        res = requests.get(base('/scaffolds/' + address + '/transactions'), headers=self.headers)
        res.raise_for_status()
        return res

    def get_quota(self):
        res = requests.get(base('/scaffolds/quota'))
        res.raise_for_status()
        return res

    def deploy(self, data):
        res = requests.post(base('/scaffolds/doDeploy'), data, headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def deactivate(self, address):
        validate_address(address)
        res = requests.delete(base('/scaffolds/' + address), headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def set_webhook(self, address, data):
        validate_address(address)
        res = requests.patch(base('/scaffolds/' + address), data, headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res


class Shareholder:
    def __init__(self, open_key, headers=None):
        self.open_key = open_key
        self.headers = headers

    def create(self, address, data):
        validate_address(address)
        res = requests.post(base('/scaffolds/' + address + '/holders'), data,
                            headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def update(self, address, holder_address, data):
        validate_address(address)
        res = requests.post(('/scaffolds/' + address + '/holders/' + holder_address), data,
                            headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def remove(self, address, holder_address):
        validate_address(address)
        res = requests.delete(base('/scaffolds/' + address + '/holders/' + holder_address),
                              headers=self.headers)
        res.raise_for_status()
        return res
