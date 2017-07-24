import redis

pool = redis.ConnectionPool(host='192.168.5.128', port=6379, password='alan', db=1)

rd = redis.Redis(connection_pool=pool)

rd.set(name="name1", value='123')