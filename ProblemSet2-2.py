# Problem Set 2 - Problem 2

annualInterestRate = 0.2
minPay = 10
t_balance = balance = 32000 

while (t_balance > 0):
    i = 1
    t_balance = balance
    minPay = minPay + 10
    while (i <= 12):
        unpaidB = t_balance - minPay
        interest = annualInterestRate/12.0 * unpaidB
        t_balance = unpaidB + interest
        i += 1
print('Lowest payment : ' + str(minPay))