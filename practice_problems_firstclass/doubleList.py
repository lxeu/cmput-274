from cmput274 import *

def doubleList(l):
    '''
    doubleList returns a new LList that is the result of multiplying every number in l by 2

    l - a LList of Num
    returns - a LList of Num

    Examples
        doubleList(<1, 2, 3>) -> <2, 4, 6>
    '''
    if isEmpty(l):
        return empty()

    ror = doubleList(rest(l))
    return cons(2 * first(l), ror)

print(doubleList(cons(1, cons(2, cons(3, empty())))))