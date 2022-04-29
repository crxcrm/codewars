# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    new_string="" 
    for i in range(len(text)): 
        if (text[i-1] == '-' or text[i-1] == '_'): 
            new_string += text[i].upper() 
        else: 
            new_string += text[i] 
    new_string = new_string.replace('-','')
    new_string = new_string.replace('_','')
    return new_string
