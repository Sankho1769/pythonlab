from sklearn.cluster import AgglomerativeClustering

values = [[float(v)] for v in input("Enter values: ").split()]
clusters = int(input("Enter number of clusters: "))
labels = AgglomerativeClustering(n_clusters=clusters).fit_predict(values)
print("Cluster labels:", labels)
