values = list(map(int, input("Enter numbers: ").split()))
for i in range(len(values)):
    for j in range(0, len(values)-i-1):
        if values[j] > values[j+1]:
            values[j], values[j+1] = values[j+1], values[j]
print("Sorted:", values)
