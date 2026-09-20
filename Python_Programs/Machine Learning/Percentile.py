import numpy as np

values = list(map(float, input("Enter numbers: ").split()))
p = float(input("Enter percentile (0-100): "))
print("Percentile:", np.percentile(values, p))
