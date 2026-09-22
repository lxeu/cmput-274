from cmput274 import *

def descendList(n):
    '''
    descendList produces the LList that contains the natural numbers from n to zero in descending order

    n - a natural number
    returns - a LList of natural numbers

    Examples:
        descendList(5) -> (5, 4, 3, 2, 1, 0)
        descendList(2) -> (2, 1, 0)
        descendList(0) -> (0)
    '''
    assert n >= 0

    if n == 0:
        return cons(0, empty())
    return cons(n, descendList(n - 1))

print(descendList(5))