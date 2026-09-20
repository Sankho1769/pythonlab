values = sorted(set(map(int, input('Enter values: ').split())))
target = int(input('Enter value to search: '))
print('Found:', target in values)
