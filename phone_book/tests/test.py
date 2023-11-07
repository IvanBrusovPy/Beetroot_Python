import os
import unittest
import json
from copy import deepcopy

from databse_comands.open_save_db import open_dataset, save_dataset
from databse_comands.read_print_contact import read_contact
from databse_comands.contact_manager import add_contact, update_contact, delete_contact
from databse_comands.search_contact import get_contact


class PhoneBookTest(unittest.TestCase):
    test_contact_1 = {"123": {"first_name": "vasya", "last_name": "pupkin", "city": "paris"}}
    test_contact_2 = {"456": {"first_name": "sasha", "last_name": "brusov", "city": "odesa"}}
    test_db_path = f'test_db.json'


    def test_save_dataset(self):
        with open(self.test_db_path, 'w', encoding='utf-8') as file:
            save_dataset(self.test_contact_1, self.test_db_path)

        with open(self.test_db_path, 'r', encoding='utf-8') as file:
            self.assertEqual(json.load(file), self.test_contact_1)

    def test_open_dataset(self):
        with open(self.test_db_path, 'r', encoding='utf-8') as file:
            self.assertEqual(self.test_contact_1, open_dataset(self.test_db_path))


    def test_read_contact(self):
        print(f"Enter data from: {self.test_contact_1}")
        self.assertEqual(self.test_contact_1, read_contact())

    def test_add_contact(self):
        data_set = deepcopy(self.test_contact_1)
        data_set.update(self.test_contact_2)
        self.assertEqual(data_set, add_contact(data_set, self.test_contact_2))

    def test_del_contact(self):
        print("Enter 456")
        # NOTE (Ivan Brusov): (8/16/2023) - (Вводити 456 в якості ключа)
        data_set = deepcopy(self.test_contact_1)
        data_set.update(self.test_contact_2)
        self.assertEqual(self.test_contact_1, delete_contact(data_set))

    def test_edit_contact(self):
        print("Enter 456, first_name = alex, next -> pass")
        # NOTE (Ivan Brusov): (8/16/2023) - (Замінити ім'я на alex, телефон 456)
        data_set = deepcopy(self.test_contact_1)
        data_set.update(self.test_contact_2)
        data_set['456']['name'] = 'alex'
        self.assertEqual(data_set, update_contact(data_set))

    def test_get_contact(self):
        print("Enter 456")
        # NOTE (Ivan Brusov): (8/16/2023) - (Ввести телефон 456)
        data_set = deepcopy(self.test_contact_1)
        data_set.update(self.test_contact_2)
        self.assertEqual(data_set.get("456"), get_contact(data_set, "p"))

