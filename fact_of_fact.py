# 11 Jun 2025

# Factorial of Factorials

# Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n-1)

# def fact_of_fact(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= factorial(i)
#     return result

def fact_of_fact(n):
    factorial = 1
    result = 1
    for i in range(1, n + 1):
        factorial *= i
        result *= factorial
    return result

if __name__ == "__main__":
    print(fact_of_fact(4))
    print(fact_of_fact(5)) 
    print(fact_of_fact(6)) 
