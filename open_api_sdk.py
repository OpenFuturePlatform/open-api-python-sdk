from openplatform.senders import Scaffold, Shareholder


class OpenPlatform(object):
    def __init__(self, open_key=''):
        self.headers = {'Authorization': open_key}
        if open_key == '':
            raise AttributeError('open_key can not be empty')
        self.scaffold = Scaffold(self.headers)
        self.shareholder = Shareholder(self.headers)
