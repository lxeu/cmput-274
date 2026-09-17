from cmput274 import *

def append(elem, l):
    '''
    append produces a new llist that is the result of appending elem onto l
    
    elem    - Any
    l       - a llist of any
    returns - a llist of any

    Examples:
        append(5, cons(0, cons(1, empty()))) -> <0,1,5>
    '''
    if isEmpty(l):
        return cons(elem, empty())
    ror = append(elem, rest(l))
    return cons(first(l), ror)

def ascendList(n):
    '''
    ascendList produces the LList from 0...n in ascending order

    n       - a natural number
    returns - a LList of natural numbers

    Examples:
        ascendList(3) -> (0, 1, 2, 3)
        ascendList(0) -> (0)
    '''
    assert n >= 0

    if n == 0:
        return cons(0, empty())
    ror = ascendList(n - 1)
    return append(n, ror)
