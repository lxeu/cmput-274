from cmput274 import *

def sumOfList(n):
    '''
    sumOfList returns the sum of a list of numbers

    n       - a LList
    returns - a Num

    Examples:
        sumOfList(cons1())
    '''
    if isEmpty(n):
        return 0
    curVal = first(n)
    return curVal + sumOfList(rest(n))

def countOfList(n):
    '''
    countOfList returns the number of elements in n

    l       - A LList of Any
    returns - A natural number

    Examples:
        countOfList(cons(1, cons(2, empty()))) -> 2
        countOfList(empty()) -> 0
    '''
    if isEmpty(n):
        return 0
    return 1 + countOfList(rest(l))
    
def mean(n):
    '''
    mean takes a LList of numbers and returns the mean of that list of numbers.

    n       - A non empty LList
    returns - A float

    Examples:
        mean(cons(3.0, cons(4.0, cons(5.0, empty())))) -> 4.0
    '''
    return sumOfList(n)/countOfList(n)