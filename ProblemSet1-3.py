# Problem Set 1 - Problem 3

# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in
# which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring.
# For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc
# For problems such as these, do not include raw_input 
# statements or define the variable s in any way. 
# Our automated testing will provide a value of s for you - 
# so the code you submit in the following box should assume s is already defined. 
# If you are confused by this instruction,
# please review L4 Problems 10 and 11 before you begin this problem set.

s = 'zyxwvutsrqponmlkjihgfedcba'
ordAr = binStatus = []
count = size = max_size = ctr = ul = 0

for i in s:
    ordAr.append(ord(i))
#print('The string converted to ASCII values is : \n' + str(ordAr))

# backconversion
#str1 = ''
#for i in ordAr:
#    str1 = str1 + chr(i)
#print str1


for i in ordAr[1:]:
    count=count+1
#    print str(ordAr[count-1]) +' '+ str(ordAr[count])
    binStatus.append(int(ordAr[count] >= ordAr[count-1]))

result = None
prev = None

str1 = ''


for i in binStatus:
    ctr = ctr + 1
    if i == prev and i == 1:
        size += 1
        if size > max_size:
            ul = ctr
            max_size = size 
    else:
        size = 0
    prev = i
#print (max_size+1) 

ll = ul-(max_size+1)

for i in range(ll,ul+1):
    str1 = str1 + chr(ordAr[i])
print('Longest substring in alphabetical order is: '+ str1)
        
     
    
        
        

    