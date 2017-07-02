class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return "{} by {}".format(self.title, self.author)


class Bookcase:
    def __init__(self, books):
        self.books = books

    @classmethod
    def create_books(klass, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return klass(books)


bc = Bookcase.create_books([("Moby dick", "Herman Melville"),("Jungle book", "Rudyard Kipling")])

print(str(bc.books[0]))