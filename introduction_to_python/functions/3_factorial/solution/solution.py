
def factorial(n):
    fact = 1
    if (n == 0):
        return fact
    elif n >= 1:        
        fact = n * factorial(n-1)
    return fact