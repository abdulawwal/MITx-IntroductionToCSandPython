# Problem Set 1 - Problem 3
# Passed the grader with 14.25/15.00 accuracy. Failed certain test cases. Must rework.

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

s = 'wyinskwvesnqowrpuf'

ordAr = []
count = 0
binStatus = []
# Creating list of ASCII values from string
for i in s:
    ordAr.append(ord(i))
# Creating binary list of comparisons
for i in ordAr[1:]:
    count=count+1
    binStatus.append(int(ordAr[count] >= ordAr[count-1]))

result = None
prev = None
size = max_size = ctr = e_i =0
str1 = ''

# Finding longest sequence of consecutive binary 1s
for i in binStatus:
    ctr = ctr + 1
    if i == prev and i == 1:
        size += 1
        if size > max_size:
            e_i = ctr
            max_size = size 
    else:
        size = 0
    prev = i
# Finding indexes of desired substring
ul = e_i
ll = e_i-(max_size+1)

for i in range(ll,ul+1):
    str1 = str1 + chr(ordAr[i])
print('Longest substring in alphabetical order is: '+ str1)
     
    
        
        

    