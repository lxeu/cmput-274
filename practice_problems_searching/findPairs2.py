from cmput274 import *

def findPairs(t, target):
    def fpHelper(start, end):
        if start > end:
            return empty()
        if t[start] + t[end] == target:
            return cons(LL(t[start], t[end]), fpHelper(start + 1, end - 1))
        if t[start] + t[end] > target:
            return fpHelper(start, end - 1)
        if t[start] + t[end] < target:
            return fpHelper(start + 1, end)
    return fpHelper(0, len(t) - 1)

print(findPairs((-1,2,4,5,6,7,8,9,11), 10))