import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

class redis_get():
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.0.132', port=6379,password='kxyx92108',db=3, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都起着 redis默认端口是6379
        self.r = redis.Redis(connection_pool=pool)
        

    def redis_hash(self,hash_value):

        return self.r.hkeys(hash_value)[0]      # gender 取出键male对应的值

    def redis_key(self,hash_value):
        return self.r.hget(hash_value,self.redis_hash(hash_value))


if __name__=="__main__":
    rds=redis_get()
    print(rds.redis_hash("pv:activity:hash:2019-04-01:1269:1005"))
    print(rds.redis_key("pv:activity:hash:2019-04-01:1269:1005"))


