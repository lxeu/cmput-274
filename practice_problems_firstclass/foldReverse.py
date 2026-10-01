from cmput274 import *

def append(elem, alreadyReversed):
    return foldr(alreadyReversed, cons, cons(elem, empty()))
    
def foldReverse(l):
    return foldr(l, append, empty())

print(foldReverse(LL(1,2,3,)))