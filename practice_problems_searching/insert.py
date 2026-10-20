from cmput274 import*

def insert(elem, sl):
    '''
    insert produces a new list sorted in non-decreasing order, the result of inserting elem into sl

    elem    - X
    sl      - LList of X, sorted in non-decreasing order
    returns - LList of X

    Example:
        insert(5, LL(-1, 4, 10, 20)) -> LL(-1, 4, 5, 10, 20)
    '''
    if isEmpty(sl):
        return cons(elem, empty())
    cur = first(sl)
    if elem <= cur:
        return cons(elem, sl)
    return cons(cur, insert(elem, rest(sl)))