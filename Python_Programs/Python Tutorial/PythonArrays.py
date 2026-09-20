from array import array

values = input("Enter integers separated by spaces: ").split()
numbers = array("i", map(int, values))
print("Array:", numbers.tolist())
