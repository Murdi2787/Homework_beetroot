def L_fun(L):
    if len(L) > 4 and sum(L[:4]) is 9:
        retutn True
    else:
        return False
L = list(map(int,input('Введите список: ').split( )))
L_fun(L)
