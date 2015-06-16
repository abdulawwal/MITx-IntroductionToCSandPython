# Example from Lecture Video to convert fraction into decimal

x = float(raw_input('Enter the decimal number between 0 and 1: \n'))
idealMult = 0
while((2**idealMult)*x)%1!=0:
    idealMult += 1
    #print idealMult

num = int(x*(2**idealMult))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2

for i in range(idealMult-len(result)):
    result = '0' + result
    
result = result[0:-idealMult] + '.' + result[-idealMult:]
print('Binary representation of ' + str(x) + ' is: ' + str(result))