import statistics

values = list(map(float, input("Enter numbers: ").split()))
print("Standard deviation:", statistics.stdev(values))
