from openplatform import config
from openplatform.config import base_url
import urllib.parse


def base(rest):
    predefined_url = urllib.parse.urljoin(base_url, config.api_prefix)
    return urllib.parse.urljoin(predefined_url, rest)
