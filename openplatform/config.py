configuration = {
    'api_prefix': '/api',
    'remote_api': ''
}


def api(open_key):
    return {
        # 'base_URL': 'https://api.openfuture.io',
        'base_URL': 'https://api.open-platform.zensoft.io',
        'headers': {'Authorization': open_key}
    }
