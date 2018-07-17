from openplatform import config


def base(rest):
    return config.configuration.api_prefix + rest
