def digitSum(n):
    '''
    digitSum returns the sum of the digits of n

    n       - an natural number
    returns - a natural number

    Examples:
        digitSum(735) -> 15
        digitSum(10000) -> 1
    '''
    assert n > 0

    if n < 10:
        return n
    currentDigit = n % 10
    ror = digitSum(n // 10)
    return currentDigit + ror

print(digitSum(735))