from openplatform.senders import Scaffold, Shareholder


class OpenPlatform(object):
    def __init__(self, open_key=''):
        self.headers = {'Authorization': open_key}
        self.scaffold = Scaffold(open_key)
        self.shareholder = Shareholder(open_key)

