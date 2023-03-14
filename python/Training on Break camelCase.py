#Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    l = []
    for i in range(0, len(s)):
        if s[i].isupper():
            l.append(" ")
        l.append(s[i])
    return ''.join(l)
