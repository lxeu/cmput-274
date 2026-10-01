from cmput274 import *

def isNegative(x, base):
    return x < 0

def isShort(s, base):
    return len(s) < 6

def filter(func, s):
    foldr(s, func, empty())

print(filter(isNegative, LL(-10,0,10,-2)))