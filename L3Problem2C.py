# L3 Problem 2C
#----- Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:
#----- 21

s = 0
ctr = 1
# end = 6 
while (ctr <= end):
    s = s + ctr
    ctr = ctr + 1
print(s)
