from logFloor import logFloor

def digitSum(n):
    '''
    digitSum returns the sum of the digits of n

    n       - an natural number
    returns - a natural number

    Examples:
        digitSum(735) -> 15
        digitSum(10000) -> 1
    '''
    if n < 10:
        return n
    currentDigit = n // (10**logFloor(n))
    nextNumber = n - currentDigit * 10**logFloor(n)
    ror = digitSum(nextNumber)
    return currentDigit + ror

print(digitSum(735))