# 4. 
a = (int(input("Enter First numbers: ")))
b = (int(input("Enter Second numbers: ")))
c = (int(input("Enter third numbers: ")))
a, b, c = c, a, b
print("After swap:", a, b, c)