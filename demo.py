def findMax(L):
    max = L[0]
    for n in L:
        if n > max:
            max = n
    return max
