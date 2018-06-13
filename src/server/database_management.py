import pymongo

class Collection:

    def __init__(self, database, name):
        self.database = database
        self.name = name
        self.client = pymongo.MongoClient()

    def __enter__(self):
        return self.client[self.database][self.name]

    def __exit__(self, *arg):
        self.client.close()

DB_NAME = 'sauron'

COLLECTIONS = {
    'users': Collection(DB_NAME, 'users'),
    'processes': Collection(DB_NAME, 'processes'),
    'whitelists': Collection(DB_NAME, 'whitelists'),
    'screenshots': Collection(DB_NAME, 'screenshots'),
}