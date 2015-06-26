def iterPower(base,exp):
    itr = exp
    res = 1.0
    while (itr > 0):
        res = res * base
        itr = itr - 1
    return res