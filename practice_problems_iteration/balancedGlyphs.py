from cmput274 import *

def isOpenGlyph(c):
    return c == "{" or c == "[" or c == "("

def isClosedGlyph(c):
    return c == "}" or c == "]" or c == ")"

def matchingGlyphs(open, close):
    '''
    matchingGlyps returns True if the opening glyph matches the closing glyph

    open    - one of "(", "[", or "{"
    close   - one of ")", "]", or "}"
    returns - bool

    Examples
        matchingGlyphs("(", "}") -> False
        matchingGlyphs("[", "]") -> True
    '''
    parens = open == "(" and close == ")"
    bracks = open == "[" and close == "]"
    braces = open == "{" and close == "}"
    return parens or braces or bracks
    
def balancedGlyphs(s):
    '''
    balancedGlyphs returns True if all of the parentheses brackets, and braces are balanced in string S and False otherwise

    s       - str
    returns - bool

    Examples:
        balancedGlyphs("{[xt()]z}[hello]") -> True
        balancedGlyphs("{[(]}") -> False
        balancedGlyphs("[Hey there :)]") -> False
    '''
    i = 0
    while i < len(s):
        c = s[i]
        if isEnclosingGlyph(c):
            if isOpenGlyph(c):
                openedGlyphs = cons(c, openedGlyphs)
            else:
                if matchingGlyphs(c) == first(openedGlyphs):
                    openedGlyphs = rest(openedGlyphs)
                else:
                    return False
        i = i + 1
    return isEmpty(openedGlyphs)
        

print(balancedGlyphs(")("))

def main():
    testExact("isBalanced", True, balancedGlyphs, '{[xt(y)]z}[hello]')
    testExact("wrongOrder", False, balancedGlyphs, '{[(]}')
    testExact("closeNoOpen", False, balancedGlyphs, '[Hey there :)]')
    testExact("openNoClose", False, balancedGlyphs, '((())')
    runTests()

if __name__ == "__main__":
    main()