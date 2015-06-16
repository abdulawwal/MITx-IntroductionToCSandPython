# Newton Raphson method for root finding - from Lecture Videos
#----- to find the square root of 24, find the root of x^2-24
#----- if g is an approximation to the root then g-[p(g)/p'(g)] where p'(g) is the first derivative of p(g)

tolerance = 0.01
y = 24.0
guess = y/2.0

while abs(guess*guess - y) >= tolerance:
    guess = guess - (((guess**2)-y)/(2*guess))
print('The square root of: ' + str(y) + ' is ' + str(guess))
