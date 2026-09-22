from cmput274 import *

def append(elem, l):
    if isEmpty(l):
        return cons(elem, empty())
    return cons(first(l), append(elem, rest(l)))

def reverse(l):
    '''
    reverse produces the reversed version of a LList l

    l       - LList of Any
    returns - LList of Any

    Examples:
        reverse(cons(1, (cons(2, cons(3, empty()))))) -> <3, 2, 1>
    '''

    if isEmpty(l):
        return empty()
    ror = reverse(rest(l))
    return append(first(l), ror)

print(reverse(cons(3, cons(2, cons(1, empty())))))