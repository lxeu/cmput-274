from cmput274 import *

def multiTable(row, col):
    if row == 0:
        return empty()
    return cons(buildList(lambda x: row * (x + 1), col), multiTable(row-1, col))



print(multiTable(3, 4))


'''1 2 3 4
2 4 6 8
3 6 9 12'''

