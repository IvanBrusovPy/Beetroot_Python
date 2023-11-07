from random import randint
from functools import wraps
import tracemalloc
from time import perf_counter
global partition_limit


def measure_performance(func):
    """Measure performance of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'Limit: {partition_limit}')
        print(f'{"-" * 40}')

        tracemalloc.stop()

    return wrapper


def insertion_sort(array):
    for index in range(1, len(array)):
        current_value = array[index]
        position = index
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = current_value


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr, low, high):
    if low < high:
        if high - low < partition_limit:
            insertion_sort(arr[low: high])
        pi = partition(arr, low, high)
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)
    return arr


@measure_performance
def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr)-1)


if __name__ == "__main__":
    for i in range(0, 10):
        a = [randint(0, 100) for _ in range(100)]
        partition_limit = i
        quick_sort(a)

# Після проведення вимірювання швидкості
# було визначено, що додавання сортування вставками
# оптимізує час виконання,але тільки у випадках коли
# довжина масива, що вона сортує менше 4
