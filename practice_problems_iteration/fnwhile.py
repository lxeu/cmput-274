from cmput274 import *

def fnwhile(p, f):
    def helper(x):
        if not p(x):
            return x
        return helper(f(x))
    return helper

def main():
    predicate = lambda p: not isEmpty(p[1])
    f = lambda p: (p[0] + first(p[1]), rest(p[1]))
    sumLList = fnwhile(predicate, f)