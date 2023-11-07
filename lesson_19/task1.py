def my_enumerate(iterable, start = 0):
    el_num = start
    for el in iterable:
        yield el, el_num
        el_num += 1

