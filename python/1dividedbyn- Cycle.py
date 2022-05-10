# Let be n an integer prime with 10 e.g. 7.
# 1/7 = 0.142857 142857 142857 ....
# We see that the decimal part has a cycle: 142857. The length of this cycle is 6. In the same way:
# 1/11 = 0.09 09 09 .... Cycle length is 2.
# Task
# Given an integer n (n > 1) the function cycle(n) returns the length of the cycle if there is one otherwise (n and 10 not coprimes) return -1.

def cycle(n) :
    if n%2 == 0 or n%5 == 0:
        return -1
    d = 9
    count = 1
    while d % n != 0:
        d = d%n*10 + 9
        count += 1
    return count
