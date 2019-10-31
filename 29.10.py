# Задание №1
# Объявить словарь, в котором ключом будет permission (admin, loggedin, unknown etc) а значениями будут ссылки на функции,
# которые отображают доступный функционал данного пользователя. Объявить класс Person, у которого есть атрибут (свойство) permission.
# Создать экземпляры класса Person с различными permission и отобразить доступный функционал по словарю.


def admin():
    print('You logged as admin')


def loggedIn():
    print('You logged successFull')


def unknown_etc():
    print('You logged as unknown')


class Person:
    def __init__(self, permiss):
        self.permission = permiss


a = input('Who are u?: ')
p1 = Person(a)

dict_ex = {
    'p1': admin,
    'p2': loggedIn,
    'p3': unknown_etc,
}

b = dict_ex[p1.permission]()
print(b)


# Задание №2
# Пользователь вводить возраст. Написать функцию, если возраст больше 16 то объявить внутри функции функцию show_available_content,
# которая будет показывать доступные фильмы, вызвать show_available_content которая показывает скрытые данные.
# Если возраст меньше 16, вернуть сообщение что пользователю информация недоступна.


def access(age):
    if c < 16:
        def access_d():
            print('Earth is round!')

        access_d()
    else:
        print('Shh, Earth is flat!')


c = int(input('How old are you?: '))
access(c)

# Задание №3
# Объявить две функции: 1 - принимает список чисел как аргумент и сортирует его по убыванию,
# 2 - принимает список чисел как аргумент и сортирует его по возрастанию.
# Отсортировать список чисел по убыванию или по возрастанию, в зависимости от того что выберет пользователь.
# Реализовать с помощью функции, которая передается как аргумент
import random


def increase(l):
    L.sort()
    print(L)


def decrease(l):
    L.sort(reverse=True)
    print(L)


def list_sort(l):
    if inp == '+':
        increase(l)

    else:
        decrease(l)


L = random.sample(range(50), 25)
inp = input('Введите действие + или - : ')
list_sort(L)

# Задание №4
# Написать функцию таймер, которая будет принимать функцию как аргумент и вычислять время выполнения этой функции.

import timeit


def list_s(arg1, arg2 ):
    arg1 = [1, [12, 13], 'qweqeq', 3]
    arg2 = ['213123', 2, [5, 6, 7, 7], 11]
    return list_s(arg1, arg2)


def speed(arg3):
    tmr = timeit.Timer(arg3).repeat(1)
    return tmr


x = speed(list_s)
print(x)

# Задание №5
# Создать функцию create_adder, внутри которой будет объявлена функция add_elems(list_of_elems) и будет возвращаться эта функция.
# Вызвать функцию create_adder и сложить несколько рандомных чисел (произвольное количество) с помощью add_elems.


def create_adder(e):
    sum_1 = sum(elem_lst)
    print(sum_1)

    def add_elems(elem):
        return add_elems(elem)


elem_lst = random.sample(range(1, 50), 3)
print(elem_lst)
create_adder(elem_lst)


# Задание №6
# Написать функцию create_counter, в которой будет объявлена переменная counter и функция generate_password,
# вернуть функцию generate_password. Функция generate_password должна генерировать пароль и увеличивать counter на 1.
# Вызвать функцию для генерации пароля несколько раз и посмотреть как изменится счетчик.


# class Counter:
#     def __init__(self, fnc):
#         self.fnc= fnc
#         self.count = count
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.fnc(*args, **kwargs)

def create_counter(e):
    def gen_pswrd(e):
        for n in range(nmbr):
            pswrd = ''
            for i in range(ln):
                pswrd += random.choice(chars)
                uppers = [l for l in pswrd if l.isupper]
            print(pswrd)

    return gen_pswrd(e)


nmbr = int(input('Выберите кол-во паролей: '))
ln = int(input('Выберите длинну пароля: '))
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
create_counter(chars)

# Задание №7
# Изменить пример make_averager, так чтоб функция хранила результат предыдущей суммы и количество елементов,
# тогда зная эти два числа можно вычислить новое среднее значение. (используйте nonlocal)


# Задание №8
# С помощью функции map преобразовать случайного список целых чисел в новый список где каждый елеменет будет умножен на 2


# Задание №9
# С помощью функции filter выбрать только положительные целочисленные елементы случайного списка


# Задание №10
# С помощью функции reduce умножить все числа в списке


# Задание №11
# С помощью функции map преобразовать список строк в список чисел: [‘1’, ‘2’, ‘3’, ‘4’] => [1, 2, 3, 4]


# Задание №12
# С помощью функции map преобразовать список с милями в список с километрами, где 1 mile = 1.6 km
