from sklearn.linear_model import LogisticRegression

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter binary labels: ").split()))
model = LogisticRegression().fit(x, y)
value = float(input("Enter value to predict: "))
print("Prediction:", model.predict([[value]])[0])
