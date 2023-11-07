def some_func():
    a, b, c = 1, 2, 3
    string = "HelloWord!"


def count_locals(func):
    return func.__code__.co_nlocals


print(count_locals(some_func))



