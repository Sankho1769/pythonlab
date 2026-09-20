from sklearn.model_selection import train_test_split

values = list(map(float, input("Enter values: ").split()))
train, test = train_test_split(values, test_size=0.2, random_state=42)
print("Train:", train)
print("Test:", test)
