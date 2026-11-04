from cmput274 import *

def upper(c):
    if 97 < ord(c) < 122:
        c = chr(ord(c) - 32)
    return c

def makeUpper(s):
    return foldr(s, lambda c, acc: upper(c) + acc, "")

print(makeUpper("hello"))