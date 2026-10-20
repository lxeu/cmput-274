from cmput274 import *

def merge(sl1, sl2):
    '''
    merge takes two LLists ssorted in non-decreasing order and produces the sorted result of combining both LLists

    sl1     - Sorted Llist of X
    sl2     - Sorted LList of X
    returns - Sorted LList of X

    Examples:
        merge(LL(1, 6, 9), LL(7, 10, 12)) -> LL(1, 6, 7, 9, 10, 12)
    '''

    if isEmpty(sl1):
        return sl2

    if isEmpty(sl2):
        return sl1
    if first(sl1) < first(sl2):
        return cons(first(sl1), merge(rest(sl1), sl2))
    return cons(first(sl2), merge(sl1, rest(sl2)))