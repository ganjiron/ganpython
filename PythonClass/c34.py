# from sklearn import datasets , linear_model
# diabetes = datasets.load_diabetes()
# print(diabetes)

from sklearn import datasets
n_neighbors = 15
iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target
h = .02

from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

print(clf)
