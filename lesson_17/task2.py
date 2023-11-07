class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return f"Hello, my name {self.name}, I was born in {self.country} {self.birthday}.\nMy books: {', '.join(self.books)}"

    def __repr__(self):
        return self


class Book:
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f"Book name: {self.name}, was written in {self.year} by {self.author.name}"

    def __repr__(self):
        return self


class Library:
    def __init__(self, name):
        self.name = name
        self.book_list = []
        self.book_amount = 0

    def __str__(self):
        return f"This is {self.name}. Here is {self.book_amount} books."

    # def __repr__(self):
    #     return f"Repr library"

    def add_book(self, name: str, year: int, author: Author):
        new_book = Book(name, year, author)
        self.book_list.append(new_book)
        self.book_amount += 1

    def group_by_author(self, author: Author):
        return list(filter(lambda a: a.author == author, self.book_list))

    def group_by_year(self, year: int):
        return [filter(lambda a: a.year == year, self.book_list)]


if __name__ == '__main__':
    franko = Author("Franko", "Ukraine", "28.05.1856", ["Fateful Crossroad", "Kameniari", "The Involuntary Hero"])
    tolkien = Author("Tolkien", "England", "3.01.1892", ["Lord of the Rings", "Hobbit"])
    king = Author("King", "USA", "21.09.1947", ["The Shining", "The Green Mile", "11/22/63", "Mr. Mercedes"])

    test_book = Book("Kamenyari", 1878, franko)

    my_library = Library("Library of Alexandria")
    my_library.add_book("Kamenyari", 1878, franko)
    my_library.add_book('11/22/63', 2011, king)
    my_library.add_book("Hobbit", 1937, tolkien)

    print(franko)
    print(test_book)
    print(my_library)
    print(str(my_library.group_by_author(king)[0]))



