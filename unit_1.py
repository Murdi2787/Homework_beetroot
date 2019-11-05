# Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97
# Сколько существует круговых простых чисел меньше миллиона?

# for nmbr in range(1, 10000):
#     for i in (2, nmbr):
#         if nmbr % i != 0:
#             print(nmbr)
        # with open('u nit_1.txt', 'w') as f:
        #     f.write(nmbr)
        # f.close()

import math
print(2)
for num in range(3,1000001,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        print(num)
# with open('u nit_1.txt', 'w') as f:
        #     f.write(num)
        # f.close()