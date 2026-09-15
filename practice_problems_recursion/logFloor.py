def logFloor(n):
    '''
    logFloor takes a positive integer and produces the floor of the base ten log of that number.

    n       - a natural number
    returns - a natural number

    Examples:
        logFloor(199) -> 2
        logFloor(2000) -> 3
    '''
    assert n > 0
    if n < 10:
        return 0
    ror = logFloor(n // 10)
    return 1 + ror

logFloor(9999)