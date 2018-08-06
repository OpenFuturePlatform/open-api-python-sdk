# open-api-sdk

Open-api-sdk is a library for interaction with Open Platform.

## Content


* [Installing](#installing)
* [Get started](#get-started)
* [API](#api)
* [Scaffold](#scaffold)
* [Shareholder](#shareholder)


## Installing
Using pip:
```sh
$ pip install open-api-sdk
```

## Get started
OPEN Platform uses OpenKeys to allow access to the API. You can register a new OpenKey at your [Account.](https://api.openfuture.io/ "Open API")

OPEN Platform expects the OpenKey to be included in all API requests to the server in a header.

We assume that you have the OpenKey by this moment. 

To access the library import an OpenPlatform class and call an instance with the OpenKey as following: 


```python
from openp_py import OpenPy

# Access API via instance of OpenPlatform class
op = OpenPy(open_key)
```
`open_key` - your open key. 

In the following examples, it is assumed that `op` is a result of instantiating the `OpenPlatform` class with the `open_key`

### API

#### Page request attributes

Attribute | Type | Description
----------|------|-----------
offset    |Long  | Page offset
limit     |Int   | Page limit

#### Page response attributes

Attribute | Type | Description
----------|------|-----------
totalCount|Long  | Total count of entities in a database
list      |[]   | List of entities with type T (T is generic)

#### Scaffold

##### Scaffold attributes

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
address         |String                                               | Scaffold address
abi             |String                                               | Scaffold json interface
description     |String                                               | Scaffold description
fiatAmount      |String                                               | Scaffold fiat amount
currency        |String                                               | Fiat amount currency
conversionAmount|String                                               | Fiat amount converted to ethereum 
developerAddress|String                                               | Scaffold developer address
webHook         |String                                               | Scaffold webhook for events
properties      |[ScaffoldProperty](#scaffold-properties-attributes)[]| Scaffold properties

##### Scaffold properties attributes

Attribute   | Type       | Description
------------|------------|-----------
name        |String      | Property name
type        |PropertyType| Property type
defaultValue|String      | Property default value

##### get_all()

```python
scaffolds = op.scaffold.get_all()
```

##### get_single(address)

```python
address = '0x1c297f40beb075936d6dbe4b245b92738867ecb1' # an address of the scaffold (example)
scaffold = op.scaffold.get_single(address)
```

##### Scaffold summary attributes

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
scaffold        |[Scaffold](#scaffold-attributes)                     | Scaffold
transactionIndex|BigInteger                                           | Transaction index
tokenBalance    |BigInteger                                           | Scaffold token balance
enabled         |Boolean                                              | Scaffold enabled
currency        |String                                               | Fiat amount currency
shareHolders    |[ShareHolder](#shareholder-attributes)               | Scaffold shareholders

##### get_summary(address)

```python
summary = op.scaffold.get_summary(address)
```

##### get_transactions(address)

```python
transactions = op.scaffold.get_summary(address)
```

##### Set web hook request `data`

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
address         |String                                               | Scaffold address
webHook         |String                                               | Scaffold webhook for events

##### example:

```python
data = {'webHook': 'https://example.com'}
```
##### set_webhook(address, data)

```python
scaffold = op.scaffold.set_webhook(address, data)
```

##### Deploy scaffold request `data`

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
openKey         |String                                               | User open key
description     |String                                               | Scaffold description
fiatAmount      |String                                               | Scaffold fiat amount
currency        |String                                               | Fiat amount currency
conversionAmount|String                                               | Fiat amount converted to ethereum 
developerAddress|String                                               | Scaffold developer address
webHook         |String                                               | Scaffold webhook for events
properties      |[ScaffoldProperty](#scaffold-properties-attributes)[]| Scaffold properties

##### example:

```python
data = {
    'openKey': open_key,
    'developerAddress': '0x0000000000000000000000000000000000000000',
    'description': "any_description",
    'fiatAmount': "123",
    'currency': "USD",
    'conversionAmount': '0.2139521163',
    'properties': [
      {
        'name': "property_name",
        'type': "STRING",
        'defaultValue': "property_value"
      }
    ]
  }
```

##### deploy_scaffold(data)

```python
scaffold = op.scaffold.deploy(data)
```

##### deactivate_scaffold(address)

```python
scaffold = op.scaffold.deactivate(address)
```

##### Quota attributes

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
currentCount    |Int                                                  | Current deactivated scaffolds count
limitCount      |Int                                                  | Limit of deactivated scaffolds count


##### get_quota()

```python
quota = op.scaffold.get_quota()
```
#### Shareholder

##### Shareholder attributes

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
address         |String                                               | Shareholder address
percent         |Int                                                  | Shareholder percent


##### example:
```python
# Shareholder attributes
data = {
    'address': '0x0000000000000000000000000000000000000000',
    'percent': 30
  }
```

##### add(address, data)

```python
summary = op.shareholder.create(address, data)
```

##### Update shareholder request `data`

Attribute       | Type                                                | Description
----------------|-----------------------------------------------------|-----------
percent         |Int                                                  | Shareholder percent

##### example:

```python
data = {'percent': 50}
```

##### update(address , holder_address , data)

```python
shareholder_address = "0xDc29484cc9C02Ee01015f33BcA8bBb5C7293Fb54" # an example of shareholder's address
summary = op.shareholder.update(address, shareholder_address, data)
```

##### remove(address, holder_address)

```python
summary = op.shareholder.remove(address, shareholder_address)
```
