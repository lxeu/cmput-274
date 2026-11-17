from cmput274 import *

def llistSUm(l):
    resSoFar = 0
    while not isEmpty(l):
        resSoFar = resSoFar + first(l)
        l = rest(l)
    return resSoFar

print(llistSUm(LL(1,2,4,1,2)))