# -*- coding: utf-8 -*-
# L4 Problem 4

# Write a Python function, evalQuadratic(a, b, c, x), 
# that the value of the quadratic a⋅x2+b⋅x+c.

# This function takes in four numbers and returns a single number.

def evalQuadratic(a, b, c, x):
    qr = a*(x**2)+b*x+c
    return qr