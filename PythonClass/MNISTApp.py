from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier

mnist = fetch_mldata('MNIST original')

print(mnist)

X, y = mnist.data / 255, mnist.target
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10,
                    alpha=1e-4, solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=0.1)

mlp.fit(X_train, y_train)

print(mlp.score(X_train, y_train))
print(mlp.score(X_test, y_test))
