from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter class labels: ").split()))
params = {"max_depth": [1, 2, 3, None]}
search = GridSearchCV(DecisionTreeClassifier(random_state=42), params, cv=2)
search.fit(x, y)
print("Best parameters:", search.best_params_)
