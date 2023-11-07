def outer_func(a, b):
    def inner_func():
        return a+b

    return inner_func()**2


print(outer_func(1, 2))
