def printMove(to,fr):
    print('Move from : ' + str(to) + ' to ' + str(fr))

def towerOfHanoi(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        towerOfHanoi(n-1,fr,spare,to)
        towerOfHanoi(1,fr,to,spare)
        towerOfHanoi(n-1,spare,to,fr)