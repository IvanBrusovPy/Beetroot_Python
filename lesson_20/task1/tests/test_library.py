from unittest import TestCase

from Python_homework.lesson_20.task1.library import Library, Author, Book


class TestLibrary(TestCase):
    def setUp(self):
        self.my_lib = Library('My Lib')
        self.franko = Author("Franko", "Ukraine", "28.05.1856",
                             ["Fateful Crossroad", "Kameniari", "The Involuntary Hero"])
        self.tolkien = Author("Tolkien", "England", "3.01.1892", ["Lord of the Rings", "Hobbit"])
        self.king = Author("King", "USA", "21.09.1947", ["The Shining", "The Green Mile", "11/22/63", "Mr. Mercedes"])

        self.franko_book_1 = Book("Zakhar Berkut", 1883, self.franko)
        self.franko_book_2 = Book("Z vershyn i nyzyn", 1887, self.franko)

        self.king_book_1 = Book("The Shining", 1977, self.king)
        self.king_book_2 = Book("The Green Mile", 1996, self.king)

        self.tolkien_book_1 = Book("Silmarillion", 1977, self.tolkien)
        self.tolkien_book_2 = Book("The War of the Ring", 1990, self.tolkien)

        self.all_books = [self.franko_book_1, self.franko_book_2, self.king_book_1, self.king_book_2,
                          self.tolkien_book_1, self.tolkien_book_2]

        self.franko_books = list(filter(lambda b: b.author == self.franko, self.all_books))
        self.books_1977 = list(filter(lambda b: b.year == 1977, self.all_books))

        self.my_lib.add_book("Zakhar Berkut", 1883, self.franko)
        self.my_lib.add_book("Z vershyn i nyzyn", 1887, self.franko)
        self.my_lib.add_book("The Shining", 1977, self.king)
        self.my_lib.add_book("The Green Mile", 1996, self.king)
        self.my_lib.add_book("Silmarillion", 1977, self.tolkien)
        self.my_lib.add_book("The War of the Ring", 1990, self.tolkien)
            
    def test_add_book(self):
        self.assertEqual(self.all_books, self.my_lib.book_list)

    def test_group_by_author(self):
        for b1, b2 in zip(self.my_lib.group_by_author(self.franko), self.franko_books):
            self.assertEqual(b1, b2)


    def test_group_by_year(self):
        for b1, b2 in zip(self.my_lib.group_by_year(1977), self.books_1977):
            self.assertEqual(b1, b2)
