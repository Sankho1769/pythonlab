# Add and print the sum of all even numbers from 1 to 50.

sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
print("Sum of all even numbers from 1 to 50 is:", sum_even)
