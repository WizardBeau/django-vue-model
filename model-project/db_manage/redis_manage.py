import redis

class REDIS_MANAGE(object):
    def __init__(self):
        super(REDIS_MANAGE, self).__init__()
        self.redis_client = redis.StrictRedis(host="localhost",port=6379,
        decode_responses=True, db=0)

        try:
            self.redis_client.ping()
        except:
            print("localhost:6379 redis connenct out")

    def get_all_dir_memory(self):
        return self.redis_client.hgetall('dirMemory')
    
    def set_dir_memory(self, value):
        self.redis_client.hset('dirMemory', 'dict', value)