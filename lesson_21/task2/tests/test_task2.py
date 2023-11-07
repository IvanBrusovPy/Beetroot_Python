from datetime import datetime
from unittest import TestCase

from random import randint

from Python_homework.lesson_21.task2.task2 import MyOpen


class TestMyOpen(TestCase):
    def setUp(self):
        self.test_data = "123456789"
        self.true_path = "test_file.txt"
        self.false_path = "wrong_path.txt"
        self.error_path = "FileNotFoundError(2, 'No such file or directory')"

    def test_readfile(self):
        with open(self.true_path, "w") as f:
            f.write(self.test_data)
        with MyOpen(self.true_path) as f:
            self.assertEqual(self.test_data, f.readline())

    def test_write(self):
        with MyOpen(self.true_path, "w") as f:
            f.write(self.test_data)

        with open(self.true_path) as f:
            self.assertEqual(self.test_data, f.readline())

    def test_counter(self):
        c = randint(1, 1000)
        f_test = MyOpen(self.true_path)
        self.assertEqual(0, f_test.counter)
        for _ in range(c):
            with f_test as _:
                pass
        self.assertEqual(f_test.counter, c)

    def test_logs(self):
        with open("logs.txt", "w") as f:
            f.write("")
        with MyOpen(self.true_path):
            pass
        with open("logs.txt") as f_logs:
            self.assertEqual("", f_logs.readline())

        try:
            with MyOpen(self.false_path):
                pass

        except Exception as e:
            print(e)
        finally:
            log_f = open("logs.txt", "r")
            self.assertEqual(log_f.readline(), f"{datetime.now().strftime('%d/%m/%y %H:%M:%S')} {self.error_path}\n")
            f.close()
