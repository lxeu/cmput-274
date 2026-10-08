from cmput274 import *

def isOrdered(t, cmp):
    '''
    isOrdered returns true if the tuple t is ordered with respect to the cmp fn. That is, every pair of values in t t[i] and t[i + 1] then cmp(t[i], t[i + 1]) -> True

    t       - a Tuple of X
    cmp     - (X X -> bool)
    returns - bool

    Examples:
        isOrdered((1, 5, 10, 12), lambda x, y: x <= y) -> True
        isOrdered((10, 8, 4, 2), lambda x, y >= y) -> True
        isOrdered((1, 5, 10, 12), lambda x, y: x >= y) -> False
    '''
    def tupleHelper(i):
        if i >= len(t) - 1:
            return True
        return cmp(t[i], t[i] + 1) and tupleHelper(i + 1)
    return tupleHelper(0)

def isSorted(t):
    return isOrdered(t, lambda x, y: x <= y) or isOrdered(t, lambda x, y: x >= y)

print(isSorted((1,3,5,3456,345324,)))