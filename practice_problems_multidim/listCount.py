from cmput274 import *

def listCount(sl):
    '''
    listCount should return the number of LLists contained within any depth of sl, including sl
    '''
    if isEmpty(sl):
        return 1
    if type(first(sl)) == LList:
        return listCount(first(sl)) + listCount(rest(sl))
    return listCount(rest(sl))

print(listCount(LL(LL(2),2,3, LL(1,LL(LL(23))))))