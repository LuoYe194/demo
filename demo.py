def findMax(L):
    max = L[0]
    for n in L:
        if n > max:
            max = n
    return max

def findMin(L):
    min = L[0]
    for n in L:
        if n < L:
            min = n
    return min
