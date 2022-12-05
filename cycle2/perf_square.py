import math


def even_check(n):
    for i in str(n):
        if(int(n)%2!=0):
            return False
    return True

def check_p_square(n):
    if(isInt(math.sqrt(n))==True):
        return True
    else:
        return False

def isInt(x):
    if x%1 == 0:
        return True
    else:
        return False

def gen_list():
    a=int(input("enter a 4 digit starting value "))
    b=int(input("enter a 4 digit ending value "))
    l=[]
    for i in range(a,b):
        if (even_check(i)==True and check_p_square(i)==True):
            l.append(i)
    print(l)

gen_list()
