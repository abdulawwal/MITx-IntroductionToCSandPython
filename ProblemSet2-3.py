# Problem Set 2 - Problem 3

balance = 320000
annualInterestRate = 0.2

t_balance = balance 
monthlyInterest = annualInterestRate/12.0
low = float(balance/12) # Lower Bound
high = (balance*(1+monthlyInterest)**12)/12.0 # UpperBound
minPay = (high+low)/2.0 # Initial Dichotomy Value

while (high - low > 0.01): # To maintain the tolerance value within 0.01 decimal
    minPay = (low+high)/2.0 
    i = 1
    t_balance = balance
    while (i <= 12):
        unpaidB = t_balance - minPay
        interest = monthlyInterest * unpaidB
        t_balance = unpaidB + interest
        i += 1
    # Conditions to re-assign the boundary values:
    if t_balance > 0.01: 
        low = minPay 
    elif t_balance < 0.01:
        high = minPay  
print('Lowest payment : ' + str(round(minPay,2)))