def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr=='':
        return False
        
    if len(aStr)==1:
        return aStr == char

    
    midI = len(aStr)/2
    midC = aStr[midI]
    
    if char == midC:
        return True
        
    elif char < midC:
        return isIn(char,aStr[:midI])
        
    else:
        return isIn(char,aStr[midI+1:])
    