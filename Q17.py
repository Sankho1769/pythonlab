#Print numbers from 1 to 30, skipping every 5th number.

for i in range(1, 31):
    if i % 5 == 0:
        continue
    print(i)
    