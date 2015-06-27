def fibonacciSum(x):
    assert type(x)==int and x>=0
    if x==1 or x==0:
        return 1
    else:
        return fibonacciSum(x-1) + fibonacciSum(x-2)