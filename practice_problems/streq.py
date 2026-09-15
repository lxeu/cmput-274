from strlen import strlen

def streq(s1, s2):
    '''
    streq returns True if s1 == s2 and false otherwise

    s1      - string
    s2      - string
    returns - a bool

    Examples:
        streq("hello", "Hello") -> False
        streq("abc", "abc") -> True
    '''
    if strlen(s1) == 0 and strlen(s2) == 0:
        return True
    if strlen(s1) != strlen(s2):
        return False
    char1 = s1[0]
    char2 = s2[0]
    ror = streq(s1[1:], s2[1:])

    return char1 == char2 and ror


print(streq("hello", "hello"))