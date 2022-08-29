from _base.cache import default_redis
from aggregation.enums import RECEIVED_DATA_CACHE_KEY
import pickle


def get_cached_data():
    return {int(k.decode()): pickle.loads(v) for k, v in default_redis.hgetall(RECEIVED_DATA_CACHE_KEY).items()}
