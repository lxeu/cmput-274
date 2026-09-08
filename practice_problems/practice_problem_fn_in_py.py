i = int(input(""))

def firstThreshold(i, tax):
    '''
    '''
    if i <= 57375:
        tax = i * 0.145
        return i, tax
    if i > 57375:
        tax = 57375 * 0.145
        i -= 57375
        return i, tax

def incomeTax(i):
    '''
    
    '''
    tax = 0
    i, tax = firstThreshold(i, tax)


    print(tax)

incomeTax(i)