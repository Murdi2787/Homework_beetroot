# Задание №1
# Создать файл nums.txt с рандомными цифрами
# и нужно среди них найти самую большую цифру и написать его уже в новый max_num.txt файл

import random
with open('nums.txt', 'w') as op_f:
    rnd_s = random.sample(range(1,50), 5)
    rnd_s_str = ','.join(map(str, rnd_s))
    op_f.write(rnd_s_str)
with open('nums.txt' , 'r') as op_f:
    r_obj = op_f.read()
    r_obj1 = map(int, r_obj.split(','))
    r_obj2 = max(r_obj1)
    print(r_obj)
    print(r_obj2)
with open('max_nums.txt' , 'w') as max_f:
    max_str = str(r_obj2)
    max_n = max_f.write(max_str)

# Задание №2
# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел.
# Напишите программу, которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.

import random
with open('nums1.txt', 'w') as op_f:
    rnd_s = random.sample(range(5),5)
    rnd_s_str = ','.join(map(str, rnd_s))
    op_f.write(rnd_s_str)
with open('nums1.txt') as num_s:
    sum_n = num_s.read()
    sum_n1 = map(int, sum_n.split(','))
    sum_n2 = sum(sum_n1)
    print(rnd_s)
    print(sum_n2)