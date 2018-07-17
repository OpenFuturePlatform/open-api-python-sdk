def address_validation(address):
    errors = []
    if not address.startswith('0x'):
        errors.append('The address of a developer should start with 0x')
    if address.length != 42:
        errors.append('The address of a developer should be 42 characters long')
    return errors
