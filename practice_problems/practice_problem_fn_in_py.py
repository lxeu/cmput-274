i = int(input())

def firstThreshold(i):
    '''
    firstThreshold returns the amount of tax owed in the first canadian tax bracket (the first 57375)

    i - a floating point number
    return - a floating point number

    Examples:
    firstThreshold(30000) -> 4350.0
    firstThreshold(60000) -> 8319.375
    firstThreshold(2000000) -> 8319.375
    '''
    if i > 57375:
        return 57375 * 0.145
    return i * 0.145

def secondThreshold(i):
    '''
    secondThreshold returns the amount of tax owed in the second canadian tax bracket (the first 114750)

    i - a floating point number
    return - a floating point number
    '''
    if i - 57375 < 0:
        return 0
    if i - 57375 > 57375:
        return 57375 * 0.205
    return (i - 57375) * 0.205

def thirdThreshold(i):
    '''
    thirdThreshold returns the amount of tax owed in the third canadian tax bracket (the first 177882)

    i - a floating point number
    return - a floating point number
    '''
    if i - 114750 < 0:
        return 0
    if i - 114750 > 63132:
        return 63132 * 0.29
    return (i - 114750) * 0.29

def fourthThreshold(i):
    '''
    fourthThreshold returns the amount of tax owed in the fourth canadian tax bracket (the first 253414)

    i - a floating point number
    return - a floating point number
    '''
    if i - 177882 < 0:
        return 0
    if i - 177882 > 75532:
        return 75532 * 0.29
    return (i - 177882) * 0.29

def fifthThreshold(i):
    '''
    fithThreshold returns the amount of tax owed in the fith canadian tax bracket (beyond 253414)

    i - a floating point number
    return - a floating point number
    '''
    if i - 253414 < 0:
        return 0
    return (i - 253414) * 0.33

def incomeTax(i):
    '''
    incomeTax returns the amount of tax owed in total of all canadian tax brackets

    i - a floating point number
    return - a floating point number
    '''
    return firstThreshold(i) + secondThreshold(i) + thirdThreshold(i) + fourthThreshold(i) + fifthThreshold(i)

print(incomeTax(i))