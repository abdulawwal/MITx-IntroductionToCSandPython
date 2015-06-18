# Computing powers of a number using Iteration

x = float(raw_input('Enter the number: \n'))
po = int(raw_input('Enter the power: \n'))
result = 1

for turn in range(po):
    result = result * x
    print('Iteration number : ' + str(turn+1) + ' Current result : ' + str(result))
    
print('The answer is : ' + str(result))