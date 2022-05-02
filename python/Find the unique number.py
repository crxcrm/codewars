# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# def find_uniq(arr):
#    str_len=len(arr)
#    vec = ['']*str_len
#    result = 0
#    for i in range(0, str_len):
#        vec[i] = arr.count(arr[i])
#        if vec[i]==1:
#            result = arr[i]
#            break
#    return result  

from collections import Counter
def find_uniq(arr):
    frequency = Counter(arr)
    print(frequency)
    res = [key for (key, value) in frequency.items() if value == 1]
    res = res[0]
    return res
