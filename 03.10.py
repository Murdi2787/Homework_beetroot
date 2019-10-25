#Вывести количество четный и нечетных елементов в рандомной последовательности.

import random
r_list = random.sample(range(20),10)
print(r_list)
count1 = 0
count2 = 0
for i in r_list:
    if i % 2 == 0:
        print('Odd ', i)
        count1 +=1
    else:
        print('Even ', i)
        count2 +=1
print(count1, count2)