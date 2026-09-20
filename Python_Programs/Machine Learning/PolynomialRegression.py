import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

x = np.array(list(map(float, input("Enter X values: ").split()))).reshape(-1, 1)
y = np.array(list(map(float, input("Enter Y values: ").split())))
degree = int(input("Enter polynomial degree: "))
model = make_pipeline(PolynomialFeatures(degree), LinearRegression()).fit(x, y)
print("Predictions:", model.predict(x))
