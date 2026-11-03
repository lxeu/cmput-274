from cmput274 import *

def findLeaves2(t):
    if t[1] == ():
        return LL(t[0])
    concat = lambda l1, l2: foldr(l1, cons, l2)
    answer = foldr(t[1], lambda c, ror: concat(findLeaves2(c), ror), empty())
    return answer

print(findLeaves2((10, ((22, ((4, ()), (9, ()))), (15, ((-12, ()),))))))