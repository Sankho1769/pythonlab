# 20. Shopping cart total
total = 0
for i in range(3):
    price = float(input(f"Enter price of item {i+1}: "))
    qty = int(input(f"Enter quantity of item {i+1}: "))
    total += price * qty
print("Total bill:", total)
