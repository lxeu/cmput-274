# from cmput274 import *

# def sub(x, y):
#     return x - y

# print(foldr(LL(7, 10, 1, 22), sub, 0))

from cmput274 import *

def sub(x, y):
    return x - y

print(foldl(LL(7, 10, 1, 22), sub, 0))