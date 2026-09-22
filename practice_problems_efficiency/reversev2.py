from cmput274 import *

def reverseHelper(l, asf):
    '''
    reverseHelper takes a LList l and a LList asf that is the answer so far of reversing a LList and returns the reversed list.
    if l is <v0, ..., vn> and asf is <q0, ..., qn>
    we produce <vn, ..., v0, q0, ...qn>. Semantically asf can be thought of as "all the parts of my list I've already reversed"


    l       - LList of Any
    asf     - LList of Any
    returns - LList of Any

    Examples:
        reverseHelper(<1, 2, 3>, <0, -1>) -> <3, 2, 1, 0, -1>
    '''
    if isEmpty(l):
        return asf
    return reverseHelper(rest(l), cons(first(l), asf))


def reverse(l):
    return reverseHelper(l, empty())

print(reverse(cons(5, cons(2, cons(9, cons(0, empty()))))))