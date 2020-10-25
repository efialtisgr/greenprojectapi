MONOGO_URI = 'mongodb://10.135.0.2:27017/projectgreen'


RESOURCE_METHODS = ['GET', 'POST', 'DELETE']


ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#turn off ifmatch for headers
IF_MATCH = False

# domain definition
betxkey_schema = {
    'x-key': {'type': 'string'}
}

DOMAIN = {
    'betxkey': {
        'schema': betxkey_schema
    }
}