from cmput274 import *

def flatten(sl):
    if isEmpty(sl):
        return empty()
    if type(first(sl)) != LList:
        return cons(first(sl), flatten(rest(sl)))
    return foldr(flatten(first(sl)), cons, flatten(rest(sl)))

print(flatten(LL(1,2,3,4, LL(1, LL(3,3)))))