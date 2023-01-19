import time
from datetime import datetime
from typing import Callable, Any

cache: dict[str, Any] = {}

# wrapper function, edits a function to print the time it took to run
def timeit(func: Callable[..., Any]) -> Callable[..., Any]:
    def timed(*args, **kwargs) -> Callable[..., Any]:
        start_time: datetime = datetime.utcnow()
        result: Any = func(*args, **kwargs)
        end_time: datetime = datetime.utcnow()
        print(
            f"{(end_time - start_time).microseconds} microseconds to count {func.__name__}"
        )
        return result

    return timed


# wrapper function, edits a function to cache its output
def in_memory_cache(func: Callable[..., Any]) -> Callable[..., Any]:
    def cached(*args, **kwargs) -> Callable[..., Any]:
        # create a cache key from the function name and its arguments
        cache_key: str = f"{func.__name__}({args}, {kwargs})"
        # if key already exists in cache, return it
        if cache_key in cache:
            return cache[cache_key]
        # else, compute it and store it in cache
        result: Any = func(*args, **kwargs)
        cache[cache_key] = result
        return result

    return cached


@timeit
@in_memory_cache
def check_seeds() -> int:
    """
    Mocks a database query to count number of seeds
    SELECT COUNT(*) FROM tree;

    Lets say it takes 5 seconds to count our seeds
    """
    time.sleep(5)
    return 100


@timeit
@in_memory_cache
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
