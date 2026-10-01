from cmput274 import *

def countOne(char, countSoFar):
    if char == "1":
        return 1 + countSoFar
    return countSoFar

def parity(bs):
    count = foldr(bs, countOne, 0)
    return count % 2 == 0

print(parity("110001101011"))

# from cmput274 import *

# def countOne(char, asf):
#     if char == "1":
#         return not asf
#     return asf

# def parity(bs):
#     return foldr(bs, countOne, True)

# print(parity("11000110011"))
