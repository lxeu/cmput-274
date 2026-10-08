from cmput274 import *

def skipGen(n):
    def skipN(l, step):
        if isEmpty(l):
            return empty()
        if step == n:
            return skipN(rest(l), 1)
        return cons(first(l), skipN(rest(l), step + 1))
    return lambda l: skipN(l, 1)