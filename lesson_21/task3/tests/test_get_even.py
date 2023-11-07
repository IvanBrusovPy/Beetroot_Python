from Python_homework.lesson_21.task3.task3 import get_even


def test_get_even():
    test_data = "1 12 3 4 5 6 7 8 9"
    with open("test_data.txt", "w") as f:
        print(test_data, file = f)
    result = "12 4 6 8".split()
    print(result)
    test_file = open("test_data.txt",)
    assert get_even(test_file) == result
