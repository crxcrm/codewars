# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

def comp(array1, array2):
    print(array1, array2)
    if (array1 == None and array2 != None):
        return False
    if (array2 == None and array1 != None):
        return False
    if(len(array1) != len(array2)):
        return False
    else:
        a = sorted(array1)
        for i in range(0,len(array1)):
            array1[i] = abs(array1[i])
        a = sorted(array1)
        b = sorted(array2)
        c = ['']*len(a)
        for i in range(0,len(a)):
            if b[i] ==abs(a[i]*a[i]):
                c[i] = True
            else:
                c[i] = False
        if sum(c) != len(a):
            return False
        else: 
            return True
	
