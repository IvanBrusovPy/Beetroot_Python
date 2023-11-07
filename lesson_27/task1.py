def fibonacci_search(arr: list, search_value):
    n = len(arr)
    offset = -1
    fn_2 = 0
    fn_1 = 1
    fn = fn_1 + fn_2
    while fn < n:
        fn_1, fn_2 = fn, fn_1
        fn = fn_1 + fn_2

    def search():
        nonlocal fn, fn_1, fn_2, offset
        curr = min(offset + fn_2, n - 1)

        if arr[curr] == search_value:
            return curr

        elif arr[curr] > search_value:
            fn = fn_2
            fn_1 = fn_1 - fn_2
            fn_2 = fn_2 - fn_1
            return search()

        else:
            fn = fn_1
            fn_1 = fn_2
            fn_2 = fn - fn_1
            offset = curr
            return search()

        raise ValueError("No such element")

    return search()


if __name__ == '__main__':
    a = [i for i in range(-2, 26, 3)]
    print(a)
    print("Index:", fibonacci_search(a, 7))
