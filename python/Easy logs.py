# Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.

import math
def logs(x, a, b):
    c = math.log(a,x)
    d = math.log(b,x)
    return c+d
