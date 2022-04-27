## Code given:
def approx_equals(a, b):
    a = round(a, 3)
    b = round(b, 3)
    return a == b

## Solution:
import math
def approx_equals(a, b):
    return math.isclose(a, b, abs_tol = 0.001) 
