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

    

def balancedGlyphsHelper(s, open):
    '''
    balancedGlyphsHelper takes a string to process s and a LList of open glyphs open and returns True if s is balanced assuming the glyphs in open have already previously been opened in the order given

    s       - str
    open    - LList of Char
    returns - bool

    Examples:
        balancedGlyphsHelper(")]z}[hello]", cons("(", cons("[", cons("{", empty())))) -> True
    '''
    if s == "":
        return isEmpty(open)

    c0 = s[0]
    if isOpenGlyph(c0):
        return balancedGlyphsHelper(s[1:], cons(c0, open))
    if isClosedGlyph(c0):
        if isEmpty(open):
            return False
        lastOpen = first(open)
        matched = matchingGlyphs(lastOpen, c0)
        if matched:
            return balancedGlyphsHelper(s[1:], rest(open))
        else:
            return False
    return balancedGlyphsHelper(s[1:], open)
        
    
    
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
    return balancedGlyphsHelper(s, empty())

print(balancedGlyphs(")("))

def main():
    testExact("isBalanced", True, balancedGlyphs, '{[xt(y)]z}[hello]')
    testExact("wrongOrder", False, balancedGlyphs, '{[(]}')
    testExact("closeNoOpen", False, balancedGlyphs, '[Hey there :)]')
    testExact("openNoClose", False, balancedGlyphs, '((())')
    runTests()

if __name__ == "__main__":
    main()