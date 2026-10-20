from cmput274 import *

def displayWorld(world, pPos):
    '''
    displayWorld returns a string that represents the display of the game of one dimensional warrior described by world and pPos

    world  - Tuple of anyof(0,1)
    pPos   - A Nat
    return - A Str

    Examples:
        displayWorld((0,1,0,0,0,1,0,0,0), 3) -> "_|_T_|___"
    '''
    natToChar = lambda n: "_" if n == 0 else "|"
    indices = buildList(lambda x: x, len(world))
    indToChar = lambda i: "T" if pPos == i else natToChar(world[i])
    return foldr(indices, lambda i, ror: indToChar(i) + ror, "")

def validMoves(world, pPos):
    leftCoord = pPos - 1
    ans = ()
    if leftCoord >= 0 and world[leftCoord] == 0:
        ans = cons("left", ans)
    rightCoord = pPos + 1
    if rightCoord < len(world) and world[rightCoord] == 0:
        ans = cons("right", ans)
    return ans

def main():
    sampleWorld = (0, 1, 0, 0, 0, 1, 0, 0, 0)
    playerPosition = 3
    print(displayWorld(sampleWorld,playerPosition))

main()
