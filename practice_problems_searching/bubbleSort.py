from cmput274 import *

def bubble(l):
    if len(l) <= 1:
        return l
    if first(l) > first(rest(l)):
        newFirst = first(rest(l))
        newRest = cons(first(l), rest(rest(l)))
        return cons(newFirst, bubble(newRest))
    return cons(first(l), bubble(rest(l)))

def bubbleSort(l):
    return foldr(l, lambda _, bl: bubble(bl), l)


print(bubbleSort(LL(1,4,2,9,-1)))