from cmput274 import *

def displayWorld(world, pPos, enemies):
    '''
    displayWorld returns a string that represents the display of the game of one dimensional warrior described by world and pPos

    world  - Tuple of anyof(0,1)
    pPos   - A Nat
    return - A Str

    Examples:
        displayWorld((0,1,0,0,0,1,0,0,0), 3) -> "_|_T_|___"
    '''
    def indToChar(i):
        if pPos == i:
            return "T"
        if foldr(enemies, lambda e, ans: e == i or ans, False):
            return "X"
        return natToChar(world[i])
    natToChar = lambda n: "_" if n == 0 else "|"
    indices = buildList(lambda x: x, len(world))
    indToChar = lambda i: "T" if pPos == i else natToChar(world[i])
    return foldr(indices, lambda i, ror: indToChar(i) + ror, "")

def validMoves(world, pPos):
    '''
    validMove returns a tuple of the strings that represent the directions the player in twoDimensional Warrior can move

    world   - a tuple of anyof(0, 1)
    pPos    - a tuple of (Nat, Nat) (x, y)
    returns - a tuple of str
    '''
    def isBounded(coord):
        x = coord[0]
        y = coord[1]
        minYCoord = 0
        minXCoord = 0
        yCoordEnd = len(world)
        if y < minYCoord and y >= ycoordEnd:
            return False
        xCoordEnd = len(world[y])
        return x >= minXCoord and x < xCoordEnd
    def isWall(coord):
        x = coord[0]
        y = coord[1]
        return world[y][x] == 1
    leftCoord = (pPos[0] - 1, pPos[1])
    rightCoord = (pPos[0] + 1, pPos[1])
    upCoord = (pPos[0], pPos[1] - 1)
    downCoord = (pPos[0], pPos[1] + 1)
    ans = ()
    options = ((leftCoord, "left"), (rightCoord, "right"), (upCoord, "up"), (downCoord, "down"))
    goodPos = lambda pos: isBounded(pos) and not isWall(pos)
    foldF = lambda pair, ans: (pair[1],) + ans if goodPos(pair[0]) else ans
    return foldr(options, foldF, ())

def main():
    sampleWorld = (0, 1, 0, 0, 0, 1, 0, 0, 0)
    playerPosition = 3
    print(displayWorld(sampleWorld,playerPosition, 0))
    print(displayWorld(sampleWorld,playerPosition, 0))

main()
