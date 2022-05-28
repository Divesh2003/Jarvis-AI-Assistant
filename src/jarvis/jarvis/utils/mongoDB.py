import logging
from pymongo import MongoClient, DESCENDING


class MongoDB:
    """
    This class encapsulates methods related to MongoDB 
    """

    def __init__(self, host='localhost', port=27017):
        self.client = MongoClient(host, port)
        self.database = self.client['jarvis']

    def get_documents(self, collection, key=None, limit=None):
        collection_obj = self.database[collection]
        try:
            result = collection_obj.find(key).sort('_id', DESCENDING)
            return list(result.limit(limit) if limit else result)
        except Exception as e:
            logging.error(e)

    def insert_many_documents(self, collection, documents):
        collection_obj = self.database[collection]
        try:
            collection_obj.insert_many(documents)
        except Exception as e:
            logging.error(e)

    def drop_collection(self, collection):
        collection_obj = self.database[collection]
        try:
            collection_obj.drop()
        except Exception as e:
            logging.error(e)

    def update_collection(self, collection, documents):
        self.drop_collection(collection)
        self.insert_many_documents(collection, documents)

    def update_document(self, collection, query, new_value, upsert=True):
        collection_obj = self.database[collection]
        try:
            collection_obj.update_one(query, {'$set': new_value}, upsert)
        except Exception as e:
            logging.error(e)

    def is_collection_empty(self, collection):
        collection_obj = self.database[collection]
        try:
            return collection_obj.estimated_document_count() == 0
        except Exception as e:
            logging.error(e)


# ----------------------------------------------------------------------------------------------------------------------
# Create MongoDB connection instance
# ----------------------------------------------------------------------------------------------------------------------
db = MongoDB()
