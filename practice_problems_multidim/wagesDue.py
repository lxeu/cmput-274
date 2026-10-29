from cmput274 import *

def payrollItemToWages(pri):
    '''
    pri - a PayrollItem
    returns 0 LL(str, float)
    '''
    name = first(pri)
    wages = foldr(rest(pri), lambda x, y: x + y, 0) * 22.5
    return LL(name, wages)

def wagesDue(prl):
    '''
    wagesDue takes a PayROllList and returns a LList of pairs of all the employees and how much money they are owed for this pay period.

    pList - PayRollList
    returns - LList of LL(str, float)

    Example:
        wagesDue(LL(LL("Erik", 5, 8, 4, 7), LL("Ashley", 6, 2), LL("Stefan", 2, 2, 2, 2, 2, 2, 2)) -> LL(LL("Erik", 540), LL("Ashley", 180.0), LL("Stefan", 315.0))
    '''
    return map(payrollItemToWages, prl)

print(wagesDue(LL(LL("Erik", 5, 8, 4, 7), LL("Ashley", 6, 2), LL("Stefan", 2, 2, 2, 2, 2, 2, 2))))