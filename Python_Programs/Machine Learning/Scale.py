from sklearn.preprocessing import StandardScaler

values = list(map(float, input("Enter numbers: ").split()))
scaled = StandardScaler().fit_transform([[x] for x in values])
print("Scaled values:", scaled.ravel())
