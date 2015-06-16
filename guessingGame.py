# Number guessing game based on BISECTION SEARCH
#----- The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

print('Please think of a number between 0 and 100!')
high = 100
low = 0

flagEntry = True

while (flagEntry == True):
    ans = (high+low)/2
    print('Is your secret number '+ str(ans)+ '?')
    userResp = raw_input('Enter ''h'' to indicate the guess is too high. Enter ''l'' to indicate the guess is too low. Enter ''c'' to indicate I guessed correctly.')
    if (userResp == 'c'):      
        flagEntry = False
        print('Game over. Your secret number was:'+ str(ans))
        break
    elif (userResp == 'h'):
        high = ans
        flagEntry = True
    elif (userResp == 'l'):
        low = ans
        flagEntry = True
    elif (userResp != 'c' or userResp != 'l' or userResp != 'h'):
        print('Sorry, I did not understand your input.')
        flagEntry = True
