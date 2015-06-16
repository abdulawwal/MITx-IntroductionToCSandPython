# Example for iteration 
#----- Squaring a number by using summation

x = int(raw_input('Enter the number: '))
ans = 0
counter = x
while (counter != 0):
    ans = ans + x
    counter = counter - 1
print('The answer is: '+ str(ans))