from cmput274 import *

def findPairs(t, target):
    '''
    Construct a LList of pairs of the values in t that sum to target
    '''
    def searchRest(current, val):
        if current >= len(t):
            return False
        if t[current] == val:
            return True
        return searchRest(current + 1, val)
    def searchCurrent(i):
        '''
        Finds all pairs of t that sum to target in t[i + 1:]
        '''
        if i>= len(t):
            return empty()
        toFind = target - t[i]
        if searchRest(i + 1, toFind):
            return cons(LL(t[i], toFind), searchCurrent(i + 1))
        return searchCurrent(i + 1)
    return searchCurrent(0)

print(findPairs((1,-2,32,4,2,1,4,1,2,4,3,4,8,9,0,-2,-1,-2,3), 4))