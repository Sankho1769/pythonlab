#Find and print the sum of numbers between 1 and 40 that are divisible by 4.
sum_divisible_by_4 = 0
for i in range(1, 41):
    if i % 4 == 0:
        sum_divisible_by_4 += i
print("Sum of numbers between 1 and 40 that are divisible by 4 is:", sum_divisible_by_4)
