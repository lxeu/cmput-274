from cmput274 import *

def slice(l, start, end):
    '''
    slice returns the subllist of a llist of the range [start, end]

    l - a LList of Any
    start - an integer < length of l
    end - an integer <= length of l
    returns - a LList of Any

    Examples:
        slice(cons(5, cons(4, cons(3, cons(2, cons(1, cons(-1, empty())))))), 1, 3) -> cons(4, cons(3), empty())
    '''
    if start != 0:
        return slice(rest(l), start - 1, end - 1)
    if end <= start:
        return empty()
    return cons(first(l), slice(rest(l), 0, end -1))