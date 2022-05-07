import redis
import json

class redisHandler:
    
    def __init__(self):
        print("redis handler init")
        
        host = "redis"
        
        port = 6379
        
        self.redis = redis.Redis(
            host=host,
            port=port
        )
    
    def set(self,key,value):
        self.redis.set(
            key,
            json.dumps(value)
        )
    
    def get(self,key):
        return json.loads(self.redis.get(key))