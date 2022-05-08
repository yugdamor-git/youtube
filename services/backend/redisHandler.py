import redis
import json
import os

class redisHandler:
    
    def __init__(self):
        print("redis handler init")
        
        host = "redis-manager"
        
        port = 6379
        
        password = os.environ.get("REDIS_PASSWORD")
        
        print(password)
        
        self.expireAfter = 1 * 5 * 60 * 60
        # 5 hour expire
        
        self.redis = redis.Redis(
            host=host,
            port=port,
            password=password
        )
    
    def set(self,key,value):
        self.redis.set(
            key,
            json.dumps(value),
            ex=self.expireAfter
        )
    
    def get(self,key):
        try:
            return json.loads(self.redis.get(key))
        except:
            return None