def get_even(file_obj):
    data = file_obj.readline().split()
    return list(filter(lambda x: int(x) % 2 == 0, data))


# a = open("test_file.txt")
# print(get_even(a))
