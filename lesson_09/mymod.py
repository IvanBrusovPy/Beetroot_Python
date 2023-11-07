import sys


def count_lines(name):
    file = open(f"{name}", "r")
    file.seek(0)
    return len(file.readlines())


def count_chars(name):
    file = open(f"{name}", "r")
    file.seek(0)
    return len(file.read())


def test(file_name):
    print("Quantity of lines: " + str(count_lines(file_name)))
    print("Quantity of characters: " + str(count_chars(file_name)))


test("mymod.py")
