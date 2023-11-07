from config import values
from databse_comands.open_save_db import open_dataset, save_dataset
from databse_comands.read_print_contact import read_contact
from databse_comands.contact_manager import add_contact, update_contact, delete_contact
from databse_comands.search_contact import get_contact
dataset = {}
file_path = ""


def run_app(path):
    global file_path
    file_path = path
    global dataset
    dataset = open_dataset(file_path)
    main_menu()


def main_menu():
    while True:
        show_main_commands()
        cmd = input('Choose main command: ')
        match cmd:
            case "e":
                edit_database()
            case "s":
                search_contact()
            case "c":
                print("Exit...")
                save_dataset(dataset, file_path)
                exit()
            case _:
                print("Wrong command")


def show_main_commands():
    print("e - Edit database",
          "s - Search contact",
          "c - Save and close",
          sep="\n")


def edit_database():
    print("a - Add contact",
          "u - Update_contact",
          "d - Delete contact",
          "b - To main menu",
          sep="\n")

    while True:
        global dataset
        cmd = input('Choose edit command: ')
        match cmd:
            case "a":
                new_contact = read_contact()
                dataset = add_contact(dataset, new_contact)
            case "u":
                dataset = update_contact(dataset)
            case "d":
                dataset = delete_contact(dataset)
            case "b":
                main_menu()
            case _:
                print("Wrong command")


def search_contact():
    print("Search contact by:",
          "p - phone",
          "fl - full name",
          sep="\n")
    for key, value in values.items():
        print(f"{key} - {value}")
    print("b - To main menu")

    while True:
        cmd = input('Choose search command: ')
        if cmd in values.keys() or cmd == "p" or cmd == "fl":
            get_contact(dataset, cmd)
        elif cmd == "b":
            main_menu()
        else:
            print("Wrong command")



