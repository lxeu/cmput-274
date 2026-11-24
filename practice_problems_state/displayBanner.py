from cmput274 import *

def displayBanner(msg, borderChar):
    '''
    displayBanner prints to the screen a banner that contains the given message within a border madeup of borderChar

    msg        - a Str
    borderChar - a single-character Str
    returns    - None

Side Effects: prints to the screens

    Examples:
    displayBanner("Hello World", "-") -> None
        Side Effect: omega has "------------\n- Hello World -\n-------------" appeneded to the end of it
    '''
    borderLen = len(msg) + 4
    print(borderChar*borderLen)
    print(borderChar + " " + msg + " " + borderChar)