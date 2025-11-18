import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
    y_true = y_true.reshape(-1, 1)   
    observations, features = X.shape 

    w = w.reshape(-1, 1)

    residuals = y_true - (X @ w)
    mean_squared_error = 1/observations * (residuals.T @ residuals)
    l2_penalty = alpha * (w.T @ w)

    result = mean_squared_error + l2_penalty

    return round(result.item(), 4)

X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

print(y_true.reshape(-1, 1))
w = w.reshape(-1, 1)
print(X)
print(w.reshape(-1, 1))
print(X@w)
print((X@w).shape)
print((X@w).reshape(-1 ,1))
print(y_true.reshape(-1, 1) - X@w)

loss = ridge_loss(X, w, y_true, alpha)
print(loss)