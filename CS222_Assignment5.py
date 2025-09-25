def fahrenheitToCelsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Tempurature has to be a number.")
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius

def intToFibonacci(n):
    if not isinstance(n, int):
        raise TypeError("Input has to be an integer.")
    if (n < 0):
        raise ValueError("Input has to be a non negative integer.")
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        fib1 = 0
        fib2 = 1
        for fib in range(2, n + 1):
            fib1, fib2 = fib2, fib1 + fib2
        return fib2