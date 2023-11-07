def my_range(start, end, step=1):
    i = start
    while i <= end:
        yield i
        i += step
