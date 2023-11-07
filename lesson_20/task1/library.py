class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.name == other.name and self.books == other.books and self.birthday == other.birthday
        return False


class Book:
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.name == other.name and self.year == other.year and self.author == other.author
        return False


class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []
        self.book_amount = 0

    def add_book(self, name: str, year: int, author: Author):
        new_book = Book(name, year, author)
        self.book_list.append(new_book)
        self.book_amount += 1

    def group_by_author(self, author: Author):
        return list(filter(lambda a: a.author == author, self.book_list))

    def group_by_year(self, year: int):
        return list(filter(lambda a: a.year == year, self.book_list))
