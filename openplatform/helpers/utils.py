CONTENT_JSON = {'Content-Type': 'application/json'}


def validate_address(address):
    is_valid = True
    if not address.startswith('0x'):
        print('\033[91m' + 'The address of a developer should start with 0x')
        is_valid = False
    if len(address) != 42:
        print('\033[91m' + 'The address of a developer should be 42 characters long')
        is_valid = False
    if not is_valid:
        raise Exception('Address validation failed.')


def merge_headers(*args):
    if len(args) == 0:
        return
    headers = {}
    for header in args:
        headers.update(header)
    return headers
