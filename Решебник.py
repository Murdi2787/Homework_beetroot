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