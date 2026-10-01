from cmput274 import *

def isNegative(x):
    return x < 0

def isShort(s):
    return len(s) < 6

def filter(func, s):
    '''
    filter produces the LList that is the result of filtering l with the given predicate

    func   - (X -> bool)
    l      - LList of x
    return - LList of X

    Examples:
        def isNegative(x):
            return x < 0
        filter(isNegative, LL(-10, 5, 0, -2)) -> LL(-10, -2)
    '''
    if isEmpty(s):
        return s
    current = first(s)
    ror = filter(func, rest(s))
    if func(current):
        return ror
    return cons(current, ror)

print(filter(isNegative, LL(-10,0,10,-2)))
print(filter(isShort, LL("test", "asldkfjasld;kfj", "sho", "2342342", ";asldf", "e")))