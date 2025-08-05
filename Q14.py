#Ask the user for a number (e.g., 123) and print the sum of its digits (e.g., 1 + 2 + 3 = 6).
num = input("Enter a number: ")
sum_of_digits = 0
for digit in num:
    sum_of_digits += int(digit)
print("Sum of the digits is:", sum_of_digits)
