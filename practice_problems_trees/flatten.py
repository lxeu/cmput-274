from cmput274 import *

def concat(a, b):
    lambda a, b: foldr(a, cons, b)

def flatten1(bt):
    '''
    flatten produces a Llist of all the values in the binary tree bt

    bt      - BinaryTree of X
    returns - LList of X
    '''
    if bt == ():
        return empty()
    val = bt[0]
    lTree = bt[1]
    rTree = bt[2]
    lRor = flatten1(lTree)
    rRor = flatten1(rTree)
    concat(val, concat(lRor, rRor))