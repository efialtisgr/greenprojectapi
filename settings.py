MONOGO_URI = 'mongodb://localhost:27017/eve-course'


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