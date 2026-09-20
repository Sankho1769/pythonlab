value = input("Enter a value (leave blank for None): ")
data = None if value == "" else value
print("Value:", data)
print("Is None:", data is None)
