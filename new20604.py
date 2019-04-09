import random


class BookReader:
    dict = {}
    pages = 0
    pagesNew = 0

    def __init__(self, name):
        self.name = name
        BookReader.pages = random.randrange(1, 100)
        BookReader.pagesNew = BookReader.pages
        self.pages = BookReader.pages
        print("this book is {} pages".format(self.pages))

    def read(self):
        BookReader.pages += 1
        print("we are on  {} page".format(BookReader.pages))

    def voiceRead(self):
        BookReader.pages += 1
        print("we are on  {} page".format(BookReader.pages))

    def mark(self):
        BookReader.dict[self.name] = BookReader.pages
        print(BookReader.dict)
        return BookReader.pages


class ElectroReader(BookReader):
    def price(self):
        howMuch = BookReader.pages - BookReader.pagesNew
        print("\n you must pay {} cents for {} book".format(howMuch))


book = ElectroReader("david")
book.read()
book.voiceRead()
book.mark()
book.price()
