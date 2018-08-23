# from sklearn import datasets , linear_model
# diabetes = datasets.load_diabetes()
# print(diabetes)

from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
n_neighbors = 15
iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target
h = .02