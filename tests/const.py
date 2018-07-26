abi = """[
    {"constant": true, "inputs": [], "name": "fiatCurrency", "outputs": [{"name": "", "type": "bytes32"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [], "name": "activate", "outputs": [], "payable": false,
     "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [], "name": "activated", "outputs": [{"name": "", "type": "bool"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": false, "inputs": [{"name": "_shareHolderAddress", "type": "address"}], "name": "deleteShareHolder",
     "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": false, "inputs": [], "name": "deactivate", "outputs": [], "payable": false,
     "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [], "name": "getScaffoldSummary",
     "outputs": [{"name": "", "type": "bytes32"}, {"name": "", "type": "bytes32"}, {"name": "", "type": "uint256"},
                 {"name": "", "type": "uint256"}, {"name": "", "type": "address"}, {"name": "", "type": "uint256"},
                 {"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": false,
     "inputs": [{"name": "_shareHolderAddress", "type": "address"}, {"name": "_partnerShare", "type": "uint256"}],
     "name": "editShareHolder", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": false, "inputs": [{"name": "user_id", "type": "bytes32"}], "name": "payDeveloper", "outputs": [],
     "payable": true, "stateMutability": "payable", "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "openScaffoldTransactions",
     "outputs": [{"name": "customerAddress", "type": "address"}, {"name": "user_id", "type": "bytes32"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "uint256"}], "name": "shareHolderAddresses",
     "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": false,
     "inputs": [{"name": "_shareHolderAddress", "type": "address"}, {"name": "_partnerShare", "type": "uint256"}],
     "name": "addShareHolder", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"},
    {"constant": true, "inputs": [], "name": "fiatAmount", "outputs": [{"name": "", "type": "bytes32"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_index", "type": "uint256"}],
     "name": "getShareHolderAddressAndShareAtIndex",
     "outputs": [{"name": "", "type": "address"}, {"name": "", "type": "uint256"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "partners",
     "outputs": [{"name": "share", "type": "uint256"}, {"name": "index", "type": "uint256"}], "payable": false,
     "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_shareHolderAddress", "type": "address"}], "name": "getHoldersShare",
     "outputs": [{"name": "partnerShare", "type": "uint256"}], "payable": false, "stateMutability": "view",
     "type": "function"},
    {"constant": true, "inputs": [], "name": "OPENToken", "outputs": [{"name": "", "type": "address"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "scaffoldAmount", "outputs": [{"name": "", "type": "uint256"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "developerAddress", "outputs": [{"name": "", "type": "address"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [], "name": "scaffoldTransactionIndex", "outputs": [{"name": "", "type": "uint256"}],
     "payable": false, "stateMutability": "view", "type": "function"},
    {"constant": true, "inputs": [{"name": "_index", "type": "uint256"}], "name": "getShareHolderAtIndex",
     "outputs": [{"name": "shareHolderAddress", "type": "address"}], "payable": false, "stateMutability": "view",
     "type": "function"},
    {"constant": true, "inputs": [], "name": "getShareHolderCount", "outputs": [{"name": "count", "type": "uint256"}],
     "payable": false, "stateMutability": "view", "type": "function"}, {
        "inputs": [{"name": "_developerAddress", "type": "address"}, {"name": "_platformAddress", "type": "address"},
                   {"name": "_fiatAmount", "type": "bytes32"}, {"name": "_fiatCurrency", "type": "bytes32"},
                   {"name": "_scaffoldAmount", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable",
        "type": "constructor"}, {"anonymous": false,
                                 "inputs": [{"indexed": false, "name": "_eventType", "type": "uint256"},
                                            {"indexed": false, "name": "_customerAddress", "type": "address"},
                                            {"indexed": false, "name": "_transactionAmount", "type": "uint256"},
                                            {"indexed": false, "name": "_scaffoldTransactionIndex", "type": "uint256"},
                                            {"indexed": false, "name": "user_id", "type": "bytes32"}],
                                 "name": "PaymentCompleted", "type": "event"}, {"anonymous": false, "inputs": [
        {"indexed": false, "name": "_eventType", "type": "uint256"},
        {"indexed": false, "name": "_amount", "type": "uint256"},
        {"indexed": false, "name": "_toAddress", "type": "address"}], "name": "FundsDeposited", "type": "event"},
    {"anonymous": false, "inputs": [{"indexed": false, "name": "_eventType", "type": "uint256"},
                                    {"indexed": false, "name": "activated", "type": "bool"}],
     "name": "ActivationScaffold", "type": "event"}, {"anonymous": false, "inputs": [
        {"indexed": false, "name": "_eventType", "type": "uint256"},
        {"indexed": false, "name": "_shareHolderAddress", "type": "address"},
        {"indexed": false, "name": "_share", "type": "uint256"}], "name": "ShareHolderEvent", "type": "event"},
    {"anonymous": false, "inputs": [{"indexed": false, "name": "_eventType", "type": "uint256"},
                                    {"indexed": false, "name": "_userAddress", "type": "address"},
                                    {"indexed": false, "name": "_amount", "type": "uint256"}],
     "name": "PaidForShareHolder", "type": "event"}]
"""
developer_address = '0xDc29484cc9C02Ee01015f33BcA8bBb5C7293Fb54'

