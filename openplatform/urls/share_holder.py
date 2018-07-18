from .base import base


def add(address):
    return base('/scaffolds/' + address + '/holders')


def update(address, holder_address):
    return base('/scaffolds/' + address + '/holders/' + holder_address)


def remove(address, holder_address):
    return base('/scaffolds/' + address + '/holders/' + holder_address)
