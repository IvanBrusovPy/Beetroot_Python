class Mathematician:
    def square_nums(self, math_list: list):
        return list(map(lambda x: x ** 2, math_list))

    def remove_positives(self, math_list: list):
        return list(filter(lambda x: x>0, math_list))

    def filter_leaps(self, math_list: list):
        return list(filter(lambda x: x % 4 ==0, math_list))


m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
