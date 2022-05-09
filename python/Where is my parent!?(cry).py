# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".

def find_children(dancing_brigade):
    string = sorted(dancing_brigade.lower())
    str2 = string.copy()
    for i in range(0, len(string)):
        if ((string[i] != string[i-1]) | (i == 0)):
            str2[i] = string[i].upper()
    str = ''.join(str2)
    return str
