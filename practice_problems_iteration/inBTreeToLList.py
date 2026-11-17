from cmput274 import *

emptyStack = empty
push = cons
pop = rest
peek = first
stackIsEmpty = isEmpty

def inBTToLList(t):
    cStack = push(t, emptyStack())
    ans = empty()
    while not stackIsEmpty(cStack):
        curTree = peek(cStack)
        cStack = pop(cStack)
        if t[1] == () and t[2] == ():
            ans = append(ans, t[0])
        else:
            if t[2] != ():
                cStack = push(t[2], cStack)
            cStack = push((t[0], (), ()), cStack)