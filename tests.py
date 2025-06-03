import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_initial_state(self):
        collector = BooksCollector()
        assert collector.get_books_genre() == {} and collector.get_list_of_favorites_books() == []

    def test_add_new_book_correct_add_book_successful_add(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        assert collector.get_book_genre('Три поросенка') == ''

    @pytest.mark.parametrize("name, expected_count", [
        ('Три поросенка', 1),
        ('', 0),
        ('Три поросенка' * 10, 0)
    ])
    def test_add_new_book_incorrect_add_book_unsuccessful_add(self, name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == expected_count

    def test_set_book_genre_correct_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.set_book_genre('Три поросенка', 'Ужасы')
        assert collector.books_genre['Три поросенка'] == 'Ужасы'

    def test_set_book_genre_incorrect_genre_unsuccess(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.set_book_genre('Три поросенка', 'FFFFFF')
        assert collector.books_genre['Три поросенка'] == ''

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.set_book_genre('Три поросенка', 'Ужасы')
        assert collector.get_book_genre('Три поросенка') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        books = ['Три поросенка', 'Золушка', 'Красная шапочка']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Ужасы')

        collector.add_new_book('Волшебник Изумрудного города')
        collector.set_book_genre('Волшебник Изумрудного города', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Ужасы') == books

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        assert collector.get_books_genre() == {'Три поросенка': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Детская')
        collector.add_new_book('Взрослая')
        collector.set_book_genre('Детская', 'Фантастика')
        collector.set_book_genre('Взрослая', 'Ужасы')

        assert collector.get_books_for_children() == ['Детская']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_book_in_favorites('Три поросенка')
        assert collector.get_list_of_favorites_books() == ['Три поросенка']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_book_in_favorites('Три поросенка')
        collector.delete_book_from_favorites('Три поросенка')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Три поросенка')
        collector.add_new_book('Золушка')
        collector.add_book_in_favorites('Три поросенка')
        collector.add_book_in_favorites('Золушка')
        assert collector.get_list_of_favorites_books() == ['Три поросенка', 'Золушка']