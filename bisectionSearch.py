# Bisection Search from Lecture Videos
#----- code from Lecture Video for Bisection Search Algorithm

x = 25
epsilon = 0.01 #tolerance
numGuess = 0
low = 0.0
high = x
ans = (high+low)/2.0

while abs(ans**2 - x) >= epsilon:
    print(' low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('\n')
print('The number of guesses were: \n' + str(numGuess))
print(str(ans))