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
def list_low(L):

def list_upper(L):