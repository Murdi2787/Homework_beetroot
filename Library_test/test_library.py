import unittest
from Library import *
from unittest.mock import patch, Mock


class TestPerson(unittest.TestCase):

    def test_creat_person(self):
        vasia = Persona('Vasia', 'Petrov')
        self.assertEqual(vasia.name, 'Vasia')
        self.assertEqual(vasia.lastname, 'Petrov')

    def test_magic_str(self):
        vasia = Persona('Vasia', 'Petrov')
        self.assertEqual(str(vasia),'Vasia Petrov')


class TestLibrary(unittest.TestCase):
        def setUp(self):
            self.library = Library()
            self.person = Persona('Vasia', 'Petrov')
            self.myrka = Book('Myra', petia, '/path')

        @patch('Library_test.Library.is_person_registered')
        def test_get_book(self, mock_ipr):
            mock_ipr.return_value = False
            self.library.get_book(self.person, self.myrka)
            mock_ipr.assert_called()

        def test_add_book(self):
            pass

        def is_person_registered(self):
            # self.library.person_cards.append(PersonCard(self.person, id=uuid4()))
            self.library.person_cards.append(Mock(person=self.person))
            is_reg = self.library.is_person_registered(self.person)
            self.assertTrue(is_reg)
            self.library.person_cards.clear()

        def is_person_notregistered(self):
            not_reg = self.library.is_person_registered(self.person)
            self.assertFalse(not_reg)

        @patch('Library.uuid.uuid4')
        def test_register_person(self, mock_uuid):
            mock_uuid.return_value = 123456
            self.library.register_person(self.person)
            self.assertEqual(self.library.person_cards[0].id, 123456)
            self.library.person_cards.clear()

        def test_get_person_card(self):
            self.library.person_cards.append(Mock(person=self.person))
            card = self.library.get_person_card(person=self.person)
            self.assertEqual(self.person, card.person)

# class TestBook(unittest.TestCase):
#     book = Book('Storm', 'Lenon', '/sum_path')


if __name__ == 'main':
    unittest.main()
