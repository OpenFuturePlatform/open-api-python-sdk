import requests

from openplatform.helpers.utils import validate_address
from openplatform.urls import scaffold
from openplatform.urls import share_holder

CONTENT_JSON = {'Content-Type': 'application/json'}


def merge_headers(*args):
    if len(args) == 0:
        return
    headers = {}
    for header in args:
        headers.update(header)
    return headers


class OpenPlatform(object):
    def __init__(self, open_key=''):
        self.headers = {'Authorization': open_key}

    def get_scaffolds(self):
        try:
            res = requests.get(scaffold.get_all(), headers=self.headers)
            res.raise_for_status()
            return res
        except requests.exceptions.HTTPError as err:
            print(err)

    def get_scaffold(self, address):
        validate_address(address)
        res = requests.get(scaffold.get_item(address), headers=self.headers)
        res.raise_for_status()
        return res

    def get_scaffold_summary(self, address):
        validate_address(address)
        res = requests.get(scaffold.get_summary(address), headers=self.headers)
        res.raise_for_status()
        return res

    def get_scaffold_transactions(self, address):
        validate_address(address)
        res = requests.get(scaffold.get_transactions(address), headers=self.headers)
        res.raise_for_status()
        return res

    def get_scaffold_quota(self):
        res = requests.get(scaffold.get_quota())
        res.raise_for_status()
        return res

    def deploy_scaffold(self, data):
        res = requests.post(scaffold.deploy(), data, headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def deactivate_scaffold(self, address):
        validate_address(address)
        res = requests.delete(scaffold.deactivate(address), headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def set_webhook(self, address, data):
        validate_address(address)
        res = requests.patch(scaffold.set_webhook(address), data, headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def create_shareholder(self, address, data):
        validate_address(address)
        res = requests.post(share_holder.add(address), data, headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def update_shareholder(self, address, holder_address, data):
        validate_address(address)
        res = requests.post(share_holder.update(address, holder_address), data,
                            headers=merge_headers([CONTENT_JSON, self.headers]))
        res.raise_for_status()
        return res

    def remove_shareholder(self, address, holder_address):
        validate_address(address)
        res = requests.delete(share_holder.update(address, holder_address),
                              headers=self.headers)
        res.raise_for_status()
        return res

    def create_repository(self):
        pass
