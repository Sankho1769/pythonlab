from sklearn.neighbors import KNeighborsClassifier

x = [[float(v)] for v in input("Enter feature values: ").split()]
y = list(map(int, input("Enter class labels: ").split()))
k = int(input("Enter K: "))
model = KNeighborsClassifier(n_neighbors=k).fit(x, y)
value = float(input("Enter value to classify: "))
print("Prediction:", model.predict([[value]])[0])
