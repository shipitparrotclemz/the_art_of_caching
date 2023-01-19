import json
import time
from datetime import datetime, timedelta
from functools import wraps
from typing import Callable, Any, Optional

import redis as redis

redis_database = redis.Redis(host="localhost", port=6379)


# wrapper function, edits a function to print the time it took to run
def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    def timed(*args, **kwargs) -> Callable[..., Any]:
        start_time: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end_time: datetime = datetime.utcnow()
        print(f"{(end_time - start_time).seconds} seconds to count {func.__name__}")
        return result

    return timed


# wrapper function, edits a function to cache its output into redis
# note: we didn't implement an lru eviction here for simplicity!
# instead, we set a time to live for each cache!
def redis_cache(
    func: Callable[..., Any], time_to_live: timedelta = timedelta(days=5)
) -> Callable[..., Any]:
    # add a @wraps decorator here, so timeit can log the right function.
    # else, it will incorrectly log the function name as cached
    @wraps(func)
    def cached(*args, **kwargs) -> Callable[..., Any]:
        # create a cache key from the function name and its arguments
        cache_key: str = f"{func.__name__}({args}, {kwargs})"
        result_json: Optional[bytes] = redis_database.get(cache_key)
        # if key already exists in cache, return it
        if result_json:
            # Note, this can fail if the output of the function is not json serializable
            # More on this in the next article
            result: Any = json.loads(result_json)
            return result
        # else, compute it and store it in cache
        result: Any = func(*args, **kwargs)
        result_json: str = json.dumps(result)
        redis_database.setex(name=cache_key, time=time_to_live, value=result_json)
        return result

    return cached


@timeit
@redis_cache
def check_seeds() -> int:
    """
    Mocks a database query to count number of seeds
    SELECT COUNT(*) FROM tree;

    Lets say it takes 5 seconds to count our seeds
    """
    time.sleep(5)
    return 100


@timeit
@redis_cache
def check_feathers() -> int:
    """
    Mocks a database query to count number of feathers
    SELECT COUNT(*) FROM feathers;

    Lets say it takes 5 seconds to count our feathers
    """
    time.sleep(5)
    return 100


seeds: int = check_seeds()
print(f"seeds: {seeds}")

seeds: int = check_seeds()
print(f"seeds: {seeds}")

feathers: int = check_feathers()
print(f"feathers: {feathers}")

feathers: int = check_feathers()
print(f"feathers: {feathers}")
