# For numbers 1 to 30, print each number and whether it is even or odd.

for num in range(1, 31):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")