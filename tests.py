from main import BooksCollector

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

    def test_add_new_book_check_add_two_books(self, new_book):
        new_book.add_new_book('Гордость и предубеждение и зомби')
        new_book.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert new_book.get_book_rating('Гордость и предубеждение и зомби') == 1, \
            'Не удалось добавить книгу - Гордость и предубеждение и зомби '
        assert new_book.get_book_rating('Что делать, если ваш кот хочет вас убить') == 1, \
            'не удалось добавить книгу - Что делать, если ваш кот хочет вас убить '

    def test_add_new_book_add_identical_two_books(self, new_book):
        new_book.add_new_book('Гордость и предубеждение и зомби')
        new_book.add_new_book('Гордость и предубеждение и зомби')
        assert (len(new_book.get_books_rating()) == 1)

    def test_set_book_rating_rating_13(self, new_one_book):
        new_one_book.set_book_rating('Найди время', 13)
        assert new_one_book.get_book_rating('Найди время') == 1

    def test_get_book_rating_get_rating_for_two_book(self, new_book):
        new_book.add_new_book('Найди время')
        new_book.set_book_rating('Найди время', 8)
        assert new_book.get_book_rating('Найди время') == 8

    def test_get_books_with_specific_rating_rated_10(self, new_collection):
        assert new_collection.get_books_with_specific_rating(10) == ['Грокаем алгоритмы']

    def test_get_books_rating_new_dictionary(self, new_book):
        dictionary = {
            'Найди время': 8,
            'Грокаем алгоритмы': 10,
            'Справочник Python': 9,
            'Победи прокрастинацию': 7
        }
        for key, value in dictionary.items():
            new_book.add_new_book(key)
            new_book.set_book_rating(key, value)
        assert new_book.get_books_rating() == dictionary

    def test_add_book_in_favorites_two_books_in_favorites(self, new_collection):
        new_collection.add_book_in_favorites('Найди время')
        new_collection.add_book_in_favorites('Грокаем алгоритмы')
        assert new_collection.get_list_of_favorites_books() == new_collection.favorites

    def test_delete_book_from_favorites_delete_one_book_positive(self,favorites_collection):
        favorites_collection.delete_book_from_favorites('Грокаем алгоритмы')
        assert favorites_collection.get_list_of_favorites_books() == ['Найди время', 'Справочник Python',
                                                                      'Победи прокрастинацию']
    def test_delete_book_from_favorites_delete_one_book_negative(self, favorites_collection):
        favorites_collection.delete_book_from_favorites('Найди время')
        assert 'Найди время' not in favorites_collection.get_list_of_favorites_books()
