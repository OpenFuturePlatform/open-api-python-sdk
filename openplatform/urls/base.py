from openplatform import config
from openplatform.config import base_url


def base(rest):
    return base_url + config.api_prefix + rest
