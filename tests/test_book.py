import unittest

from book_manager.book import Book
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

        book_list = book_manager.list_books()
        self.assertIn(book, book_list)
        self.assertRaises(ValueError, book_manager.add_book, book)


if __name__ == '__main__':
    unittest.main()