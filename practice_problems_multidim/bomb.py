from cmput274 import *

g = (("B", "O", "B"), ("O", "B", "O"), ("B", "B", "B"))

def inBounds(grid, pos):
    xPos = pos[0]
    yPos = pos[1]
    if yPos < 0 or yPos >= len(grid):
        return False
    return xPos >= 0 and xPos < len(grid[yPos])

def adjacentBombs(grid, x, y):
    possibleDeltas = map(lambda xD: map(lambda yD: (xD, yD), (-1, 0, 1)), (-1,0,1))
    concat = lambda l1, l2: foldr(l1, cons, l2)
    allDeltas = foldr(possibleDeltas, lambda l1, ror: concat(l1, ror), empty())
    adjPos = map(lambda pair: (x+pair[0], y+pair[1]), allDeltas)
    goodPos = filter(lambda coord: coord != (x, y), adjPos)
    inBoundPos = filter(lambda coord: inBounds(grid, coord), goodPos)
    bombPos = filter(lambda coord: grid[coord[1]][coord[0]] == "B", inBoundPos)
    return len(bombPos)

print(adjacentBombs(g, 1, 1))