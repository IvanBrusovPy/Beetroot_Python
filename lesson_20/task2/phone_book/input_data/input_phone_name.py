from input_data.validator import is_valid


def input_phone():
    phone_num = input('Input phone number: ')
    while not is_valid(phone_num, "phone_num"):
        phone_num = input('Wrong format\nInput phone number: ')
    return phone_num


def input_name(value):
    name = input(f'Input {value}: ')
    while not is_valid(name, "name"):
        name = input(f'Wrong format\nInput {value}: ')
    return name



