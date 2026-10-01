from cmput274 import *

lon = LL(1, 2, 3, 4, 5, 6, 100)

mean = (foldr(lon, lambda x, y : x + y, 0)) / len(lon)

print(mean)