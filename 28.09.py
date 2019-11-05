#Задание №1
def summ(a,b):
    c = a*b
    if c >= 10:
        print(c)
summ(5,6)

#Задание №2
a = input('Введите пароль: ')
def pswrd(a):
    if len(a) >= 10:
        print('Your password is strong')
    if len(a) < 10:
        print('Your password is not strong enough')
pswrd(a)

#Задание №3
summer = True
t1 = int(input('T: '))
def temp(t1, summer):
    if t1 >= 60 and t1 <= 90:
         print('True')
    elif summer is True and t1 >= 60 and t1 <= 100:
         print('True')
    else:
         print('False')
temp(t1, summer)

#Задание №1 Урок 4
import random
a = random.randint(1,100)
print(a)

#Задание №2 Урок 4
import random
a = [1,2,3,4,5,6]
random.shuffle(a)
b = random.choice(a)
print(b)

#Задание №3 Урок 4
import random
a = random.random()
print(a)

#Задание №4 Урок 4
import random
a = random.uniform(0,25)
print(a)
# Задание №5 Урок 4
import random

print('Enter Rock, Paper or Scissors: ')
user = str.title(input())
print(f'Your choice: {user}')
var = ['Rock', 'Scissors', 'Paper']
comp = random.choice(var)
print(f'Computer choice: {comp}')
if comp == 'Rock' and user == 'Scissors':
    print('AI wins!')

elif comp == 'Rock' and user == 'Paper':
    print('User wins!')

elif comp == 'Scissors' and user == 'Paper':
    print('AI wins!')

elif comp == 'Scissors' and user == 'Rock':
    print('User wins!')

elif comp == 'Paper' and user == 'Scissors':
    print('User wins!')

elif comp == 'Paper' and user == 'Rock':
    print('AI wins!')

else:
    print('Try again!')