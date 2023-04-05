import pytest

from main import BooksCollector

@pytest.fixture
def new_book():
    collector = BooksCollector()
    return collector

@pytest.fixture
def new_one_book():
    collector = BooksCollector()
    collector.add_new_book('Найди время')
    return collector

@pytest.fixture
def comparison_dictionary():
    dictionary = {
        'Найди время': 8,
        'Грокаем алгоритмы': 10,
        'Справочник Python': 9,
        'Победи прокрастинацию': 7
    }
    return dictionary

@pytest.fixture
def new_collection():
    collector = BooksCollector()
    collector.add_new_book('Найди время')
    collector.set_book_rating('Найди время', 8)
    collector.add_new_book('Грокаем алгоритмы')
    collector.set_book_rating('Грокаем алгоритмы', 10)
    collector.add_new_book('Справочник Python')
    collector.set_book_rating('Справочник Python', 9)
    collector.add_new_book('Победи прокрастинацию')
    collector.set_book_rating('Победи прокрастинацию', 7)
    return collector

@pytest.fixture
def favorites_collection():
    collector = BooksCollector()
    collector.favorites = ['Найди время', 'Грокаем алгоритмы', 'Справочник Python', 'Победи прокрастинацию']
    return collector