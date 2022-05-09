# In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

# Examples:

# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:

# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

def parse_int(string: str) -> int:
    d = {word: number for number, word in enumerate('''
        zero one two three four five six seven eight nine
        ten eleven twelve thirteen fourteen fifteen
        sixteen seventeen eighteen nineteen'''.split())}
    d.update({word: number for number, word in zip(range(20, 101, 10),
        'twenty thirty forty fifty sixty seventy eighty ninety hundred'.split())})
    a = []
    for s in string.split('thousand'):
        total = 0
        for i in s.strip().split():
            if '-' in i:
                for j in i.split('-'):
                    total += d.get(j)
            else:
                if i in d:
                    total = total * d.get(i) if 'hund' in i else total + d.get(i)
        a.append(total)
    return 1000000 if 'million' in string else a[0] * 1000 + a[1] if len(a) > 1 else a[0]
