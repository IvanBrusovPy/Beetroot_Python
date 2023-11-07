from config import keys, values


def add_contact(dataset: dict, data: dict):
    dataset.update(data)
    return dataset


def update_contact(dataset: dict):
    phone = input("Input phone number:\n")
    if phone in dataset:
        for key, value in zip(keys.values(), values.values()):
            updated_value = input(f"Input {value}: ")
            if updated_value != "":
                dataset[phone][key] = updated_value
    else:
        print("No phone in database. Try again")
    return dataset


def delete_contact(dataset: dict):
    phone = input("Input phone number:\n")
    if phone in dataset:
        del dataset[phone]
        print("Successfully deleted")
    else:
        print("No phone in database. Try again")
    return dataset
