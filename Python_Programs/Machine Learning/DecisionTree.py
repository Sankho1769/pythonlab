from sklearn.tree import DecisionTreeClassifier

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter class labels: ").split()))
model = DecisionTreeClassifier(random_state=42).fit(x, y)
value = float(input("Enter value to classify: "))
print("Prediction:", model.predict([[value]])[0])
