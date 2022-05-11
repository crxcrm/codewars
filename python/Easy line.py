# In the drawing below we have a part of the Pascal's triangle, horizontal lines are numbered from zero (top).

# We want to calculate the sum of the squares of the binomial coefficients on a given horizontal line with a function called easyline (or easyLine or easy-line).

# Can you write a program which calculate easyline(n) where n is the horizontal line number?

# The function will take n (with: n>= 0) as parameter and will return the sum of the squares of the binomial coefficients on line n.

def easyline(n):
    a = [[1]]
    for size in range(2,n+2):
        tmp = [1]*size
        for i in range(1,size-1):
            tmp[i] = a[-1][i-1] + a[-1][i]
        a.append(tmp)
    return sum(x*x for x in a[-1])
