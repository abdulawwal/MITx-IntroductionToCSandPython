def recMul(a,b):
    if b == 1:
        return a
    else:
        return a + recMul(a,b-1)
        