test_key = 'op_pk_50g48642-1af1-5dfg-54sz-f868s5v8796c'

test_base_url = 'https://api.open-platform.zensoft.io'

scaffold = {
    'version': 'V2',
    'conversionAmount': '0.021833823',
    'address': '0x1c297f40beb075936d6dbe4b245b92738867ecb1',
    'currency': 'USD',
    'developerAddress': developer_address,
    'description': 'scaffold_for_testing',
    'fiatAmount': '2',
    'abi': abi,
    'properties': [{'type': 'STRING', 'defaultValue': None, 'name': 'user_id'}],
    'user': {
        'id': 1,
        'roles': [{'key': 'ROLE_MASTER'}],
        'credits': 0,
        'openKeys': [{'value': 'op_pk_029bbb64-a31d-4ec6-b881-8d8db19c70ee',
                      'expiredDate': None,
                      'enabled': True}],
    },
    'webHook': None}

list_of_scaffolds = {'totalCount': 1, 'list': [scaffold]}

authorization_header = {'Authorization': test_key}

request_headers = {'Authorization': test_key, 'Content-Type': 'application/json'}

valid_address = "0x0000000000000000000000000000000000000000"

summary = {
    'transactionIndex': 0,
    'shareHolders': [],
    'tokenBalance': 0,
    'enabled': False,
    'scaffold': scaffold}

transactions = {
    'totalCount': 1,
    'list': [{
        'date': '2018-07-26T04:34:36.815+0000',
        'event': {
            'userAddress': developer_address,
            'partnerShare': 30,
            'type': 'ADDED_SHARE_HOLDER'},
        'scaffold': scaffold}]}

scaffold_data = {
    "openKey": test_key,
    "developerAddress": developer_address,
    "description": "testing_scaffold",
    "fiatAmount": "2",
    "currency": "USD",
    "conversionAmount": "0.021833823",
    "properties": [
        {
            "name": "user_id",
            "type": "STRING"
        }
    ]
}

shareholder_to_be_added = {'address': developer_address, 'percent': 30}

shareholder_to_be_updated = {'percent': 30}

new_shareholders = {
    'shareHolders': [{'percent': 30, 'address': developer_address}],
    'tokenBalance': 0,
    'enabled': False,
    'scaffold': scaffold,
    'transactionIndex': 0}

updated_shareholder = {
    'tokenBalance': 0,
    'scaffold': scaffold,
    'shareHolders': [{'address': developer_address, 'percent': 10}],
    'enabled': False,
    'transactionIndex': 0}

removing_shareholder = {
    'tokenBalance': 0,
    'scaffold': scaffold,
    'shareHolders': [],
    'enabled': False,
    'transactionIndex': 0}
