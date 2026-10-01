from cmput274 import *

def add3(x):
    return x + 3

def map(f, l):
    if isEmpty(l):
        return l
    current = first(l)
    ror = map(f, rest(l))
    return cons(f(current), ror)

print(map(add3, LL(1,2,3)))