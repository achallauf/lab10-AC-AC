"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
import math

def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    try:
        return b / a
    except ZeroDivisionError:
        return "Error: Division by zero"

def log(a, b): 
    try:
        return math.log(b, a)
    except ValueError:
        return "Error: Invalid logarithm"

def exp(a, b): 
    return a ** b


