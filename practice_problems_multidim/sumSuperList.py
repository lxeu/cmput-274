from cmput274 import *

def sumSuperList(sl):
    if isEmpty(sl):
          return 0
    if type(first(sl)) == int:
         return first(sl) + sumSuperList(rest(sl))
    if type(first(sl)) == LList:
         return sumSuperList(first(sl)) + sumSuperList(rest(sl))

print(sumSuperList())