import pymongo
import os

class Database:
    def __init__(self):
        db_name = "Ytshorts-Savetube-Me"
        connection_uri = os.environ.get("MONGO_DB_URI")
        client = pymongo.MongoClient(connection_uri)
        db = client[db_name]
        self.requestCount = db["request-count"]
        self.storage = db["storage"]
        self.resolutionCount = db["resolution-count"]
        self.errorLogs = db["errors"]