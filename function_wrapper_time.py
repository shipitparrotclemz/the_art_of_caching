import time
from datetime import datetime
from typing import Callable, Any

cache: dict[str, int] = {}


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


@timeit
def check_seeds() -> int:
    """
    Mocks a database query to count number of seeds
    SELECT COUNT(*) FROM tree;

    Lets say it takes 5 seconds to count our seeds
    """
    if "seeds" in cache:
        return cache["seeds"]
    time.sleep(5)
    cache["seeds"] = 100
    return cache["seeds"]


@timeit
def check_feathers() -> int:
    """
    Mocks a database query to count number of feathers
    SELECT COUNT(*) FROM feathers;

    Lets say it takes 5 seconds to count our feathers
    """
    if "feathers" in cache:
        return cache["feathers"]
    time.sleep(5)
    cache["feathers"] = 100
    return cache["feathers"]


seeds: int = check_seeds()
print(f"seeds: {seeds}")

seeds: int = check_seeds()
print(f"seeds: {seeds}")


feathers: int = check_feathers()
print(f"feathers: {feathers}")

feathers: int = check_feathers()
print(f"feathers: {feathers}")
