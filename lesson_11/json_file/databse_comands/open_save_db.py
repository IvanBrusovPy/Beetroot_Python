import json


def open_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_dataset(dataset, file_path):

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dataset, file)
