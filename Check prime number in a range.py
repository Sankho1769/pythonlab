start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for n in range(start, end + 1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
