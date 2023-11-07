import asyncio
import math
import time


async def calc_fibonachi(n):
    f1 = 0
    f2 = 1
    for _ in range(n):
        f1, f2 = f1+f2, f1
    return f1


async def calc_factorial(n):
    return math.factorial(n)


async def square(n):
    return n * n


async def cubic(n):
    return n*n*n


async def gather_tasks():
    fib_arr = []
    fac_arr = []
    sqr_arr = []
    cub_arr = []
    for i in range(10):
        fib, fac, sqr, cub = await asyncio.gather(
            calc_fibonachi(i),
            calc_factorial(i),
            square(i),
            cubic(i)
        )
        fib_arr.append(fib)
        fac_arr.append(fac)
        sqr_arr.append(sqr)
        cub_arr.append(cub)
    return fib_arr, fac_arr, sqr_arr, cub_arr


if __name__ == '__main__':
    print("Start Async calculation...")
    start = time.time()
    result = asyncio.run(gather_tasks())
    end = time.time()
    print(end - start, "sec")   # 0.0030024051666259766 sec

    # print(result[0])
    # print(result[1])
    # print(result[2])
    # print(result[3])

    print("Start Async calculation...")
    start = time.time()

    end = time.time()
    print(end - start, "sec")


