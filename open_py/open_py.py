from open_py.senders import EthereumScaffold, EthereumShareholder


class OpenPy(object):
    def __init__(self, open_key=''):
        if open_key == '':
            raise AttributeError('open_key can not be empty')
        self.headers = {'Authorization': open_key}
        self.ethereum_scaffold = EthereumScaffold(self.headers)
        self.ethereum_shareholder = EthereumShareholder(self.headers)
