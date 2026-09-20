from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter class labels: ").split()))
model = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10, random_state=42)
model.fit(x, y)
value = float(input("Enter value to classify: "))
print("Prediction:", model.predict([[value]])[0])
