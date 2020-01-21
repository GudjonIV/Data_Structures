# Author: Guðjón Ingi Valdimarsson
# Date: 21.01.2020
import sys
sys.setrecursionlimit(10000)

def power(base, exp):
    if exp == 1:            # Base case
        return base
    return power(base, exp - 1) * base

def multiply(a, b):
    if b == 1:
        return a
    return multiply(a, b - 1) + a

def factorial(n):
    if n == 1:      # Base case
        return 1
    print (n)
    return factorial(n-1) * n

def natural(n):
    if n == 0:
        return 1
    natural(n - 1)
    print (n, end=" ")

def sum_of_digits(x):
    if x // 10 == 0:
        return x
    return sum_of_digits(x // 10) + x % 10

def fibonacci(n):
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = fibonacci(n - 1)
        return a + b, a

def ackerman(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackerman(m - 1, 1)
    else:
        return ackerman(m - 1, ackerman(m, n-1))

#print (factorial(5))
#print (power(5, 3))
#print (multiply(5, 5))
#natural(5)
#print (sum_of_digits(254))
#print (fibonacci(5))
#print (ackerman(4, 1))
print(ackerman(2, 1))
print (2 ** 2 ** 2 ** 2)