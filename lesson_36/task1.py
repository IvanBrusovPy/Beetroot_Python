import math
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

NUMBERS = [
    2,  # prime
    1099726899285419,
    1570341764013157,  # prime
    1637027521802551,  # prime
    1880450821379411,  # prime
    1893530391196711,  # prime
    2447109360961063,  # prime
    3,  # prime
    2772290760589219,  # prime
    3033700317376073,  # prime
    4350190374376723,
    4350190491008389,  # prime
    4350190491008390,
    4350222956688319,
    2447120421950803,
    5,  # prime
]


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


if __name__ == "__main__":

    print("Start Process calculation...")
    start = time.time()
    with ProcessPoolExecutor(max_workers = 4) as pool:
        print(list(pool.map(is_prime, NUMBERS)))
    end = time.time()
    print(end - start , "sec")  # 22.193998336791992 sec

    print("Start Thread calculation...")
    start = time.time()
    with ThreadPoolExecutor(max_workers = 4) as pool:
        print(list(pool.map(is_prime, NUMBERS)))
    end = time.time()
    print(end - start, "sec")  # 55.0419180393219 sec

