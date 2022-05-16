# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. 
# This means, you have to shuffle all letters from the input in all possible orders.

from itertools import permutations as perm

def permutations(string):
    return [''.join(combination) for combination in set(perm(string, len(string)))]
