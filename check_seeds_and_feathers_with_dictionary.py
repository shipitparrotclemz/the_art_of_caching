import time
from datetime import datetime

cache: dict[str, int] = {}


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


start_time: datetime = datetime.utcnow()
seeds: int = check_seeds()
print(f"seeds: {seeds}")
end_time: datetime = datetime.utcnow()
print(f"{(end_time - start_time).microseconds} microseconds to count seeds")

start_time: datetime = datetime.utcnow()
seeds: int = check_seeds()
print(f"seeds: {seeds}")
end_time: datetime = datetime.utcnow()
print(f"{(end_time - start_time).microseconds} microseconds to count seeds again!")


start_time: datetime = datetime.utcnow()
feathers: int = check_feathers()
print(f"feathers: {feathers}")
end_time: datetime = datetime.utcnow()
print(f"{(end_time - start_time).microseconds} microseconds to count feathers")

start_time: datetime = datetime.utcnow()
feathers: int = check_feathers()
print(f"feathers: {feathers}")
end_time: datetime = datetime.utcnow()
print(f"{(end_time - start_time).microseconds} microseconds to count feathers again!")
