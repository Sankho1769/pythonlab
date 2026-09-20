values = list(map(int, input("Enter non-negative integers: ").split()))
if values:
    count = [0] * (max(values) + 1)
    for v in values: count[v] += 1
    result = []
    for i, c in enumerate(count): result.extend([i] * c)
    print("Sorted:", result)
else:
    print("Sorted: []")
