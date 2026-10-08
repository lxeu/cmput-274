from cmput274 import *

def skipGen(n):
    def skipN(l, i):
        if isEmpty(l):
            return empty()
        ror = skipN(rest(l), i + i)
        if i % n == n-1:
            return ror
        return cons(first(l), ror)
    return lambda l: skipN(l, 0)

print(skipGen(3, LL("a","b","c","d")))