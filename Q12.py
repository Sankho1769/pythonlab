# Count and print how many numbers between 1 and 30 are divisible by 3.
count_divisible_by_3 = 0
for i in range(1, 31):  
    if i % 3 == 0:
        count_divisible_by_3 += 1
print("Count of numbers between 1 and 30 that are divisible by 3:", count_divisible_by_3)
