def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    counter = max(a,b)
    while (counter > 0):
        if (a%counter==0 and b%counter==0): 
            return counter
            break
        counter = counter - 1