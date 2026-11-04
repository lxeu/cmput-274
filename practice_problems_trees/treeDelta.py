from cmput274 import *

def PreTD(bt):
    if bt == ():
        return empty()
    CurNode = bt[0]
    ltree = bt[1]
    rtree = bt[2]
    return CurNode - PreTD(ltree) - PreTD(rtree)

def InTD(bt):
    if bt == ():
        return empty()
    CurNode = bt[0]
    ltree = bt[1]
    rtree = bt[2]
    return InTD(ltree) - CurNode - InTD(rtree)

def postTD(bt):
    if bt == ():
        return empty()
    CurNode = bt[0]
    ltree = bt[1]
    rtree = bt[2]
    return postTD(ltree) - postTD(rtree) - CurNode