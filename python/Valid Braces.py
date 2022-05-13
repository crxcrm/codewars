# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

def validBraces(string):
    braces = {")":"(","]":"[","}":"{"}
    s = string
    for i in braces:
        if s.count(i) != s.count(braces[i]):
            return False 
    c = 0 
    while len(s) > 0:
        c += 1
        if s[c] in ")]}":
            if s[c-1] != braces[s[c]]:
                return False
            s = s[:c-1]+s[c+1:]
            c = 0
    return True
