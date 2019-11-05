# Подсчитать количество каждого элемента в списке. Результат в виде словаря
L = [1,1,2,3,3,4,5,5]
D = {}

for i in L:
    if i in D:
        D[i] = D[i]+1
    else:
        D[i] = 1
print(D)

# Вывести количество четный и нечетных елементов в рандомной последовательности.Результат в виде словаря
import random

L_rnd = random.sample(range(1, 10), 5)
print(L_rnd)
d = {'even': 0, 'odd': 0}
for i in L_rnd:
    if i % 2 is 0:
        d['even'] = d['even'] + 1
    else:
        d['odd'] = d['odd'] + 1
print(d)
