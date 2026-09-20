from sklearn.cluster import KMeans

values = [[float(v)] for v in input("Enter numeric values: ").split()]
k = int(input("Enter number of clusters: "))
model = KMeans(n_clusters=k, random_state=42, n_init=10).fit(values)
print("Labels:", model.labels_)
print("Centers:", model.cluster_centers_.ravel())
