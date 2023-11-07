from config import values, keys
from input_data.input_phone_name import input_phone, input_name


def read_contact():
    phone = input_phone()
    new_data = {phone: {}}
    for key, value in zip(keys.values(), values.values()):
        new_data[phone][key] = input_name(value)
    return new_data


def print_contact(contact: dict):
    for phone, data in contact.items():
        print(f'Phone number: {phone}')
        for name, record in zip(values.values(), data):
            print(f'\t{name.capitalize()}: {str(data[record]).capitalize()}')

