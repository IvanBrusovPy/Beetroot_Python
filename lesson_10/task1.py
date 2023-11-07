def oops():
    raise IndexError("Oops")


def try_func():
    a = []
    try:
        print(a[3])
    except IndexError:
        oops()


try_func()
