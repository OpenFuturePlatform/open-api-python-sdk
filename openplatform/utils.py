CONTENT_JSON = {'Content-Type': 'application/json'}


def validate_address(address):
    if not address.startswith('0x'):
        raise AttributeError('The address of a developer should start with 0x. Your address is ' + address)
    if len(address) != 42:
        raise AttributeError('The address of a developer should be 42 characters long. Your address is ' + address)


def merge_headers(args):
    if len(args) == 0:
        return
    headers = {}
    for header in args:
        headers.update(header)
    return headers
