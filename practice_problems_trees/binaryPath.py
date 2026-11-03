from cmput274 import *

def findPath(bt, v):
    '''
    findPath finds the series of directions from the tree rooted at bt to the value v within that tree

    bt - a Binary Tree
    v - x
    returns - A LList of anyof("left", "right")

    Examples:
        findPath((5,
                    (3,
                        (),
                        (2, (), ())
                    ),
                    (7,
                        (8, (), ()),
                        (9, (), ())
                    )
                  ), 2) -> LL("left", "right")
    '''
    if bt == ():
        return None
    if bt[0] == v:
        return empty()
    if bt[1] == () and bt[2] == ():
        return None
    lChild = bt[1]
    rChild = bt[2]
    leftRor = findPath(lChild, v)
    rightRor = findPath(rChild, v)
    if leftRor != None:
        return cons("left", leftRor)
    if rightRor != None:
        return cons("right", rightRor)
    return None

print(findPath((5,
                    (3,
                        (),
                        (2, (), ())
                    ),
                    (7,
                        (8, (), ()),
                        (9, (), ())
                    )
                  ), 2), 2)