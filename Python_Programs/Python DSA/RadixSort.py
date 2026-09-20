values = list(map(int, input("Enter non-negative integers: ").split()))
exp = 1
while values and max(values)//exp > 0:
    output = [[] for _ in range(10)]
    for v in values: output[(v//exp)%10].append(v)
    values = [v for bucket in output for v in bucket]
    exp *= 10
print("Sorted:", values)
