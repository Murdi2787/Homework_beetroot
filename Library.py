from datetime import datetime, timedelta
from uuid import uuid4

class Persona:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Book:
    def __init__(self, name, author, file_path):
        self.name = name
        self.author = author
        self.file_path = file_path
        self.id = uuid4()

    @property
    def counter_lines(self):
        with open(self.file_path) as book:
            lines_in_book = len(book.readlines())
        return lines_in_book

petia =  Persona('Petr', 'Petrov')
myrka = Book('Myra', petia, '/path')


class PersonCard:
    def __init__(self, person, id):
        self.date_of_registration = datetime.now()
        self.person = person
        self.id = id
        self.taken_books = []

    def taken_book(self, order):
        self.taken_books.append(order)


class Library:
    all_books = []
    person_cards = []

    def add_book(self, *args):
        self.all_books.extend(args)

    def is_person_registered(self, person):
        for person_card in Library.person_cards:
            if person == person_card.person:
                return True
        return False

    def register_person(self, person):
        """
        создать карточку для пользователей и добавить ее в список уже существующих
        :return: user for add
        """
        new_person_card = PersonCard(person, id=uuid4())
        self.person_cards.append(new_person_card)

    def get_person_card(self, person):
        # вернуть карточку пользователя
        for card in self.person_cards:
            if person == card.person:
                return card
            else:
                raise Exception('Not exists')

    def get_book(self, person, book):
        '''
        выдать книгу определенному пользователю если она свободна
        если пользователь зарегестрирован в библиотеке
        проверить зарегестрирован ли пользователь в библиотеке
        если нет - зарегестрировать
        :param person:
        :param book:
        :return:
        '''

        if not self.is_person_registered(person):
            self.register_person(person)
        person_cards = self.get_person_card(person)

        if book in self.all_books:
            order = {
                'book_name': book,
                'when_was_taken': datetime.now(),
                'expiration_date': datetime.now() + timedelta(days=30)
            }

            person_cards.taken_books(order)

    def book_count(self):
        '''
        вернуть количество всех книг
        :return:
        '''
        return len(self.all_books)

    def show_all_books_info(self):
        '''
        вывести на экран информацию о пользователе и книгах которые у него на руках
        :return:
        '''
        pass