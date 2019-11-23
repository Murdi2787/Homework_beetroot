# Задание №1
# Создать класс Карта с свойствами масть и значение.
# Создать класс Колода, которая будет итератором для экземпляров класса Карт.
from collections import Iterator


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"


class CardIterator(Iterator):

    def __init__(self, collection, position):
        self._collection = collection
        self._position = position

    def __next__(self):
        if self._position + 1 >= len(self._collection):
            raise StopIteration
        self._position += 1
        return self._collection[self._position]


class Deck:
    def __init__(self, collection, position):
        self._collection = collection
        self._position = position

    def __iter__(self):
        return CardIterator(self._collection, self._position)


deck_coll = [Card('2', "diamonds"), Card('3', 'Diamonds'), '4', '5', '6', '7', '8', '9', '10', 'jack', 'dame', 'king', 'ace']
agr = Deck(deck_coll, -1)

for i in agr:
    print(i)
