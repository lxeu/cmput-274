from cmput274 import *

def fold(s, combine, base, getRest, getFirst, checkBase):
    if checkBase(s):
        return base
    return combine(getFirst(s), fold(getRest(s), combine, base, getRest, getFirst, checkBase))

def doubleAndCons(elem, lon):
    return cons(2*elem, lon)

def sumUp(elem, sor):
    return elem + sor

def product(elem, sor):
    return elem*sor

def censorA(s, ror):
    if s == "A" or s == "a":
        return "*" + ror
    return s + ror

def restOfString(s):
    return s[1:]

def firstOfString(s):
    return s[0]

def emptyString(s):
    return s == ""

print(fold("hello this is a string full of characters we don't know what they are", censorA, "", restOfString, firstOfString, emptyString))