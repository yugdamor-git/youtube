import redis
import json
import os

class redisHandler:
    
    def __init__(self):
        print("redis handler init")
        
        host = os.environ.get("REDIS_HOST")
        
        port = 6379
        
        password = os.environ.get("REDIS_PASSWORD")
        
        print(password)
        
        self.expireAfter = 1 * 1 * 60 * 60
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
        except Exception as e:
            print(f'error : {str(e)}')
            return None
        

if __name__ == "__main__":
    r = redisHandler()
    
    print(r.get("1f245908c31b5743042f8765885eb017013e8496"))