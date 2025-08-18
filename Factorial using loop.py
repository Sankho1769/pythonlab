# 14. Factorial using while loop
n = int(input("Enter a number: "))
fact, i = 1, 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)