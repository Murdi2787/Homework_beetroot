# 1. Создать классы с методами __str__, __repr__ и собственными методами классов, построить правильную иерархию классов.
# Перечень классов:
# Студент, Преподаватель Персона, Зав. кафедрой.


class Person:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age


class VicePrincipal(Person):
    def __init__(self, name, lname, qualification):
        super().__init__(name, lname, age)
        self.squalification = qualification


class Teacher(Person):
    def __init__(self, name='Ivan', lname='Ivanov', age='23', subject='Math'):
        super().__init__(name, lname, age)
        self.subject = subject

    def __str__(self):
        return f'Teachers name {self.name} {self.lname}'


a = Teacher()
print(a)


class Student(Person):
    def __init__(self, name, lname, age, studing):
        super().__init__(name, lname, age)
        self.studing = studing

# Автомобиль, Поезд, Транспортное средство, Мотоцикл


class Transport:
    def __init__(self, cost, speed):
        self.cost = cost
        self.speed = speed


class Car(Transport):
    def __init__(self, cost, speed, comfort):
        super(Car, self).__init__(cost, speed)
        self.comfort = comfort

    def __repr__(self):
        return f'{self.cost} {self.speed} {self.comfort}'


b = Car('11', '100', 'best')
print(b)

class Train(Transport):
    def __init__(self, cost, speed, safe):
        super().__init__(cost, speed)
        self.safe = safe


class Motorcycle(Transport):
    def __init__(self, cost, speed, not_safe):
        super().__init__(cost,speed)
        self.not_safe = not_safe




# Республика, Монархия, Королевство, государство.


# class State:
#     def __init__(self, gaverment, money, ):


# Деталь, Механизм, Изделие.
# Журнал, Книга, Печатное издание, Учебник
# Тест, Экзамен, Выпускной экзамен, Испытания.
# Служащий, Персона, Рабочий, Инженер
# Игрушка, Продукт(Еда), товар, Молочный продукт. (множественное наслед)
