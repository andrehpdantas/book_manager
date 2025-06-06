class BookManager:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def get_book_qty(self):
        return len(self.book_list)