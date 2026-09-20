from sklearn.preprocessing import OneHotEncoder

values = input("Enter categories separated by spaces: ").split()
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
encoded = encoder.fit_transform([[v] for v in values])
print(encoded)
