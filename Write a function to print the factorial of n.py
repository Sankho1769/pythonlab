def factorial(n):
    # if n <= 0:
    #     raise ValueError("Factorial is not defined for negative numbers.")
    # else:
    #     result = 1
    #     for i in range(1, n + 1):
    #         result *= i
    #     return result
    fact=1
    for i in range(1, n + 1):
        fact *= i
    return fact
n=5
print(f"The factorial of {n} is {factorial(n)}")