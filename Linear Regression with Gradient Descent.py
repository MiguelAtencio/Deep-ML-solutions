import numpy as np

# Gradient descent with Matrix multiplication
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
    m, n = X.shape
    thetas = np.zeros((n, 1))

    y = y.reshape(-1, 1)

    for j in range(iterations):
        hypothesis_minus_target = X @ thetas - y
        print(thetas)
        thetas = thetas - alpha * (1/m) * (X.T @ hypothesis_minus_target)

    return thetas

thetas = np.zeros((2, 1))
X = np.array([[1, 1], [1, 2], [1, 3]])

print(X.shape)
print(thetas.shape)
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000

print(X.T)
print(X@thetas)
print(y.reshape(-1, 1))
print(X@thetas - y.reshape(-1, 1))
print(X.T @ (X@thetas - y.reshape(-1, 1)))

print(linear_regression_gradient_descent(X, y, alpha, iterations))

