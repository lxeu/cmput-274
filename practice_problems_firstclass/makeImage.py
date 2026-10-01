from cmput274 import *

# A Pixel is a - LL(CV, CV, CV)

def redShiftHelper(p, sAmt):
    newRed = first(p) + sAmt
    if newRed > 255:
        return cons(255, rest(p))
    if newRed < 0:
        return cons(0, rest(p))
    return(cons(newRed, rest(p)))

def redShiftGenerator(sAmt):
    '''
    redShiftGenerator produdces a unary function that takes a single Pixel parameter and shifts its colour red componenet by a particular shift amount

    sAmt    - int
    returns - (Pixel -> Pixel)

    Examples:
        redShiftGenerator(50) -> fn that takes a pixel and adds 50 to its red component
        redShiftGenerator(50)(LL(20,30,70)) -> LL(70,30,70)
    '''
    return lambda p: redShiftHelper(p, sAmt)

def snapTo255(n):
    if n > 255:
        return 255
    return n

def snapTo0(n):
    if n < 0:
        return 0
    return n

def genShiftHelper(p, r, g, b):
    newRed = first(p) + r
    newGreen = first(rest(p)) + g
    newBlue = first(rest(rest(p))) + b
    newPixel = LL(newRed, newGreen, newBlue)
    return map(snapTo0, map(snapTo255, newPixel))

def genShiftGenerator(r, g, b):
    return lambda p: genShiftHelper(p, r, g, b)

def redShift(pixel):
    newRed = first(pixel) + 30
    if newRed > 255:
        return cons(255, rest(pixel))
    return cons(newRed, rest(pixel))

def redShiftImage(img):
    '''
    redShiftImage applies our redshift transformation to an image
    
    img - LList of pixels
    returns - LList of piels
    '''
    return map(redShift, img)