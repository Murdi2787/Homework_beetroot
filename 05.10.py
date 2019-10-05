# Lesson 6 Задание №1
# Посчитать количество 9 в списке
List_ex = [1, 2, 9, 4, 9, 4, 9]
i = 0
a = 0
while i < len(List_ex):
    if List_ex[i] is 9:
        a += 1
    i += 1

print(a)
----------------------------------------------------
List_ex = [1,2,9,4,9,4,9]
count = 0
for i in List_ex:
    if i is 9:
        count += 1
print(count)

#Lesson 6 Задание №2
#Вывести количество четный и нечетных елементов в рандомной последовательности.

import random
r_list = random.sample(range(20),10)
print(r_list)
i = 0
a = 0
b = 0
while i < len(r_list):
    if r_list[i] % 2:
        a += 1
    else:
        b += 1
    i += 1
print(a,b)
-----------------------------------------------
import random
r_list = random.sample(range(20),10)
print(r_list)
count1 = 0
count2 = 0
for i in r_list:
    if i % 2 == 0:
       # print('Odd ', i)
        count1 +=1
    else:
       # print('Even ', i)
        count2 +=1
print(count1, count2)

#Lesson 6 Задание №3
#Пользователь должен ввести последовательность чисел через пробел.Для каждого числа выведите слово YES (в отдельной строке),
#если это число ранее встречалось в последовательности или NO, если не встречалось.

a = input('Введите последовательность чисел через пробел: ')
s = set()
for n in a:
    if n in s:
        print('Yes')
    else:
        print('No')
        s.add(n)