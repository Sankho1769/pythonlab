import statistics

values = list(map(float, input("Enter numbers: ").split()))
print("Mean:", statistics.mean(values))
print("Median:", statistics.median(values))
print("Mode:", statistics.mode(values))
