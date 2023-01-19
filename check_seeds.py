import time
from datetime import datetime


def check_seeds() -> int:
    """
    Mocks a database query to count number of seeds
    SELECT COUNT(*) FROM tree;

    Lets say it takes 5 seconds to count our seeds
    """
    time.sleep(5)
    return 100


start_time: datetime = datetime.utcnow()
seeds: int = check_seeds()
print(f"seeds: {seeds}")
end_time: datetime = datetime.utcnow()
print(f"{(end_time - start_time).microseconds} microseconds to count seeds")