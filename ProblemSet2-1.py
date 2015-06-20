# Problem Set 2 - Problem 1

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
minMonthlyPayment = 0
totalPaid = 0

i = 1
while (i <= 12):
    minMonthlyPayment = monthlyPaymentRate * balance
    unpaidB = balance - minMonthlyPayment
    interest = annualInterestRate/12.0 * unpaidB
    balance = unpaidB + interest
    totalPaid += minMonthlyPayment
    print('Month: ' + str(i))
    print('Minimum monthly payment: ' + str(round(minMonthlyPayment,2)))
    print('Remaining balance: ' + str(round(balance,2)))
    i += 1
print('The total amount paid is : '+ str(round(totalPaid,2)))
print('The remaining balance is : '+ str(round(balance,2)))