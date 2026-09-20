values = list(map(int, input('Enter numbers: ').split()))
target = int(input('Enter target: '))
print('Index:', values.index(target) if target in values else -1)
