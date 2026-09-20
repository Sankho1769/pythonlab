values = list(map(int, input("Enter numbers: ").split()))
for i in range(len(values)):
    m = i
    for j in range(i+1, len(values)):
        if values[j] < values[m]:
            m = j
    values[i], values[m] = values[m], values[i]
print("Sorted:", values)
