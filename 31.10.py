# Задание №1
# Написать декоратор, который будет валидировать входные данные (параметры декорируемой функции, например разрешить только числа).
# Применить декоратор к функции, которая принимает несколько чисел.
# Вызвать декорируемую функцию. (И реализовать как класс)


def validator(f):
    def wrapper(e):
        if isinstance(exp, int):
            exp.sort()

    return wrapper


@validator
def ex(e):
    print()


exp = list(map(int, input('Введите значения через запятую: ').split(',')))

# Задание №2
# Объявить класс Person с переменной класса _secret_data и переменной инстанса is_admin.
# Написать декоратор, который проверяет есть ли у пользователя доступ к данной функции(if is_admin).
# Применить декоратор к методу класса Person.get_secret_data (getter для _secret_data).
# Создать несколько объектов Person с разными is_admin значениями и вызвать у каждого метод get_secret_data.


# Задание №3
# Написать функцию-декоратор и класс таймер и декорировать им несколько функций с вычислениями.
