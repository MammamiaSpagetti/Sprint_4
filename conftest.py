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
