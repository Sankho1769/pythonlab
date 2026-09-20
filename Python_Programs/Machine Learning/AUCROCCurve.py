from sklearn.metrics import roc_auc_score

actual = list(map(int, input("Enter binary actual labels: ").split()))
scores = list(map(float, input("Enter prediction scores: ").split()))
print("AUC:", roc_auc_score(actual, scores))
