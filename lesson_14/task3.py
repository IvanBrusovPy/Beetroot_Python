def arg_rules(type_: type, max_length: int, contains: list):
    def out_wrap(func):
        def in_wrap(*args):
            if type(func(args)) != type_:
                print(f'Incorrect type of argument. Only {type_} support {type(func(args))}')
                return False
            if len(str(args)) > max_length:
                print(f'Too long name. Max {max_length} symbols')
                return False
            if -1 in [str(args).find(i) for i in contains]:
                print(f'Name should include {contains}')
                return False
            else:
                return func(args[0])

        return in_wrap

    return out_wrap


@arg_rules(type_=str, max_length=25, contains=['05', '@'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('S@SH05'))
