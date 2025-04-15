#https://github.com/achallauf/lab10-AC-AC.git
#Partner 1 - Akhil Challa
#Partner 2 - Akhil Challa


import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Negative input not allowed")
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b



def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(b, a)




def mul(a, b): 
    return a * b

def div(a, b): 
    try:
        return b / a
    except ZeroDivisionError:
        return "Error: Division by zero"



def exp(a, b): 
    return a ** b

