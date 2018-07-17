from openplatform.urls.base import base


def get_all():
    return base('/scaffolds')


def get_item(address):
    return base('/scaffolds/' + address)


def get_summary(address):
    return base('/scaffolds/' + address + '/summary')


def get_transactions(address):
    return base('/scaffolds/' + address + '/transactions')


def deploy():
    return base('/scaffolds/doDeploy')


def deactivate(address):
    return base('/scaffolds/' + address)


def set_webhook(address):
    return base('/scaffolds/' + address)


def get_quota():
    return base('/scaffolds/quota')
