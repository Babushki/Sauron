from pymongo import MongoClient

class MongoAPI:

    def __init__(self, database, collection):
        self.connection = MongoClient()
        self.collection = self.connection[database][collection]

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.connection.close()

    def insert(self, value, many=False):
        self.collection.insert_one(value) if not many else self.collection.insert_many(value)
    
    def get(self, conditions, many=False):
        try:
            return dict(self.collection.find_one(conditions, {'_id': False})) if not many else list(self.collection.find(conditions, {'_id': False}))
        except TypeError:
            return None

