# Task
# Given a Divisor and a Bound , Find the largest integer N , Such That ,

# Conditions :
# N is divisible by divisor
# N is less than or equal to bound
# N is greater than 0.

# Notes
# The parameters (divisor, bound) passed to the function are only positive values .
# It's guaranteed that a divisor is Found .

def max_multiple(divisor, bound):
    N = 1
    for i in range(1, bound+1):
        if i%divisor == 0:
            N = i
    return N
