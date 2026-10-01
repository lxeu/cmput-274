from cmput274 import *

def add3(x, base):
    return cons(x + 3, base)

def double(x, base):
    return cons(x * 2, base)

def map(func, l):
    '''
    map maps the function func onto the LList l

    f       - (X -> Y)
    l       - LList of X
    returns - LList of Y

    Examples:
        def add3(n):
            return 3 + n
        map(add3, LL(1,2,3)) -> LL(4,5,6)
    '''
    return foldr(l, func, empty())

print(map(double, LL(1,23,3)))