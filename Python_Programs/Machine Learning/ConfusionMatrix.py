from sklearn.metrics import confusion_matrix

actual = list(map(int, input("Enter actual labels: ").split()))
predicted = list(map(int, input("Enter predicted labels: ").split()))
print(confusion_matrix(actual, predicted))
