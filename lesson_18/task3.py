class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrapper(value):
            try:
                return int(func(value))
            except Exception:
                raise ValueError("Wrong value")
        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(value):
            try:
                return str(func(value))
            except Exception:
                raise ValueError("Wrong value")
        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(value):
            try:
                return bool(func(value))
            except Exception:
                raise ValueError("Wrong value")
        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(value):
            try:
                return float(func(value))
            except Exception:
                raise ValueError("Wrong value")
        return wrapper


@TypeDecorators.to_int
def func_1(value):
    return value


@TypeDecorators.to_str
def func_2(value):
    return value


@TypeDecorators.to_bool
def func_3(value):
    return value


@TypeDecorators.to_float
def func_4(value):
    return value


print(func_1("123"))
print(func_2(123.5))
print(func_3(None))
print(func_4(123))
