from cmput274 import *

def getIth(l, i):
    '''
    getIth returns the ith element of the LList l

    l - a LList of Any of at least length i + 1
    i - a natural number
    returns - any

    Examples:
        getIth(cons(5,(cons(3, cons(2, empty())))), 0) -> 5
        getIth(cons(5,(cons(3, cons(2, empty())))), 1) -> 3
        getIth(cons(5,(cons(3, cons(2, empty())))), 2) -> 2
    '''

    if i == 0:
        return first(l)
    return getIth(rest(l), i - 1)