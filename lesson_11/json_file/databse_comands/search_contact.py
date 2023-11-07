from config import keys, values
from databse_comands.read_print_contact import print_contact


def get_contact(dataset: dict, type_value):
    if type_value == "p":
        phone = input("Input phone number: ")
        if str(phone) not in dataset.keys():
            print("No phone in book. Try again")
        else:
            print_contact({phone: dataset[phone]})
    if type_value == "fl":
        full_name = input("Input full name: ").split()
        if len(full_name) != 2:
            print("Wrong format. Input name and surname")
        else:
            first_name, last_name = full_name[0], full_name[1]
            if first_name in (dataset[phone]['first_name'] for phone in dataset):
                if last_name in (dataset[phone]['last_name'] for phone in dataset):
                    for phone in dataset:
                        if dataset[phone]['first_name'] == first_name:
                            if dataset[phone]['last_name'] == last_name:
                                print_contact({phone: dataset[phone]})
            else:
                print(f"No such {values[type_value]} in book. Try again")

    else:
        search_value = input(f"Input {values[type_value]}: ")
        if search_value in (dataset[phone][keys.get(type_value)] for phone in dataset):
            for phone in dataset:
                if dataset[phone][keys.get(type_value)] == search_value:
                    print_contact({phone: dataset[phone]})
        else:
            print(f"No such {values[type_value]} in book. Try again")


