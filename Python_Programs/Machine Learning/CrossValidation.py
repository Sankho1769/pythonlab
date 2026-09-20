from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter class labels: ").split()))
scores = cross_val_score(DecisionTreeClassifier(random_state=42), x, y, cv=2)
print("Scores:", scores)
print("Average:", scores.mean())
