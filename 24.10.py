# Задание №1
# Создать класс Person с атрибутами имя, фамилия, дата рождения. Добавить методы get_age, displayInfo.
from datetime import date


class Person:
    def __init__(self, name, lastname, birth_date):
        self.name = name
        self.lname = lastname
        self.b_date = birth_date
        self.age = Person.get_age(birth_date)

    @classmethod
    def get_age(cls, b_date):
        d_today = date.today()
        b_dat = int(b_date[0:4])
        age = d_today.year - b_dat
        return age

    def displayInfo(self):
        return (f'Пивет, если ты вдруг не знал, тебя зовут {self.name} {self.lname} и тебе к сожалению {self.age}')


a = Person('Aleksandr', 'Shavlak', '1990-08-25')
print(a.displayInfo())

# Задание №2
# Создать класс Ученик наследуя от Person. Создать экземпляры этого класса и добавить в ClassRoom.
# Переопределить метод displayInfo.


class Student(Person):
    frst_st = Student('Ivan')





# Задание №3
# Создать класс Учитель наследуя от Person. Переопределить метод displayInfo.
# Создать экземпляры этого класса и добавить в Школу еще одну переменную класса - словарь,
# где ключ это название предмета а значение - список учителей, работающих в данной школе.
