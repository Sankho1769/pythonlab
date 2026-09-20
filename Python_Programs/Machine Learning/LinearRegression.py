import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array(list(map(float, input("Enter X values: ").split()))).reshape(-1, 1)
y = np.array(list(map(float, input("Enter Y values: ").split())))
model = LinearRegression().fit(x, y)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
