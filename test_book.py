import unittest

import book
from book import Book
from book_manager import BookManager

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        """
         Testa a criação bem-sucedida de um livro com todos os atributos.
        """
        title = "O Senhor dos Anéis"
        author = "J.R.R. Tolkien"
        isbn = "978-0618053267"

        book = Book(title, author, isbn)
        # Assert: Verificação dos atributos do livro

        self.assertEqual(book.title, title)
        self.assertEqual(book.author, author)
        self.assertEqual(book.isbn, isbn)
        self.assertFalse(book.read)

    def test_add_book_to_manager(self):
        """
        Testa se o livro foi adicionado corretamente ao gerenciador de livros.
        """
        book_manager = BookManager()

        title = "O Senhor dos Anéis"
        author = "J.R.R. Tolkien"
        isbn = "978-0618053267"

        book = Book(title, author, isbn)
        book_manager.add_book(book)

        self.assertEqual(book_manager.get_book_qty(), 1)


if __name__ == '__main__':
    unittest.main()