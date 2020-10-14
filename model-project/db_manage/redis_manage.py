import redis

pool = redis.Connection()

r = redis.Redis(connection_pool=pool)
