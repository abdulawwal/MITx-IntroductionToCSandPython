# Example from Lecture Video
#---works like a left-shift converter

num = int(raw_input('Enter the number to be converted to BINARY: \n'))
if num < 0:
    isNeg = True
    num = abs(Num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num/2
if isNeg:
    result = '-' + result
print('The binary representation is: \n' + result)