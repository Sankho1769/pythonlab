import matplotlib.pyplot as plt

x = list(map(float, input("Enter X values: ").split()))
y = list(map(float, input("Enter Y values: ").split()))
plt.scatter(x, y)
plt.show()
