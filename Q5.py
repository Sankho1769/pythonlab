#Ask the user to enter a number and print its multiplication table (1 to 10)
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")