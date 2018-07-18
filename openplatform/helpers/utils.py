from openplatform.helpers.constants import *


def get_headers(open_key):
    return {
        'headers': {'Authorization': open_key}
    }


def validate_address(address):
    is_valid = True
    if not address.startswith('0x'):
        print('\033[91m' + ADDRESS_START_ERROR)
        is_valid = False
    if len(address) != 42:
        print('\033[91m' + ADDRESS_LENGTH_ERROR)
        is_valid = False
    if not is_valid:
        raise Exception('Address validation failed.')
