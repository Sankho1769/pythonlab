import bisect
values = sorted(map(int, input('Enter numbers: ').split()))
target = int(input('Enter target: '))
i = bisect.bisect_left(values, target)
print('Found:', i < len(values) and values[i] == target)
