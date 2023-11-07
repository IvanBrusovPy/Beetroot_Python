def make_operation(operator, *args):
    res = int()
    if operator == '+':
        res = sum(args)
    if operator == '-':
        res = args[0]*2
        for i in args:
            res -= i
    if operator == '*':
        res = 1
        for i in args:
            res *= i
    return res


print(make_operation('-', 2, 4, 6))
