table = {}
for item in input('Enter key=value pairs separated by spaces: ').split():
    key, value = item.split('=', 1); table[key] = value
print('Hash table:', table)
