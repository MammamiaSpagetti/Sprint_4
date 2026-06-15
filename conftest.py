import pytest
from main import BooksCollector
from data import (
    BOOK_DUNE,
    BOOK_IT,
    BOOK_TOM_AND_JERRY,
    GENRE_FANTASY,
    GENRE_HORROR,
    GENRE_CARTOONS
)


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_books(collector):
    for book in [BOOK_DUNE, BOOK_IT, BOOK_TOM_AND_JERRY]:
        collector.add_new_book(book)
    return collector


@pytest.fixture
def collector_with_genres(collector_with_books):
    collector_with_books.set_book_genre(BOOK_DUNE, GENRE_FANTASY)
    collector_with_books.set_book_genre(BOOK_IT, GENRE_HORROR)
    collector_with_books.set_book_genre(BOOK_TOM_AND_JERRY, GENRE_CARTOONS)
    return collector_with_books


@pytest.fixture
def collector_with_favorites(collector_with_books):
    collector_with_books.add_book_in_favorites(BOOK_DUNE)
    collector_with_books.add_book_in_favorites(BOOK_IT)
    return collector_with_books
