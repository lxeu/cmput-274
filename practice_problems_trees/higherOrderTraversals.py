from cmput274 import *

def concat(l1, l2, l3):
    return foldr(l1, cons( foldr(l2, cons, l3)))

'''
A BinaryTree of X is one of
- (X, (), ())
- (X, BinaryTree of X, ())
- (X, (), BinaryTree of X)
- (X, BinaryTree of X, BinaryTree of X)
'''

def preOrderTraversal(bt, comb, f, base):
    '''
    preOrderTraversal performs a pre-order traversal of bt mapping f onto each element and combining the results with comb, producing base when reaching the empty tree.

    bt      - BinaryTree of X
    comb    - (Y Z Z -> Z)
    f       - (X -> Y)
    base    - Z
    returns - Z

    Examples:
        t = (5,
                (3, (7, (), ()), ()),
                (9, (2, (), ()), ()))
        preOrderTraversal(t, lambda v, rorl, rorr: v - rorl - rorr, lambda x: x, 0) -> 2
        preOrderTraversal(t, concat, lambda x: LL(x), empty()) -> <5, 3, 7, 9, 2>
    '''
    if bt[1] == () and bt[2] == ():
        return f(bt[0])
    if bt[1] != () and bt[0] == ():
        return comb(f(bt[0]), preOrderTraversal(bt[1], comb, f, base), base)
    if bt[1] == () and bt[0] != ():
        return comb(f(bt[0]), base, preOrderTraversal(bt[0], comb, f, base))
    return comb(f(bt[0]), preOrderTraversal(bt[1], comb, f, base), preOrderTraversal(bt[2], comb, f, base))