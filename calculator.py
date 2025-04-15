"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
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


