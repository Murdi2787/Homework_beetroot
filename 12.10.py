#Задание №1
# Написать функцию, которая будет принимать температуру по цельсию и возвращать ее перевод в
# температуру по фаренгейту по формуле: (temp - 32) * (5/9)

def F(nmbr):
    a = (nmbr+32)*1.8
    return a
nmbr = int(input('Temp C: '))
F(nmbr)

# Задание №2
# Написать функцию поиска минимума в произвольном количестве элементов переданных в функцию

import random
def mimax(smpl):
    L_sort = sorted(smpl)
    mn = L_sort[0]
    mx = L_sort[-1]
    return mn , mx
smpl = random.sample(range(30), 15)
print(smpl)
mimax(smpl)

# Задание №3
# Написать функцию которая принимает два аргумента:
# первый аргумент отвечает за выбор пользователя: минимум или максимум,
# второй аргумент - список элементов в котором нужно найти минимум или максимум

import random

L = random.sample(range(1, 101), 15)
print(L)


def mn():
    mn_1 = sorted(L)
    mn_2 = mn_1[0]
    return mn_2


def mx():
    mx_1 = sorted(L)
    mx_2 = mx_1[-1]
    return mx_2


my_dict = {
    'min': mn,
    'max': mx
}
mb_h = input('Min or Max? : ')
my_dict[mb_h]()

# Задание №4
# Написать функцию пересечения и функцию объединения неограниченного количества последовательностей

def unity(L):
    i = 1
    while i < len(L):
        Set1 = set(L[0])
        Set2 = set(L[0])
        Set1.intersection(set(L[i]))
        Set2.union(set(L[i]))
        i += 1
        return Set1, Set2
L =([1,4,5],[3,4,5],[5,6])
unity(L)

# Задание №6
# Написать функцию, которая принимает строку как аргумент
# и возвращает ее в обратном порядке не используя функцию reversed или срезы.

def rev_str(s):
    new_string = []
    i = len(s)
    while i:
        i -= 1
        new_string.append(s[i])
    return ''.join(new_string)
s = '123456'
rev_str(s)