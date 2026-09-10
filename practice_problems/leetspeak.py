def convertChar(c):
    if c == "E" or c == "e":
        return "3"
    if c == "T" or c == "t":
        return "7"
    if c == "A" or c == "a":
        return "4"
    if c == "L" or c == "l":
        return "1"
    if c == "S" or c == "s":
        return "5"
    if c == "O" or c == "o":
        return "0"
    return c

def leetSpeak(s):
    if s == "":
        return ""
    if s == "er":
        return "z0r"
    return convertChar(s[0]) + leetSpeak(s[1:])

print(leetSpeak("hacker"))