import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([list(map(float, input("Enter features for a row: ").split())) for _ in range(
    int(input("Enter number of rows: "))
)])
y = np.array(list(map(float, input("Enter target values: ").split())))
model = LinearRegression().fit(x, y)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
