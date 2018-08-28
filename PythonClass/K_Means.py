import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
X, y = iris.data[:, 2:4], iris.target

print(X.shape, X)

est = KMeans(n_clusters=3)
est.fit(X)

print(est)

labels = est.labels_
print(labels)
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()
