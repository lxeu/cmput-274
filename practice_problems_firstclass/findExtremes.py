from cmput274 import *

def selectExtreme(elem, pair):
    if elem < first(pair):
        return cons(elem, rest(pair))
    if elem > first(rest(pair)):
        return LL(first(pair), elem)
    return pair


def findExtremes(l):
    '''
    findExtremes produces a pair of the form (vi, vj) where vi is the minimal element in l and vj is the maximal element in l
    '''
    return foldl(l, selectExtreme, LL(first(l), first(l)))

print(findExtremes(LL(7,10, -41 ,2123,12,-1)))