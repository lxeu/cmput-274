from cmput274 import *

def composeMap(fns, vals):
    return foldr(fns, lambda fn, val: map(fn, val), vals)

print(composeMap(LL(lambda x: x*2, lambda x:x+1, lambda x: x*3), LL(1,2,3)))