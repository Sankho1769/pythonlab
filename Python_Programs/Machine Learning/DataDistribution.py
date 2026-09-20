import matplotlib.pyplot as plt

values = list(map(float, input("Enter numbers: ").split()))
plt.hist(values)
plt.title("Data Distribution")
plt.show()
