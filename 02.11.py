# Задание №1
# Написать класс Distance с приватным атрибутом _distance (в метрах).
# Объявить для этого атрибута setter, getter, deleter, который будет показывать дистанцию в метрах.
# Создать вычисляемый атрибут для перевода дистанции в шаги (in_feet, 1м = 0.67 шагов)


class Distance:
    def __init__(self, distance=5):
        self.__distance = distance

    def getdistance(self):
        a = self.__distance / 0.67
        return round((a), 2)

    def setdistance(self, distance):
        self.__distance = distance

    def deldistance(self):
        del self.__distance

    distance = property(getdistance, setdistance, deldistance, 'Distance Docs')


obj = Distance()
print(obj.distance)
obj.setdistance(30)  # obj.distance = 30
print(obj.distance)
print(obj._Distance__distance)
print(Distance.distance.__doc__)


# Задание №2
# Написать класс Wallet с приватными атрибутами класса: dollars, cents.
# Написать setter, deleter, getter для cents и вычисляемый атрибут для общего количества денег.


class Wallet:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @property
    def value(self):
        return self.dollars + (self.cents / 100)

    @value.setter
    def value(self, total):
        # self.dollars = total // 100  в случае одного значения типа float
        # self.cents = total % 100
        self.dollars = total[0]
        self.cents = total[1]

    @value.deleter
    def value(self):
        del self.dollars
        del self.cents
        print('Del success')


obj_total = Wallet(25, 150) #class ( dollar, cents)
print(obj_total.value) # getter

obj_total.value = (10, 5) #setter
print(obj_total.value)

# Задание №3
# Создать класс Celcius с приватным атрибутом _temperature. Объявить для этого атрибута setter, getter, deleter.
# Создать вычисляемый атрибут для перевода по фаренгейту.

class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def far(self):
        return (self._temperature + 32) * 1.8

    @far.setter
    def far(self, temp):
        self._temperature = temp

    @far.deleter
    def far(self):
        del self._temperature


obj_temp = Celsius(32)
print(obj_temp.far)
obj_temp.far = 55
print(obj_temp.far)

# Задание №4
# Создать класс USDCurrencyConverter, с приватным атрибутом current_value (в USD) и вычисляемыми
# атрибутами для перевода из USD в другие валюты, например EUR, UAH.


class USDcorrencyConverter:

    def __init__(self, value, currency):
        self._value = value
        self.currency = currency

    @property
    def convert(self):
        if self.currency == 'USD':
            return self._value * 24.95
        else:
            return self._value * 27.85

    @convert.setter
    def convert(self, obj_curr):
        self.currency = obj_curr[1]
        self._value = obj_curr[0]

    @convert.deleter
    def convert(self):
        del self._value
        del self.currency


obj_curr = USDcorrencyConverter(200, 'USD')
obj_curr.convert = 350, 'EUR'
print(obj_curr.convert)

#---------------------------------------------------------------------------------------------------

curr_inp = input('Введите валюту: ')
val_inp = int(input('Введите сумму: '))


class UAHcurrencyConverter:

    def __init__(self, value, currency):
        self._value = value
        self.currency = currency

    @property
    def convert(self):
        find_curr = dict_curr[curr_inp]
        return find_curr * val_inp

    @convert.setter
    def convert(self, currency):
        self.currency = curr_inp
        self._value = val_inp

    @convert.deleter
    def convert(self):
        del self._value
        del self.currency


dict_curr = {
    'USD': 24.72, 'EUR': 27.46, 'PLN': 6.44, 'RUB': 0.39,
    'GBP': 31.89, 'CHF': 24.94, 'AUD': 17.08, 'HUF': 0.08,
    'DKK': 3.68, 'CAD': 18.83, 'NOK': 2.71, 'CZK': 1.08,
    'SEK': 2.57, 'JPY': 0.23,
}
obj_curr = UAHcurrencyConverter(val_inp, curr_inp)
print(obj_curr.convert)


# Задание №5
# Создать класс Карта с атрибутами значение и масть, перегрузить методы __lt__, __gt__, __eq__ для сравнения карт

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.suit > other.suit

    def __eq__(self, other):
        return self is other
