import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    for book in ['Дюна', 'Оно', 'Том и Джерри']:
        collector.add_new_book(book)
    return collector

@pytest.fixture
def collector_with_genres(collector_with_books):
    collector_with_books.set_book_genre('Дюна', 'Фантастика')
    collector_with_books.set_book_genre('Оно', 'Ужасы')
    collector_with_books.set_book_genre('Том и Джерри', 'Мультфильмы')
    return collector_with_books

@pytest.fixture
def collector_with_favorites(collector_with_books):
    collector_with_books.add_book_in_favorites('Дюна')
    collector_with_books.add_book_in_favorites('Оно')
    return collector_with_books

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book_name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_not_added(self, collector, book_name):
        collector.add_new_book(book_name)

        assert book_name not in collector.get_books_genre()

    def test_add_new_book_same_book_added_once(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_valid_genre_sets_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Роман')

        assert collector.get_book_genre('Дюна') == ''

    def test_get_book_genre_returns_genre_by_book_name(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Дюна']),
        ('Ужасы', ['Оно']),
        ('Мультфильмы', ['Том и Джерри'])
    ])
    def test_get_books_with_specific_genre_returns_books(
        self,
        collector_with_genres,
        genre,
        expected_books
    ):
        assert collector_with_genres.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_genre_returns_books_dictionary(self, collector_with_books):
        assert collector_with_books.get_books_genre() == {
            'Дюна': '',
            'Оно': '',
            'Том и Джерри': ''
        }

    def test_get_books_for_children_returns_books_without_age_rating(self, collector_with_genres):
        assert collector_with_genres.get_books_for_children() == ['Дюна', 'Том и Джерри']

    def test_add_book_in_favorites_adds_existing_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Дюна')

        assert collector_with_books.get_list_of_favorites_books() == ['Дюна']

    def test_add_book_in_favorites_same_book_added_once(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Дюна')
        collector_with_books.add_book_in_favorites('Дюна')

        assert collector_with_books.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_deletes_book(self, collector_with_favorites):
        collector_with_favorites.delete_book_from_favorites('Дюна')

        assert collector_with_favorites.get_list_of_favorites_books() == ['Оно']

    def test_get_list_of_favorites_books_returns_favorites_list(
        self,
        collector_with_favorites
    ):
        assert collector_with_favorites.get_list_of_favorites_books() == [
            'Дюна',
            'Оно'
        ]
