from datetime import datetime
import os
from Database import Database

class LogManager:
    def __init__(self) -> None:
        self.database = Database()
        
        self.ip = os.environ.get("IP")
    
    def increaseRequestCount(self, countFor):

        currentTime = datetime.now()
        
        today = currentTime.strftime("%d-%m-%Y")
        
        self.database.requestCount.update_one(
            {"timestamp": today , "type":f'{countFor}',"server":self.ip},
            {"$setOnInsert": {"type": f'{countFor}',"server":self.ip, "count": 0,"createdAt":currentTime,"updatedAt":currentTime}
             
             },
            upsert=True,
        )

        self.database.requestCount.update_one(
            {"timestamp": today,"type":f'{countFor}',"server":self.ip}, {"$inc": {"count": 1},"$set":{"updatedAt":currentTime}}
        )
        
        
        self.database.requestCount.update_one(
            {"timestamp": today , "type":f'{countFor}',"server":"all"},
            {"$setOnInsert": {"type": f'{countFor}',"server":"all", "count": 0,"createdAt":currentTime,"updatedAt":currentTime}
             
             },
            upsert=True,
        )

        self.database.requestCount.update_one(
            {"timestamp": today,"type":f'{countFor}',"server":"all"}, {"$inc": {"count": 1},"$set":{"updatedAt":currentTime}}
        )
    
    def increaseResolutionCount(self, countFor):

        currentTime = datetime.now()
        
        today = currentTime.strftime("%d-%m-%Y")
        
        self.database.resolutionCount.update_one(
            {"timestamp": today , "type":f'{countFor}',"server":self.ip},
            {"$setOnInsert": {"type": f'{countFor}',"server":self.ip, "count": 0,"createdAt":currentTime,"updatedAt":currentTime}
             
             },
            upsert=True,
        )

        self.database.resolutionCount.update_one(
            {"timestamp": today,"type":f'{countFor}',"server":self.ip}, {"$inc": {"count": 1},"$set":{"updatedAt":currentTime}}
        )
        
        
        
        self.database.resolutionCount.update_one(
            {"timestamp": today , "type":f'{countFor}',"server":"all"},
            {"$setOnInsert": {"type": f'{countFor}',"server":"all", "count": 0,"createdAt":currentTime,"updatedAt":currentTime}
             
             },
            upsert=True,
        )

        self.database.resolutionCount.update_one(
            {"timestamp": today,"type":f'{countFor}',"server":"all"}, {"$inc": {"count": 1},"$set":{"updatedAt":currentTime}}
        )
        
    def updateStorageInfo(self,size):
        
        currentTime = datetime.now()
        
        today = currentTime.strftime("%d-%m-%Y")

        self.database.storage.update_one(
            {"timestamp": today , "server":self.ip},
            {"$setOnInsert": {"server":self.ip, "storageUsed": size,"createdAt":currentTime,"updatedAt":currentTime}
             
             },
            upsert=True,
        )

        self.database.resolutionCount.update_one(
            {"timestamp": today,"server":self.ip}, {"$set":{"updatedAt":currentTime,"storageUsed": size}}
        )
        