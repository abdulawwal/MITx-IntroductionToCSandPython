# Problem Set 1 - Problem 2

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob'
# occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2
# For problems such as these, do not include raw_input statements or 
# define the variable s in any way. Our automated testing will provide a 
# value of s for you - so the code you submit in the following box should assume 
# s is already defined. If you are confused by this instruction, please review
# L4 Problems 10 and 11 before you begin this problem set.

s = 'azcbobobegboabghabobbobkl'
compStr = 'bob' # The comparison string.
index = 0 # To maintain an index system inside the looping construct. Possibly a bad technique, a result of learning code using C.
bobCount = 0 # Number of detected substrings having the character sequence 'bob' in them
for ch in s:
    index += 1
    if ch == 'b': # To stimulate the substring detection
        tempStr = s[index-1:index+2] # Create a temporary string with the next 2 consecutive characters following the stimulant
        # print(tempStr) if you would like to see intermediate temporary strings. 
        if tempStr == compStr: 
            bobCount += 1
print('Number of bobs is: \n' + str(bobCount))     
    